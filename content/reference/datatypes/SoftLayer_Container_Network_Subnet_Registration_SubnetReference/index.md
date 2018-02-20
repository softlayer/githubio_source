---
title: "SoftLayer_Container_Network_Subnet_Registration_SubnetReference"
description: "SoftLayer_Container_Network_Subnet_Registration_SubnetReference is provided to reference [[SoftLayer_Network_Subnet_Regi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Subnet_Registration_SubnetReference"
---

# SoftLayer_Container_Network_Subnet_Registration_SubnetReference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Subnet_Registration_SubnetReference' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Network_Subnet_Registration_SubnetReference is provided to reference [[SoftLayer_Network_Subnet_Registration]] object and the [[SoftLayer_Network_Subnet]] it references, in CIDR form. 
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
            <span class='views-field-title'><a href="#registrationId" name=registrationId>registrationId</a></span>
            <div class='views-field-body'>The ID of the [[SoftLayer_Network_Subnet_Registration]] object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnetCidr" name=subnetCidr>subnetCidr</a></span>
            <div class='views-field-body'>The subnet address in CIDR form. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


