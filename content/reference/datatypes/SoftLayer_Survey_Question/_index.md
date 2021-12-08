---
title: "SoftLayer_Survey_Question"
description: "The SoftLayer_Survey_Question data type contains general information relating to a single SoftLayer survey question."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Survey"
classes:
    - "SoftLayer_Survey_Question"
---

# SoftLayer_Survey_Question
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Survey_Question' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Survey_Question data type contains general information relating to a single SoftLayer survey question. 





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
[id]: #id
#### [id]
A survey question's Id.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[isRequired]: #isrequired
#### [isRequired]
A flag indicating that a survey question requires a response.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[multiAnswer]: #multianswer
#### [multiAnswer]
A flag indicating that a survey question can have multiple answers responded to.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[question]: #question
#### [question]
A survey question's question.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[questionOrder]: #questionorder
#### [questionOrder]
A value indicating the order in when a survey question will be asked.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[surveyId]: #surveyid
#### [surveyId]
A survey question's associated [SoftLayer_Survey]({{<ref "reference/datatypes/SoftLayer_Survey">}}) Id.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[answers]: #answers
#### [answers]
The possible answers for a survey question.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Answer'>SoftLayer_Survey_Answer[] </a>**  



</div>
<div class="prop-row">

-----
[survey]: #survey
#### [survey]
The survey that a question belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey'>SoftLayer_Survey </a>**  



</div>

## Count
<div class="prop-row">

-----
[answerCount]: #answercount
#### [answerCount]
A count of the possible answers for a survey question.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


