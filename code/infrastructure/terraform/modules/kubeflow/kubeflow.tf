module "kubeflow_manifests" {
  source = "github.com/Azure/kubeflow-aks"
}

variable "kubeflow_manifests_path" {
  default = "./.terraform/modules/kubeflow_manifests/manifests"
}

resource "local_file" "kubeconfig" {
  filename     = "${var.kubeflow_manifests_path}/kubeconfig"
  content      = var.kube_config
}

resource "null_resource" "kubeflow" {
  depends_on = [module.kubeflow_manifests, local_file.kubeconfig]

  provisioner "local-exec" {
    command = "while ! kubectl apply -k vanilla --kubeconfig kubeconfig; do echo 'Retrying to apply resources'; sleep 10; done"
    working_dir = var.kubeflow_manifests_path
  }
}