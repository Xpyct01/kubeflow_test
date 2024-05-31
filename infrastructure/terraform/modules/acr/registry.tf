resource "azurerm_container_registry" "registry" {
  location            = resource_group_location
  name                = "registry"
  resource_group_name = resource_group_name
  sku                 = "Basic"
}