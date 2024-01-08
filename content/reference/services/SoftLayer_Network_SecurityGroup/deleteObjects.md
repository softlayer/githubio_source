---
title: "deleteObjects"
description: "Delete security groups for an account. A security group cannot be deleted if any network components are attached or if the security group is a remote security group for a [SoftLayer_Network_SecurityGroup_Rule](/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule). "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_SecurityGroup"
---

### [REST Example](#deleteObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_SecurityGroup]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/deleteObjects'
```
