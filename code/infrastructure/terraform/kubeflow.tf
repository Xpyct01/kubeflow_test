module "kubeflow" {
  source = "./modules/kubeflow"
  kube_config = module.aks.kube_config
}