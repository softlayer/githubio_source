---
title: "SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
description: "This service manages purge group associated with a CDN mapping Configuration."
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
---
# SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup' >Datatype</a></li>
    </ul>
</div>

## Description
This service manages purge group associated with a CDN mapping Configuration. 



        
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

#### [createPurgeGroup](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/createPurgeGroup)
This method creates a purge group record in the table, and also initiates the purge action based on the input option value. The unsaved groups will be deleted after 15 days if no purge actions executed. The possible input option value can be: 1: (Default) Only purge the paths in the group, don't save the group as favorite. 2: Only save the group as favorite, don't purge the paths. 3: Save the group as favorite and also purge the paths in the group. 
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/getObject)
Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup record.
</div>

<div class="method-row">

#### [getPurgeGroupByGroupId](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/getPurgeGroupByGroupId)
This method returns the purge group for a given domain and group ID. 
</div>

<div class="method-row">

#### [getPurgeGroupQuota](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/getPurgeGroupQuota)
This method gets a purge group quota. 
</div>

<div class="method-row">

#### [listFavoriteGroup](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/listFavoriteGroup)
This method returns the list of favorite purge groups. 
</div>

<div class="method-row">

#### [listUnfavoriteGroup](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/listUnfavoriteGroup)
This method returns the list of unsaved purge groups. 
</div>

<div class="method-row">

#### [purgeByGroupIds](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/purgeByGroupIds)
This method purges the content from purge groups. 
</div>

<div class="method-row">

#### [removePurgeGroupFromFavorite](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/removePurgeGroupFromFavorite)
This method removes a purge group from favorite. 
</div>

<div class="method-row">

#### [savePurgeGroupAsFavorite](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup/savePurgeGroupAsFavorite)
This method saves a purge group as favorite. 
</div>
</div>

</div>

