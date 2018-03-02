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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hostId" name=hostId>hostId</a></span>
            <div class='views-field-body'>A interface's host.  The host stores the pod number for the bandwidth data. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentId" name=networkComponentId>networkComponentId</a></span>
            <div class='views-field-body'>The network component for this interface. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#host" name=host>host</a></span>
            <div class='views-field-body'>The host for an interface. This is not to be confused with a SoftLayer hardware </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Host'>SoftLayer_Network_Bandwidth_Version1_Host </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponent" name=networkComponent>networkComponent</a></span>
            <div class='views-field-body'>The switch for an interface. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


