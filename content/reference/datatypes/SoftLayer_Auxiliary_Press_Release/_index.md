---
title: "SoftLayer_Auxiliary_Press_Release"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release"
---

# SoftLayer_Auxiliary_Press_Release
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Auxiliary_Press_Release' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release' >Datatype</a></li>
    </ul>
</div>

## Description 



### associatedMethods

*  [SoftLayer_Auxiliary_Press_Prelease::getObject](/reference/services/SoftLayer_Auxiliary_Press_Prelease/getObject )



### seeAlso

* [SoftLayer_Auxiliary_Press_Release_Content](/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Content )


* [SoftLayer_Auxiliary_Press_Release_About_Press_Release](/reference/datatypes/SoftLayer_Auxiliary_Press_Release_About_Press_Release )


* [SoftLayer_Auxiliary_Press_Release_Contact_Press_Release](/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release )


* [SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release](/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release )




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
A press release's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[publishDate]: #publishdate
#### [publishDate]
The data a press release was published.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[releaseLocation]: #releaselocation
#### [releaseLocation]
A press release's location.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[subTitle]: #subtitle
#### [subTitle]
A press release's sub-title.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[title]: #title
#### [title]
A press release's title.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[websiteHighlightFlag]: #websitehighlightflag
#### [websiteHighlightFlag]
Whether or not a press release is highlighted on the SoftLayer Website.  
<span class="type-label">Type: </span>**boolean**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[about]: #about
#### [about]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_About_Press_Release'>SoftLayer_Auxiliary_Press_Release_About_Press_Release[] </a>**


</div>
<div class="prop-row">

-----
[contacts]: #contacts
#### [contacts]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release'>SoftLayer_Auxiliary_Press_Release_Contact_Press_Release[] </a>**


</div>
<div class="prop-row">

-----
[mediaPartners]: #mediapartners
#### [mediaPartners]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release'>SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release[] </a>**


</div>
<div class="prop-row">

-----
[pressReleaseContent]: #pressreleasecontent
#### [pressReleaseContent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Content'>SoftLayer_Auxiliary_Press_Release_Content </a>**


</div>

## Count
<div class="prop-row">

-----
[aboutCount]: #aboutcount
#### [aboutCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[contactCount]: #contactcount
#### [contactCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[mediaPartnerCount]: #mediapartnercount
#### [mediaPartnerCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


