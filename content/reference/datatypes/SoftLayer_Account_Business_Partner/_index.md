---
title: "SoftLayer_Account_Business_Partner"
description: "Contains business partner details associated with an account. Country Enterprise Identifier (CEID), Channel ID, Segment... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Business_Partner"
---

# SoftLayer_Account_Business_Partner
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Business_Partner' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Business_Partner' >Datatype</a></li>
    </ul>
</div>

## Description 


Contains business partner details associated with an account. Country Enterprise Identifier (CEID), Channel ID, Segment ID and Reseller Level. 





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
[channelId]: #channelid
#### [channelId]
Account business partner channel identifier   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[countryEnterpriseCode]: #countryenterprisecode
#### [countryEnterpriseCode]
Account business partner country enterprise code   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[resellerLevel]: #resellerlevel
#### [resellerLevel]
Reseller level of an account business partner   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[segmentId]: #segmentid
#### [segmentId]
Account business partner segment identifier   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
Account associated with the business partner data  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[channel]: #channel
#### [channel]
Channel indicator used to categorize business partner revenue.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Business_Partner_Channel'>SoftLayer_Business_Partner_Channel </a>**  



</div>
<div class="prop-row">

-----
[segment]: #segment
#### [segment]
Segment indicator used to categorize business partner revenue.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Business_Partner_Segment'>SoftLayer_Business_Partner_Segment </a>**  



</div>

## Count
</div>


