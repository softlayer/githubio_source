---
title: "SoftLayer_Network_Bandwidth_Version1_Interface"
description: "[DEPRECATED] All bandwidth tracking is maintained through the switch that the bandwidth is used through.  All bandwidth... "
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

<div class="deprecated"><span class="deprecation-label">Deprecated  </span></div>

[DEPRECATED] All bandwidth tracking is maintained through the switch that the bandwidth is used through.  All bandwidth is stored in a "pod" repository.  An interface links the hardware switch with the pod repository identification number. This is only relevant to bandwidth data.  It is not common to use this. 





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
[hostId]: #hostid
#### [hostId]
A interface's host.  The host stores the pod number for the bandwidth data.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[networkComponentId]: #networkcomponentid
#### [networkComponentId]
The network component for this interface.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[host]: #host
#### [host]
[DEPRECATED] The host for an interface. This is not to be confused with SoftLayer Hardware  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Host'>SoftLayer_Network_Bandwidth_Version1_Host </a>**  



</div>
<div class="prop-row">

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
[DEPRECATED] The switch for an interface.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**  



</div>

## Count
</div>


