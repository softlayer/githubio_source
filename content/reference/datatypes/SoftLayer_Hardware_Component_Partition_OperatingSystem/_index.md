---
title: "SoftLayer_Hardware_Component_Partition_OperatingSystem"
description: "The SoftLayer_Hardware_Component_Partition_OperatingSystem data type contains general information relating to a single S... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_OperatingSystem"
---

# SoftLayer_Hardware_Component_Partition_OperatingSystem
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_Component_Partition_OperatingSystem' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_OperatingSystem' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Hardware_Component_Partition_OperatingSystem data type contains general information relating to a single SoftLayer Operating System Partition Template. 





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
[description]: #description
#### [description]
A partition template operating system's description.  Typically the title of the Operating System.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A partition template operating system's id.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
Information about the kinds of partition templates assigned to this operating system.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[partitionTemplates]: #partitiontemplates
#### [partitionTemplates]
Information regarding an operating system's [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template'>SoftLayer_Hardware_Component_Partition_Template[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[partitionTemplateCount]: #partitiontemplatecount
#### [partitionTemplateCount]
A count of information regarding an operating system's [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}).   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


