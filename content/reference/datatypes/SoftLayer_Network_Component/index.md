---
title: "SoftLayer_Network_Component"
description: "Every piece of hardware running in SoftLayer's datacenters connected to the public, private, or management networks (whe... "
layout: "datatype"
tags:
    - "datatype"
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
Every piece of hardware running in SoftLayer's datacenters connected to the public, private, or management networks (where applicable) have a corresponding network component. These network components are modeled by the SoftLayer_Network_Component data type. These data types reflect the servers' local ethernet and remote management interfaces. 
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
            <span class='views-field-title'><a href="#duplexModeId" name=duplexModeId>duplexModeId</a></span>
            <div class='views-field-body'>A network component's Duplex mode.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareId" name=hardwareId>hardwareId</a></span>
            <div class='views-field-body'>The internal identifier of the hardware that a network component belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A network component's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipmiIpAddress" name=ipmiIpAddress>ipmiIpAddress</a></span>
            <div class='views-field-body'>The IP address of an IPMI-based management network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipmiMacAddress" name=ipmiMacAddress>ipmiMacAddress</a></span>
            <div class='views-field-body'>The MAC address of an IPMI-based management network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#macAddress" name=macAddress>macAddress</a></span>
            <div class='views-field-body'>A network component's unique MAC address. IPMI-based management network interfaces may not have a MAC address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maxSpeed" name=maxSpeed>maxSpeed</a></span>
            <div class='views-field-body'>A network component's maximum allowed speed, measured in Mbit per second. ''maxSpeed'' is determined by the capabilities of the network interface and the port speed purchased on your SoftLayer server.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a network component was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A network component's short name. For most servers this is the string "eth" for ethernet ports or "mgmt" for remote management ports. Use this in conjunction with the ''port'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlanId" name=networkVlanId>networkVlanId</a></span>
            <div class='views-field-body'>The unique internal id of the network VLAN that the port belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#port" name=port>port</a></span>
            <div class='views-field-body'>A network component's port number. Most hardware has more than one network interface. The port property separates these interfaces. Use this in conjunction with the ''name'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryIpAddress" name=primaryIpAddress>primaryIpAddress</a></span>
            <div class='views-field-body'>A network component's primary IP address. IPMI-based management network interfaces may not have an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#speed" name=speed>speed</a></span>
            <div class='views-field-body'>A network component's speed, measured in Mbit per second. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>A network component's status. This can take one of four possible values: "ACTIVE", "DISABLE", "USER_OFF", or "MACWAIT". "ACTIVE" network components are enabled and in use on a servers. "DISABLE" status components have been administratively disabled by SoftLayer accounting or abuse. "USER_OFF" components have been administratively disabled by you, the user. "MACWAIT" components only exist on network components that have not been provisioned. You should never see a network interface in MACWAIT state. If you happen to see one please contact SoftLayer support.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeCommand" name=activeCommand>activeCommand</a></span>
            <div class='views-field-body'>Reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command currently executing by the server's remote management card. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downlinkComponent" name=downlinkComponent>downlinkComponent</a></span>
            <div class='views-field-body'>The network component linking this object to a child device </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#duplexMode" name=duplexMode>duplexMode</a></span>
            <div class='views-field-body'>The duplex mode of a network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Duplex_Mode'>SoftLayer_Network_Component_Duplex_Mode </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardware" name=hardware>hardware</a></span>
            <div class='views-field-body'>The hardware that a network component resides in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#highAvailabilityFirewallFlag" name=highAvailabilityFirewallFlag>highAvailabilityFirewallFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#interface" name=interface>interface</a></span>
            <div class='views-field-body'>A hardware switch's interface to the bandwidth pod. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Interface'>SoftLayer_Network_Bandwidth_Version1_Interface </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddressBindings" name=ipAddressBindings>ipAddressBindings</a></span>
            <div class='views-field-body'>The records of all IP addresses bound to a network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_IpAddress'>SoftLayer_Network_Component_IpAddress[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddresses" name=ipAddresses>ipAddresses</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastCommand" name=lastCommand>lastCommand</a></span>
            <div class='views-field-body'>Last reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command issued to the server's remote management card. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#metricTrackingObject" name=metricTrackingObject>metricTrackingObject</a></span>
            <div class='views-field-body'>The metric tracking object for this network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentFirewall" name=networkComponentFirewall>networkComponentFirewall</a></span>
            <div class='views-field-body'>The upstream network component firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentGroup" name=networkComponentGroup>networkComponentGroup</a></span>
            <div class='views-field-body'>A network component's associated group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Group'>SoftLayer_Network_Component_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkHardware" name=networkHardware>networkHardware</a></span>
            <div class='views-field-body'>All network devices in SoftLayer's network hierarchy that this device is connected to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlan" name=networkVlan>networkVlan</a></span>
            <div class='views-field-body'>The VLAN that a network component's subnet is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlanTrunks" name=networkVlanTrunks>networkVlanTrunks</a></span>
            <div class='views-field-body'>The VLANs that are trunked to this network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Network_Vlan_Trunk'>SoftLayer_Network_Component_Network_Vlan_Trunk[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryIpAddressRecord" name=primaryIpAddressRecord>primaryIpAddressRecord</a></span>
            <div class='views-field-body'>The primary IPv4 Address record for a network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primarySubnet" name=primarySubnet>primarySubnet</a></span>
            <div class='views-field-body'>The subnet of the primary IP address assigned to this network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryVersion6IpAddressRecord" name=primaryVersion6IpAddressRecord>primaryVersion6IpAddressRecord</a></span>
            <div class='views-field-body'>The primary IPv6 Address record for a network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#recentCommands" name=recentCommands>recentCommands</a></span>
            <div class='views-field-body'>The last five reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) commands issued to the server's remote management card. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#redundancyCapableFlag" name=redundancyCapableFlag>redundancyCapableFlag</a></span>
            <div class='views-field-body'>Indicates whether the network component is participating in a group of two or more components capable of being operationally redundant, if enabled. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#redundancyEnabledFlag" name=redundancyEnabledFlag>redundancyEnabledFlag</a></span>
            <div class='views-field-body'>Indicates whether the network component is participating in a group of two or more components which is actively providing link redundancy. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#remoteManagementUsers" name=remoteManagementUsers>remoteManagementUsers</a></span>
            <div class='views-field-body'>User(s) credentials to issue commands and/or interact with the server's remote management card. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_User'>SoftLayer_Hardware_Component_RemoteManagement_User[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#router" name=router>router</a></span>
            <div class='views-field-body'>A network component's routers. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#storageNetworkFlag" name=storageNetworkFlag>storageNetworkFlag</a></span>
            <div class='views-field-body'>Whether a network component's primary ip address is from a storage network subnet or not. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnets" name=subnets>subnets</a></span>
            <div class='views-field-body'>A network component's subnets. A subnet is a group of IP addresses </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#uplinkComponent" name=uplinkComponent>uplinkComponent</a></span>
            <div class='views-field-body'>The network component linking this object to parent </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#uplinkDuplexMode" name=uplinkDuplexMode>uplinkDuplexMode</a></span>
            <div class='views-field-body'>The duplex mode of the uplink network component linking to this object </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Duplex_Mode'>SoftLayer_Network_Component_Duplex_Mode </a></p></div>
        </div>
            </div>
</div>


