---
title: "Getting started with SoftLayer and Terraform"
description: "Some general getting started information for using Terraform with SoftLayer."
date: "2016-09-30"
tags:
  - "cli"
---

### Overview

Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions. Terraform supports several Cloud Service providers by default but is also extensible with plugins written in Go.

The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

### Installing Terraform

You can grab the installer for your specific Operating System on the Terraform [Download Page](https://www.terraform.io/downloads.html). Terraform will run on OS X, Linux, FreeBSD and Windows.


### Terraform Configuration 

Terraform uses text files to describe infrastructure and to set variables. These text files are called Terraform configurations and end in `.tf`. This section talks about the format of these files as well as how they're loaded.

The format of the configuration files are able to be in two formats: Terraform format and JSON. The Terraform format is more human-readable, supports comments, and is the generally recommended format for most Terraform files. The JSON format is meant for machines to create, modify, and update, but can also be done by Terraform operators if you prefer. Terraform format ends in `.tf` and JSON format ends in `.tf.json`.

If you don't want to put credentials in your configuration file, you can leave them out and use `provider "softlayer" {}` in the configuration file and instead set these environment variables:

SOFTLAYER_USERNAME: Your SoftLayer username
SOFTLAYER_API_KEY: Your API key
