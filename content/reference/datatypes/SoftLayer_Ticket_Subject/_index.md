---
title: "SoftLayer_Ticket_Subject"
description: "The SoftLayer_Ticket_Subject data type models one of the possible subjects that a standard support ticket may belong to.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Subject"
---

# SoftLayer_Ticket_Subject
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Ticket_Subject' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Subject' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Ticket_Subject data type models one of the possible subjects that a standard support ticket may belong to. A basic support ticket's title matches it's corresponding subject's name. 


### associatedMethods

*  [SoftLayer_Ticket_Subject::getObject](/reference/services/SoftLayer_Ticket_Subject/getObject )
*  [SoftLayer_Ticket_Subject::getAllObjects](/reference/services/SoftLayer_Ticket_Subject/getAllObjects )
*  [SoftLayer_Ticket::getSubject](/reference/services/SoftLayer_Ticket/getSubject )



### seeAlso

* [SoftLayer_Ticket (type)](/reference/datatypes/SoftLayer_Ticket (type) )


* [SoftLayer_Ticket_Subject](/reference/services/SoftLayer_Ticket_Subject )




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
[categoryId]: #categoryid
#### [categoryId]
The subject category id that this ticket subject belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A ticket subject's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A ticket subject's name. This name is used for a standard support ticket's title.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[parentId]: #parentid
#### [parentId]
Specifies the parent subject id.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[category]: #category
#### [category]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Subject_Category'>SoftLayer_Ticket_Subject_Category </a>**


</div>
<div class="prop-row">

-----
[children]: #children
#### [children]
A child subject  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Subject'>SoftLayer_Ticket_Subject[] </a>**


</div>
<div class="prop-row">

-----
[group]: #group
#### [group]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Group'>SoftLayer_Ticket_Group </a>**


</div>
<div class="prop-row">

-----
[parent]: #parent
#### [parent]
A parent subject  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Subject'>SoftLayer_Ticket_Subject </a>**


</div>

## Count
<div class="prop-row">

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of a child subject   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


