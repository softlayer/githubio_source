---
title: "SoftLayer_Hardware_Component_Motherboard_Reboot_Time"
description: "The SoftLayer_Hardware_Component_Motherboard_Reboot_Time contains the average reboot times for motherboards. There are t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Motherboard_Reboot_Time"
---

# SoftLayer_Hardware_Component_Motherboard_Reboot_Time
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Motherboard_Reboot_Time' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Motherboard_Reboot_Time contains the average reboot times for motherboards. There are two types of average times.  One is for motherboards without raid, and the other is for motherboards with raid.  These times are based on averages and have been gathered through numerous test cases. 





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
            <span class='views-field-title'><a href="#withRaid" name=withRaid>withRaid</a></span>
            <div class='views-field-body'>Average reboot time in seconds for the motherboard when raid is installed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#withoutRaid" name=withoutRaid>withoutRaid</a></span>
            <div class='views-field-body'>Average reboot time in seconds for the motherboard when NO raid is installed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentModel" name=hardwareComponentModel>hardwareComponentModel</a></span>
            <div class='views-field-body'>Motherboard's specifications (manufacturer, version, etc....) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


