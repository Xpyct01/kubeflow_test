output "cluster_name" {
  value = azurerm_kubernetes_cluster.cluster.name
}

output "resource_group_name" {
  value = azurerm_resource_group.cluster_rg.name
}

output "kubeconfig" {
  value = azurerm_kubernetes_cluster.cluster.kube_config_raw
}