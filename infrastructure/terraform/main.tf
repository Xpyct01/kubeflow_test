terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.67.0"
    }
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
  backend "azurerm" {}
  required_version = ">= 0.14"
}

provider "azurerm" {
  features {}
}