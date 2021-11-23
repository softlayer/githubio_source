---
title: "deleteObject"
description: "Delete a domain's SRV record. '''This cannot be undone.''' Be wary of running this method. If you remove a resource record in error you will need to re-create it by creating a new SoftLayer_Dns_Domain_ResourceRecord_SrvType object. The serial number of the domain associated with this SRV record is updated upon deletion. 

''deleteObject'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "deleteObject"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
---
