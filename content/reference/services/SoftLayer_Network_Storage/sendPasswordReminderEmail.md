---
title: "sendPasswordReminderEmail"
description: "The method will retrieve the password for the StorageLayer or Virtual Server Storage Account and email the password.  The Storage Account passwords will be emailed to the master user.  For Virtual Server Storage, the password will be sent to the email address used as the username. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---

# [REST Example](#sendPasswordReminderEmail-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#sendPasswordReminderEmail-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/sendPasswordReminderEmail'
```
