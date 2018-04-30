---
title: "SoftLayer_Hardware_Component_Partition_OperatingSystem"
description: "The SoftLayer_Hardware_Component_Partition_OperatingSystem data type contains general information relating to a single S... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_OperatingSystem"
---

# SoftLayer_Hardware_Component_Partition_OperatingSystem
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_Component_Partition_OperatingSystem' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_OperatingSystem' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Partition_OperatingSystem data type contains general information relating to a single SoftLayer Operating System Partition Template. 





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
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>A partition template operating system's description.  Typically the title of the Operating System. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A partition template operating system's id. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notes" name=notes>notes</a>
            </span>
            <div class='views-field-body'>Information about the kinds of partition templates assigned to this operating system. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#partitionTemplates" name=partitionTemplates>partitionTemplates</a>
            </span>
            <div class='views-field-body'>Information regarding an operating system's [[SoftLayer_Hardware_Component_Partition_Template|Partition Templates]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template'>SoftLayer_Hardware_Component_Partition_Template[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#partitionTemplateCount" name=partitionTemplateCount>partitionTemplateCount</a>
            </span>
            <div class='views-field-body'>A count of information regarding an operating system's [[SoftLayer_Hardware_Component_Partition_Template|Partition Templates]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


