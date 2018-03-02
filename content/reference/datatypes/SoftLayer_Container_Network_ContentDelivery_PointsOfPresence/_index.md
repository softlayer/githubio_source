---
title: "SoftLayer_Container_Network_ContentDelivery_PointsOfPresence"
description: "SoftLayer's CDN content delivery network offering replicates your data to a number of Points of Presence (POP's) around... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_ContentDelivery_PointsOfPresence"
---

# SoftLayer_Container_Network_ContentDelivery_PointsOfPresence
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_PointsOfPresence' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer's CDN content delivery network offering replicates your data to a number of Points of Presence (POP's) around the world. SoftLayer_Container_Network_ContentDelivery_PointsOfPresence models one of these POP locations. 

### External Links


* [CDN Services at softlayer.com](http://www.softlayer.com/services_cdnlayer.html)



### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::getBandwidthOverage](/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthOverage )
*  [SoftLayer_Network_ContentDelivery_Account::getPopNames](/reference/services/SoftLayer_Network_ContentDelivery_Account/getPopNames )



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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A CDN Point of Presence's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A CDN Point of Presence's name. This is typically the city that the POP is located in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


