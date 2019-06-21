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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>The ID of the SoftLayer Account to which this Virtual License belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hostHardwareId" name=hostHardwareId>hostHardwareId</a>
            </span>
            <div class='views-field-body'>The ID of the SoftLayer Hardware Server record to which this Virtual License belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>An ID number for this Virtual License instance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ipAddress" name=ipAddress>ipAddress</a>
            </span>
            <div class='views-field-body'>The specific IP address this Virtual License belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#key" name=key>key</a>
            </span>
            <div class='views-field-body'>The License Key for this specific Virtual License. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notes" name=notes>notes</a>
            </span>
            <div class='views-field-body'>A "notes" string attached to this specific Virtual License. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#softwareDescriptionId" name=softwareDescriptionId>softwareDescriptionId</a>
            </span>
            <div class='views-field-body'>The Software Description ID this Virtual License is for. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnetId" name=subnetId>subnetId</a>
            </span>
            <div class='views-field-body'>The ID of the SoftLayer Network Subnet this Virtual License belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The customer account this Virtual License belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingItem" name=billingItem>billingItem</a>
            </span>
            <div class='views-field-body'>The billing item for a software virtual license. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hostHardware" name=hostHardware>hostHardware</a>
            </span>
            <div class='views-field-body'>The hardware record to which the software virtual license is assigned. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ipAddressRecord" name=ipAddressRecord>ipAddressRecord</a>
            </span>
            <div class='views-field-body'>The IP Address record associated with a virtual license. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#softwareDescription" name=softwareDescription>softwareDescription</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Software_Description that this virtual license is for. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnet" name=subnet>subnet</a>
            </span>
            <div class='views-field-body'>The subnet this Virtual License's IP address belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


