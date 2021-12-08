---
title: "SoftLayer_Workload_Citrix_Deployment_Resource_Response"
description: "The SoftLayer_Workload_Citrix_Deployment_Resource_Response constructs a response object for [SoftLayer_Workload_Citrix_D... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Deployment_Resource_Response"
---

# SoftLayer_Workload_Citrix_Deployment_Resource_Response
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource_Response' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Workload_Citrix_Deployment_Resource_Response constructs a response object for [SoftLayer_Workload_Citrix_Deployment_Resource_Response]({{<ref "reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource_Response">}}) for the CVAD resource. 





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
[hardware]: #hardware
#### [hardware]
Represents the hardware resource of the CVAD deployment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[isDeploymentOwned]: #isdeploymentowned
#### [isDeploymentOwned]
It is a flag for internal usage that represents if the underlying resource is ordered by another system of the same infrastructure provider.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[role]: #role
#### [role]
It represents the role of a VSI resource in the CVAD deployment, e.g., a proxy server, DHCP server, cloud connector.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource_Role'>SoftLayer_Workload_Citrix_Deployment_Resource_Role </a>**  



</div>
<div class="prop-row">

-----
[storage]: #storage
#### [storage]
Storage resource for the CVAD deployment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**  



</div>
<div class="prop-row">

-----
[subnet]: #subnet
#### [subnet]
Represents the subnet resource of the CVAD deployment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
It contains the category of the item which is set for the current response.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
VSI resource for the CVAD deployment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>
<div class="prop-row">

-----
[vlan]: #vlan
#### [vlan]
Represents the VLAN resource of the CVAD deployment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


