resource "azurerm_resource_group" "cluster_rg" {
  name     = "kubeflow-test-rg"
  location = "East US"
}