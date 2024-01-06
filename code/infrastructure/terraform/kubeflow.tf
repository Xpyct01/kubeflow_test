# set up kubeflow
module "kubeflow_manifests" {
  source = "github.com/kubeflow//manifests"
}

resource "null_resource" "kubeflow" {
  depends_on = [module.kubeflow_manifests, kubernetes_namespace.namespace]
  provisioner "local-exec" {
    command = <<-EOT
      kubectl apply -k common/istio-1-17/istio-crds/base
      kubectl apply -k common/istio-1-17/istio-namespace/base
      kubectl apply -k common/istio-1-17/istio-install/base
    EOT
    working_dir = path.module
  }

  provisioner "local-exec" {
    command = "kubectl apply -k common/istio-1-17/kubeflow-istio-resources/base"
    working_dir = path.module
  }

  provisioner "local-exec" {
    command = "kubectl apply -k common/kubeflow-roles/base"
    working_dir = path.module
  }

  provisioner "local-exec" {
    command = "kubectl apply -k common/oidc-client/oidc-authservice/base"
    working_dir = path.module
  }

  provisioner "local-exec" {
    command = "kubectl apply -k apps/profiles/upstream/overlays/kubeflow"
    working_dir = path.module
  }

  provisioner "local-exec" {
    command = "kubectl apply -k apps/pipeline/upstream/env/cert-manager/platform-agnostic-multi-user"
    working_dir = path.module
  }
}