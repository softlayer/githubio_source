---
title: "SoftLayer_Network_Subnet_IpAddress"
description: "The SoftLayer_Network_Subnet_IpAddress data type contains general information relating to a single SoftLayer IPv4 addres... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
---

# SoftLayer_Network_Subnet_IpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Subnet_IpAddress data type contains general information relating to a single SoftLayer IPv4 address. 

### External Links


* [Ip address at Wikipedia](http://en.wikipedia.org/wiki/Ip_address)


* [RFC791: Internet Protocol Specification at ietf.org](http://tools.ietf.org/html/rfc791)



### associatedMethods

*  [SoftLayer_Network_Subnet_IpAddress::getObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/getObject )
*  [SoftLayer_Network_Subnet_IpAddress::editObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/editObject )



### seeAlso

* [SoftLayer_Network_Vlan](/reference/datatypes/SoftLayer_Network_Vlan )


* [SoftLayer_Network_Subnet](/reference/datatypes/SoftLayer_Network_Subnet )


* [SoftLayer_Network_Subnet_IpAddress_Version6](/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Version6 )




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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>An IP's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddress" name=ipAddress>ipAddress</a></span>
            <div class='views-field-body'>An IP address expressed in dotted quad format. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isBroadcast" name=isBroadcast>isBroadcast</a></span>
            <div class='views-field-body'>Indicates if an IP address is reserved to be used as the network broadcast address and cannot be assigned to a network interface  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isGateway" name=isGateway>isGateway</a></span>
            <div class='views-field-body'>Indicates if an IP address is reserved to a gateway and cannot be assigned to a network interface  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isNetwork" name=isNetwork>isNetwork</a></span>
            <div class='views-field-body'>Indicates if an IP address is reserved to a network address and cannot be assigned to a network interface  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isReserved" name=isReserved>isReserved</a></span>
            <div class='views-field-body'>Indicates if an IP address is reserved and cannot be assigned to a network interface  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#note" name=note>note</a></span>
            <div class='views-field-body'>An IP address' user defined note.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnetId" name=subnetId>subnetId</a></span>
            <div class='views-field-body'>An IP address' subnet id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allowedHost" name=allowedHost>allowedHost</a></span>
            <div class='views-field-body'>The SoftLayer_Network_Storage_Allowed_Host information to connect this IP Address to Network Storage supporting access control lists. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allowedNetworkStorage" name=allowedNetworkStorage>allowedNetworkStorage</a></span>
            <div class='views-field-body'>The SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allowedNetworkStorageReplicas" name=allowedNetworkStorageReplicas>allowedNetworkStorageReplicas</a></span>
            <div class='views-field-body'>The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#applicationDeliveryController" name=applicationDeliveryController>applicationDeliveryController</a></span>
            <div class='views-field-body'>The application delivery controller using this address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#contextTunnelTranslations" name=contextTunnelTranslations>contextTunnelTranslations</a></span>
            <div class='views-field-body'>An IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endpointSubnets" name=endpointSubnets>endpointSubnets</a></span>
            <div class='views-field-body'>All the subnets routed to an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestNetworkComponent" name=guestNetworkComponent>guestNetworkComponent</a></span>
            <div class='views-field-body'>A network component that is statically routed to an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestNetworkComponentBinding" name=guestNetworkComponentBinding>guestNetworkComponentBinding</a></span>
            <div class='views-field-body'>A network component that is statically routed to an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IpAddress'>SoftLayer_Virtual_Guest_Network_Component_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardware" name=hardware>hardware</a></span>
            <div class='views-field-body'>A server that this IP address is routed to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponent" name=networkComponent>networkComponent</a></span>
            <div class='views-field-body'>A network component that is statically routed to an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateNetworkGateway" name=privateNetworkGateway>privateNetworkGateway</a></span>
            <div class='views-field-body'>The network gateway appliance using this address as the private IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protectionAddress" name=protectionAddress>protectionAddress</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Protection_Address'>SoftLayer_Network_Protection_Address[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicNetworkGateway" name=publicNetworkGateway>publicNetworkGateway</a></span>
            <div class='views-field-body'>The network gateway appliance using this address as the public IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#remoteManagementNetworkComponent" name=remoteManagementNetworkComponent>remoteManagementNetworkComponent</a></span>
            <div class='views-field-body'>An IPMI-based management network component of the IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnet" name=subnet>subnet</a></span>
            <div class='views-field-body'>An IP address' associated subnet. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#syslogEventsOneDay" name=syslogEventsOneDay>syslogEventsOneDay</a></span>
            <div class='views-field-body'>All events for this IP address stored in the datacenter syslogs from the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#syslogEventsSevenDays" name=syslogEventsSevenDays>syslogEventsSevenDays</a></span>
            <div class='views-field-body'>All events for this IP address stored in the datacenter syslogs from the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByDestinationPortOneDay" name=topTenSyslogEventsByDestinationPortOneDay>topTenSyslogEventsByDestinationPortOneDay</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByDestinationPortSevenDays" name=topTenSyslogEventsByDestinationPortSevenDays>topTenSyslogEventsByDestinationPortSevenDays</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by destination port, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByProtocolsOneDay" name=topTenSyslogEventsByProtocolsOneDay>topTenSyslogEventsByProtocolsOneDay</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by source port, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByProtocolsSevenDays" name=topTenSyslogEventsByProtocolsSevenDays>topTenSyslogEventsByProtocolsSevenDays</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by source port, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourceIpOneDay" name=topTenSyslogEventsBySourceIpOneDay>topTenSyslogEventsBySourceIpOneDay</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourceIpSevenDays" name=topTenSyslogEventsBySourceIpSevenDays>topTenSyslogEventsBySourceIpSevenDays</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourcePortOneDay" name=topTenSyslogEventsBySourcePortOneDay>topTenSyslogEventsBySourcePortOneDay</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by source port, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourcePortSevenDays" name=topTenSyslogEventsBySourcePortSevenDays>topTenSyslogEventsBySourcePortSevenDays</a></span>
            <div class='views-field-body'>Top Ten network datacenter syslog events, grouped by source port, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuest" name=virtualGuest>virtualGuest</a></span>
            <div class='views-field-body'>A virtual guest that this IP address is routed to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualLicenses" name=virtualLicenses>virtualLicenses</a></span>
            <div class='views-field-body'>Virtual licenses allocated for an IP Address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allowedNetworkStorageCount" name=allowedNetworkStorageCount>allowedNetworkStorageCount</a></span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allowedNetworkStorageReplicaCount" name=allowedNetworkStorageReplicaCount>allowedNetworkStorageReplicaCount</a></span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#contextTunnelTranslationCount" name=contextTunnelTranslationCount>contextTunnelTranslationCount</a></span>
            <div class='views-field-body'>A count of an IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endpointSubnetCount" name=endpointSubnetCount>endpointSubnetCount</a></span>
            <div class='views-field-body'>A count of all the subnets routed to an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protectionAddressCount" name=protectionAddressCount>protectionAddressCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#syslogEventsOneDayCount" name=syslogEventsOneDayCount>syslogEventsOneDayCount</a></span>
            <div class='views-field-body'>A count of all events for this IP address stored in the datacenter syslogs from the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#syslogEventsSevenDayCount" name=syslogEventsSevenDayCount>syslogEventsSevenDayCount</a></span>
            <div class='views-field-body'>A count of all events for this IP address stored in the datacenter syslogs from the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByDestinationPortOneDayCount" name=topTenSyslogEventsByDestinationPortOneDayCount>topTenSyslogEventsByDestinationPortOneDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByDestinationPortSevenDayCount" name=topTenSyslogEventsByDestinationPortSevenDayCount>topTenSyslogEventsByDestinationPortSevenDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by destination port, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByProtocolsOneDayCount" name=topTenSyslogEventsByProtocolsOneDayCount>topTenSyslogEventsByProtocolsOneDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by source port, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsByProtocolsSevenDayCount" name=topTenSyslogEventsByProtocolsSevenDayCount>topTenSyslogEventsByProtocolsSevenDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by source port, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourceIpOneDayCount" name=topTenSyslogEventsBySourceIpOneDayCount>topTenSyslogEventsBySourceIpOneDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourceIpSevenDayCount" name=topTenSyslogEventsBySourceIpSevenDayCount>topTenSyslogEventsBySourceIpSevenDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourcePortOneDayCount" name=topTenSyslogEventsBySourcePortOneDayCount>topTenSyslogEventsBySourcePortOneDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by source port, for the last 24 hours </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topTenSyslogEventsBySourcePortSevenDayCount" name=topTenSyslogEventsBySourcePortSevenDayCount>topTenSyslogEventsBySourcePortSevenDayCount</a></span>
            <div class='views-field-body'>A count of top Ten network datacenter syslog events, grouped by source port, for the last 7 days </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualLicenseCount" name=virtualLicenseCount>virtualLicenseCount</a></span>
            <div class='views-field-body'>A count of virtual licenses allocated for an IP Address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


