---
title: "SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
description: "The SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup data type contains information for specifi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
---

# SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup data type contains information for specific responses from the Purge Group API. Each of the Purge Group APIs returns a collection of this type 





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
[createDate]: #createdate
#### [createDate]
Date in which record is created   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[groupUniqueId]: #groupuniqueid
#### [groupUniqueId]
A identifier that is unique to purge group.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[lastPurgeDate]: #lastpurgedate
#### [lastPurgeDate]
The Unix timestamp of the last purge.   
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Purge Group name. The favorite group name must be unique, but non-favorite groups do not have this limitation   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[option]: #option
#### [option]
The following options are available to create a Purge Group: option 1: only purge the paths in the group, but don't save as favorite. option 2: only save the purge group as favorite, but don't purge paths. option 3: save the purge group as favorite and also purge paths.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[pathCount]: #pathcount
#### [pathCount]
Total number of purge paths.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[paths]: #paths
#### [paths]
A collection of purge paths.   
<span class="type-label">Type: </span>**array of strings**  



</div>
<div class="prop-row">

-----
[purgeStatus]: #purgestatus
#### [purgeStatus]
The purge's status when the input option field is 1 or 3. Status can be SUCCESS, FAILED, or IN_PROGRESS.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[saved]: #saved
#### [saved]
Type of the Purge Group, currently SAVED or UNSAVED.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[uniqueId]: #uniqueid
#### [uniqueId]
A identifier that is unique to domain mapping.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


