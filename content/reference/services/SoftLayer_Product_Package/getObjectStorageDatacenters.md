---
title: "getObjectStorageDatacenters"
description: "This method will return a collection of [SoftLayer_Container_Product_Order_Network_Storage_Hub_Datacenter](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Hub_Datacenter) objects which contain a datacenter location and all the associated active usage rate prices where object storage is available. This method is really only applicable to the object storage additional service package which has a [SoftLayer_Product_Package_Type](/reference/datatypes/SoftLayer_Product_Package_Type) of '''ADDITIONAL_SERVICES_OBJECT_STORAGE'''. This information is useful so that you can see the 'pay as you go' rates per datacenter. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Package"
---

### [REST Example](#getObjectStorageDatacenters-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObjectStorageDatacenters-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/{SoftLayer_Product_PackageID}/getObjectStorageDatacenters'
```
