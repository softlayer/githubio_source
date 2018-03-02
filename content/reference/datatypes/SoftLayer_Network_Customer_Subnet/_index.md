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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet' >Datatype</a></li>
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The account id a customer subnet belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cidr" name=cidr>cidr</a></span>
            <div class='views-field-body'>A subnet's Classless Inter-Domain Routing prefix. This is a number between 0 and 32 signifying the number of bits in a subnet's netmask. These bits separate a subnet's network address from it's host addresses. It performs the same function as the ''netmask'' property, but is represented as an integer.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A customer subnet's unique identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#netmask" name=netmask>netmask</a></span>
            <div class='views-field-body'>A bitmask in dotted-quad format that is used to separate a subnet's network address from it's host addresses. This performs the same function as the ''cidr'' property, but is expressed in a string format.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkIdentifier" name=networkIdentifier>networkIdentifier</a></span>
            <div class='views-field-body'>A subnet's network identifier. This is the first IP address of a subnet.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalIpAddresses" name=totalIpAddresses>totalIpAddresses</a></span>
            <div class='views-field-body'>The total number of ip addresses in a subnet. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddresses" name=ipAddresses>ipAddresses</a></span>
            <div class='views-field-body'>All ip addresses associated with a subnet. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet_IpAddress'>SoftLayer_Network_Customer_Subnet_IpAddress[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddressCount" name=ipAddressCount>ipAddressCount</a></span>
            <div class='views-field-body'>A count of all ip addresses associated with a subnet. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


