---
title: "SoftLayer_Container_Network_ContentDelivery_SupportedProtocol"
description: "SoftLayer's CDN content delivery network allows for multiple types of media hosting in addition to traditional HTTP host... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_ContentDelivery_SupportedProtocol"
---

# SoftLayer_Container_Network_ContentDelivery_SupportedProtocol
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_SupportedProtocol' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer's CDN content delivery network allows for multiple types of media hosting in addition to traditional HTTP hosting. Each of these media types are accessible form a different URL. SoftLayer_Container_Network_ContentDelivery_SupportedProtocol holds details about CDN supported media types and their associated URLs. 

CDN media URLs follow the standard <protocol>://<cdn-name>.<platform-name>.cdn.softlayer.net 

Flash streaming, Windows Media streaming and HTTP protocols are supported: Flash streaming: <nowiki>rtmp://<cdn-name>.flash.cdn.softlayer.net</nowiki> Windows Media streaming: <nowiki>mms://<cdn-name>.wm.cdn.softlayer.net</nowiki> HTTP: <nowiki>http://<cdn-name>.http.cdn.softlayer.net</nowiki> 


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::getMediaUrls](/reference/services/SoftLayer_Network_ContentDelivery_Account/getMediaUrls )



### seeAlso

* [SoftLayer_Network_ContentDelivery_Account](/reference/datatypes/SoftLayer_Network_ContentDelivery_Account )




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
            <span class='views-field-title'><a href="#host" name=host>host</a></span>
            <div class='views-field-body'>The host name related to CDN supported media, and is represented in the hostname portion of a CDN URL. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#mediaType" name=mediaType>mediaType</a></span>
            <div class='views-field-body'>The type of a media supported by CDN such as "FLASH", "WINDOWSMEDIA" or "HTTP" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#platform" name=platform>platform</a></span>
            <div class='views-field-body'>The platform name. It's a friendly name of media type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protocol" name=protocol>protocol</a></span>
            <div class='views-field-body'>The media protocol supported by CDN. This represents the media portion of a CDN URL.  Currently supported protocols are: rtmp, mms and http </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


