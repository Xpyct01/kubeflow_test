module "fast_api" {
  source = "fast_api"
  depends_on = [kubernetes_namespace.namespace]
}

module "mongo" {
  source = "mongo"
  depends_on = [kubernetes_namespace.namespace]
}