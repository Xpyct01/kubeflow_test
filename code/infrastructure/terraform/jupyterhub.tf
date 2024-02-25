resource "local_file" "kubeconfig" {
  filename     = "kubeconfig"
  content      = module.aks.kubeconfig
}

provider "helm" {
  kubernetes {
    config_path = local_file.kubeconfig.filename
  }
}

module "jupyterhub" {
  source = "./modules/jupyterhub"
}