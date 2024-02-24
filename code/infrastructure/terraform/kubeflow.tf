module "kubeflow" {
  source = "./modules/kubeflow"
  cluster_name        = module.aks.cluster_name
  resource_group_name = module.aks.resource_group_name
}