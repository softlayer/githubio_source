---
title: "SoftLayer_Container_Network_IntrusionProtection_SubnetReport"
description: "The IntrusionProtection_SubnetReport object is the container that holds the SoftLayer_Container_Network_IntrusionProtect... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_IntrusionProtection_SubnetReport"
---

# SoftLayer_Container_Network_IntrusionProtection_SubnetReport
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_SubnetReport' >Datatype</a></li>
    </ul>
</div>

## Description 
The IntrusionProtection_SubnetReport object is the container that holds the SoftLayer_Container_Network_IntrusionProtection_Event objects for a particular subnet, or "All Subnets", whatever the case may be.  Subnet, subnet mask, direction, and the individual events are returned by this object. 


### associatedMethods

*  [SoftLayer_Network_TippingPointReporting::getSubnetReportForEntireAccount](/reference/services/SoftLayer_Network_TippingPointReporting/getSubnetReportForEntireAccount )
*  [SoftLayer_Network_TippingPointReporting::getReportForIpAddressOrSubnet](/reference/services/SoftLayer_Network_TippingPointReporting/getReportForIpAddressOrSubnet )
*  [SoftLayer_Network_TippingPointReporting::drillDownAttack](/reference/services/SoftLayer_Network_TippingPointReporting/drillDownAttack )





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
            <span class='views-field-title'><a href="#cidr" name=cidr>cidr</a></span>
            <div class='views-field-body'>cidr for this report.  If the subnetIpAddress is "All Subnets", this is set to 32 and should be ignored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#direction" name=direction>direction</a></span>
            <div class='views-field-body'>Direction of the attack, either 'Inbound' or 'Outbound' </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#events" name=events>events</a></span>
            <div class='views-field-body'>The class SoftLayer_Container_Network_IntrusionProtection_Event objects on this report. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Event'>SoftLayer_Container_Network_IntrusionProtection_Event[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnetIpAddress" name=subnetIpAddress>subnetIpAddress</a></span>
            <div class='views-field-body'>The "target" of this report, could be an IP address, a subnet's network identifier, or "All Subnets" </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


