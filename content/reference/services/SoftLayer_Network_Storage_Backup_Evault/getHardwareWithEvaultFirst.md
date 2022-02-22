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
