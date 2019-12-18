---
title: "SoftLayer_Network_Bandwidth_Version1_Interface"
description: "All bandwidth tracking is maintained through the switch that the bandwidth is used through.  All bandwidth is stored in... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Interface"
---

# SoftLayer_Network_Bandwidth_Version1_Interface
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Interface' >Datatype</a></li>
    </ul>
</div>

## Description 
All bandwidth tracking is maintained through the switch that the bandwidth is used through.  All bandwidth is stored in a "pod" repository.  An interface links the hardware switch with the pod repository identification number. This is only relevant to bandwidth data.  It is not common to use this. 





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
[hostId]: #hostid
#### [hostId]
A interface's host.  The host stores the pod number for the bandwidth data.  
<span class="type-label">Type: </span>**integer**

-----
[networkComponentId]: #networkcomponentid
#### [networkComponentId]
The network component for this interface.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[host]: #host
#### [host]
The host for an interface. This is not to be confused with a SoftLayer hardware  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Host'>SoftLayer_Network_Bandwidth_Version1_Host </a>**

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
The switch for an interface.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**


## Count
</div>


