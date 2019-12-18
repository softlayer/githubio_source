---
title: "SoftLayer_Network_Customer_Subnet"
description: "The SoftLayer_Network_Customer_Subnet data type contains general information relating to a single customer subnet (remot... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Customer_Subnet"
---

# SoftLayer_Network_Customer_Subnet
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Customer_Subnet' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Customer_Subnet data type contains general information relating to a single customer subnet (remote). 





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
[accountId]: #accountid
#### [accountId]
The account id a customer subnet belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[cidr]: #cidr
#### [cidr]
A subnet's Classless Inter-Domain Routing prefix. This is a number between 0 and 32 signifying the number of bits in a subnet's netmask. These bits separate a subnet's network address from it's host addresses. It performs the same function as the ''netmask'' property, but is represented as an integer.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A customer subnet's unique identifier.  
<span class="type-label">Type: </span>**integer**

-----
[netmask]: #netmask
#### [netmask]
A bitmask in dotted-quad format that is used to separate a subnet's network address from it's host addresses. This performs the same function as the ''cidr'' property, but is expressed in a string format.   
<span class="type-label">Type: </span>**string**

-----
[networkIdentifier]: #networkidentifier
#### [networkIdentifier]
A subnet's network identifier. This is the first IP address of a subnet.   
<span class="type-label">Type: </span>**string**

-----
[totalIpAddresses]: #totalipaddresses
#### [totalIpAddresses]
The total number of ip addresses in a subnet.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[ipAddresses]: #ipaddresses
#### [ipAddresses]
All ip addresses associated with a subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet_IpAddress'>SoftLayer_Network_Customer_Subnet_IpAddress[] </a>**


## Count

-----
[ipAddressCount]: #ipaddresscount
#### [ipAddressCount]
A count of all ip addresses associated with a subnet.   
<span class="type-label">Type: </span>**unsigned long**

</div>


