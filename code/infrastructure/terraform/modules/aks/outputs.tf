output "kubeconfig" {
  value = azurerm_kubernetes_cluster.cluster.kube_config
  sensitive = true
}