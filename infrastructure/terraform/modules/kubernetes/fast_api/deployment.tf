resource "kubernetes_deployment" "app-deployment" {
  metadata {
    name = "flask-app"
    namespace = var.namespace_name
  }
  spec {
    selector {
      match_labels = {
        app: "flask-app"
      }
    }
    template {
      metadata {
        labels = {
          app: "flask-app"
        }
      }
      spec {
        container {
          name = "app"
          image = "${var.ecr_repository_url}:app"
          image_pull_policy = "Always"
          port {
            container_port = 5000
          }
        }
        restart_policy = "Always"
      }
    }
  }
}