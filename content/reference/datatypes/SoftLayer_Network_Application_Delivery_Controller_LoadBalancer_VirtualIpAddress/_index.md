---
title: "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
---

# SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[accountId]: #accountid
#### [accountId]
The unique identifier of the SoftLayer customer account that owns the virtual IP address   
<span class="type-label">Type: </span>**integer**

-----
[connectionLimit]: #connectionlimit
#### [connectionLimit]
The connection limit for this virtual IP address   
<span class="type-label">Type: </span>**integer**

-----
[connectionLimitUnits]: #connectionlimitunits
#### [connectionLimitUnits]
The units for the connection limit   
<span class="type-label">Type: </span>**string**

-----
[dedicatedFlag]: #dedicatedflag
#### [dedicatedFlag]
A flag that determines if a VIP is dedicated or not. This is used to override the connection limit and use an unlimited value.   
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
The unique identifier of the virtual IP address record   
<span class="type-label">Type: </span>**integer**

-----
[ipAddressId]: #ipaddressid
#### [ipAddressId]
ID of the IP address this virtual IP utilizes   
<span class="type-label">Type: </span>**integer**

-----
[notes]: #notes
#### [notes]
User-created notes for this load balancer virtual IP address   
<span class="type-label">Type: </span>**string**

-----
[securityCertificateId]: #securitycertificateid
#### [securityCertificateId]
The unique identifier of the Security Certificate to be utilized when SSL support is enabled.   
<span class="type-label">Type: </span>**integer**

-----
[sslActiveFlag]: #sslactiveflag
#### [sslActiveFlag]
Determines if the VIP currently has SSL acceleration enabled   
<span class="type-label">Type: </span>**boolean**

-----
[sslEnabledFlag]: #sslenabledflag
#### [sslEnabledFlag]
Determines if the VIP is _allowed_ to utilize SSL acceleration   
<span class="type-label">Type: </span>**boolean**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[applicationDeliveryController]: #applicationdeliverycontroller
#### [applicationDeliveryController]
A virtual IP address's associated application delivery controller.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller </a>**

-----
[applicationDeliveryControllers]: #applicationdeliverycontrollers
#### [applicationDeliveryControllers]
A virtual IP address's associated application delivery controllers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for the load balancer virtual IP. This is only valid when dedicatedFlag is false. This is an independent virtual IP, and if canceled, will only affect the associated virtual IP.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[dedicatedBillingItem]: #dedicatedbillingitem
#### [dedicatedBillingItem]
The current billing item for the load balancing device housing the virtual IP. This billing item represents a device which could contain other virtual IPs. Caution should be taken when canceling. This is only valid when dedicatedFlag is true.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Network_LoadBalancer'>SoftLayer_Billing_Item_Network_LoadBalancer </a>**

-----
[highAvailabilityFlag]: #highavailabilityflag
#### [highAvailabilityFlag]
Denotes whether the virtual IP is configured within a high availability cluster.  
<span class="type-label">Type: </span>**boolean**

-----
[ipAddress]: #ipaddress
#### [ipAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**

-----
[loadBalancerHardware]: #loadbalancerhardware
#### [loadBalancerHardware]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[managedResourceFlag]: #managedresourceflag
#### [managedResourceFlag]
A flag indicating that the load balancer is a managed resource.  
<span class="type-label">Type: </span>**boolean**

-----
[secureTransportCiphers]: #securetransportciphers
#### [secureTransportCiphers]
The list of security ciphers enabled for this virtual IP address  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportCipher'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportCipher[] </a>**

-----
[secureTransportProtocols]: #securetransportprotocols
#### [secureTransportProtocols]
The list of secure transport protocols enabled for this virtual IP address  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol[] </a>**

-----
[securityCertificate]: #securitycertificate
#### [securityCertificate]
The SSL certificate currently associated with the VIP.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate'>SoftLayer_Security_Certificate </a>**

-----
[securityCertificateEntry]: #securitycertificateentry
#### [securityCertificateEntry]
The SSL certificate currently associated with the VIP. Provides chosen certificate visibility to unprivileged users.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate_Entry'>SoftLayer_Security_Certificate_Entry </a>**

-----
[virtualServers]: #virtualservers
#### [virtualServers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer[] </a>**


## Count

-----
[applicationDeliveryControllerCount]: #applicationdeliverycontrollercount
#### [applicationDeliveryControllerCount]
A count of a virtual IP address's associated application delivery controllers.   
<span class="type-label">Type: </span>**unsigned long**


-----
[loadBalancerHardwareCount]: #loadbalancerhardwarecount
#### [loadBalancerHardwareCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[secureTransportCipherCount]: #securetransportciphercount
#### [secureTransportCipherCount]
A count of the list of security ciphers enabled for this virtual IP address   
<span class="type-label">Type: </span>**unsigned long**


-----
[secureTransportProtocolCount]: #securetransportprotocolcount
#### [secureTransportProtocolCount]
A count of the list of secure transport protocols enabled for this virtual IP address   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualServerCount]: #virtualservercount
#### [virtualServerCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


