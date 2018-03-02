---
title: "SoftLayer_Container_Network_ContentDelivery_PurgeService_Response"
description: "This container holds information on a purge request. [[SoftLayer_Network_ContentDelivery_Account::purgeCache|Purge metho... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_ContentDelivery_PurgeService_Response"
---

# SoftLayer_Container_Network_ContentDelivery_PurgeService_Response
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_PurgeService_Response' >Datatype</a></li>
    </ul>
</div>

## Description 
This container holds information on a purge request. [[SoftLayer_Network_ContentDelivery_Account::purgeCache|Purge method]] for more details. 

Status code can be "SUCCESS", "FAILED", or "INVALID_URL" "INVALID_URL" code is returned when a URL is malformed or does not belong to customer. "FAILED" is returned in case there was an internal error. 

### External Links


* [CDN Services at softlayer.com](http://www.softlayer.com/services_cdnlayer.html)



### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::purgeCache](/reference/services/SoftLayer_Network_ContentDelivery_Account/purgeCache )





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
            <span class='views-field-title'><a href="#statusCode" name=statusCode>statusCode</a></span>
            <div class='views-field-body'>A status code indicates whether your request was successful or not </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#url" name=url>url</a></span>
            <div class='views-field-body'>A URL that you wish to purge its cache object </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


