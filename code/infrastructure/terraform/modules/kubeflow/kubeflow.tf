module "kubeflow_manifests" {
  source = "github.com/Azure/kubeflow-aks"
}

variable "kubeflow_manifests_path" {
  default = "./.terraform/modules/kubeflow_manifests/manifests"
}

resource "local_file" "kubeconfig" {
  filename     = "kubeconfig"
  content      = var.kubeconfig
}

resource "null_resource" "kubeflow" {
  depends_on = [module.kubeflow_manifests, local_file.kubeconfig.filename]

  provisioner "local-exec" {
    command = "export KUBECONFIG=$PWD/${local_file.kubeconfig.filename}"
  }

  provisioner "local-exec" {
    command = "while ! kubectl apply -k vanilla; do echo 'Retrying to apply resources'; sleep 10; done"
    working_dir = var.kubeflow_manifests_path
  }
}