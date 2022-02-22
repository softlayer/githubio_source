---
title: "SoftLayer_Dns_Domain_ResourceRecord_MxType"
description: "SoftLayer_Dns_Domain_ResourceRecord_MxType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type'' property is set to 'mx' and used to describe MX resource records. MX records control which hosts are responsible as mail exchangers for a domain. For instance, in the domain example.org, an MX record whose host is '@' and data is 'mail' says that the host 'mail.example.org' is responsible for handling mail for example.org. That means mail sent to users @example.org are delivered to mail.example.org. 

Domains can have more than one MX record if it uses more than one server to send mail through. Multiple MX records are denoted by their priority, defined by the mxPriority property. 

MX records must be defined for hosts with accompanying A or AAAA resource records. They may not point mail towards a host defined by a CNAME record. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Dns_Domain_ResourceRecord_MxType"
---
