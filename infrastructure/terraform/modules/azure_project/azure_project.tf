resource "azuredevops_project" "azure_project" {
  name               = "kubeflow-test"
  visibility         = "private"
  version_control    = "Git"
}

resource "azuredevops_variable_group" "variable_group" {
  name       = "kubeflow-variable-group"
  project_id = azuredevops_project.azure_project.id

  variable {
    name = ""
  }
}