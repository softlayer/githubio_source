---
title: "Tools"
description: "These are external tools which integrate with SoftLayer. Please select one below to see details"
date: "2015-09-16"
tags:
    - "tools"
    - "devops"
---


### [Bluemix for AWS professionals](/tools/compareorator/index.html)

### [Ansible](/ansible/)

Ansible offers an agentless way to administer your servers and is a great way to quickly make changes across your infrastructure.

---
### [Vagrant](/vagrant/)

Vagrant allows for development environments to be configured in consistent ways and can provision SoftLayer servers as part of the environment creation process.

Use the following command to install the SoftLayer vagrant plugin:
`vagrant plugin install vagrant-softlayer`

---
### [SoftLayer CLI](https://softlayer.github.io/softlayer-python/)

The SoftLayer CLI tool is bundled with the softlayer-python project and offers access to many API functions from the command line. Additional information and documentation can be [found here](https://softlayer.github.io/softlayer-python/).

---
### [Salt-Cloud](https://docs.saltstack.com/en/latest/topics/cloud/index.html)
Salt-Cloud is a part of [SaltStack](http://saltstack.com/) which is a python based configuration management platform. Salt-Cloud can provision [Virtual Guests](https://docs.saltstack.com/en/develop/ref/clouds/all/salt.cloud.clouds.softlayer.html) and [Bare Metal Instances](https://docs.saltstack.com/en/latest/ref/clouds/all/salt.cloud.clouds.softlayer_hw.html) on SoftLayer's platform, along with a variety of other providers.

See the [Getting Started](http://salt-cloud.readthedocs.org/en/latest/topics/softlayer.html) guide for more details.

---
### [Fog-Softlayer](/fog/)

A module for the 'fog' gem to support SoftLayer. This gem is a module for the fog gem that allows you to manage resources in the SoftLayer Cloud. It is included by the main fog metagem but can used as an independent library in other applications.

See the [Getting Started](https://github.com/fog/fog-softlayer/blob/master/examples/getting_started.md) guide for more details.

---
### [Apache Libcloud](https://libcloud.apache.org/)

Apache Libcloud is a Python library which hides allows you to manage different cloud resources through a unified and easy to use API. Libcloud can provision [Virtual Guests](https://libcloud.readthedocs.org/en/latest/apidocs/libcloud.compute.drivers.html#module-libcloud.compute.drivers.softlayer), manage SSH keys, interact with Load Balancers, manage DNS, and a whole lot more.

See the [Getting Started](https://libcloud.readthedocs.org/en/latest/getting_started.html) guide for more details.

---
### [Terraform](/terraform/)

Terraform provides a common configuration to launch infrastructure — from physical and virtual servers to email and DNS providers.
