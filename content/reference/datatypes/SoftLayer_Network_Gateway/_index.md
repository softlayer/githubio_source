---
title: "SoftLayer_Network_Gateway"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
---

# SoftLayer_Network_Gateway
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Gateway' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Gateway' >Datatype</a></li>
    </ul>
</div>

## Description 






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
The internal identifier of the account assigned to this gateway.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[groupNumber]: #groupnumber
#### [groupNumber]
The VRRP group number for this gateway. This is set internally and cannot be provided on create.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A gateway's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A gateway's name. This is required on create and can be no more than 255 characters.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkSpace]: #networkspace
#### [networkSpace]
A gateway's network space. Currently, only 'private'  or 'both' is allowed. When this value is 'private', it is a backend gateway only. Otherwise, it is a gateway for both frontend and backend traffic.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[privateIpAddressId]: #privateipaddressid
#### [privateIpAddressId]
The internal identifier of the private IP address for this gateway.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[privateVlanId]: #privatevlanid
#### [privateVlanId]
The internal identifier of the private VLAN for this gateway.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[publicIpAddressId]: #publicipaddressid
#### [publicIpAddressId]
The internal identifier of the public IP address for this gateway.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[publicIpv6AddressId]: #publicipv6addressid
#### [publicIpv6AddressId]
The internal identifier of the public IPv6 address for this gateway.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[publicVlanId]: #publicvlanid
#### [publicVlanId]
The internal identifier of the public VLAN for this gateway. This is set internally and cannot be provided on create.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
The current status of this gateway. This is always active unless there is a process running to change the gateway. This can not be set on creation.   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account for this gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[insideVlans]: #insidevlans
#### [insideVlans]
All VLANs trunked to this gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan[] </a>**


</div>
<div class="prop-row">

-----
[members]: #members
#### [members]
The members for this gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member[] </a>**


</div>
<div class="prop-row">

-----
[networkFirewall]: #networkfirewall
#### [networkFirewall]
The firewall associated with this gateway, if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall'>SoftLayer_Network_Vlan_Firewall </a>**


</div>
<div class="prop-row">

-----
[networkFirewallFlag]: #networkfirewallflag
#### [networkFirewallFlag]
Whether or not there is a firewall associated with this gateway.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[privateIpAddress]: #privateipaddress
#### [privateIpAddress]
The private gateway IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[privateVlan]: #privatevlan
#### [privateVlan]
The private VLAN for accessing this gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>
<div class="prop-row">

-----
[publicIpAddress]: #publicipaddress
#### [publicIpAddress]
The public gateway IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[publicIpv6Address]: #publicipv6address
#### [publicIpv6Address]
The public gateway IPv6 address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[publicVlan]: #publicvlan
#### [publicVlan]
The public VLAN for accessing this gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The current status of the gateway.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Status'>SoftLayer_Network_Gateway_Status </a>**


</div>

## Count
<div class="prop-row">

-----
[insideVlanCount]: #insidevlancount
#### [insideVlanCount]
A count of all VLANs trunked to this gateway.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[memberCount]: #membercount
#### [memberCount]
A count of the members for this gateway.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


