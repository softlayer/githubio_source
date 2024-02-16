---
title: "createObject"
description: "The subnet registration service has been deprecated. 

Create registration with a global registrar to associate an assigned subnet with the provided contact details. 

Contact information is provided in the form of a [SoftLayer_Account_Regional_Registry_Detail](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail), which reference can be provided when the registration is created or afterwards. Registrations without an associated person detail will remain in the ``OPEN`` status. To specify a person detail when creating a registration, the ``detailReferences`` property should be populated with a list item providing a ``detailId`` value referencing the [SoftLayer_Account_Regional_Registry_Detail](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail). 

The same applies to [SoftLayer_Account_Regional_Registry_Detail](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail), though these references need not be provided. The system will create a reference to the network described by the registration's subnet in the absence of a provided network detail reference. However, if a specific detail is referenced, it must describe the same subnet as the registration. 

A template containing the following properties will create a subnet registration: 


* networkIdentifier
* cidr
* detailReferences


``networkIdentifier`` is the base address of the public, SoftLayer owned subnet which is being registered. ``cidr`` must be an integer representing the CIDR of the subnet to be registered. The ``networkIdentifier``/``cidr`` must represent an assigned subnet. ``detailReferences`` tie the registration to SoftLayer_Account_Regional_Registry_Detail objects. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Registration"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Subnet_Registration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Registration/createObject'
```
