---
title: "SoftLayer_Scale_Asset_Hardware"
description: "A hardware asset is a fixed asset of scale group. It is not automatically scaled up or down in any way. Its purpose is t... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Asset_Hardware"
---
# SoftLayer_Scale_Asset_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Asset_Hardware' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Asset_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description
A hardware asset is a fixed asset of scale group. It is not automatically scaled up or down in any way. Its purpose is to provide information (e.g. metrics) to policies to affect scaling decisions. Currently hardware assets are unsupported. 



        
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

#### [createObject](/reference/services/SoftLayer_Scale_Asset_Hardware/createObject)
Pin hardware on a group. This can be done at anytime, whether the group is active or not. 

#### [deleteObject](/reference/services/SoftLayer_Scale_Asset_Hardware/deleteObject)
Delete this group asset.

#### [getHardware](/reference/services/SoftLayer_Scale_Asset_Hardware/getHardware)
Retrieve the hardware for this asset.

#### [getHardwareId](/reference/services/SoftLayer_Scale_Asset_Hardware/getHardwareId)
Retrieve the identifier of the hardware for this asset.

#### [getObject](/reference/services/SoftLayer_Scale_Asset_Hardware/getObject)
Retrieve a SoftLayer_Scale_Asset_Hardware record.

#### [getScaleGroup](/reference/services/SoftLayer_Scale_Asset_Hardware/getScaleGroup)
Retrieve the group this asset belongs to.

</div>

