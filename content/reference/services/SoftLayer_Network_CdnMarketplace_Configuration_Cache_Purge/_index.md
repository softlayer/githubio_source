---
title: "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"
description: "This service manages purges associated with a CDN mapping Configuration."
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"
---
# SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge' >Datatype</a></li>
    </ul>
</div>

## Description
This service manages purges associated with a CDN mapping Configuration. 



        
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

#### [createPurge](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge/createPurge)
This method creates a purge record in the purge table, and also initiates the create purge call. 

#### [getObject](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge/getObject)
Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge record.

#### [getPurgeHistoryPerMapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge/getPurgeHistoryPerMapping)
This method returns the purge history for a given domain and CDN account. 

#### [getPurgeStatus](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge/getPurgeStatus)
This method gets the status of a given purge path. 

#### [saveOrUnsavePurgePath](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge/saveOrUnsavePurgePath)
Creates a new saved purge if a purge path is saved. Deletes a saved purge record if the path is unsaved. 

</div>

