---
title: "SoftLayer_Container_Search_Result"
description: "The SoftLayer_Container_Search_Result data type represents a result row from an execution of Search service."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Search_Result"
---

# SoftLayer_Container_Search_Result
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Search_Result' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Search_Result data type represents a result row from an execution of Search service. 





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
                <a href="#matchedTerms" name=matchedTerms>matchedTerms</a>
            </span>
            <div class='views-field-body'>An array of terms that were matched in the resource object. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of strings</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#relevanceScore" name=relevanceScore>relevanceScore</a>
            </span>
            <div class='views-field-body'>The score ratio of the result for relevance to the search criteria. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resource" name=resource>resource</a>
            </span>
            <div class='views-field-body'>A search results resource object that matched search criteria. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceType" name=resourceType>resourceType</a>
            </span>
            <div class='views-field-body'>The type of the resource object that matched search criteria. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


