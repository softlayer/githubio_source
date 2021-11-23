---
title: "SoftLayer_Dns_Domain_ResourceRecord"
description: "Every domain record hosted on the SoftLayer name servers is comprised of a series or resource records that control how the domain operates, translates host names, and translates service location. Each of those resource records is controlled by the SoftLayer_Dns_Domain_ResourceRecord service. SoftLayer domains have the following resource records: 
* A single SOA record
* A records
* AAAA records
* Optional CNAME records
* At least one MX record
* NS records for ns1.softlayer.com and ns2.softlayer.com
* Optional TXT records
* Optional SPF records


The SoftLayer_Dns_Domain_ResourceRecords service also controls the records contained in reverse DNS records. SoftLayer_Dns_Domain_Reverse records contain multiple PTR type resource records. 

As with domain changes, resource record changes happen immediately, but may take up to 72 hours to propagate to the rest of the Internet's name servers. The SoftLayer_Dns_Domain_ResourceRecord service only applies to domains hosted on the SoftLayer name servers. "
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
