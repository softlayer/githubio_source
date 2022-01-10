---
title: "SoftLayer_User_Customer_ApiAuthentication"
description: "The SoftLayer_User_Customer_ApiAuthentication type contains user's authentication key(s)."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_ApiAuthentication"
---

# SoftLayer_User_Customer_ApiAuthentication
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_ApiAuthentication' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_ApiAuthentication' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_User_Customer_ApiAuthentication type contains user's authentication key(s). 


### associatedMethods

*  [SoftLayer_User_Customer::getApiAuthenticationKeys](/reference/services/SoftLayer_User_Customer/getApiAuthenticationKeys )
*  [SoftLayer_User_Customer_ApiAuthentication::getObject](/reference/services/SoftLayer_User_Customer_ApiAuthentication/getObject )



### seeAlso

* [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer )




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
[authenticationKey]: #authenticationkey
#### [authenticationKey]
The user's authentication key for API access.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The user's API authentication identifying number.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[ipAddressRestriction]: #ipaddressrestriction
#### [ipAddressRestriction]
The IP addresses or IP ranges from which this user may access the SoftLayer API. Specify subnets in CIDR format and separate multiple addresses and subnets by commas. You may combine IPv4 and IPv6 addresses and subnets, for example: 192.168.0.0/16,fe80:021b::0/64.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[timestampKey]: #timestampkey
#### [timestampKey]
The user's authentication key modification date.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
The user's identifying number.  
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
The user who owns the api authentication key.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>

## Count
</div>


