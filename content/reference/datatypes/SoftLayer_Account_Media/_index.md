---
title: "SoftLayer_Account_Media"
description: "The SoftLayer_Account_Media data type contains information on a single piece of media associated with a Data Transfer Se... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Media"
---

# SoftLayer_Account_Media
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Media' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Media' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Media data type contains information on a single piece of media associated with a Data Transfer Service request. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[description]: #description
#### [description]
The description of the media.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique id of the media.  
<span class="type-label">Type: </span>**integer**

-----
[requestId]: #requestid
#### [requestId]
The request id of the media.  
<span class="type-label">Type: </span>**integer**

-----
[serialNumber]: #serialnumber
#### [serialNumber]
The manufacturer's serial number of the media.  
<span class="type-label">Type: </span>**string**

-----
[typeId]: #typeid
#### [typeId]
The type id of the media.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account to which the media belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[createUser]: #createuser
#### [createUser]
The customer user who created the media object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[datacenter]: #datacenter
#### [datacenter]
The datacenter where the media resides.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[modifyEmployee]: #modifyemployee
#### [modifyEmployee]
The employee who last modified the media.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[modifyUser]: #modifyuser
#### [modifyUser]
The customer user who last modified the media.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[request]: #request
#### [request]
The request to which the media belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Media_Data_Transfer_Request'>SoftLayer_Account_Media_Data_Transfer_Request </a>**

-----
[type]: #type
#### [type]
The media's type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Media_Type'>SoftLayer_Account_Media_Type </a>**

-----
[volume]: #volume
#### [volume]
A guest's associated EVault network storage service account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


## Count
</div>


