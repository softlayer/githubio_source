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

* [SoftLayer_Auxiliary_Press_Release_Content](/reference/services/SoftLayer_Auxiliary_Press_Release_Content )


* [SoftLayer_Auxiliary_Press_Release_About_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release_About_Press_Release )


* [SoftLayer_Auxiliary_Press_Release_Contact_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release )


* [SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release )




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
A press release's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[publishDate]: #publishdate
#### [publishDate]
The data a press release was published.  
<span class="type-label">Type: </span>**dateTime**

-----
[releaseLocation]: #releaselocation
#### [releaseLocation]
A press release's location.  
<span class="type-label">Type: </span>**string**

-----
[subTitle]: #subtitle
#### [subTitle]
A press release's sub-title.  
<span class="type-label">Type: </span>**string**

-----
[title]: #title
#### [title]
A press release's title.  
<span class="type-label">Type: </span>**string**

-----
[websiteHighlightFlag]: #websitehighlightflag
#### [websiteHighlightFlag]
Whether or not a press release is highlighted on the SoftLayer Website.  
<span class="type-label">Type: </span>**boolean**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[about]: #about
#### [about]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_About_Press_Release'>SoftLayer_Auxiliary_Press_Release_About_Press_Release[] </a>**

-----
[contacts]: #contacts
#### [contacts]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release'>SoftLayer_Auxiliary_Press_Release_Contact_Press_Release[] </a>**

-----
[mediaPartners]: #mediapartners
#### [mediaPartners]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release'>SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release[] </a>**

-----
[pressReleaseContent]: #pressreleasecontent
#### [pressReleaseContent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Content'>SoftLayer_Auxiliary_Press_Release_Content </a>**


## Count

-----
[aboutCount]: #aboutcount
#### [aboutCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[contactCount]: #contactcount
#### [contactCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[mediaPartnerCount]: #mediapartnercount
#### [mediaPartnerCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


