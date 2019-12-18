---
title: "SoftLayer_Auxiliary_Press_Release_Contact_Press_Release"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release_Contact_Press_Release"
---

# SoftLayer_Auxiliary_Press_Release_Contact_Press_Release
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release' >Datatype</a></li>
    </ul>
</div>

## Description 



### associatedMethods

*  [SoftLayer_Auxiliary_Press_Release_Contact_Press_Release::getObject](/reference/services/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release/getObject )



### seeAlso

* [SoftLayer_Auxiliary_Press_Release_Contact_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release )




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
A press release contact cross  
<span class="type-label">Type: </span>**integer**

-----
[pressReleaseContactId]: #pressreleasecontactid
#### [pressReleaseContactId]
A press release contact's internal  
<span class="type-label">Type: </span>**integer**

-----
[pressReleaseId]: #pressreleaseid
#### [pressReleaseId]
A press release internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[sortOrder]: #sortorder
#### [sortOrder]
The number that associated a contact  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[contacts]: #contacts
#### [contacts]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Contact'>SoftLayer_Auxiliary_Press_Release_Contact[] </a>**

-----
[pressReleases]: #pressreleases
#### [pressReleases]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release'>SoftLayer_Auxiliary_Press_Release[] </a>**


## Count

-----
[contactCount]: #contactcount
#### [contactCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[pressReleaseCount]: #pressreleasecount
#### [pressReleaseCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


