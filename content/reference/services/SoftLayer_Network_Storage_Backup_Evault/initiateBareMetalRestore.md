---
title: "initiateBareMetalRestore"
description: "Evault Bare Metal Restore is a special version of Rescue Kernel designed specifically for making full system restores made with Evault's BMR backup. This process works very similar to Rescue Kernel, except only the Evault restore program is available. The process takes approximately 10 minutes. Once completed you will be able to access your server to do a restore through VNC or your servers KVM-over-IP. IP information and credentials can be found on the hardware page of the customer portal. The Evault Application will be running automatically upon startup, and will walk you through the restore process. "
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

### [REST Example](#initiateBareMetalRestore-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#initiateBareMetalRestore-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/initiateBareMetalRestore'
```
