resource "kubernetes_service" "app-service" {
  metadata {
    name = "flask-app"
    namespace = var.namespace_name
  }
  spec {
    selector = {
      app : "flask-app"
    }
    port {
      port = "5000"
      target_port = "5000"
    }
    type = "LoadBalancer"
  }
}