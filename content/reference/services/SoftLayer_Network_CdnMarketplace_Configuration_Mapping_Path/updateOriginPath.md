---
title: "updateOriginPath"
description: "SOAP API will update Origin Path for an existing mapping and for a particular customer. 

When passing the $input object as a parameter, it will expect the following properties to be set: $oldPath $uniqueId $originType, $path, $origin, $httpPort, $httpsPort, and if the path's origin type is object storage, the $bucketName and the $fileExtension. 

Out of the properties listed above only the following path properties are allowed to be changed: $path, $origin, $httpPort, $httpsPort These properties may not be changed: $originType "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
---

### [REST Example](#updateOriginPath-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateOriginPath-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Network_CdnMarketplace_Configuration_Input]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path/updateOriginPath'
```
