---
title: "SoftLayer_Network_Service_Vpn_Overrides"
description: "The SoftLayer_Network_Service_Vpn_Overrides data type contains information relating user ids to subnet ids when VPN acce... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Service_Vpn_Overrides"
---

# SoftLayer_Network_Service_Vpn_Overrides
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Service_Vpn_Overrides' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Service_Vpn_Overrides' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Service_Vpn_Overrides data type contains information relating user ids to subnet ids when VPN access is manually configured.  It is essentially an entry in a 'white list' of subnets a SoftLayer portal VPN user may access. 


### associatedMethods

*  [SoftLayer_User_Customer::updateVpnUser](/reference/services/SoftLayer_User_Customer/updateVpnUser )





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
[id]: #id
#### [id]
The internal identifier of the record.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[subnetId]: #subnetid
#### [subnetId]
The identifier of a subnet accessible by the SoftLayer portal VPN user.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
The identifier of the SoftLayer portal VPN user.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[subnet]: #subnet
#### [subnet]
Subnet components accessible by a SoftLayer VPN portal user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**  



</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
SoftLayer VPN portal user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>

## Count
</div>


