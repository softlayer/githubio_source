---
title: "SoftLayer_Network_ContentDelivery_Authentication_Token"
description: "The SoftLayer_Network_ContentDelivery_Authentication_Address data type models an individual IP address that CDN allow or... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Token"
---

# SoftLayer_Network_ContentDelivery_Authentication_Token
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Token' >Datatype</a></li>
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
            <span class='views-field-title'><a href="#cdnAccountId" name=cdnAccountId>cdnAccountId</a></span>
            <div class='views-field-body'>The internal identifier of a CDN account </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#clientIp" name=clientIp>clientIp</a></span>
            <div class='views-field-body'>The client IP address. This is optional. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The created date </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The customer id.  You can use this optional value to tie a user id to an authentication token. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#referrer" name=referrer>referrer</a></span>
            <div class='views-field-body'>The referrer information.  This is optional. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#token" name=token>token</a></span>
            <div class='views-field-body'>The managed token string </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


