from google.cloud import compute_v1

from template.vm import create_instance
from template.s3 import create_bucket
import yaml
import sys
app_name=sys.argv[1]
with open(f'apps/{app_name}.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)
print(data)
     

if __name__ == "__main__":
    project_id = "nonprod-424912"
    zone = "us-central1-a"
    if data['template'] == "vm":
        create_instance(project_id, zone, data['instance_name'], data['machine_type'], data['source_image'])
    if data['template'] == "s3":
        create_bucket(data['bucket_name'])