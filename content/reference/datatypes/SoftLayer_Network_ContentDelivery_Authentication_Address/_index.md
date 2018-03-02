---
title: "SoftLayer_Network_ContentDelivery_Authentication_Address"
description: "The SoftLayer_Network_ContentDelivery_Authentication_Address data type models an individual IP address that CDN allow or... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Address"
---

# SoftLayer_Network_ContentDelivery_Authentication_Address
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Address' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_ContentDelivery_Authentication_Address data type models an individual IP address that CDN allow or deny access from. 





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
            <span class='views-field-title'><a href="#accessType" name=accessType>accessType</a></span>
            <div class='views-field-body'>The type of access on an IP address.  It can be "ALLOW" or "DENY" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cdnAccountId" name=cdnAccountId>cdnAccountId</a></span>
            <div class='views-field-body'>The internal identifier of the CDN account </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The created date </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The internal identifier of an authentication IP address </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddress" name=ipAddress>ipAddress</a></span>
            <div class='views-field-body'>The IP address that you want to block or allow access to </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The last modified date </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The name of an authentication IP.  This helps you to keep track of IP addresses. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#priority" name=priority>priority</a></span>
            <div class='views-field-body'>The priority of an authentication IP address.  The smaller number, the higher in priority.  Higher priority IP will be matched first. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userId" name=userId>userId</a></span>
            <div class='views-field-body'>The internal identifier of the user who created an authentication IP record </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


