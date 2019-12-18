---
title: "SoftLayer_Network_Service_Vpn_Overrides"
description: "Use to manually decide which subnets within your virtual private address space a SoftLayer portal VPN user may access.... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
Use to manually decide which subnets within your virtual private address space a SoftLayer portal VPN user may access.  Stores a 'white list' consisting of a collection of subnet ids matched up against user ids. This class will reject any subnets or users, that don't belong to the account holder.  Note that simply assigning overrides to a user does not enforce the rule change.  You must set the manual override flag for the VPN user in the SoftLayer_User_Customer class.  It is recommended that before you create new VPN subnet overrides, you delete any old ones for a user, since the VPN authentication system limits the number of accessible subnets by a single user to sixty four.  This holds true regardless of whether the VPN user accesses the network via SSL or PPTP.  After making any changes to a user's VPN settings, you should call SoftLayer_User_Customer::updateVpnUser() on that customer object. 





### seeAlso

* [SoftLayer_Network_Subnet](/reference/datatypes/SoftLayer_Network_Subnet )


* [SoftLayer_User_Customer](/reference/datatypes/SoftLayer_User_Customer )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [createObjects](/reference/services/SoftLayer_Network_Service_Vpn_Overrides/createObjects)
Create Softlayer portal user VPN overrides.

#### [deleteObject](/reference/services/SoftLayer_Network_Service_Vpn_Overrides/deleteObject)
Delete single override.

#### [deleteObjects](/reference/services/SoftLayer_Network_Service_Vpn_Overrides/deleteObjects)
Delete multiple entries in the overrides 'white list' for a SoftLayer portal VPN user.

#### [getObject](/reference/services/SoftLayer_Network_Service_Vpn_Overrides/getObject)
Retrieve a SoftLayer_Network_Service_Vpn_Overrides record.

#### [getSubnet](/reference/services/SoftLayer_Network_Service_Vpn_Overrides/getSubnet)
Retrieve subnet components accessible by a SoftLayer VPN portal user.

#### [getUser](/reference/services/SoftLayer_Network_Service_Vpn_Overrides/getUser)
Retrieve softLayer VPN portal user.

</div>

