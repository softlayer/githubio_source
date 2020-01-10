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





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[withRaid]: #withraid
#### [withRaid]
Average reboot time in seconds for the motherboard when raid is installed.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[withoutRaid]: #withoutraid
#### [withoutRaid]
Average reboot time in seconds for the motherboard when NO raid is installed.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardwareComponentModel]: #hardwarecomponentmodel
#### [hardwareComponentModel]
Motherboard's specifications (manufacturer, version, etc....)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a>**


</div>

## Count
</div>


