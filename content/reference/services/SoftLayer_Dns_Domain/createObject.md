---
title: "createObject"
description: "Create a new domain on the SoftLayer name servers. The SoftLayer_Dns_Domain object passed to this function must have at least one A or AAAA resource record. 

createObject creates a default SOA record with the data: 
* '''host''': '@'
* '''data''': 'ns1.softlayer.com.'
* '''responsible person''': 'root.[your domain name].'
* '''expire''': 604800 seconds
* '''refresh''': 3600 seconds
* '''retry''': 300 seconds
* '''minimum''': 3600 seconds


If your new domain uses the .de top-level domain then SOA refresh is set to 10000 seconds, retry is set to 1800 seconds, and minimum to 10000 seconds. 

If your domain doesn't contain NS resource records for ns1.softlayer.com or ns2.softlayer.com then ''createObject'' will create them for you. 

''createObject'' returns a Boolean ''true'' on successful object creation or ''false'' if your domain was unable to be created.. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain"
---
