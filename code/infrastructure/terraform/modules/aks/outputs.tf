output "kubeconfig" {
  value = azurerm_kubernetes_cluster.cluster.kube_config
  sensitive = true
}

output "resource_group_location" {
  value = azurerm_resource_group.cluster_rg.location
}

output "resource_group_name" {
  value = azurerm_resource_group.cluster_rg.name
}