---
title: "SoftLayer_Software_VirtualLicense"
description: "SoftLayer_Software_VirtualLicense is the application class that handles a special type of Software License.  Most softwa... "
layout: "datatype"
tags:
    - "datatype"
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


### associatedMethods

*  [SoftLayer_Software_VirtualLicense::getObject](/reference/services/SoftLayer_Software_VirtualLicense/getObject )
*  [SoftLayer_Account::getObject](/reference/services/SoftLayer_Account/getObject )



### seeAlso

* [SoftLayer_Software_Description](/reference/services/SoftLayer_Software_Description )


* [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet )


* [SoftLayer_Account](/reference/services/SoftLayer_Account )




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
The ID of the SoftLayer Account to which this Virtual License belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[hostHardwareId]: #hosthardwareid
#### [hostHardwareId]
The ID of the SoftLayer Hardware Server record to which this Virtual License belongs.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
An ID number for this Virtual License instance.  
<span class="type-label">Type: </span>**integer**

-----
[ipAddress]: #ipaddress
#### [ipAddress]
The specific IP address this Virtual License belongs to.  
<span class="type-label">Type: </span>**string**

-----
[key]: #key
#### [key]
The License Key for this specific Virtual License.  
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
A "notes" string attached to this specific Virtual License.  
<span class="type-label">Type: </span>**string**

-----
[softwareDescriptionId]: #softwaredescriptionid
#### [softwareDescriptionId]
The Software Description ID this Virtual License is for.  
<span class="type-label">Type: </span>**integer**

-----
[subnetId]: #subnetid
#### [subnetId]
The ID of the SoftLayer Network Subnet this Virtual License belongs to.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The customer account this Virtual License belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a software virtual license.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[hostHardware]: #hosthardware
#### [hostHardware]
The hardware record to which the software virtual license is assigned.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a>**

-----
[ipAddressRecord]: #ipaddressrecord
#### [ipAddressRecord]
The IP Address record associated with a virtual license.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The SoftLayer_Software_Description that this virtual license is for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**

-----
[subnet]: #subnet
#### [subnet]
The subnet this Virtual License's IP address belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**


## Count
</div>


