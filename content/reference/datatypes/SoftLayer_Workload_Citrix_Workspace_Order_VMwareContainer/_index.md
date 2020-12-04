---
title: "SoftLayer_Workload_Citrix_Workspace_Order_VMwareContainer"
description: "This is the datatype that needs to be populated and sent to SoftLayer_Workload_Citrix_Workspace_Order::placeWorkspaceOrd... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Workspace_Order_VMwareContainer"
---

# SoftLayer_Workload_Citrix_Workspace_Order_VMwareContainer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Workspace_Order_VMwareContainer' >Datatype</a></li>
    </ul>
</div>

## Description 
This is the datatype that needs to be populated and sent to SoftLayer_Workload_Citrix_Workspace_Order::placeWorkspaceOrder to order and provision one or more VMware server instances to be used with Citrix Virtual Apps and Desktops. 


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
[disks]: #disks
#### [disks]
The bare metal disks  
<span class="type-label">Type: </span>**array of strings**


</div>
<div class="prop-row">

-----
[domain]: #domain
#### [domain]
The domain for the ordered hosts (e.g. example.org)  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[licenseKeys]: #licensekeys
#### [licenseKeys]
Customer provided license keys (optional)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Workspace_Order_LicenseKey'>SoftLayer_Workload_Citrix_Workspace_Order_LicenseKey[] </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The datacenter location  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name associated with the order  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[nickname]: #nickname
#### [nickname]
The nickname for the vSRX service  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[quantity]: #quantity
#### [quantity]
The number of instances to order  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ram]: #ram
#### [ram]
The bare metal ram type  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[server]: #server
#### [server]
The bare metal server type  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sharedStorage]: #sharedstorage
#### [sharedStorage]
The bare metal shared nfs storage (optional)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Workspace_Order_SharedStorage'>SoftLayer_Workload_Citrix_Workspace_Order_SharedStorage[] </a>**


</div>
<div class="prop-row">

-----
[subdomain]: #subdomain
#### [subdomain]
The subdomain for the ordered hosts (e.g. corp)  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[vsanCacheDisks]: #vsancachedisks
#### [vsanCacheDisks]
The bare metal vsan cache disks (optional)  
<span class="type-label">Type: </span>**array of strings**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


