resource "azurerm_kubernetes_cluster" "cluster" {
  name                = "kubeflow-test-aks"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  dns_prefix          = "kubeflow-test-k8s"
  kubernetes_version  = "1.27.9"

  default_node_pool {
    name            = "default"
    min_count = 1
    max_count = 5
    node_count      = 3
    vm_size         = "Standard_A2m_v2"
    os_disk_size_gb = 30
    enable_auto_scaling = true
  }

  service_principal {
    client_id     = var.aks_service_principal_app_id
    client_secret = var.aks_service_principal_client_secret
  }

  role_based_access_control_enabled = true

  tags = {
    environment = "Dev"
  }
}
