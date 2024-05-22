resource "azuredevops_project" "azure_project" {
  name               = "kubeflow-test"
  visibility         = "private"
  version_control    = "Git"
}