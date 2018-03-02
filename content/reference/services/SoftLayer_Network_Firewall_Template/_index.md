---
title: "SoftLayer_Network_Firewall_Template"
description: "The SoftLayer_Network_Firewall_Template service can be used to retrieve recommended SoftLayer network firewall templates... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Template"
---
# SoftLayer_Network_Firewall_Template
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Firewall_Template' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Template' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_Firewall_Template service can be used to retrieve recommended SoftLayer network firewall templates and template rules. 

The provided firewall templates are recommend rule sets for use with SoftLayer Hardware Firewall (Dedicated).  These optimized templates are designed to balance security restriction with application availability.  The templates given may be altered to provide custom network security, or may be used as-is for basic security. At least one rule set MUST be applied for the firewall to block traffic. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))




### seeAlso

* [SoftLayer_Network_Component_Firewall](/reference/datatypes/SoftLayer_Network_Component_Firewall )


* [SoftLayer_Network_Firewall_Update_Request](/reference/datatypes/SoftLayer_Network_Firewall_Update_Request )


* [SoftLayer_Network_Component_Firewall](/reference/datatypes/SoftLayer_Network_Component_Firewall )


* [SoftLayer_Network_Firewall_Update_Request](/reference/datatypes/SoftLayer_Network_Firewall_Update_Request )


* [SoftLayer_Network_Firewall_Update_Request](/reference/datatypes/SoftLayer_Network_Firewall_Update_Request )


        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Template/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'>Get all available firewall template objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Template/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Firewall_Template record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Firewall_Template/getRules'> getRules</a> </span>
            <div class='views-field-body'>Retrieve the rule set that belongs to this firewall rules template.</div>
        </div>
        </div>
</div>

