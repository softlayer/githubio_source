---
title: "SoftLayer_Software_License"
description: "This class describes a specific type of license, like a Microsoft Windows Site License, a GPL license, or a license of a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_License"
---

# SoftLayer_Software_License
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_License' >Datatype</a></li>
    </ul>
</div>

## Description 
This class describes a specific type of license, like a Microsoft Windows Site License, a GPL license, or a license of another type. 



### seeAlso

* [SoftLayer_Software_Component](/reference/datatypes/SoftLayer_Software_Component )


* [SoftLayer_Software_Description](/reference/datatypes/SoftLayer_Software_Description )




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
An ID number for this specific License type.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[softwareDescriptionId]: #softwaredescriptionid
#### [softwareDescriptionId]
The ID number of a Software Description that this specific license is valid for.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that owns this specific License instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[owner]: #owner
#### [owner]
The account that owns this specific License instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
A Description of the software that this license instance is valid for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**


</div>

## Count
</div>


