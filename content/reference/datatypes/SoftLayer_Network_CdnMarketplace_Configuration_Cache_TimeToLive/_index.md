---
title: "SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive"
description: "This data type models a purge event that occurs repetitively and automatically in caching server after a set interval of... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive"
---

# SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type models a purge event that occurs repetitively and automatically in caching server after a set interval of time. A time to live instance contains a reference to a mapping configuration, the path to execute the purge on, the result of the purge, and the time interval after which the purge will be executed. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
    <div id="localProperties" class="prop-content" >
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>date record is created  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#path" name=path>path</a>
            </span>
            <div class='views-field-body'>Path where purge will be executed after TTL  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#timeToLive" name=timeToLive>timeToLive</a>
            </span>
            <div class='views-field-body'>Time interval after which purge will occur repeatedly  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>


