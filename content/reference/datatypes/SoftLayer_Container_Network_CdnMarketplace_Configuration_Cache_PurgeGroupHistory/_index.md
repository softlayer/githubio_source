---
title: "SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory"
description: "The SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory data type contains information for... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory"
---

# SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory data type contains information for specific responses from the Purge Group API and Purge History API. 





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
[groupName]: #groupname
#### [groupName]
Purge Group name. The favorite group name must be unique, but un-favorite groups do not have this limitation   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[groupUniqueId]: #groupuniqueid
#### [groupUniqueId]
Purge group unique ID   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The purge's status. Status can be SUCCESS, FAILED, or IN_PROGRESS.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[uniqueId]: #uniqueid
#### [uniqueId]
Domain mapping unique ID.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


