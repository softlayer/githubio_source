---
title: "getDirectoryInformation"
description: "This method returns an array of [[SoftLayer_Container_Network_Directory_Listing|Directory Listing]] objects. You must ha... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getDirectoryInformation"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getDirectoryInformation

Returns a directory list


## Overview 
This method returns an array of [[SoftLayer_Container_Network_Directory_Listing|Directory Listing]] objects. You must have CDN_FILE_MANAGE privilege and you can only retrieve directory information within <b>/media</b> directory. A [[SoftLayer_Container_Network_Directory_Listing|Directory Listing]] object contains type (indicating whether it is a file or a directory), name and file count if it is a directory. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|directoryName| string| directory name|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_Directory_Listing'>SoftLayer_Container_Network_Directory_Listing[] </a>

