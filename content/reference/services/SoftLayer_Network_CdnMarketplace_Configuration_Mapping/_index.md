---
title: "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
description: "This service manages domain mapping configurations for enabling CDN services."
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
---
# SoftLayer_Network_CdnMarketplace_Configuration_Mapping
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_CdnMarketplace_Configuration_Mapping' >Datatype</a></li>
    </ul>
</div>

## Description
This service manages domain mapping configurations for enabling CDN services. 



        
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

#### [createDomainMapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/createDomainMapping)
SOAP API will create a new CDN domain mapping for a particular customer. 
</div>

<div class="method-row">

#### [deleteDomainMapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/deleteDomainMapping)
SOAP API will delete CDN domain mapping for a particular customer. 
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/getObject)
Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Mapping record.
</div>

<div class="method-row">

#### [listDomainMappingByUniqueId](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/listDomainMappingByUniqueId)
SOAP API will return the domain mapping based on the uniqueId. 
</div>

<div class="method-row">

#### [listDomainMappings](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/listDomainMappings)
SOAP API will return all domains for a particular customer. 
</div>

<div class="method-row">

#### [retryHttpsActionRequest](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/retryHttpsActionRequest)
For specific mappings in HTTPS-related error states, this SOAP API will determine whether it needs to re-attempt an enable or disable HTTPS. 
</div>

<div class="method-row">

#### [startDomainMapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/startDomainMapping)
SOAP API will start CDN domain mapping for a particular customer. 
</div>

<div class="method-row">

#### [stopDomainMapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/stopDomainMapping)
SOAP API will stop CDN mapping for a particular customer. 
</div>

<div class="method-row">

#### [updateDomainMapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/updateDomainMapping)
SOAP API will update the Domain Mapping identified by the Unique Id. Following fields are allowed to be changed: originHost, HttpPort/HttpsPort, RespectHeaders, ServeStale 

Additionally, bucketName and fileExtension if OriginType is Object Store 
</div>

<div class="method-row">

#### [verifyCname](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/verifyCname)
This method will verify the CNAME given is unique. 
</div>

<div class="method-row">

#### [verifyDomainMapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/verifyDomainMapping)
This method will verify the status of a domain mapping 
</div>
</div>

</div>

