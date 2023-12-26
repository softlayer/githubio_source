---
title: "getFileDetail"
description: "This method returns detailed information of a media file that resides in the Transcode FTP server. A [SoftLayer_Container_Network_Media_Information](/reference/datatypes/SoftLayer_Container_Network_Media_Information) object contains media details such as file size, media format, frame rate, aspect ratio and so on.  This information is merely for reference purposes. You should not rely on this data. Our library grabs small pieces of data from a media file to gather media details.  This information may not be available for some files. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Media_Transcode_Account/{SoftLayer_Network_Media_Transcode_AccountID}/getFileDetail'
```
