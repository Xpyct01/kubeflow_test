provider "helm" {
  kubernetes {
    host                   = module.aks.kubeconfig.0.host
    client_certificate     = base64decode(module.aks.kubeconfig.0.client_certificate)
    client_key             = base64decode(module.aks.kubeconfig.0.client_key)
    cluster_ca_certificate = base64decode(module.aks.kubeconfig.0.cluster_ca_certificate)
  }
}

module "jupyterhub" {
  source = "./modules/jupyterhub"
}