provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "minikube"
}

module "aks" {
  source = "./modules/aks"
  aks_service_principal_app_id        = var.aks_service_principal_app_id
  aks_service_principal_client_secret = var.aks_service_principal_client_secret
}