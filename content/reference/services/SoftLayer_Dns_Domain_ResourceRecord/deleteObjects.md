---
title: "deleteObjects"
description: "Remove multiple resource records from a domain. This follows the same logic as ''deleteObject'' and '''cannot be undone'''. The serial number of the domain associated with this resource record is updated upon deletion. You may not delete SOA records, PTR records, or NS resource records that point to ns1.softlayer.com or ns2.softlayer.com. 

''deleteObjects'' returns Boolean ''true'' on successful deletion or ''false'' if it was unable to remove a resource record. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_ResourceRecord"
---
