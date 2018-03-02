---
title: "SoftLayer_Hardware_Component_Partition_Template_Partition"
description: "The SoftLayer_Hardware_Component_Partition_Template_Partition data type contains general information relating to a singl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_Template_Partition"
---

# SoftLayer_Hardware_Component_Partition_Template_Partition
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template_Partition' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Partition_Template_Partition data type contains general information relating to a single SoftLayer Template Partition. 





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
            <div class='views-field-body'>A partition's id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isGrow" name=isGrow>isGrow</a></span>
            <div class='views-field-body'>A flag indication if a partition will be the grow partition.  The grow partition will have its size adjusted to fill all available space on a hard drive.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#partitionName" name=partitionName>partitionName</a></span>
            <div class='views-field-body'>A partition's default name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#partitionSize" name=partitionSize>partitionSize</a></span>
            <div class='views-field-body'>A partition's default size. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#partitionTemplateId" name=partitionTemplateId>partitionTemplateId</a></span>
            <div class='views-field-body'>A partition's associated [[SoftLayer_Hardware_Component_Partition_Template|Partition Template]] Id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#volumeNumber" name=volumeNumber>volumeNumber</a></span>
            <div class='views-field-body'>The volume the partition will be put on </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#filesystemType" name=filesystemType>filesystemType</a></span>
            <div class='views-field-body'>The filesystem type of a partition </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Storage_Filesystem_Type'>SoftLayer_Configuration_Storage_Filesystem_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#partitionTemplate" name=partitionTemplate>partitionTemplate</a></span>
            <div class='views-field-body'>A partition's [[SoftLayer_Hardware_Component_Partition_Template|Partition Template]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template'>SoftLayer_Hardware_Component_Partition_Template </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


