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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Brand_Business_Partner' >Datatype</a></li>
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#channelId" name=channelId>channelId</a></span>
            <div class='views-field-body'>Brand business partner channel identifier  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#countryEnterpriseCode" name=countryEnterpriseCode>countryEnterpriseCode</a></span>
            <div class='views-field-body'>Brand business partner country enterprise code  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resellerLevel" name=resellerLevel>resellerLevel</a></span>
            <div class='views-field-body'>Reseller level of a brand business partner  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#segmentId" name=segmentId>segmentId</a></span>
            <div class='views-field-body'>Brand business partner segment identifier  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#brand" name=brand>brand</a></span>
            <div class='views-field-body'>Brand associated with the business partner data </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#channel" name=channel>channel</a></span>
            <div class='views-field-body'>Channel indicator used to categorize business partner revenue. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Business_Partner_Channel'>SoftLayer_Business_Partner_Channel </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#segment" name=segment>segment</a></span>
            <div class='views-field-body'>Segment indicator used to categorize business partner revenue. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Business_Partner_Segment'>SoftLayer_Business_Partner_Segment </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


