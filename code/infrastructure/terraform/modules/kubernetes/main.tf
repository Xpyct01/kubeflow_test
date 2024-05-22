module "flask_app" {
  source = "flask_app"
  depends_on = [kubernetes_namespace.namespace]
}

module "mongo" {
  source = "mongo"
  depends_on = [kubernetes_namespace.namespace]
}