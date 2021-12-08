---
title: "SoftLayer_Network_Component"
description: ""
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
---
# SoftLayer_Network_Component
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Component' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component' >Datatype</a></li>
    </ul>
</div>

## Description






        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [addNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/addNetworkVlanTrunks)
Add VLAN trunks to network component

</div>

<div class="method-row">

#### [clearNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/clearNetworkVlanTrunks)
Remove all VLANs trunked to this port.

</div>

<div class="method-row">

#### [getActiveCommand](/reference/services/SoftLayer_Network_Component/getActiveCommand)
Retrieve reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command currently executing by the server's remote management card.

</div>

<div class="method-row">

#### [getCustomBandwidthDataByDate](/reference/services/SoftLayer_Network_Component/getCustomBandwidthDataByDate)
Retrieve bandwidth graph by date.

</div>

<div class="method-row">

#### [getDownlinkComponent](/reference/services/SoftLayer_Network_Component/getDownlinkComponent)
Retrieve the network component linking this object to a child device

</div>

<div class="method-row">

#### [getDuplexMode](/reference/services/SoftLayer_Network_Component/getDuplexMode)
Retrieve the duplex mode of a network component.

</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Component/getHardware)
Retrieve the hardware that a network component resides in.

</div>

<div class="method-row">

#### [getHighAvailabilityFirewallFlag](/reference/services/SoftLayer_Network_Component/getHighAvailabilityFirewallFlag)


</div>

<div class="method-row">

#### [getInterface](/reference/services/SoftLayer_Network_Component/getInterface)
Retrieve [DEPRECATED] A hardware switch's interface to the bandwidth pod.

</div>

<div class="method-row">

#### [getIpAddressBindings](/reference/services/SoftLayer_Network_Component/getIpAddressBindings)
Retrieve the records of all IP addresses bound to a network component.

</div>

<div class="method-row">

#### [getIpAddresses](/reference/services/SoftLayer_Network_Component/getIpAddresses)


</div>

<div class="method-row">

#### [getLastCommand](/reference/services/SoftLayer_Network_Component/getLastCommand)
Retrieve last reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command issued to the server's remote management card.

</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Component/getMetricTrackingObject)
Retrieve the metric tracking object for this network component.

</div>

<div class="method-row">

#### [getNetworkComponentFirewall](/reference/services/SoftLayer_Network_Component/getNetworkComponentFirewall)
Retrieve the upstream network component firewall.

</div>

<div class="method-row">

#### [getNetworkComponentGroup](/reference/services/SoftLayer_Network_Component/getNetworkComponentGroup)
Retrieve a network component's associated group.

</div>

<div class="method-row">

#### [getNetworkHardware](/reference/services/SoftLayer_Network_Component/getNetworkHardware)
Retrieve all network devices in SoftLayer's network hierarchy that this device is connected to.

</div>

<div class="method-row">

#### [getNetworkVlan](/reference/services/SoftLayer_Network_Component/getNetworkVlan)
Retrieve the VLAN that a network component's subnet is associated with.

</div>

<div class="method-row">

#### [getNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/getNetworkVlanTrunks)
Retrieve the VLANs that are trunked to this network component.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Component/getObject)
Retrieve a SoftLayer_Network_Component record.

</div>

<div class="method-row deprecated">

#### [getPortStatistics](/reference/services/SoftLayer_Network_Component/getPortStatistics)
Retrieve various network statistics for the specific port.

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getPrimaryIpAddressRecord](/reference/services/SoftLayer_Network_Component/getPrimaryIpAddressRecord)
Retrieve the primary IPv4 Address record for a network component.

</div>

<div class="method-row">

#### [getPrimarySubnet](/reference/services/SoftLayer_Network_Component/getPrimarySubnet)
Retrieve the subnet of the primary IP address assigned to this network component.

</div>

<div class="method-row">

#### [getPrimaryVersion6IpAddressRecord](/reference/services/SoftLayer_Network_Component/getPrimaryVersion6IpAddressRecord)
Retrieve the primary IPv6 Address record for a network component.

</div>

<div class="method-row">

#### [getRecentCommands](/reference/services/SoftLayer_Network_Component/getRecentCommands)
Retrieve the last five reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) commands issued to the server's remote management card.

</div>

<div class="method-row">

#### [getRedundancyCapableFlag](/reference/services/SoftLayer_Network_Component/getRedundancyCapableFlag)
Retrieve indicates whether the network component is participating in a group of two or more components capable of being operationally redundant, if enabled.

</div>

<div class="method-row">

#### [getRedundancyEnabledFlag](/reference/services/SoftLayer_Network_Component/getRedundancyEnabledFlag)
Retrieve indicates whether the network component is participating in a group of two or more components which is actively providing link redundancy.

</div>

<div class="method-row">

#### [getRemoteManagementUsers](/reference/services/SoftLayer_Network_Component/getRemoteManagementUsers)
Retrieve user(s) credentials to issue commands and/or interact with the server's remote management card.

</div>

<div class="method-row">

#### [getRouter](/reference/services/SoftLayer_Network_Component/getRouter)
Retrieve a network component's routers.

</div>

<div class="method-row">

#### [getStorageNetworkFlag](/reference/services/SoftLayer_Network_Component/getStorageNetworkFlag)
Retrieve whether a network component's primary ip address is from a storage network subnet or not. [Deprecated]

</div>

<div class="method-row">

#### [getSubnets](/reference/services/SoftLayer_Network_Component/getSubnets)
Retrieve a network component's subnets. A subnet is a group of IP addresses

</div>

<div class="method-row">

#### [getUplinkComponent](/reference/services/SoftLayer_Network_Component/getUplinkComponent)
Retrieve the network component linking this object to parent

</div>

<div class="method-row">

#### [getUplinkDuplexMode](/reference/services/SoftLayer_Network_Component/getUplinkDuplexMode)
Retrieve the duplex mode of the uplink network component linking to this object

</div>

<div class="method-row">

#### [removeNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/removeNetworkVlanTrunks)
Remove VLAN trunks from a network component

</div>
</div>

</div>

