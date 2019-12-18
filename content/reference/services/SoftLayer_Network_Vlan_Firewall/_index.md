---
title: "SoftLayer_Network_Vlan_Firewall"
description: "The SoftLayer_Network_Vlan_Firewall service accesses general information relating to a single SoftLayer VLAN firewall.... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
---
# SoftLayer_Network_Vlan_Firewall
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Vlan_Firewall' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_Vlan_Firewall service accesses general information relating to a single SoftLayer VLAN firewall.  This is the object which ties the running rules to a specific downstream server. The current running rule set can be pulled from this service. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))




### seeAlso

* [SoftLayer_Network_Firewall_Template](/reference/services/SoftLayer_Network_Firewall_Template )


* [SoftLayer_Network_Firewall_Update_Request](/reference/services/SoftLayer_Network_Firewall_Update_Request )


        
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

#### [approveBypassRequest](/reference/services/SoftLayer_Network_Vlan_Firewall/approveBypassRequest)
Approve a request from technical support to bypass the firewall.

#### [getAccountId](/reference/services/SoftLayer_Network_Vlan_Firewall/getAccountId)


#### [getBandwidthAllocation](/reference/services/SoftLayer_Network_Vlan_Firewall/getBandwidthAllocation)
Retrieve a firewall's allotted bandwidth (measured in GB).

#### [getBillingCycleBandwidthUsage](/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingCycleBandwidthUsage)
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this firewall is attached to.

#### [getBillingCyclePrivateBandwidthUsage](/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingCyclePrivateBandwidthUsage)
Retrieve the raw private bandwidth usage data for the current billing cycle.

#### [getBillingCyclePublicBandwidthUsage](/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingCyclePublicBandwidthUsage)
Retrieve the raw public bandwidth usage data for the current billing cycle.

#### [getBillingItem](/reference/services/SoftLayer_Network_Vlan_Firewall/getBillingItem)
Retrieve the billing item for a Hardware Firewall (Dedicated).

#### [getBypassRequestStatus](/reference/services/SoftLayer_Network_Vlan_Firewall/getBypassRequestStatus)
Retrieve administrative bypass request status.

#### [getDatacenter](/reference/services/SoftLayer_Network_Vlan_Firewall/getDatacenter)
Retrieve the datacenter that the firewall resides in.

#### [getFirewallType](/reference/services/SoftLayer_Network_Vlan_Firewall/getFirewallType)
Retrieve the firewall device type.

#### [getFullyQualifiedDomainName](/reference/services/SoftLayer_Network_Vlan_Firewall/getFullyQualifiedDomainName)
Retrieve a name reflecting the hostname and domain of the firewall. This is created from the combined values of the firewall's logical name and vlan number automatically, and thus can not be edited directly.

#### [getManagementCredentials](/reference/services/SoftLayer_Network_Vlan_Firewall/getManagementCredentials)
Retrieve the credentials to log in to a firewall device. This is only present for dedicated appliances.

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Vlan_Firewall/getMetricTrackingObject)
Retrieve a firewall's metric tracking object.

#### [getMetricTrackingObjectId](/reference/services/SoftLayer_Network_Vlan_Firewall/getMetricTrackingObjectId)
Retrieve the metric tracking object ID for this firewall.

#### [getNetworkFirewallUpdateRequests](/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkFirewallUpdateRequests)
Retrieve the update requests made for this firewall.

#### [getNetworkGateway](/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkGateway)
Retrieve the gateway associated with this firewall, if any.

#### [getNetworkVlan](/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkVlan)
Retrieve the VLAN object that a firewall is associated with and protecting.

#### [getNetworkVlans](/reference/services/SoftLayer_Network_Vlan_Firewall/getNetworkVlans)
Retrieve the VLAN objects that a firewall is associated with and protecting.

#### [getObject](/reference/services/SoftLayer_Network_Vlan_Firewall/getObject)
Retrieve a SoftLayer_Network_Vlan_Firewall record.

#### [getRules](/reference/services/SoftLayer_Network_Vlan_Firewall/getRules)
Retrieve the currently running rule set of this network component firewall.

#### [getTagReferences](/reference/services/SoftLayer_Network_Vlan_Firewall/getTagReferences)


#### [getUpgradeRequest](/reference/services/SoftLayer_Network_Vlan_Firewall/getUpgradeRequest)
Retrieve a firewall's associated upgrade request object, if any.

#### [isHighAvailabilityUpgradeAvailable](/reference/services/SoftLayer_Network_Vlan_Firewall/isHighAvailabilityUpgradeAvailable)


#### [rejectBypassRequest](/reference/services/SoftLayer_Network_Vlan_Firewall/rejectBypassRequest)
Reject a request from technical support to bypass the firewall.

#### [restoreDefaults](/reference/services/SoftLayer_Network_Vlan_Firewall/restoreDefaults)


#### [setTags](/reference/services/SoftLayer_Network_Vlan_Firewall/setTags)


#### [updateRouteBypass](/reference/services/SoftLayer_Network_Vlan_Firewall/updateRouteBypass)


</div>

