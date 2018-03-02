---
title: "SoftLayer_Hardware_Component_Partition"
description: "The SoftLayer_Hardware_Component_Partition data type contains general information relating to a single hard drive partit... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition"
---

# SoftLayer_Hardware_Component_Partition
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Partition data type contains general information relating to a single hard drive partition. 





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
            <span class='views-field-title'><a href="#diskNumber" name=diskNumber>diskNumber</a></span>
            <div class='views-field-body'>A hardware component partition's order in the [[SoftLayer_Hardware_Hardware|hardware]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#grow" name=grow>grow</a></span>
            <div class='views-field-body'>A flag indicating if a partition is the grow partition. The grow partition will grow to fill all remaining space on a disk.  There can only be one.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentId" name=hardwareComponentId>hardwareComponentId</a></span>
            <div class='views-field-body'>A hardware component partition's associated [[SoftLayer_Hardware_Component|hardware component]] Id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#minimumSize" name=minimumSize>minimumSize</a></span>
            <div class='views-field-body'>A hardware component partition's minimum size(GB). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A hardware component partition's name. On a server with windows this may be 'C' and on Linux this may be '/var'  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponent" name=hardwareComponent>hardwareComponent</a></span>
            <div class='views-field-body'>A hardware component partitions's associated [[SoftLayer_Hardware_Component|Hardware Component]]. Likely to be a [[SoftLayer_Hardware_Component_HardDrive|Hard Drive]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


