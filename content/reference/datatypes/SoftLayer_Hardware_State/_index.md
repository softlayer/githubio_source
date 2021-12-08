---
title: "SoftLayer_Hardware_State"
description: "The SoftLayer_Hardware_State type contains general information about the current state of it's associated hardware, incl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_State"
---

# SoftLayer_Hardware_State
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_State' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Hardware_State type contains general information about the current state of it's associated hardware, including the current power state (i.e. Running or Stopped), and it's current transitioning state (e.g. Provisioning, Reloading). 





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
[hardwareId]: #hardwareid
#### [hardwareId]
The hardware this state is assigned to.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A hardware state's unique identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[state]: #state
#### [state]
Represents the current state of the assigned hardware.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


