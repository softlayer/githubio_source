---
title: "SoftLayer_Network_Subnet"
description: "Every SoftLayer ip address is associated with a subnet which is defined in the SoftLayer_Network_Subnet service. SoftLay... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
---
# SoftLayer_Network_Subnet
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer ip address is associated with a subnet which is defined in the SoftLayer_Network_Subnet service. SoftLayer subnets define a group of ip addresses and are assigned to a SoftLayer_Network_Vlan.  The SoftLayer_Network_Subnet service gives you information about your subnet such as your network address, broadcast address, the subnet gateway address, and the total number of IP addresses within the subnet. Use the data returned by these methods with other API services to get more detailed information about your services. 

Along with VLANs, subnets are an integral part of the SoftLayer network. Each server ordered by SoftLayer comes with at least one public and one private subnet, with more available for order in the customer portal. Subnets exist in the SoftLayer network as either interfaces on a VLAN or as route destination from an IP address or VLAN. 

SoftLayer customers can order and manage subnets through the customer portal. If you need to cancel a subnet please open a sales ticket in our customer portal and our account management staff will assist you. 

### External Links


* [Subnetwork at Wikipedia](http://en.wikipedia.org/wiki/Subnetwork)


* [RFC950:Internet Standard Subnetting Procedure at ietf.org](http://tools.ietf.org/html/rfc950)




### seeAlso

* [SoftLayer_Network_Vlan](/reference/datatypes/SoftLayer_Network_Vlan )


* [SoftLayer_Network_IpAddress](/reference/datatypes/SoftLayer_Network_IpAddress )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Network_Subnet/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Network_Subnet/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 

#### [createReverseDomainRecords](/reference/services/SoftLayer_Network_Subnet/createReverseDomainRecords)
Create the default PTR records for this subnet

#### [createSubnetRouteUpdateTransaction](/reference/services/SoftLayer_Network_Subnet/createSubnetRouteUpdateTransaction)
create a new transaction to modify a subnet route.

#### [createSwipTransaction](/reference/services/SoftLayer_Network_Subnet/createSwipTransaction)
create a SWIP transaction for a subnet

#### [editNote](/reference/services/SoftLayer_Network_Subnet/editNote)
Edit the note for this subnet.

#### [findAllSubnetsAndActiveSwipTransactionStatus](/reference/services/SoftLayer_Network_Subnet/findAllSubnetsAndActiveSwipTransactionStatus)
Retrieve a list of subnets along with their SWIP transaction statuses.

#### [getAccount](/reference/services/SoftLayer_Network_Subnet/getAccount)


#### [getActiveRegistration](/reference/services/SoftLayer_Network_Subnet/getActiveRegistration)
Retrieve if present, the active registration for this subnet.

#### [getActiveSwipTransaction](/reference/services/SoftLayer_Network_Subnet/getActiveSwipTransaction)
Retrieve all the swip transactions associated with a subnet that are still active.

#### [getActiveTransaction](/reference/services/SoftLayer_Network_Subnet/getActiveTransaction)
Retrieve the billing item for a subnet.

#### [getAddressSpace](/reference/services/SoftLayer_Network_Subnet/getAddressSpace)
Retrieve identifier which distinguishes what classification of addresses the subnet represents.

#### [getAllowedHost](/reference/services/SoftLayer_Network_Subnet/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this Subnet to Network Storage supporting access control lists.

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Network_Subnet/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Network_Subnet/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.

#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Network_Subnet/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Network_Subnet/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 

#### [getBillingItem](/reference/services/SoftLayer_Network_Subnet/getBillingItem)
Retrieve the billing item for a subnet.

#### [getBoundDescendants](/reference/services/SoftLayer_Network_Subnet/getBoundDescendants)


#### [getBoundRouterFlag](/reference/services/SoftLayer_Network_Subnet/getBoundRouterFlag)
Retrieve whether or not this subnet is associated with a router. Subnets that are not associated with a router cannot be routed.

#### [getBoundRouters](/reference/services/SoftLayer_Network_Subnet/getBoundRouters)


#### [getChildren](/reference/services/SoftLayer_Network_Subnet/getChildren)


#### [getDatacenter](/reference/services/SoftLayer_Network_Subnet/getDatacenter)
Retrieve the data center this subnet may be routed within.

#### [getDescendants](/reference/services/SoftLayer_Network_Subnet/getDescendants)


#### [getDisplayLabel](/reference/services/SoftLayer_Network_Subnet/getDisplayLabel)


#### [getEndPointIpAddress](/reference/services/SoftLayer_Network_Subnet/getEndPointIpAddress)
Retrieve a static routed ip address

#### [getGlobalIpRecord](/reference/services/SoftLayer_Network_Subnet/getGlobalIpRecord)


#### [getHardware](/reference/services/SoftLayer_Network_Subnet/getHardware)
Retrieve the hardware using IP addresses on this subnet.

#### [getIpAddresses](/reference/services/SoftLayer_Network_Subnet/getIpAddresses)
Retrieve all the ip addresses associated with a subnet.

#### [getNetworkComponentFirewall](/reference/services/SoftLayer_Network_Subnet/getNetworkComponentFirewall)
Retrieve the upstream network component firewall.

#### [getNetworkProtectionAddresses](/reference/services/SoftLayer_Network_Subnet/getNetworkProtectionAddresses)


#### [getNetworkTunnelContexts](/reference/services/SoftLayer_Network_Subnet/getNetworkTunnelContexts)
Retrieve iPSec network tunnels that have access to a private subnet.

#### [getNetworkVlan](/reference/services/SoftLayer_Network_Subnet/getNetworkVlan)
Retrieve the VLAN object that a subnet is associated with.

#### [getObject](/reference/services/SoftLayer_Network_Subnet/getObject)
Retrieve a SoftLayer_Network_Subnet record.

#### [getPodName](/reference/services/SoftLayer_Network_Subnet/getPodName)
Retrieve the pod in which this subnet resides.

#### [getProtectedIpAddresses](/reference/services/SoftLayer_Network_Subnet/getProtectedIpAddresses)


#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Network_Subnet/getRegionalInternetRegistry)


#### [getRegistrations](/reference/services/SoftLayer_Network_Subnet/getRegistrations)
Retrieve all registrations that have been created for this subnet.

#### [getReverseDomain](/reference/services/SoftLayer_Network_Subnet/getReverseDomain)
Retrieve the reverse DNS domain associated with this subnet.

#### [getReverseDomainRecords](/reference/services/SoftLayer_Network_Subnet/getReverseDomainRecords)
Retrieve all reverse DNS records associated with a subnet.

#### [getRoleKeyName](/reference/services/SoftLayer_Network_Subnet/getRoleKeyName)
Retrieve an identifier of the role the subnet is within. Roles dictate how a subnet may be used.

#### [getRoleName](/reference/services/SoftLayer_Network_Subnet/getRoleName)
Retrieve the name of the role the subnet is within. Roles dictate how a subnet may be used.

#### [getRoutableEndpointIpAddresses](/reference/services/SoftLayer_Network_Subnet/getRoutableEndpointIpAddresses)
Retrieve valid routable endpoint addresses for a subnet.

#### [getRoutingTypeKeyName](/reference/services/SoftLayer_Network_Subnet/getRoutingTypeKeyName)
Retrieve the identifier for the type of route then subnet is currently configured for.

#### [getRoutingTypeName](/reference/services/SoftLayer_Network_Subnet/getRoutingTypeName)
Retrieve the name for the type of route then subnet is currently configured for.

#### [getSubnetForIpAddress](/reference/services/SoftLayer_Network_Subnet/getSubnetForIpAddress)
Retrieve an IP addresses's associated subnet.

#### [getSwipTransaction](/reference/services/SoftLayer_Network_Subnet/getSwipTransaction)
Retrieve all the swip transactions associated with a subnet.

#### [getUnboundDescendants](/reference/services/SoftLayer_Network_Subnet/getUnboundDescendants)


#### [getUtilizedIpAddressCount](/reference/services/SoftLayer_Network_Subnet/getUtilizedIpAddressCount)
Retrieve provides the total number of utilized IP addresses on this subnet. The primary consumer of IP addresses are compute resources, which can consume more than one address. This value is only supported for primary subnet types.

#### [getVirtualGuests](/reference/services/SoftLayer_Network_Subnet/getVirtualGuests)
Retrieve the Virtual Servers using IP addresses on this subnet.

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Network_Subnet/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 

</div>

