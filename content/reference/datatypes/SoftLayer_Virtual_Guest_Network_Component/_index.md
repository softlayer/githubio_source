---
title: "SoftLayer_Virtual_Guest_Network_Component"
description: "The virtual guest network component data type presents the structure in which all computing instance network components... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Network_Component"
---

# SoftLayer_Virtual_Guest_Network_Component
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component' >Datatype</a></li>
    </ul>
</div>

## Description 
The virtual guest network component data type presents the structure in which all computing instance network components are presented. Internally, the structure supports various virtualization platforms with no change to external interaction. 

A guest, also known as a virtual server, represents an allocation of resources on a virtual host. 





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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date a computing instance's network component was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestId" name=guestId>guestId</a></span>
            <div class='views-field-body'>The unique ID of the [[SoftLayer_Virtual_Guest|computing instance]] that this network component belongs to.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A computing instance's network component's unique ID.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#macAddress" name=macAddress>macAddress</a></span>
            <div class='views-field-body'>A computing instance network component's unique MAC address.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maxSpeed" name=maxSpeed>maxSpeed</a></span>
            <div class='views-field-body'>A computing instance network component's maximum allowed speed, measured in Mbit per second. ''maxSpeed'' is determined by the capabilities of the network interface and the port speed purchased on your SoftLayer computing instance.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a computing instance's network component was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A computing instance network component's short name. This is usually ''eth''. Use this in conjunction with the ''port'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkId" name=networkId>networkId</a></span>
            <div class='views-field-body'>A computing instance's network component's [[SoftLayer_Virtual_Network|network]] ID  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#port" name=port>port</a></span>
            <div class='views-field-body'>A computing instance network component's port number. Most computing instances have more than one network interface. The port property separates these interfaces. Use this in conjunction with the ''name'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#speed" name=speed>speed</a></span>
            <div class='views-field-body'>A computing instance network component's speed, measured in Mbit per second. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>A computing instance network component's status. This can be one of four possible values: "ACTIVE", "DISABLED", "INACTIVE", or "ABUSE_DISCONNECT". "ACTIVE" network components are enabled and in use on a cloud instance. "ABUSE_DISCONNECT" status components have been administratively disabled by SoftLayer accounting or abuse. "DISABLED" components have been administratively disabled by you, the user. You should never see a network interface in MACWAIT state. If you happen to see one please contact SoftLayer support.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#uuid" name=uuid>uuid</a></span>
            <div class='views-field-body'>A computing instance's network component's unique ID on a virtualization platform.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guest" name=guest>guest</a></span>
            <div class='views-field-body'>The computing instance that this network component exists on. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#highAvailabilityFirewallFlag" name=highAvailabilityFirewallFlag>highAvailabilityFirewallFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddressBindings" name=ipAddressBindings>ipAddressBindings</a></span>
            <div class='views-field-body'>The records of all IP addresses bound to a computing instance's network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IpAddress'>SoftLayer_Virtual_Guest_Network_Component_IpAddress[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentFirewall" name=networkComponentFirewall>networkComponentFirewall</a></span>
            <div class='views-field-body'>The upstream network component firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlan" name=networkVlan>networkVlan</a></span>
            <div class='views-field-body'>The VLAN that a computing instance network component's subnet is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryIpAddress" name=primaryIpAddress>primaryIpAddress</a></span>
            <div class='views-field-body'>A computing instance network component's primary IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryIpAddressRecord" name=primaryIpAddressRecord>primaryIpAddressRecord</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primarySubnet" name=primarySubnet>primarySubnet</a></span>
            <div class='views-field-body'>A network component's subnet for its primary IP address </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#primaryVersion6IpAddressRecord" name=primaryVersion6IpAddressRecord>primaryVersion6IpAddressRecord</a></span>
            <div class='views-field-body'>A network component's primary IPv6 IP address record. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#router" name=router>router</a></span>
            <div class='views-field-body'>A network component's routers. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityGroupBindings" name=securityGroupBindings>securityGroupBindings</a></span>
            <div class='views-field-body'>The bindings associating security groups to this network component </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding'>SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnets" name=subnets>subnets</a></span>
            <div class='views-field-body'>A network component's subnets. A subnet is a group of IP addresses </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddressBindingCount" name=ipAddressBindingCount>ipAddressBindingCount</a></span>
            <div class='views-field-body'>A count of the records of all IP addresses bound to a computing instance's network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityGroupBindingCount" name=securityGroupBindingCount>securityGroupBindingCount</a></span>
            <div class='views-field-body'>A count of the bindings associating security groups to this network component </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnetCount" name=subnetCount>subnetCount</a></span>
            <div class='views-field-body'>A count of a network component's subnets. A subnet is a group of IP addresses </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


