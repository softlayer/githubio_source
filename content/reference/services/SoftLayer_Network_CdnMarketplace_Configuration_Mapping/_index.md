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



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/createDomainMapping'> createDomainMapping</a> </span>
            <div class='views-field-body'>SOAP API will create a new CDN domain mapping for a particular customer. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/deleteDomainMapping'> deleteDomainMapping</a> </span>
            <div class='views-field-body'>SOAP API will delete CDN domain mapping for a particular customer. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Mapping record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/listDomainMappingByUniqueId'> listDomainMappingByUniqueId</a> </span>
            <div class='views-field-body'>SOAP API will return the domain mapping based on the uniqueId. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/listDomainMappings'> listDomainMappings</a> </span>
            <div class='views-field-body'>SOAP API will return all domains for a particular customer. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/retryHttpsActionRequest'> retryHttpsActionRequest</a> </span>
            <div class='views-field-body'>For specific mappings in HTTPS-related error states, this SOAP API will determine whether it needs to re-attempt an enable or disable HTTPS. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/startDomainMapping'> startDomainMapping</a> </span>
            <div class='views-field-body'>SOAP API will start CDN domain mapping for a particular customer. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/stopDomainMapping'> stopDomainMapping</a> </span>
            <div class='views-field-body'>SOAP API will stop CDN mapping for a particular customer. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/updateDomainMapping'> updateDomainMapping</a> </span>
            <div class='views-field-body'>SOAP API will update the Domain Mapping identified by the Unique Id. Following fields are allowed to be changed: originHost, HttpPort/HttpsPort, RespectHeaders, ServeStale 

Additionally, bucketName and fileExtension if OriginType is Object Store </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/verifyCname'> verifyCname</a> </span>
            <div class='views-field-body'>This method will verify the CNAME given is unique. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping/verifyDomainMapping'> verifyDomainMapping</a> </span>
            <div class='views-field-body'>This method will verify the status of a domain mapping </div>
        </div>
        </div>
</div>

