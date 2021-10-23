terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=2.55.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "myRGVM"
  location = "eastus"

  tags = {
    environment = "Borrar"
  }

}

resource "azurerm_virtual_network" "vnet" {
  name                = "myVm_group-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  tags = {
    environment = "Borrar"
  }

}

resource "azurerm_subnet" "subnet" {
  name                 = "default"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefix     = "10.0.2.0/24"
}

resource "azurerm_public_ip" "publicip" {
    name                         = "myPublicIP"
    location                     = azurerm_resource_group.rg.location
    resource_group_name          = azurerm_resource_group.rg.name
    allocation_method            = "Dynamic"

  tags = {
    environment = "Borrar"
  }
}

resource "azurerm_network_interface" "ni" {
  name                = "example-nic"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.publicip.id
    }

  tags = {
    environment = "Borrar"
  }
}

resource "azurerm_network_security_group" "sg" {
  name                = "sg1"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  security_rule {
    name                       = "AllowHTTP"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "80"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "AllowRDP"
    priority                   = 101
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "3389"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  tags = {
    environment = "Borrar"
  }

}

resource "azurerm_network_interface_security_group_association" "main" {
  network_interface_id      = azurerm_network_interface.ni.id
  network_security_group_id = azurerm_network_security_group.sg.id
}

resource "azurerm_windows_virtual_machine" "vm" {
  name                = "myVm"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  size                = "Standard_D2s_v3"
  admin_username      = "azureuser"
  admin_password      = "Pa$$w0rd1234"

  #boot_diagnostics {
  #  enable=false
  #}

  network_interface_ids = [
    azurerm_network_interface.ni.id
    ]

  os_disk {
    name                 = "myOsDisk"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2019-Datacenter"
    version   = "latest"
  }

  tags = {
    environment = "Borrar"
  }
}