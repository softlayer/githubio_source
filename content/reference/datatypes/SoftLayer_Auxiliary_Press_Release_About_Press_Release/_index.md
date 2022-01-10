---
title: "SoftLayer_Auxiliary_Press_Release_About_Press_Release"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release_About_Press_Release"
---

# SoftLayer_Auxiliary_Press_Release_About_Press_Release
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Auxiliary_Press_Release_About_Press_Release' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_About_Press_Release' >Datatype</a></li>
    </ul>
</div>

## Description 





### associatedMethods

*  [SoftLayer_Auxiliary_Press_Release_About_Press_Release::getObject](/reference/services/SoftLayer_Auxiliary_Press_Release_About_Press_Release/getObject )



### seeAlso

* [SoftLayer_Auxiliary_Press_Release_About](/reference/services/SoftLayer_Auxiliary_Press_Release_About )




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
A press release about cross  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[pressReleaseAboutId]: #pressreleaseaboutid
#### [pressReleaseAboutId]
A press release about's internal  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[pressReleaseId]: #pressreleaseid
#### [pressReleaseId]
A press release internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[sortOrder]: #sortorder
#### [sortOrder]
The number that associated an about  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[aboutParagraphs]: #aboutparagraphs
#### [aboutParagraphs]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_About'>SoftLayer_Auxiliary_Press_Release_About[] </a>**  



</div>
<div class="prop-row">

-----
[pressReleases]: #pressreleases
#### [pressReleases]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release'>SoftLayer_Auxiliary_Press_Release[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[aboutParagraphCount]: #aboutparagraphcount
#### [aboutParagraphCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[pressReleaseCount]: #pressreleasecount
#### [pressReleaseCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


