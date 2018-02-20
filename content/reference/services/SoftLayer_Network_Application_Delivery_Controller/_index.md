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

Application delivery controllers support an "advanced" configuration scheme, enabling access directly to the controller's backend management interface. Enable access to this interface via the [[SoftLayer_Network_Application_Delivery_Controller::enableAdvancedView|enableAdvancedView]] method in this service. Use the username "root" and password retrieved from this service along with the management IP address retrieved from this service. Be warned that direct access to the application delivery controller exposes a high degree of functionality. Be careful when directly editing your service to avoid interruption via misconfiguration. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/createLiveLoadBalancer'> createLiveLoadBalancer</a> </span>
            <div class='views-field-body'>Add to or create load balancer service from a virtual IP address</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancer'> deleteLiveLoadBalancer</a> </span>
            <div class='views-field-body'>Remove a virtual IP address from a load balancer</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/deleteLiveLoadBalancerService'> deleteLiveLoadBalancerService</a> </span>
            <div class='views-field-body'>Remove load balancer service</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit an application delivery controller record</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer customer account that owns an application delivery controller record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getAverageDailyPublicBandwidthUsage'> getAverageDailyPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the average daily public bandwidth usage for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getBandwidthDataByDate'> getBandwidthDataByDate</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getBandwidthImageByDate'> getBandwidthImageByDate</a> </span>
            <div class='views-field-body'>Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for an application delivery controller. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the billing item for a Application Delivery Controller.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getConfigurationHistory'> getConfigurationHistory</a> </span>
            <div class='views-field-body'>Retrieve previous configurations for an Application Delivery Controller.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getCustomBandwidthDataByDate'> getCustomBandwidthDataByDate</a> </span>
            <div class='views-field-body'>Retrieve bandwidth graph by date.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>Retrieve the datacenter that the application delivery controller resides in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getDescription'> getDescription</a> </span>
            <div class='views-field-body'>Retrieve a brief description of an application delivery controller record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getLicenseExpirationDate'> getLicenseExpirationDate</a> </span>
            <div class='views-field-body'>Retrieve the date in which the license for this application delivery controller will expire.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getLiveLoadBalancerServiceGraphImage'> getLiveLoadBalancerServiceGraphImage</a> </span>
            <div class='views-field-body'>Get the connection or status graph image for an application delivery controller service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getLoadBalancers'> getLoadBalancers</a> </span>
            <div class='views-field-body'>Retrieve the virtual IP address records that belong to an application delivery controller based load balancer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getManagedResourceFlag'> getManagedResourceFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that this Application Delivery Controller is a managed resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getManagementIpAddress'> getManagementIpAddress</a> </span>
            <div class='views-field-body'>Retrieve an application delivery controller's management ip address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getNetworkVlan'> getNetworkVlan</a> </span>
            <div class='views-field-body'>Retrieve the network VLAN that an application delivery controller resides on.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getNetworkVlans'> getNetworkVlans</a> </span>
            <div class='views-field-body'>Retrieve the network VLANs that an application delivery controller resides on.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Application_Delivery_Controller record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getOutboundPublicBandwidthUsage'> getOutboundPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total public outbound bandwidth for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getPassword'> getPassword</a> </span>
            <div class='views-field-body'>Retrieve the password used to connect to an application delivery controller's management interface when it is operating in advanced view mode.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getPrimaryIpAddress'> getPrimaryIpAddress</a> </span>
            <div class='views-field-body'>Retrieve an application delivery controller's primary public IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getProjectedPublicBandwidthUsage'> getProjectedPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the projected public outbound bandwidth for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getSubnets'> getSubnets</a> </span>
            <div class='views-field-body'>Retrieve a network application controller's subnets. A subnet is a group of IP addresses</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getTagReferences'> getTagReferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getType'> getType</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/getVirtualIpAddresses'> getVirtualIpAddresses</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/restoreBaseConfiguration'> restoreBaseConfiguration</a> </span>
            <div class='views-field-body'>Restore an application delivery controller's base configuration state.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/restoreConfiguration'> restoreConfiguration</a> </span>
            <div class='views-field-body'>Restore an application delivery controller's configuration state.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/saveCurrentConfiguration'> saveCurrentConfiguration</a> </span>
            <div class='views-field-body'>Save an application delivery controller's configuration state.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateLiveLoadBalancer'> updateLiveLoadBalancer</a> </span>
            <div class='views-field-body'>Edit a virtual IP address within a load balancer</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller/updateNetScalerLicense'> updateNetScalerLicense</a> </span>
            <div class='views-field-body'>Update the NetScaler VPX License.</div>
        </div>
        </div>
</div>

