---
title: "SoftLayer_User_Access_Facility_Log"
description: "This class represents a login/logout sheet for facility visitors."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Access_Facility_Log"
---

# SoftLayer_User_Access_Facility_Log
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Access_Facility_Log' >Datatype</a></li>
    </ul>
</div>

## Description 


This class represents a login/logout sheet for facility visitors.





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
This is the account associated with a log record. For a customer logging into a datacenter, this is the customer's account. For a contractor or any other guest logging into a customer's cabinet or colocation cage, this is the customer's account.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
This is a short description of why the person is at the location.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[locationId]: #locationid
#### [locationId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[timeIn]: #timein
#### [timeIn]
This is the date and time the person arrived.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[timeOut]: #timeout
#### [timeOut]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
This is the account associated with the log entry. For users under a customer's account, it is the customer's account. For contractors and others visiting a colocation area, it is the account associated with the area they visited.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[datacenter]: #datacenter
#### [datacenter]
This is the location of the facility.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
This is the colocation hardware that was visited.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[logType]: #logtype
#### [logType]
This is the type of person entering the facility.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Access_Facility_Log_Type'>SoftLayer_User_Access_Facility_Log_Type </a>**  



</div>
<div class="prop-row">

-----
[visitor]: #visitor
#### [visitor]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a>**  



</div>

## Count
</div>


