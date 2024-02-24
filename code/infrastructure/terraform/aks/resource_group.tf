resource "azurerm_resource_group" "default" {
  name     = "kubeflow-test-rg"
  location = "East US"
}