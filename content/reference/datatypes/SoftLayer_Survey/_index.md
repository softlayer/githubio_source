---
title: "SoftLayer_Survey"
description: "The SoftLayer_Survey data type contains general information relating to a single SoftLayer survey."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Survey"
classes:
    - "SoftLayer_Survey"
---

# SoftLayer_Survey
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Survey' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Survey' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Survey data type contains general information relating to a single SoftLayer survey. 





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
[active]: #active
#### [active]
A flag indicating if a survey can be taken.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that a survey had originally started.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A survey's id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A survey's name or title.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
The status id of the survey.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The type id of the survey.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[questions]: #questions
#### [questions]
The questions for a survey.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Question'>SoftLayer_Survey_Question[] </a>**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of the survey  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Status'>SoftLayer_Survey_Status </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of survey  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Type'>SoftLayer_Survey_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[questionCount]: #questioncount
#### [questionCount]
A count of the questions for a survey.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


