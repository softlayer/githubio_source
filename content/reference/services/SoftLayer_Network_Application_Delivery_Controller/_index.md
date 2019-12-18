---
title: "SoftLayer_Network_Application_Delivery_Controller"
description: "SoftLayer_Network_Application_Delivery_Controller controls a single instance of SoftLayer's application delivery control... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
---
# SoftLayer_Network_Application_Delivery_Controller
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer_Network_Application_Delivery_Controller controls a single instance of SoftLayer's application delivery controller offerings. Application delivery controllers are capable of application filtering, layer 4 and layer 7 load balancing, and many other functions. Currently SoftLayer employs them as high power load balancers. Load balancing is accomplished similarly to SoftLayer's other load balancer options, through a collection of virtual IP address interfaces. 

Application delivery controllers support an "advanced" configuration scheme, enabling access directly to the controller's backend management interface. Enable access to this interface via the [SoftLayer_Network_Application_Delivery_Controller::enableAdvancedView]({{<ref "reference/services/SoftLayer_Network_Application_Delivery_Controller/enableAdvancedView">}}) method in this service. Use the username "root" and password retrieved from this service along with the management IP address retrieved from this service. Be warned that direct access to the application delivery controller exposes a high degree of functionality. Be careful when directly editing your service to avoid interruption via misconfiguration. 



        
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

#### [createLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/createLiveLoadBalancer)
Add to or create load balancer service from a virtual IP address

#### [deleteLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancer)
Remove a virtual IP address from a load balancer

#### [deleteLiveLoadBalancerService](/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancerService)
Remove load balancer service

#### [editObject](/reference/services/SoftLayer_Network_Application_Delivery_Controller/editObject)
Edit an application delivery controller record

#### [getAccount](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getAccount)
Retrieve the SoftLayer customer account that owns an application delivery controller record.

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.

#### [getBandwidthDataByDate](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getBandwidthDataByDate)


#### [getBandwidthImageByDate](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getBandwidthImageByDate)
Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for an application delivery controller. 

#### [getBillingItem](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getBillingItem)
Retrieve the billing item for a Application Delivery Controller.

#### [getConfigurationHistory](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getConfigurationHistory)
Retrieve previous configurations for an Application Delivery Controller.

#### [getCustomBandwidthDataByDate](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getCustomBandwidthDataByDate)
Retrieve bandwidth graph by date.

#### [getDatacenter](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getDatacenter)
Retrieve the datacenter that the application delivery controller resides in.

#### [getDescription](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getDescription)
Retrieve a brief description of an application delivery controller record.

#### [getLicenseExpirationDate](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getLicenseExpirationDate)
Retrieve the date in which the license for this application delivery controller will expire.

#### [getLiveLoadBalancerServiceGraphImage](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getLiveLoadBalancerServiceGraphImage)
Get the connection or status graph image for an application delivery controller service.

#### [getLoadBalancers](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getLoadBalancers)
Retrieve the virtual IP address records that belong to an application delivery controller based load balancer.

#### [getManagedResourceFlag](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getManagedResourceFlag)
Retrieve a flag indicating that this Application Delivery Controller is a managed resource.

#### [getManagementIpAddress](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getManagementIpAddress)
Retrieve an application delivery controller's management ip address.

#### [getNetworkVlan](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getNetworkVlan)
Retrieve the network VLAN that an application delivery controller resides on.

#### [getNetworkVlans](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getNetworkVlans)
Retrieve the network VLANs that an application delivery controller resides on.

#### [getObject](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getObject)
Retrieve a SoftLayer_Network_Application_Delivery_Controller record.

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth for the current billing cycle.

#### [getPassword](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getPassword)
Retrieve the password used to connect to an application delivery controller's management interface when it is operating in advanced view mode.

#### [getPrimaryIpAddress](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getPrimaryIpAddress)
Retrieve an application delivery controller's primary public IP address.

#### [getProjectedPublicBandwidthUsage](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getProjectedPublicBandwidthUsage)
Retrieve the projected public outbound bandwidth for the current billing cycle.

#### [getSubnets](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getSubnets)
Retrieve a network application controller's subnets. A subnet is a group of IP addresses

#### [getTagReferences](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getTagReferences)


#### [getType](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getType)


#### [getVirtualIpAddresses](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getVirtualIpAddresses)


#### [restoreBaseConfiguration](/reference/services/SoftLayer_Network_Application_Delivery_Controller/restoreBaseConfiguration)
Restore an application delivery controller's base configuration state.

#### [restoreConfiguration](/reference/services/SoftLayer_Network_Application_Delivery_Controller/restoreConfiguration)
Restore an application delivery controller's configuration state.

#### [saveCurrentConfiguration](/reference/services/SoftLayer_Network_Application_Delivery_Controller/saveCurrentConfiguration)
Save an application delivery controller's configuration state.

#### [updateLiveLoadBalancer](/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateLiveLoadBalancer)
Edit a virtual IP address within a load balancer

#### [updateNetScalerLicense](/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateNetScalerLicense)
Update the NetScaler VPX License.

</div>

