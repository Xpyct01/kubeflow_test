terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.67.0"
    }
  }
  backend "azurerm" {
    resource_group_name  = "StorageAccount-ResourceGroup"
    storage_account_name = var.storage_account_name
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
  }
  required_version = ">= 0.14"
}

provider "azurerm" {
  features {}
}