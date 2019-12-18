---
title: "SoftLayer_Ticket_Subject_Category"
description: "SoftLayer_Ticket_Subject_Category groups ticket subjects into logical group."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Subject_Category"
---

# SoftLayer_Ticket_Subject_Category
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Ticket_Subject_Category' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Subject_Category' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Ticket_Subject_Category groups ticket subjects into logical group. 



### seeAlso

* [SoftLayer_Ticket_Subject](/reference/services/SoftLayer_Ticket_Subject )




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
[id]: #id
#### [id]
A unique identifier of a ticket subject category.  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
A ticket subject category name.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[subjects]: #subjects
#### [subjects]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Subject'>SoftLayer_Ticket_Subject[] </a>**


## Count

-----
[subjectCount]: #subjectcount
#### [subjectCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


