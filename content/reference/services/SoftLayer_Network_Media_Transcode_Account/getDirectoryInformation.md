---
title: "getDirectoryInformation"
description: "This method returns a collection of SoftLayer_Container_Network_Ftp_Directory objects. You can retrieve directory information for /in and /out directories. A [SoftLayer_Container_Network_Directory_Listing](/reference/datatypes/SoftLayer_Container_Network_Directory_Listing) object contains a type (indicating whether it is a file or a directory), name and file count if it is a directory. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Media_Transcode_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Media_Transcode_Account/{SoftLayer_Network_Media_Transcode_AccountID}/getDirectoryInformation'
```
