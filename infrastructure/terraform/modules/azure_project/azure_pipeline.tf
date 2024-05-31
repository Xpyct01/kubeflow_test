resource "null_resource" "azure_pipeline" {
  provisioner "local-exec" {
    command = "az pipelines create --yaml-path azure_pipeline.yaml"
  }
}