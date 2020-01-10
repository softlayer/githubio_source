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
[arraySize]: #arraysize
#### [arraySize]
Size of the array in gigabytes. Must be within limitations of the smallest drive assigned to the storage group and the storage group type.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[arrayTypeId]: #arraytypeid
#### [arrayTypeId]
The array type id from a [SoftLayer_Configuration_Storage_Group_Array_Type]({{<ref "reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type">}}) object.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[diskControllerIndex]: #diskcontrollerindex
#### [diskControllerIndex]
Defines the disk controller to put the storage group and the hard drives on. 

This must match a disk controller price on the order. The disk controller index is 0-indexed. 'disk_controller' = 0 'disk_controller1' = 1 'disk_controller2' = 2   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardDrives]: #harddrives
#### [hardDrives]
Integer array of drive indexes to use in the storage group.  
<span class="type-label">Type: </span>**array of integers**


</div>
<div class="prop-row">

-----
[hotSpareDrives]: #hotsparedrives
#### [hotSpareDrives]
If an array should be protected by an hotspare, the drive index of the hotspares should be here. 

If a drive is a hotspare for all arrays then a separate storage group with array type GLOBAL_HOT_SPARE should be used   
<span class="type-label">Type: </span>**array of integers**


</div>
<div class="prop-row">

-----
[lvmFlag]: #lvmflag
#### [lvmFlag]
<< EOT  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[partitionTemplateId]: #partitiontemplateid
#### [partitionTemplateId]
The id for a [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}) object, which will determine the partitions to add to the storage group. 

If this storage group is not a primary storage group, then this will not be used.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[partitions]: #partitions
#### [partitions]
Defines the partitions for the storage group. 

If this storage group is not a secondary storage group, then this will not be used.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group_Partition'>SoftLayer_Container_Product_Order_Storage_Group_Partition[] </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


