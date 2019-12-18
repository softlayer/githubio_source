---
title: "SoftLayer_Hardware_Component_Partition_Template"
description: "Every SoftLayer Partition Template is defined in the SoftLayer_Hardware_Component_Partition_Template service. The '''Sof... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_Template"
---
# SoftLayer_Hardware_Component_Partition_Template
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_Component_Partition_Template' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer Partition Template is defined in the SoftLayer_Hardware_Component_Partition_Template service. The '''SoftLayer_Hardware_Component_Partition_Template''' service defines all SoftLayer Partition Templates that exist. SoftLayer Partition Templates group together several partitions that define a configuration of templates for a particular hard drive. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getAccount](/reference/services/SoftLayer_Hardware_Component_Partition_Template/getAccount)
Retrieve a partition template's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}).

#### [getData](/reference/services/SoftLayer_Hardware_Component_Partition_Template/getData)
Retrieve an individual partition for a partition template. This is identical to 'partitionTemplatePartition' except this will sort unix partitions.

#### [getExpireDate](/reference/services/SoftLayer_Hardware_Component_Partition_Template/getExpireDate)


#### [getObject](/reference/services/SoftLayer_Hardware_Component_Partition_Template/getObject)
Retrieve a SoftLayer_Hardware_Component_Partition_Template record.

#### [getPartitionOperatingSystem](/reference/services/SoftLayer_Hardware_Component_Partition_Template/getPartitionOperatingSystem)
Retrieve a partition template's associated [SoftLayer_Hardware_Component_Partition_OperatingSystem]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_OperatingSystem">}}).

#### [getPartitionTemplatePartition](/reference/services/SoftLayer_Hardware_Component_Partition_Template/getPartitionTemplatePartition)
Retrieve an individual partition for a partition template.

</div>

