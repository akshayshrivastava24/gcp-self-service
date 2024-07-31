module "lb-http" {
  source  = "terraform-google-modules/lb-http/google//modules/serverless_negs"
  version = "~> 10.0"

  name    = var.lb_name
  project = var.project_id

  ssl                             = var.ssl
  managed_ssl_certificate_domains = [var.domain]
  https_redirect                  = var.ssl
  labels                          = { "example-label" = "cloud-run-example" }

  backends = {
    default = {
      description = null
      groups = [
        {
          group = google_compute_region_network_endpoint_group.serverless_neg.id
        }
        
      ]
      enable_cdn = false

      iap_config = {
        enable = false
      }
      log_config = {
        enable = false
      }
    }
  }
}





resource "google_cloud_run_service_iam_member" "public-access" {
  location = google_cloud_run_service.default.location
  project  = google_cloud_run_service.default.project
  service  = google_cloud_run_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}