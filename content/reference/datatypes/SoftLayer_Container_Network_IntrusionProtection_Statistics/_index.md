---
title: "SoftLayer_Container_Network_IntrusionProtection_Statistics"
description: "The IntrusionProtection_Statistics Type is used as a container for SoftLayer_Container_Network_IntrusionProtection_Stati... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_IntrusionProtection_Statistics"
---

# SoftLayer_Container_Network_IntrusionProtection_Statistics
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Statistics' >Datatype</a></li>
    </ul>
</div>

## Description 
The IntrusionProtection_Statistics Type is used as a container for SoftLayer_Container_Network_IntrusionProtection_Statistic objects.  The SoftLayer_Container_Network_IntrusionProtection_Statistics class holds the "header" information, like the item being queried (either account or data center), the time frame, and the grand total of the attacks. 
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
            <span class='views-field-title'><a href="#target" name=target>target</a></span>
            <div class='views-field-body'>The actual target, either a datacenter name, an account ID, or a subnet IP </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#targetType" name=targetType>targetType</a></span>
            <div class='views-field-body'>The type of the target, right now either "datacenter", "account", or "subnet" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#timeFrame" name=timeFrame>timeFrame</a></span>
            <div class='views-field-body'>The time frame of the attack, in string form, like "Last 24 hours" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topAttacks" name=topAttacks>topAttacks</a></span>
            <div class='views-field-body'>The top attacks for this target over this time frame </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Statistic'>SoftLayer_Container_Network_IntrusionProtection_Statistic[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalAttacks" name=totalAttacks>totalAttacks</a></span>
            <div class='views-field-body'>Total attacks for this $target over this time frame </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


