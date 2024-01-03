---
title: "sendTransferApprovalEmail"
description: "The sendTransferApprovalEmail method resends a transfer approval email message for a transfer that is in 'pending owner approval' state, to the admin contact listed for the domain at the time that the transfer request was submitted "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_Registration"
---

# [REST Example](#sendTransferApprovalEmail-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#sendTransferApprovalEmail-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/{SoftLayer_Dns_Domain_RegistrationID}/sendTransferApprovalEmail'
```
