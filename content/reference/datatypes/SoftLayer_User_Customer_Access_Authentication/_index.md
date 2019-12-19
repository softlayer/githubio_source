---
title: "SoftLayer_User_Customer_Access_Authentication"
description: "SoftLayer_User_Customer_Access_Authentication models a single attempt to log into the SoftLayer customer portal. A SoftL... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Access_Authentication"
---

# SoftLayer_User_Customer_Access_Authentication
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_User_Customer_Access_Authentication models a single attempt to log into the SoftLayer customer portal. A SoftLayer_User_Customer_Access_Authentication record is created every time a user attempts to log into the portal. Use this service to audit your users' portal activity and diagnose potential security breaches of your SoftLayer portal accounts. 

Unsuccessful login attempts can be caused by an incorrect password, failing to answer or not answering a login security question if the user has them configured, or attempting to log in from an IP address outside of the user's IP address restriction list. 

SoftLayer employees periodically log into our customer portal as users to diagnose portal issues, verify settings and configuration, and to perform maintenance on your account or services. SoftLayer employees only log into customer accounts from the following IP ranges: 
* 2607:f0d0:1000::/48
* 2607:f0d0:2000::/48
* 2607:f0d0:3000::/48
* 66.228.118.67/32
* 66.228.118.86/32


### associatedMethods

*  [SoftLayer_User_Customer::getLoginAttempts](/reference/services/SoftLayer_User_Customer/getLoginAttempts )
*  [SoftLayer_User_Customer::getSuccessfulLogins](/reference/services/SoftLayer_User_Customer/getSuccessfulLogins )
*  [SoftLayer_User_Customer::getUnsuccessfulLogins](/reference/services/SoftLayer_User_Customer/getUnsuccessfulLogins )



### seeAlso

* [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer )




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
The date of an attempt to log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**dateTime**

-----
[ipAddress]: #ipaddress
#### [ipAddress]
The IP address of the user who attempted to log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**string**

-----
[successFlag]: #successflag
#### [successFlag]
Whether an attempt to log into the SoftLayer customer portal was successful or not.  
<span class="type-label">Type: </span>**boolean**

-----
[userId]: #userid
#### [userId]
The internal identifier of the user who attempted to log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**integer**

-----
[username]: #username
#### [username]
The username used when attempting to log into the SoftLayer customer portal  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[user]: #user
#### [user]
The user who has attempted to log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count
</div>


