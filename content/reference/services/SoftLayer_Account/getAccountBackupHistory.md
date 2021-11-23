---
title: "getAccountBackupHistory"
description: "This method returns an array of SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails objects for the given start and end dates. Start and end dates should be be valid ISO 8601 dates. The backupStatus can be one of null, 'success', 'failed', or 'conflict'. The 'success' backupStatus returns jobs with a status of 'COMPLETED', the 'failed' backupStatus returns jobs with a status of 'FAILED', while the 'conflict' backupStatus will return jobs that are not 'COMPLETED' or 'FAILED'. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "getAccountBackupHistory"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---
