---
title: "SoftLayer_Survey_Response"
description: "The SoftLayer_Survey_Response data type contains general information relating to a single SoftLayer survey response."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Survey"
classes:
    - "SoftLayer_Survey_Response"
---

# SoftLayer_Survey_Response
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Survey_Response' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Survey_Response data type contains general information relating to a single SoftLayer survey response. 





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
[otherAnswer]: #otheranswer
#### [otherAnswer]
The user typed response for the [SoftLayer_Survey_Answer]({{<ref "reference/datatypes/SoftLayer_Survey_Answer">}}) that a response is associated with.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[surveyAnswerId]: #surveyanswerid
#### [surveyAnswerId]
The Id of the [SoftLayer_Survey_Answer]({{<ref "reference/datatypes/SoftLayer_Survey_Answer">}}) that a response was made for.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[surveyAnswer]: #surveyanswer
#### [surveyAnswer]
The survey answer that this response was to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Answer'>SoftLayer_Survey_Answer </a>**  



</div>

## Count
</div>


