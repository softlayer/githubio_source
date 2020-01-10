---
title: "SoftLayer_User_Customer_AdditionalEmail"
description: "The SoftLayer_User_Customer_AdditionalEmail data type contains the additional email for use in ticket update notificatio... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_AdditionalEmail"
---

# SoftLayer_User_Customer_AdditionalEmail
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_AdditionalEmail' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_Customer_AdditionalEmail data type contains the additional email for use in ticket update notifications. 


### associatedMethods

*  [SoftLayer_User_Customer_AdditionalEmail::getObject](/reference/services/SoftLayer_User_Customer_AdditionalEmail/getObject )
*  [SoftLayer_Ticket::attachedAdditionalEmails](/reference/services/SoftLayer_Ticket/attachedAdditionalEmails )
*  [SoftLayer_User_Customer::additionalEmails](/reference/services/SoftLayer_User_Customer/additionalEmails )





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
[email]: #email
#### [email]
Email assigned to user for use in ticket update notifications.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
An internal identifier for the portal user who this additional email belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[user]: #user
#### [user]
The portal user that owns this additional email address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>

## Count
</div>


