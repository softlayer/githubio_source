---
title: "SoftLayer_Network_Subnet_IpAddress"
description: "Every SoftLayer IP address is defined in the SoftLayer_Network_Subnet_IpAddress service. SoftLayer IP addresses are assi... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
---
# SoftLayer_Network_Subnet_IpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_IpAddress' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer IP address is defined in the SoftLayer_Network_Subnet_IpAddress service. SoftLayer IP addresses are assigned to a SoftLayer_Network_Subnet.  The SoftLayer_Network_Subnet_IpAddress service gives you information about an IP address such if it is reserved, a network address, or a gateway.  Use the data returned by these methods with other API services to get more detailed information about your services. 

SoftLayer customers can order and manage IP addresses through the customer portal. If you need to cancel a subnet please open a sales ticket in our customer portal and our account management staff will assist you. 
### external links
        Array
(
    [url] => http://en.wikipedia.org/wiki/Ip_address
    [description] => Ip address at Wikipedia
)
1        Array
(
    [url] => http://tools.ietf.org/html/rfc791
    [description] => RFC791: Internet Protocol Specification at ietf.org
)
1        
### seeAlso
        SoftLayer_Network_Vlan1        SoftLayer_Network_Subnet1        SoftLayer_Network_Subnet_IpAddress_Version61                
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/allowAccessToNetworkStorage'> allowAccessToNetworkStorage</a> </span>
            <div class='views-field-body'>Allow access to a SoftLayer_Network_Storage volume from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/allowAccessToNetworkStorageList'> allowAccessToNetworkStorageList</a> </span>
            <div class='views-field-body'>Allow access to multiple SoftLayer_Network_Storage volumes from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit the object by passing in a modified instance of the object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/editObjects'> editObjects</a> </span>
            <div class='views-field-body'>Edit multiple objects by passing in modified instances of the object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/findByIpv4Address'> findByIpv4Address</a> </span>
            <div class='views-field-body'>Search for an IP address record by IPv4 address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getAllowedHost'> getAllowedHost</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this IP Address to Network Storage supporting access control lists.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getAllowedNetworkStorage'> getAllowedNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getAllowedNetworkStorageReplicas'> getAllowedNetworkStorageReplicas</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getApplicationDeliveryController'> getApplicationDeliveryController</a> </span>
            <div class='views-field-body'>Retrieve the application delivery controller using this address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getAttachedNetworkStorages'> getAttachedNetworkStorages</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Storage volumes authorized to this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getAvailableNetworkStorages'> getAvailableNetworkStorages</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getByIpAddress'> getByIpAddress</a> </span>
            <div class='views-field-body'>Search for an IP address record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getContextTunnelTranslations'> getContextTunnelTranslations</a> </span>
            <div class='views-field-body'>Retrieve an IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getEndpointSubnets'> getEndpointSubnets</a> </span>
            <div class='views-field-body'>Retrieve all the subnets routed to an IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getGuestNetworkComponent'> getGuestNetworkComponent</a> </span>
            <div class='views-field-body'>Retrieve a network component that is statically routed to an IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getGuestNetworkComponentBinding'> getGuestNetworkComponentBinding</a> </span>
            <div class='views-field-body'>Retrieve a network component that is statically routed to an IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve a server that this IP address is routed to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getNetworkComponent'> getNetworkComponent</a> </span>
            <div class='views-field-body'>Retrieve a network component that is statically routed to an IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Subnet_IpAddress record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getPrivateNetworkGateway'> getPrivateNetworkGateway</a> </span>
            <div class='views-field-body'>Retrieve the network gateway appliance using this address as the private IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getProtectionAddress'> getProtectionAddress</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getPublicNetworkGateway'> getPublicNetworkGateway</a> </span>
            <div class='views-field-body'>Retrieve the network gateway appliance using this address as the public IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getRemoteManagementNetworkComponent'> getRemoteManagementNetworkComponent</a> </span>
            <div class='views-field-body'>Retrieve an IPMI-based management network component of the IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getSubnet'> getSubnet</a> </span>
            <div class='views-field-body'>Retrieve an IP address' associated subnet.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getSyslogEventsOneDay'> getSyslogEventsOneDay</a> </span>
            <div class='views-field-body'>Retrieve all events for this IP address stored in the datacenter syslogs from the last 24 hours</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getSyslogEventsSevenDays'> getSyslogEventsSevenDays</a> </span>
            <div class='views-field-body'>Retrieve all events for this IP address stored in the datacenter syslogs from the last 7 days</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByDestinationPortOneDay'> getTopTenSyslogEventsByDestinationPortOneDay</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByDestinationPortSevenDays'> getTopTenSyslogEventsByDestinationPortSevenDays</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by destination port, for the last 7 days</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByProtocolsOneDay'> getTopTenSyslogEventsByProtocolsOneDay</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 24 hours</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByProtocolsSevenDays'> getTopTenSyslogEventsByProtocolsSevenDays</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 7 days</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourceIpOneDay'> getTopTenSyslogEventsBySourceIpOneDay</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourceIpSevenDays'> getTopTenSyslogEventsBySourceIpSevenDays</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourcePortOneDay'> getTopTenSyslogEventsBySourcePortOneDay</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 24 hours</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourcePortSevenDays'> getTopTenSyslogEventsBySourcePortSevenDays</a> </span>
            <div class='views-field-body'>Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 7 days</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getVirtualGuest'> getVirtualGuest</a> </span>
            <div class='views-field-body'>Retrieve a virtual guest that this IP address is routed to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/getVirtualLicenses'> getVirtualLicenses</a> </span>
            <div class='views-field-body'>Retrieve virtual licenses allocated for an IP Address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Subnet_IpAddress/removeAccessToNetworkStorageList'> removeAccessToNetworkStorageList</a> </span>
            <div class='views-field-body'>Remove access to multiple SoftLayer_Network_Storage volumes from this device. </div>
        </div>
        </div>
</div>

