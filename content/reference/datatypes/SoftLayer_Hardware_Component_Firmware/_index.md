---
title: "SoftLayer_Hardware_Component_Firmware"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Firmware"
---

# SoftLayer_Hardware_Component_Firmware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[buildDate]: #builddate
#### [buildDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[hardwareComponentModelId]: #hardwarecomponentmodelid
#### [hardwareComponentModelId]
  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[isQualified]: #isqualified
#### [isQualified]
  
<span class="type-label">Type: </span>**integer**

-----
[releaseNotes]: #releasenotes
#### [releaseNotes]
  
<span class="type-label">Type: </span>**string**

-----
[version]: #version
#### [version]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware_Attribute'>SoftLayer_Hardware_Component_Firmware_Attribute[] </a>**

-----
[hardwareComponentModel]: #hardwarecomponentmodel
#### [hardwareComponentModel]
The Hardware Component Model this Firmware applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a>**

-----
[qualificationType]: #qualificationtype
#### [qualificationType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware_QualificationTypes'>SoftLayer_Hardware_Component_Firmware_QualificationTypes </a>**

-----
[revisions]: #revisions
#### [revisions]
All revisions of this firmware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Revision'>SoftLayer_Hardware_Component_Revision[] </a>**


## Count

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[revisionCount]: #revisioncount
#### [revisionCount]
A count of all revisions of this firmware.   
<span class="type-label">Type: </span>**unsigned long**

</div>


