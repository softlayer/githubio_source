---
title: "SoftLayer_Hardware_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Group"
---

# SoftLayer_Hardware_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Group' >Datatype</a></li>
    </ul>
</div>

## Description 






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
            <span class='views-field-title'><a href="#domain" name=domain>domain</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hostname" name=hostname>hostname</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downlinkServers" name=downlinkServers>downlinkServers</a></span>
            <div class='views-field-body'>All servers attached to a network hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downlinkVirtualGuests" name=downlinkVirtualGuests>downlinkVirtualGuests</a></span>
            <div class='views-field-body'>All virtual guests attached to a network hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downstreamNetworkHardware" name=downstreamNetworkHardware>downstreamNetworkHardware</a></span>
            <div class='views-field-body'>All network hardware downstream from this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downstreamNetworkHardwareWithIncidents" name=downstreamNetworkHardwareWithIncidents>downstreamNetworkHardwareWithIncidents</a></span>
            <div class='views-field-body'>All network hardware with monitoring warnings or errors downstream from this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareChassis" name=hardwareChassis>hardwareChassis</a></span>
            <div class='views-field-body'>The chassis that a piece of hardware is housed in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Chassis'>SoftLayer_Hardware_Chassis </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkMonitorAttachedDownHardware" name=networkMonitorAttachedDownHardware>networkMonitorAttachedDownHardware</a></span>
            <div class='views-field-body'>All servers attached downstream to a hardware that have failed monitoring </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkMonitorAttachedDownVirtualGuests" name=networkMonitorAttachedDownVirtualGuests>networkMonitorAttachedDownVirtualGuests</a></span>
            <div class='views-field-body'>Virtual guests that are attached downstream to a hardware that have failed monitoring </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkStatus" name=networkStatus>networkStatus</a></span>
            <div class='views-field-body'>The value of a hardware's network status attribute. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downlinkServerCount" name=downlinkServerCount>downlinkServerCount</a></span>
            <div class='views-field-body'>A count of all servers attached to a network hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downlinkVirtualGuestCount" name=downlinkVirtualGuestCount>downlinkVirtualGuestCount</a></span>
            <div class='views-field-body'>A count of all virtual guests attached to a network hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downstreamNetworkHardwareCount" name=downstreamNetworkHardwareCount>downstreamNetworkHardwareCount</a></span>
            <div class='views-field-body'>A count of all network hardware downstream from this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downstreamNetworkHardwareWithIncidentCount" name=downstreamNetworkHardwareWithIncidentCount>downstreamNetworkHardwareWithIncidentCount</a></span>
            <div class='views-field-body'>A count of all network hardware with monitoring warnings or errors downstream from this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkMonitorAttachedDownHardwareCount" name=networkMonitorAttachedDownHardwareCount>networkMonitorAttachedDownHardwareCount</a></span>
            <div class='views-field-body'>A count of all servers attached downstream to a hardware that have failed monitoring </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkMonitorAttachedDownVirtualGuestCount" name=networkMonitorAttachedDownVirtualGuestCount>networkMonitorAttachedDownVirtualGuestCount</a></span>
            <div class='views-field-body'>A count of virtual guests that are attached downstream to a hardware that have failed monitoring </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


