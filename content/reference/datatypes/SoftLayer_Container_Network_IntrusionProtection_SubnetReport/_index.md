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

## Local
-----
[cidr]: #cidr
#### [cidr]
cidr for this report.  If the subnetIpAddress is "All Subnets", this is set to 32 and should be ignored.  
<span class="type-label">Type: </span>**integer**

-----
[direction]: #direction
#### [direction]
Direction of the attack, either 'Inbound' or 'Outbound'  
<span class="type-label">Type: </span>**string**

-----
[events]: #events
#### [events]
The class SoftLayer_Container_Network_IntrusionProtection_Event objects on this report.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Event'>SoftLayer_Container_Network_IntrusionProtection_Event[] </a>**

-----
[subnetIpAddress]: #subnetipaddress
#### [subnetIpAddress]
The "target" of this report, could be an IP address, a subnet's network identifier, or "All Subnets"  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


