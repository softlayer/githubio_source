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
[matchedTerms]: #matchedterms
#### [matchedTerms]
An array of terms that were matched in the resource object.  
<span class="type-label">Type: </span>**array of strings**  



</div>
<div class="prop-row">

-----
[relevanceScore]: #relevancescore
#### [relevanceScore]
The score ratio of the result for relevance to the search criteria.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
A search results resource object that matched search criteria.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a>**  



</div>
<div class="prop-row">

-----
[resourceType]: #resourcetype
#### [resourceType]
The type of the resource object that matched search criteria.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


