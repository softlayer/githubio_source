---
title: "SoftLayer_Container_Product_Order_Network"
description: "This type contains the structure of network-related objects that may be specified when ordering services."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Network"
---

# SoftLayer_Container_Product_Order_Network
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network' >Datatype</a></li>
    </ul>
</div>

## Description 
This type contains the structure of network-related objects that may be specified when ordering services. 





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
[network]: #network
#### [network]
The [SoftLayer_Network]({{<ref "reference/datatypes/SoftLayer_Network">}}) object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network'>SoftLayer_Network </a>**

-----
[publicVlans]: #publicvlans
#### [publicVlans]
The list of public [SoftLayer_Container_Product_Order_Network_Vlan]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan">}}) available for ordering. Each VLAN will have list of public subnets that are accessible to the VLAN.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order[] </a>**

-----
[subnets]: #subnets
#### [subnets]
The list of private [SoftLayer_Container_Product_Order_Network_Subnet]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet">}}) available for ordering with a description of their available IP space.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order[] </a>**

</div>
<!-- LOCAL PROPERTY END -->

</div>


