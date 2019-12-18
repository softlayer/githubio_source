---
title: "SoftLayer_User_Customer_Link_ThePlanet"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Link_ThePlanet"
---

# SoftLayer_User_Customer_Link_ThePlanet
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Link_ThePlanet' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[defaultFlag]: #defaultflag
#### [defaultFlag]
  
<span class="type-label">Type: </span>**integer**

-----
[destinationUserAlphanumericId]: #destinationuseralphanumericid
#### [destinationUserAlphanumericId]
  
<span class="type-label">Type: </span>**string**

-----
[destinationUserId]: #destinationuserid
#### [destinationUserId]
  
<span class="type-label">Type: </span>**integer**

-----
[iamIdVerificationFlag]: #iamidverificationflag
#### [iamIdVerificationFlag]
  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[realm]: #realm
#### [realm]
The realm of the IAMid unique identifier.  
<span class="type-label">Type: </span>**string**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
  
<span class="type-label">Type: </span>**integer**

-----
[uniqueIdentifier]: #uniqueidentifier
#### [uniqueIdentifier]
The IAMid Unique Identifier formed in the format of "realm-uniqueIdentifier"  
<span class="type-label">Type: </span>**string**

-----
[userId]: #userid
#### [userId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**

-----
[user]: #user
#### [user]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count
</div>


