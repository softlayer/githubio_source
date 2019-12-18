---
title: "SoftLayer_Network_Vlan_Firewall"
description: "The SoftLayer_Network_Vlan_Firewall data type contains general information relating to a single SoftLayer VLAN firewall.... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_Network_Vlan_Firewall data type contains general information relating to a single SoftLayer VLAN firewall. This is the object which ties the running rules to a specific downstream server. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))




### seeAlso

* [SoftLayer_Network_Firewall_Template](/reference/services/SoftLayer_Network_Firewall_Template )


* [SoftLayer_Network_Firewall_Update_Request](/reference/services/SoftLayer_Network_Firewall_Update_Request )




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
[administrativeBypassFlag]: #administrativebypassflag
#### [administrativeBypassFlag]
A flag to indicate if the firewall is in administrative bypass mode. In other words, no rules are being applied to the traffic coming through.  
<span class="type-label">Type: </span>**string**

-----
[customerManagedFlag]: #customermanagedflag
#### [customerManagedFlag]
Whether or not this firewall can be directly logged in to.  
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
A firewall's unique identifier.  
<span class="type-label">Type: </span>**integer**

-----
[primaryIpAddress]: #primaryipaddress
#### [primaryIpAddress]
A firewall's primary IP address. This field will be the IP shown when doing network traces and reverse DNS and is a read-only property.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[accountId]: #accountid
#### [accountId]
  
<span class="type-label">Type: </span>**integer**

-----
[bandwidthAllocation]: #bandwidthallocation
#### [bandwidthAllocation]
A firewall's allotted bandwidth (measured in GB).  
<span class="type-label">Type: </span>**decimal**

-----
[billingCycleBandwidthUsage]: #billingcyclebandwidthusage
#### [billingCycleBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object will be returned for each network this firewall is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**

-----
[billingCyclePrivateBandwidthUsage]: #billingcycleprivatebandwidthusage
#### [billingCyclePrivateBandwidthUsage]
The raw private bandwidth usage data for the current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**

-----
[billingCyclePublicBandwidthUsage]: #billingcyclepublicbandwidthusage
#### [billingCyclePublicBandwidthUsage]
The raw public bandwidth usage data for the current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a Hardware Firewall (Dedicated).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[bypassRequestStatus]: #bypassrequeststatus
#### [bypassRequestStatus]
Administrative bypass request status.  
<span class="type-label">Type: </span>**string**

-----
[datacenter]: #datacenter
#### [datacenter]
The datacenter that the firewall resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[firewallType]: #firewalltype
#### [firewallType]
The firewall device type.  
<span class="type-label">Type: </span>**string**

-----
[fullyQualifiedDomainName]: #fullyqualifieddomainname
#### [fullyQualifiedDomainName]
A name reflecting the hostname and domain of the firewall. This is created from the combined values of the firewall's logical name and vlan number automatically, and thus can not be edited directly.  
<span class="type-label">Type: </span>**string**

-----
[managementCredentials]: #managementcredentials
#### [managementCredentials]
The credentials to log in to a firewall device. This is only present for dedicated appliances.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password </a>**

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A firewall's metric tracking object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**

-----
[metricTrackingObjectId]: #metrictrackingobjectid
#### [metricTrackingObjectId]
The metric tracking object ID for this firewall.  
<span class="type-label">Type: </span>**integer**

-----
[networkFirewallUpdateRequests]: #networkfirewallupdaterequests
#### [networkFirewallUpdateRequests]
The update requests made for this firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request[] </a>**

-----
[networkGateway]: #networkgateway
#### [networkGateway]
The gateway associated with this firewall, if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The VLAN object that a firewall is associated with and protecting.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**

-----
[networkVlans]: #networkvlans
#### [networkVlans]
The VLAN objects that a firewall is associated with and protecting.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**

-----
[rules]: #rules
#### [rules]
The currently running rule set of this network component firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule'>SoftLayer_Network_Vlan_Firewall_Rule[] </a>**

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**

-----
[upgradeRequest]: #upgraderequest
#### [upgradeRequest]
A firewall's associated upgrade request object, if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request'>SoftLayer_Product_Upgrade_Request </a>**


## Count

-----
[billingCycleBandwidthUsageCount]: #billingcyclebandwidthusagecount
#### [billingCycleBandwidthUsageCount]
A count of the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this firewall is attached to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkFirewallUpdateRequestCount]: #networkfirewallupdaterequestcount
#### [networkFirewallUpdateRequestCount]
A count of the update requests made for this firewall.   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of the VLAN objects that a firewall is associated with and protecting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of the currently running rule set of this network component firewall.   
<span class="type-label">Type: </span>**unsigned long**


-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


