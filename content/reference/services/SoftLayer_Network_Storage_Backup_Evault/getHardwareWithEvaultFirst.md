---
title: "getHardwareWithEvaultFirst"
description: "Retrieve a list of hardware associated with a SoftLayer customer account, placing all hardware with associated EVault storage accounts at the beginning of the list. The return type is SoftLayer_Hardware_Server[] contains the results; the number of items returned in the result will be returned in the soap header (totalItems). ''getHardwareWithEvaultFirst'' is useful in situations where you wish to search for hardware and provide paginated output. 





Results are only returned for hardware belonging to the account of the user making the API call. 

This method drives the backup page of the SoftLayer customer portal. It serves a very specific function, but we have exposed it as it may prove useful for API developers too. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Backup_Evault"
---

# [REST Example](#getHardwareWithEvaultFirst-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getHardwareWithEvaultFirst-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean, string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/getHardwareWithEvaultFirst'
```
