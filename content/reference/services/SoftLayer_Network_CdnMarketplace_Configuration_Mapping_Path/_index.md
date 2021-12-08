---
title: "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
description: "This service manages the paths for domain mapping configurations."
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
---
# SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path' >Datatype</a></li>
    </ul>
</div>

## Description


This service manages the paths for domain mapping configurations. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [createOriginPath](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path/createOriginPath)
SOAP API will create Origin Path for an existing CDN mapping and for a particular customer. 

</div>

<div class="method-row">

#### [deleteOriginPath](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path/deleteOriginPath)
SOAP API will delete Origin Path for an existing mapping and for a particular customer. 

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path/getObject)
Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path record.

</div>

<div class="method-row">

#### [listOriginPath](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path/listOriginPath)
SOAP API will list origin path for an existing mapping and for a particular customer. 

</div>

<div class="method-row">

#### [updateOriginPath](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path/updateOriginPath)
SOAP API will update Origin Path for an existing mapping and for a particular customer. 

When passing the $input object as a parameter, it will expect the following properties to be set: $oldPath $uniqueId $originType, $path, $origin, $httpPort, $httpsPort, and if the path's origin type is object storage, the $bucketName and the $fileExtension. 

Out of the properties listed above only the following path properties are allowed to be changed: $path, $origin, $httpPort, $httpsPort These properties may not be changed: $originType 

</div>
</div>

</div>

