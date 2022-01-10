---
title: "SoftLayer_Network_Subnet_IpAddress_Global"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress_Global"
---

# SoftLayer_Network_Subnet_IpAddress_Global
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_IpAddress_Global' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global' >Datatype</a></li>
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
[description]: #description
#### [description]
A Global IP Address' associated description   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[destinationIpAddressId]: #destinationipaddressid
#### [destinationIpAddressId]
A Global IP Address' associated [SoftLayer_Network_Subnet_IpAddress]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_IpAddress">}}) ID   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A Global IP Address' unique identifier   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[ipAddressId]: #ipaddressid
#### [ipAddressId]
A Global IP Address' associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) ID   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
A Global IP Address' associated type [SoftLayer_Network_Subnet_IpAddress_Global_Type]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global_Type">}}) ID   
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
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row deprecated">

-----
[activeTransaction]: #activetransaction
#### [activeTransaction]
DEPRECATED  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**  

<span class="deprecation-label">Deprecated  </span>


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for this Global IP.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Network_Subnet_IpAddress_Global'>SoftLayer_Billing_Item_Network_Subnet_IpAddress_Global </a>**  



</div>
<div class="prop-row">

-----
[destinationIpAddress]: #destinationipaddress
#### [destinationIpAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**  



</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**  



</div>

## Count
</div>


