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
[active]: #active
#### [active]
A flag indicating if a survey can be taken.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date that a survey had originally started.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A survey's id.  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
A survey's name or title.  
<span class="type-label">Type: </span>**string**

-----
[statusId]: #statusid
#### [statusId]
The status id of the survey.  
<span class="type-label">Type: </span>**integer**

-----
[typeId]: #typeid
#### [typeId]
The type id of the survey.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[questions]: #questions
#### [questions]
The questions for a survey.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Question'>SoftLayer_Survey_Question[] </a>**

-----
[status]: #status
#### [status]
The status of the survey  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Status'>SoftLayer_Survey_Status </a>**

-----
[type]: #type
#### [type]
The type of survey  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey_Type'>SoftLayer_Survey_Type </a>**


## Count

-----
[questionCount]: #questioncount
#### [questionCount]
A count of the questions for a survey.   
<span class="type-label">Type: </span>**unsigned long**

</div>


