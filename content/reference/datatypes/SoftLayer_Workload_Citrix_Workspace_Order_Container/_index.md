---
title: "SoftLayer_Workload_Citrix_Workspace_Order_Container"
description: "This is the datatype that needs to be populated and sent to SoftLayer_Workload_Citrix_Workspace_Order::placeWorkspaceOrd... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Workspace_Order_Container"
---

# SoftLayer_Workload_Citrix_Workspace_Order_Container
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Workspace_Order_Container' >Datatype</a></li>
    </ul>
</div>

## Description 
This is the datatype that needs to be populated and sent to SoftLayer_Workload_Citrix_Workspace_Order::placeWorkspaceOrder. 


### associatedMethods

*  [SoftLayer_Workload_Citrix_Workspace_Order::verifyWorkspaceOrder](/reference/services/SoftLayer_Workload_Citrix_Workspace_Order/verifyWorkspaceOrder )
*  [SoftLayer_Workload_Citrix_Workspace_Order::placeWorkspaceOrder](/reference/services/SoftLayer_Workload_Citrix_Workspace_Order/placeWorkspaceOrder )





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[activeDirectoryDomainName]: #activedirectorydomainname
#### [activeDirectoryDomainName]
The active directory domain name  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[activeDirectoryNetbiosName]: #activedirectorynetbiosname
#### [activeDirectoryNetbiosName]
The active directory netbios name (optional)  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[activeDirectorySafeModePassword]: #activedirectorysafemodepassword
#### [activeDirectorySafeModePassword]
The active directory safe mode password  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[citrixAPIClientId]: #citrixapiclientid
#### [citrixAPIClientId]
The Citrix API Client Id  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[citrixAPIClientSecret]: #citrixapiclientsecret
#### [citrixAPIClientSecret]
The Citrix API Client Secret  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[citrixCustomerId]: #citrixcustomerid
#### [citrixCustomerId]
The Citrix customer id  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[citrixResourceLocationName]: #citrixresourcelocationname
#### [citrixResourceLocationName]
The Citrix resource location name  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[domain]: #domain
#### [domain]
The default domain to be used for all server orders where the domain is not specified.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The specific [SoftLayer_Location_Datacenter]({{<ref "reference/datatypes/SoftLayer_Location_Datacenter">}}) id where the order should be provisioned.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[orderContainers]: #ordercontainers
#### [orderContainers]
There should be one child orderContainer for each component ordered.  The containerIdentifier should be set on each and have these exact values: proxy server bare metal server with hypervisor dhcp server citrix connector servers active directory server vlan subnet storage   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order[] </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


