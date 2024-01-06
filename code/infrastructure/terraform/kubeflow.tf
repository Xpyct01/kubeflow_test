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
      while ! kubectl apply -k example; do echo "Retrying to apply resources"; sleep 10; done
    EOT
    working_dir = var.kubeflow_repo_path
  }

  provisioner "local-exec" {
    when = destroy
    command = <<-EOT
      cd ./.terraform/modules/kubeflow_manifests
      while ! kubectl delete -k example; do echo "Retrying to apply resources"; sleep 10; done
    EOT
  }
}