---
title: "SoftLayer_Software_VirtualLicense"
description: "SoftLayer_Software_VirtualLicense is the application class that handles a special type of Software License.  Most softwa... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_VirtualLicense"
---
# SoftLayer_Software_VirtualLicense
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Software_VirtualLicense' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_VirtualLicense' >Datatype</a></li>
    </ul>
</div>

## Description


SoftLayer_Software_VirtualLicense is the application class that handles a special type of Software License.  Most software licenses are licensed to a specific hardware ID;  virtual licenses are designed for virtual machines and therefore are assigned to an IP Address.  Not all software packages can be "virtual licensed". 

SoftLayer_Software_VirtualLicense's service allows you to retrieve the hard-copy license file for a virtual license, if one exists for your license instance. 

You can also retrieve the subnet that the IP to which a software virtual license is licensed upon exists in, as well as the software description that this virtual license is for. 



### seeAlso

* [SoftLayer_Software_Description](/reference/services/SoftLayer_Software_Description )


* [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Software_VirtualLicense/getAccount)
Retrieve the customer account this Virtual License belongs to.

</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Software_VirtualLicense/getBillingItem)
Retrieve the billing item for a software virtual license.

</div>

<div class="method-row">

#### [getHostHardware](/reference/services/SoftLayer_Software_VirtualLicense/getHostHardware)
Retrieve the hardware record to which the software virtual license is assigned.

</div>

<div class="method-row">

#### [getIpAddressRecord](/reference/services/SoftLayer_Software_VirtualLicense/getIpAddressRecord)
Retrieve the IP Address record associated with a virtual license.

</div>

<div class="method-row">

#### [getLicenseFile](/reference/services/SoftLayer_Software_VirtualLicense/getLicenseFile)
Get the file for a virtual license, if it exists

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Software_VirtualLicense/getObject)
Retrieve a SoftLayer_Software_VirtualLicense record.

</div>

<div class="method-row">

#### [getSoftwareDescription](/reference/services/SoftLayer_Software_VirtualLicense/getSoftwareDescription)
Retrieve the SoftLayer_Software_Description that this virtual license is for.

</div>

<div class="method-row">

#### [getSubnet](/reference/services/SoftLayer_Software_VirtualLicense/getSubnet)
Retrieve the subnet this Virtual License's IP address belongs to.

</div>
</div>

</div>

