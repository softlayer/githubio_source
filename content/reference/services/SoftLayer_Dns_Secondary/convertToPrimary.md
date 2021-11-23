---
title: "convertToPrimary"
description: "A secondary DNS record may be converted to a primary DNS record. By converting a secondary DNS record, the SoftLayer name servers will be the authoritative nameserver for this domain and will be directly editable in the SoftLayer API and Portal. 

Primary DNS record conversion performs the following steps: 
* The SOA record is updated with SoftLayer's primary name server.
* All NS records are removed and replaced with SoftLayer's NS records.
* The secondary DNS record is removed.


After the DNS records are converted, the following restrictions will apply to the new domain record: 
* You will need to manage the zone record using the [[SoftLayer_Dns_Domain]] service.
* You may not edit the SOA or NS records.
* You may only edit the following resource records: A, AAAA, CNAME, MX, TX, SRV.


This change can not be undone, and the record can not be converted back into a secondary DNS record once the conversion is complete. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "convertToPrimary"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Secondary"
---
