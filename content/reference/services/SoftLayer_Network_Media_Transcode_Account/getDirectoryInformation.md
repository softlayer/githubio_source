---
title: "getDirectoryInformation"
description: "This method returns a collection of SoftLayer_Container_Network_Ftp_Directory objects. You can retrieve directory inform... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
---
# SoftLayer_Network_Media_Transcode_Account::getDirectoryInformation
## Overview 
This method returns a collection of SoftLayer_Container_Network_Ftp_Directory objects. You can retrieve directory information for /in and /out directories. A [[SoftLayer_Container_Network_Directory_Listing|Directory Listing]] object contains a type (indicating whether it is a file or a directory), name and file count if it is a directory. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|directoryName| string| comma separated Extensions to restrict results to|
|extensionFilter| string| A directory name|


### Required Headers
* authenticate
* SoftLayer_Network_Media_Transcode_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_Directory_Listing'>SoftLayer_Container_Network_Directory_Listing[] </a>
