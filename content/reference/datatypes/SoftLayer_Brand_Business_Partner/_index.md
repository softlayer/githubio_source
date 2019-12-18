---
title: "SoftLayer_Brand_Business_Partner"
description: "Contains business partner details associated with a brand. Country Enterprise Identifier (CEID), Channel ID, Segment ID... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand_Business_Partner"
---

# SoftLayer_Brand_Business_Partner
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Brand_Business_Partner' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Brand_Business_Partner' >Datatype</a></li>
    </ul>
</div>

## Description 
Contains business partner details associated with a brand. Country Enterprise Identifier (CEID), Channel ID, Segment ID and Reseller Level. 





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

## Local
-----
[channelId]: #channelid
#### [channelId]
Brand business partner channel identifier   
<span class="type-label">Type: </span>**integer**

-----
[countryEnterpriseCode]: #countryenterprisecode
#### [countryEnterpriseCode]
Brand business partner country enterprise code   
<span class="type-label">Type: </span>**string**

-----
[resellerLevel]: #resellerlevel
#### [resellerLevel]
Reseller level of a brand business partner   
<span class="type-label">Type: </span>**integer**

-----
[segmentId]: #segmentid
#### [segmentId]
Brand business partner segment identifier   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[brand]: #brand
#### [brand]
Brand associated with the business partner data  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**

-----
[channel]: #channel
#### [channel]
Channel indicator used to categorize business partner revenue.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Business_Partner_Channel'>SoftLayer_Business_Partner_Channel </a>**

-----
[segment]: #segment
#### [segment]
Segment indicator used to categorize business partner revenue.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Business_Partner_Segment'>SoftLayer_Business_Partner_Segment </a>**


## Count
</div>


