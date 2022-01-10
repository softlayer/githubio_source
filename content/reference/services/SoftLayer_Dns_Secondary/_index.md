---
title: "SoftLayer_Dns_Secondary"
description: "SoftLayer's secondary DNS service allows you to use SoftLayer's name servers as a secondary server to your domain's name servers. This is accomplished through the use of zone transfers. Each record created within the secondary DNS service defines which zone is transferred, what server it is transferred from, and the frequency that zone transfers occur at. Zone transfers are performed automatically based on the transfer frequency set on the secondary DNS record. Domains created via zone transfer may not be modified by the SoftLayer portal or API. 

The secondary DNS service also provides the ability to manually initiate a zone transfer through the [SoftLayer_Dns_Secondary::transferNow](reference/datatypes/$1/#$2) method. The daemon that performs zone transfers runs once a minute, therefore it could take a full minute for the zone transfer to be completed. 

Secondary DNS transfers may periodically generate notification or error messages. Please use the [SoftLayer_Dns_Message](reference/datatypes/SoftLayer_Dns_Message) service to retrieve these notifications. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
type: "reference"
layout: "service"
mainService : "SoftLayer_Dns_Secondary"
---
