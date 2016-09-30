---
title: "Create a SoftLayer Virtual Guest"
description: "Terraform code to create a SoftLayer virtual guest."
date: "2016-09-30"
tags:
  - "cli"
---

This example will create a virtual guest running the latest offered version of Ubuntu in the Dallas 09 Datacenter. 

### Configuration File

```
provider "softlayer" {}

# Virtual Server created with existing SSH Key already in SoftLayer 

resource "softlayer_virtual_guest" "terraform" {
    name = "terraform"
    domain = "tinylab.info"
    ssh_keys = ["563523"]
    image = "UBUNTU_LATEST_64"
    region = "dal09"
    public_network_speed = 100
    cpu = 1
    ram = 1024
    local_disk = "false"
    hourly_billing = "true"
}
```

### Terraform Plan

The `terraform plan` command will look at any `.tf` file in the current directory and show you what Terraform would do if we applied the configuration aka running `terraform apply`.

```
$ terraform plan

+ softlayer_virtual_guest.terraform
    cpu:                  "1"
    domain:               "tinylab.info"
    hourly_billing:       "true"
    image:                "UBUNTU_LATEST_64"
    ipv4_address:         "<computed>"
    ipv4_address_private: "<computed>"
    local_disk:           "false"
    name:                 "terraform"
    private_network_only: "false"
    public_network_speed: "100"
    ram:                  "1024"
    region:               "dal09"
    ssh_keys.#:           "1"
    ssh_keys.0:           "563523"


Plan: 1 to add, 0 to change, 0 to destroy.
```

### Terraform apply 

```
$ terraform apply 

  cpu:                  "" => "1"
  domain:               "" => "tinylab.info"
  hourly_billing:       "" => "true"
  image:                "" => "UBUNTU_LATEST_64"
  ipv4_address:         "" => "<computed>"
  ipv4_address_private: "" => "<computed>"
  local_disk:           "" => "false"
  name:                 "" => "terraform"
  private_network_only: "" => "false"
  public_network_speed: "" => "100"
  ram:                  "" => "1024"
  region:               "" => "dal09"
  ssh_keys.#:           "" => "1"
  ssh_keys.0:           "" => "563523"

$ terraform show 

softlayer_virtual_guest.terraform:
  id = 24618829
  cpu = 1
  dedicated_acct_host_only = false
  domain = tinylab.info
  hourly_billing = true
  image = UBUNTU_LATEST_64
  ipv4_address = 169.44.104.77
  ipv4_address_private = 10.143.223.17
  local_disk = false
  name = terraform
  private_network_only = true
  public_network_speed = 100
  ram = 1024
  region = dal09
  ssh_keys.# = 1
  ssh_keys.0 = 563523
```
