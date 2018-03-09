---
title: "SoftLayer_Container_Network_IntrusionProtection_Statistic"
description: "The IntrusionProtection_Statistic is used exclusively by the getMainStatistics method on the TippingPointReporting servi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_IntrusionProtection_Statistic"
---

# SoftLayer_Container_Network_IntrusionProtection_Statistic
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Statistic' >Datatype</a></li>
    </ul>
</div>

## Description 
The IntrusionProtection_Statistic is used exclusively by the getMainStatistics method on the TippingPointReporting service, and serves mainly as a pair object, storing a name and an attack count.  Name is usually the name of an attack, but it can also be an attacking IP Address 





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
            <span class='views-field-title'>
                <a href="#attackCount" name=attackCount>attackCount</a>
            </span>
            <div class='views-field-body'>The number of attacks effecting this name over the time period </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>Either the name of the attack in question, or the attacking IP Address </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


