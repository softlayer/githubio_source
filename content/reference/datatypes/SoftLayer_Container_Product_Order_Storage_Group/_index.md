---
title: "SoftLayer_Container_Product_Order_Storage_Group"
description: "A single storage group container used for a hardware server order. 

This object describes a single storage group that c... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Storage_Group"
---

# SoftLayer_Container_Product_Order_Storage_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group' >Datatype</a></li>
    </ul>
</div>

## Description 
A single storage group container used for a hardware server order. 

This object describes a single storage group that can be added to an order container. 





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
            <span class='views-field-title'><a href="#arraySize" name=arraySize>arraySize</a></span>
            <div class='views-field-body'>Size of the array in gigabytes. Must be within limitations of the smallest drive assigned to the storage group and the storage group type.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#arrayTypeId" name=arrayTypeId>arrayTypeId</a></span>
            <div class='views-field-body'>The array type id from a [[SoftLayer_Configuration_Storage_Group_Array_Type]] object.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#diskControllerIndex" name=diskControllerIndex>diskControllerIndex</a></span>
            <div class='views-field-body'>Defines the disk controller to put the storage group and the hard drives on. 

This must match a disk controller price on the order. The disk controller index is 0-indexed. 'disk_controller' = 0 'disk_controller1' = 1 'disk_controller2' = 2  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardDrives" name=hardDrives>hardDrives</a></span>
            <div class='views-field-body'>Integer array of drive indexes to use in the storage group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>array of integers</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hotSpareDrives" name=hotSpareDrives>hotSpareDrives</a></span>
            <div class='views-field-body'>If an array should be protected by an hotspare, the drive index of the hotspares should be here. 

If a drive is a hotspare for all arrays then a separate storage group with array type GLOBAL_HOT_SPARE should be used  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>array of integers</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lvmFlag" name=lvmFlag>lvmFlag</a></span>
            <div class='views-field-body'><< EOT </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#partitionTemplateId" name=partitionTemplateId>partitionTemplateId</a></span>
            <div class='views-field-body'>The id for a [[SoftLayer_Hardware_Component_Partition_Template]] object, which will determine the partitions to add to the storage group. 

If this storage group is not a primary storage group, then this will not be used.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#partitions" name=partitions>partitions</a></span>
            <div class='views-field-body'>Defines the partitions for the storage group. 

If this storage group is not a secondary storage group, then this will not be used.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group_Partition'>SoftLayer_Container_Product_Order_Storage_Group_Partition[] </a></p></div>
        </div>
            </div>
    </div>


