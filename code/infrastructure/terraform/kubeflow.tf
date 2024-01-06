# set up kubeflow
module "kubeflow_manifests" {
  source = "github.com/kubeflow/manifests"
}

variable "kubeflow_repo_path" {
  default = "./.terraform/modules/kubeflow_manifests"
}

resource "null_resource" "kubeflow" {
  depends_on = [module.kubeflow_manifests, kubernetes_namespace.namespace]

  provisioner "local-exec" {
    command = <<-EOT
      while ! kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 10; done
    EOT
    working_dir = var.kubeflow_repo_path
  }
}