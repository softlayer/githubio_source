---
title: "SoftLayer_Network_Customer_Subnet_IpAddress"
description: "The SoftLayer_Network_Customer_Subnet_IpAddress data type contains general information relating to a single Customer Sub... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Customer_Subnet_IpAddress"
---

# SoftLayer_Network_Customer_Subnet_IpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet_IpAddress' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Customer_Subnet_IpAddress data type contains general information relating to a single Customer Subnet (Remote) IPv4 address. 





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
Unique identifier for an ip address.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
An IP address expressed in dotted quad format.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
An IP address' user defined note.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[subnetId]: #subnetid
#### [subnetId]
The unique identifier for the customer subnet (remote) the ip address belongs to.  
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
The customer subnet (remote) that the ip address belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet'>SoftLayer_Network_Customer_Subnet </a>**


</div>
<div class="prop-row">

-----
[translations]: #translations
#### [translations]
All the address translations that are tied to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a>**


</div>

## Count
<div class="prop-row">

-----
[translationCount]: #translationcount
#### [translationCount]
A count of all the address translations that are tied to an IP address.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


