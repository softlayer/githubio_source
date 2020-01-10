---
title: "SoftLayer_Event_Log"
description: "The SoftLayer_Event_Log data type contains an event detail occurred upon various SoftLayer resources."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Event"
classes:
    - "SoftLayer_Event_Log"
---

# SoftLayer_Event_Log
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Event_Log' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Event_Log' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Event_Log data type contains an event detail occurred upon various SoftLayer resources. 





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
Account id with which the event is associated   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[eventCreateDate]: #eventcreatedate
#### [eventCreateDate]
Event creation date in millisecond precision   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[eventName]: #eventname
#### [eventName]
Event name such as "reboot", "cancel", "update host" and so on.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
The remote IP Address that made the request   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[label]: #label
#### [label]
Label or description of the event object   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[metaData]: #metadata
#### [metaData]
Meta data for an event in JSON string   
<span class="type-label">Type: </span>**JSON string**


</div>
<div class="prop-row">

-----
[objectId]: #objectid
#### [objectId]
Event object id   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[objectName]: #objectname
#### [objectName]
Event object name such as "server", "dns" and so on.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[openIdConnectUserName]: #openidconnectusername
#### [openIdConnectUserName]
OpenIdConnectUserName of the customer who initiated the event   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
A resource object that is associated with the event  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a>**


</div>
<div class="prop-row">

-----
[traceId]: #traceid
#### [traceId]
A unique trace id. Multiple event can be grouped by a trace id.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
Id of customer who initiated the event   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[userType]: #usertype
#### [userType]
Type of user that triggered the event. User type can be CUSTOMER, EMPLOYEE or SYSTEM.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
Customer username who initiated the event   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[user]: #user
#### [user]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>

## Count
</div>


