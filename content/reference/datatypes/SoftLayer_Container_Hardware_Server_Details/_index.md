---
title: "SoftLayer_Container_Hardware_Server_Details"
description: "The SoftLayer_Container_Hardware_Server_Details data type contains information relating to a server's component informat... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Hardware_Server_Details"
---

# SoftLayer_Container_Hardware_Server_Details
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Details' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Container_Hardware_Server_Details data type contains information relating to a server's component information, network information, and software information. 


### associatedMethods

*  [SoftLayer_Hardware::getObject](/reference/services/SoftLayer_Hardware/getObject )





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
[components]: #components
#### [components]
The components that belong to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
The network components that belong to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**  



</div>
<div class="prop-row">

-----
[software]: #software
#### [software]
The software that belong to a piece of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component[] </a>**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


