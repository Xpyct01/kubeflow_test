resource "helm_release" "jupyter_notebook" {
  name       = "jupyter-notebook"
  repository = "https://jupyterhub.github.io/helm-chart/"
  chart      = "jupyterhub"
  version    = "1.1.0"
}