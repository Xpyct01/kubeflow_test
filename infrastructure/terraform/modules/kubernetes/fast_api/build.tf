variable "image_name" {
  default = "flask-app"
}

variable "dockerfile_location" {
  default = "/path/to/your/dockerfile"
}

resource "null_resource" "build_docker_image" {
  provisioner "local-exec" {
    command = "docker build -t ${var.image_name} ${var.dockerfile_location}"
  }
}
