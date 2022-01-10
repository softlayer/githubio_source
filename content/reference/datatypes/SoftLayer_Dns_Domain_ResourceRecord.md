---
title: "SoftLayer_Dns_Domain_ResourceRecord"
description: "The SoftLayer_Dns_Domain_ResourceRecord data type represents a single resource record entry in a SoftLayer hosted domain. Each resource record contains a ''host'' and ''data'' property, defining a resource's name and it's target data. Domains contain multiple types of resource records. The ''type'' property separates out resource records by type. ''Type'' can take one of the following values: 
* ''''a'''' for [SoftLayer_Dns_Domain_ResourceRecord_AType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_AType) records
* ''''aaaa'''' for [SoftLayer_Dns_Domain_ResourceRecord_AaaaType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_AaaaType) records
* ''''cname'''' for [SoftLayer_Dns_Domain_ResourceRecord_CnameType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_CnameType) records
* ''''mx'''' for [SoftLayer_Dns_Domain_ResourceRecord_MxType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_MxType) records
* ''''ns'''' for [SoftLayer_Dns_Domain_ResourceRecord_NsType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_NsType) records
* ''''ptr'''' for [SoftLayer_Dns_Domain_ResourceRecord_PtrType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_PtrType) records in reverse domains
* ''''soa'''' for a domain's [SoftLayer_Dns_Domain_ResourceRecord_SoaType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SoaType) record
* ''''spf'''' for [SoftLayer_Dns_Domain_ResourceRecord_SpfType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SpfType) records
* ''''srv'''' for [SoftLayer_Dns_Domain_ResourceRecord_SrvType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SrvType) records
* ''''txt'''' for [SoftLayer_Dns_Domain_ResourceRecord_TxtType](reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_TxtType) records


As ''SoftLayer_Dns_Domain_ResourceRecord'' objects are created and loaded, the API verifies the ''type'' property and casts the object as the appropriate type. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Dns_Domain_ResourceRecord"
---
