---
title: "getFtpAttributes"
description: "This method returns your Transcode FTP login credentials to the transcode.service.softlayer.com server. 

The Transcode FTP server is available via the SoftLayer private network. There is no API method that you can upload a file to Transcode server so you need to use an FTP client. You will have /in and /out directories on the Transcode FTP server.  You will have read-write privileges for /in directory and read-only privilege for /out directory. All the files in both /in and /out directories will be deleted after 72 hours from the creation date. "
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
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Media_Transcode_Account/{SoftLayer_Network_Media_Transcode_AccountID}/getFtpAttributes'
```
