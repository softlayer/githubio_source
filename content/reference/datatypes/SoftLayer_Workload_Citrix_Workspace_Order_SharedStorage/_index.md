---
title: "SoftLayer_Workload_Citrix_Workspace_Order_SharedStorage"
description: "This is the datatype that can be populated by the customer to provide NFS shared storage information for VMware orders."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Workspace_Order_SharedStorage"
---

# SoftLayer_Workload_Citrix_Workspace_Order_SharedStorage
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Workspace_Order_SharedStorage' >Datatype</a></li>
    </ul>
</div>

## Description 


This is the datatype that can be populated by the customer to provide NFS shared storage information for VMware orders. 


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
[iops]: #iops
#### [iops]
Which storage tier: e.g. READHEAVY_TIER  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[quantity]: #quantity
#### [quantity]
The number of shared storages to order  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[size]: #size
#### [size]
The size of the storage (e.g. STORAGE_SPACE_FOR_2_IOPS_PER_GB)  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[volume]: #volume
#### [volume]
The volume  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


