---
title: "SoftLayer_Survey_Answer"
description: "The SoftLayer_Survey_Answer data type contains general information relating to a single SoftLayer survey answer."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Survey"
classes:
    - "SoftLayer_Survey_Answer"
---

# SoftLayer_Survey_Answer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Survey_Answer' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Survey_Answer data type contains general information relating to a single SoftLayer survey answer. 





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
[answer]: #answer
#### [answer]
A survey answer's answer that a user can response too.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[answerOrder]: #answerorder
#### [answerOrder]
A value indicating the order in when a survey answer will be displayed to a user.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A survey answer's Id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[surveyQuestionId]: #surveyquestionid
#### [surveyQuestionId]
A survey answer's associated [SoftLayer_Survey_Question]({{<ref "reference/datatypes/SoftLayer_Survey_Question">}}) Id.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[surveyQuestion]: #surveyquestion
#### [surveyQuestion]
The survey question that this answer belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Question'>SoftLayer_Survey_Question </a>**


</div>

## Count
</div>


