---
title: "uploadFile"
description: "{{CloudLayerOnlyMethod}} Upload a file to a Storage account's root directory. Once uploaded, this method returns new file entity identifier for the upload file. 

The following properties are required in the ''file'' parameter. 
*'''name''': The name of the file you wish to upload
*'''content''': The raw contents of the file you wish to upload.
*'''contentType''': The MIME-type of content that you wish to upload."
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Utility_File_Entity]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/uploadFile'
```
