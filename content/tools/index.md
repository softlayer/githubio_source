---
title: "Tools"
description: "These are external tools which integrate with SoftLayer. Please select one below to see details"
date: "2015-09-16"
tags:
    - "tools"
    - "devops"
---


### [Ansible](/ansible/)

Ansible offers an agentless way to administer your servers and is a great way to quickly make changes across your infrastructure.

---
### [Vagrant](/vagrant/)

Vagrant allows for development environments to be configured in consistent ways and can provision SoftLayer servers as part of the environment creation process. Use the following command to install the SoftLayer vagrant plugin:
`vagrant plugin install vagrant-softlayer`

---
### [SoftLayer CLI](https://softlayer.github.io/softlayer-python/)

The SoftLayer CLI tool is bundled with the softlayer-python project and offers access to many API functions from the command line. Additional information and documentation can be [found here](https://softlayer.github.io/softlayer-python/).

---
#### [Salt-Cloud](https://docs.saltstack.com/en/develop/topics/cloud/index.html)
Salt-Cloud is a part of [SaltStack](http://saltstack.com/) which is a python based configuration management platform. Salt-Cloud can provision [Virtual Guests](https://docs.saltstack.com/en/develop/ref/clouds/all/salt.cloud.clouds.softlayer.html) and [Bare Metal Instances](https://docs.saltstack.com/en/latest/ref/clouds/all/salt.cloud.clouds.softlayer_hw.html) on SoftLayer's platform, along with a variety of other providers.
See the [Getting Started](http://salt-cloud.readthedocs.org/en/latest/topics/softlayer.html) guide for more details.