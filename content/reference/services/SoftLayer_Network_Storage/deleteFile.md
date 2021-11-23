---
title: "deleteFile"
description: "{{CloudLayerOnlyMethod}} Delete an individual file within a Storage account. Depending on the type of Storage account, Deleting a file either deletes the file permanently or sends the file to your account's recycle bin. 

Currently, Virtual Server storage is the only type of Storage account that sends files to a recycle bin when deleted. When called against a Virtual Server storage account , this method also determines if the file is in the account's recycle bin. If the file exist in the recycle bin, then it is permanently deleted. 

Please note, a file can not be restored once it is permanently deleted. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "deleteFile"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---
