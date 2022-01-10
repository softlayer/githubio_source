---
title: "SoftLayer_Layout_Profile_Preference"
description: "The SoftLayer_Layout_Profile_Preference contains definitions for layout preferences"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Preference"
---

# SoftLayer_Layout_Profile_Preference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Profile_Preference' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Layout_Profile_Preference contains definitions for layout preferences 





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
[createDate]: #createdate
#### [createDate]
Timestamp of when the preference was created  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[defaultValueFlag]: #defaultvalueflag
#### [defaultValueFlag]
Indicates whether this is a default value or not  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[layoutContainerId]: #layoutcontainerid
#### [layoutContainerId]
The id of the related [SoftLayer_Layout_Container]({{<ref "reference/datatypes/SoftLayer_Layout_Container">}})  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[layoutItemId]: #layoutitemid
#### [layoutItemId]
The id of the related [SoftLayer_Layout_Item]({{<ref "reference/datatypes/SoftLayer_Layout_Item">}})  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[layoutPreferenceId]: #layoutpreferenceid
#### [layoutPreferenceId]
The internal identifier of the overridden [SoftLayer_Layout_Preference]({{<ref "reference/datatypes/SoftLayer_Layout_Preference">}})  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[layoutProfileId]: #layoutprofileid
#### [layoutProfileId]
The internal identifier of the related [SoftLayer_Layout_Profile]({{<ref "reference/datatypes/SoftLayer_Layout_Profile">}})  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Timestamp of when the preference was last updated  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
The value overriding the default value  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[layoutContainer]: #layoutcontainer
#### [layoutContainer]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Container'>SoftLayer_Layout_Container </a>**  



</div>
<div class="prop-row">

-----
[layoutItem]: #layoutitem
#### [layoutItem]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Item'>SoftLayer_Layout_Item </a>**  



</div>
<div class="prop-row">

-----
[layoutPreference]: #layoutpreference
#### [layoutPreference]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Preference'>SoftLayer_Layout_Preference </a>**  



</div>
<div class="prop-row">

-----
[layoutProfile]: #layoutprofile
#### [layoutProfile]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile </a>**  



</div>

## Count
</div>


