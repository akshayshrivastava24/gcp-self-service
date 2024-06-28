from google.cloud import compute_v1

def create_instance(project_id, zone, instance_name, machine_type, source_image):
    instance_client = compute_v1.InstancesClient()

    # Configure the machine type
    machine_type_path = f"zones/{zone}/machineTypes/{machine_type}"

    # Configure the boot disk
    initialize_params = compute_v1.AttachedDiskInitializeParams()
    initialize_params.source_image = source_image

    disk = compute_v1.AttachedDisk()
    disk.boot = True
    disk.auto_delete = True
    disk.initialize_params = initialize_params

    # Configure the network interface
    network_interface = compute_v1.NetworkInterface()
    access_config = compute_v1.AccessConfig()
    access_config.type_ = "ONE_TO_ONE_NAT"
    access_config.name = "External NAT"
    network_interface.access_configs = [access_config]
    network_interface.name = "global/networks/default"

    # Configure the instance
    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.machine_type = machine_type_path
    instance.disks = [disk]
    instance.network_interfaces = [network_interface]

    # Create the instance
    operation = instance_client.insert(project=project_id, zone=zone, instance_resource=instance)

    print(f"Operation to create instance: {operation.name}")

    # Wait for the operation to complete
    operation_client = compute_v1.ZoneOperationsClient()
    while True:
        result = operation_client.get(project=project_id, zone=zone, operation=operation.name)
        if result.status == compute_v1.Operation.Status.DONE:
            print("Instance created.")
            break
        if result.error:
            print(f"Error creating instance: {result.error}")
            break


