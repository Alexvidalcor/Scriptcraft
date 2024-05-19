# Terraform Azure Windows VM Deployment

This repository contains Terraform scripts to deploy a Windows Virtual Machine in Azure.

## Prerequisites
- [Terraform](https://www.terraform.io/downloads.html) installed.
- Azure CLI authenticated.

## Usage
1. Clone the repository:
    ```sh
    git clone <repo-url>
    cd <repo-directory>
    ```
2. Initialize Terraform:
    ```sh
    terraform init
    ```
3. Review and apply the plan:
    ```sh
    terraform plan
    terraform apply
    ```

## Resources Created
- Azure Resource Group
- Virtual Network
- Subnet
- Network Interface
- Public IP
- Windows Virtual Machine

## Clean Up
To destroy the resources, run:
```sh
terraform destroy
```


## Disclaimer

This script was created for academic purposes and is not intended for professional use. There is no guarantee that it will function properly.
