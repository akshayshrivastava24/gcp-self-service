resource "google_compute_region_network_endpoint_group" "serverless_neg_tomcat" {
  provider              = google-beta
  name                  = "serverless-neg-tomcat"
  network_endpoint_type = "SERVERLESS"
  region                = var.region
  project = var.project_id
  cloud_run {
    service = google_cloud_run_service.tomcat.name
  }
}

resource "google_cloud_run_service" "tomcat" {
  name     = "tomcat"
  location = var.region
  project  = var.project_id

  template {
    spec {
      containers {
        image = "tomcat"
        ports {
          container_port = 8080
        }    
      }
    }
  }
  metadata {
    annotations = {
      # For valid annotation values and descriptions, see
      # https://cloud.google.com/sdk/gcloud/reference/run/deploy#--ingress
      "run.googleapis.com/ingress" = "all"
    }
  }
}


# resource "google_compute_backend_service" "tomcat" {
#   provider = google-beta
#   project = var.project_id
#   name    = "tomcat-backend"

#   load_balancing_scheme = var.load_balancing_scheme

# #   port_name = lookup(each.value, "port_name", "http")
# #   protocol  = lookup(each.value, "protocol", "HTTP")

# #   description                     = lookup(each.value, "description", null)
# #   connection_draining_timeout_sec = lookup(each.value, "connection_draining_timeout_sec", null)
# #   enable_cdn                      = lookup(each.value, "enable_cdn", false)
# #   compression_mode                = lookup(each.value, "compression_mode", "DISABLED")
# #   custom_request_headers          = lookup(each.value, "custom_request_headers", [])
# #   custom_response_headers         = lookup(each.value, "custom_response_headers", [])
# #   session_affinity                = lookup(each.value, "session_affinity", null)
# #   affinity_cookie_ttl_sec         = lookup(each.value, "affinity_cookie_ttl_sec", null)
# #   locality_lb_policy              = lookup(each.value, "locality_lb_policy", null)


#   # To achieve a null backend edge_security_policy, set each.value.edge_security_policy to "" (empty string), otherwise, it fallsback to var.edge_security_policy.
# #   edge_security_policy = lookup(each.value, "edge_security_policy") == "" ? null : (lookup(each.value, "edge_security_policy") == null ? var.edge_security_policy : each.value.edge_security_policy)

# #   # To achieve a null backend security_policy, set each.value.security_policy to "" (empty string), otherwise, it fallsback to var.security_policy.
# #   security_policy = lookup(each.value, "security_policy") == "" ? null : (lookup(each.value, "security_policy") == null ? var.security_policy : each.value.security_policy)

#   backend {
#     group =  google_compute_region_network_endpoint_group.serverless_neg_tomcat.id
#   }
# }

# resource "google_compute_url_map" "tomcat" {
#   name            = "url-map"
#   project = var.project_id
#   default_service = google_compute_backend_service.tomcat.id

#   host_rule {
#     hosts        = ["toomcat.private.net"]
#     path_matcher = "allpaths"
#   }

#   path_matcher {
#     name            = "allpaths"
#     default_service = google_compute_backend_service.tomcat.id

#     path_rule {
#       paths   = ["/*"]
#       service = google_compute_backend_service.tomcat.id
#     }
#   }
# }