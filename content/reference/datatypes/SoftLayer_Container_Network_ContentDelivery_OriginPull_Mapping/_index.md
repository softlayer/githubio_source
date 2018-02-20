---
title: "SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping"
description: "SoftLayer's CDN allows for multiple origin pull domains and CNAME records. This container holds the origin pull configur... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping"
---

# SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer's CDN allows for multiple origin pull domains and CNAME records. This container holds the origin pull configuration details. CDN currently supports origin pull method for HTTP content. 
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
            <span class='views-field-title'><a href="#cname" name=cname>cname</a></span>
            <div class='views-field-body'>The CNAME record. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier of an origin pull configuration </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isSecureContent" name=isSecureContent>isSecureContent</a></span>
            <div class='views-field-body'>This indicates if an origin pull mapping is for the secure content or not. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#mediaType" name=mediaType>mediaType</a></span>
            <div class='views-field-body'>The type of a media supported by CDN. Supported media types are: "HTTP", "FLASH" and "WM" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#originUrl" name=originUrl>originUrl</a></span>
            <div class='views-field-body'>The URL of a origin server.  A URL can contain a directory path. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


