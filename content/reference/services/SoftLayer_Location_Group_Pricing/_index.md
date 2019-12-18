---
title: "SoftLayer_Location_Group_Pricing"
description: "A pricing location group relates a set of [SoftLayer_Product_Item_Price]({{<ref 'reference/datatypes/SoftLayer_Product_I... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Group_Pricing"
---
# SoftLayer_Location_Group_Pricing
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location_Group_Pricing' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Group_Pricing' >Datatype</a></li>
    </ul>
</div>

## Description
A pricing location group relates a set of [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}). 



        
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

#### [getAllObjects](/reference/services/SoftLayer_Location_Group_Pricing/getAllObjects)
Get all pricing location groups.

#### [getLocationGroupType](/reference/services/SoftLayer_Location_Group_Pricing/getLocationGroupType)
Retrieve the type for this location group.

#### [getLocations](/reference/services/SoftLayer_Location_Group_Pricing/getLocations)
Retrieve the locations that this pricing location group is applicable for. This limits the locations that the prices referenced by this pricing location group can be used with.

#### [getObject](/reference/services/SoftLayer_Location_Group_Pricing/getObject)
Retrieve a SoftLayer_Location_Group_Pricing record.

#### [getPrices](/reference/services/SoftLayer_Location_Group_Pricing/getPrices)
Retrieve the prices that this pricing location group limits. All of these prices will only be available in the locations defined by this pricing location group.

</div>

