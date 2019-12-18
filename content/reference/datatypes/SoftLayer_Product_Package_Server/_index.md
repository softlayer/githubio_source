---
title: "SoftLayer_Product_Package_Server"
description: "The SoftLayer_Product_Package_Server data type contains summarized information for bare metal servers regarding pricing,... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Server"
---

# SoftLayer_Product_Package_Server
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Package_Server' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Server' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Package_Server data type contains summarized information for bare metal servers regarding pricing, processor stats, and feature sets. 





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
[bareMetalReservedFlag]: #baremetalreservedflag
#### [bareMetalReservedFlag]
Flag to indicate if the server a Bare Metal Reserved offering.  
<span class="type-label">Type: </span>**boolean**

-----
[catalogId]: #catalogid
#### [catalogId]
The unique identifier of a [SoftLayer_Product_Catalog]({{<ref "reference/datatypes/SoftLayer_Product_Catalog">}}).  
<span class="type-label">Type: </span>**integer**

-----
[datacenters]: #datacenters
#### [datacenters]
Comma-separated list of datacenter names this server is available in  
<span class="type-label">Type: </span>**string**

-----
[defaultRamCapacity]: #defaultramcapacity
#### [defaultRamCapacity]
The minimum amount of RAM the server is configured with.  
<span class="type-label">Type: </span>**decimal**

-----
[dualPathNetworkFlag]: #dualpathnetworkflag
#### [dualPathNetworkFlag]
Flag to indicate if the server configuration supports dual path network routing.  
<span class="type-label">Type: </span>**boolean**

-----
[flexCoreServerFlag]: #flexcoreserverflag
#### [flexCoreServerFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[gpuFlag]: #gpuflag
#### [gpuFlag]
Indicates whether or not the server contains a GPU.  
<span class="type-label">Type: </span>**boolean**

-----
[hourlyBillingFlag]: #hourlybillingflag
#### [hourlyBillingFlag]
Flag to determine if a server is available for hourly billing.  
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
The unique identifier of a [SoftLayer_Product_Package_Server]({{<ref "reference/datatypes/SoftLayer_Product_Package_Server">}}).  
<span class="type-label">Type: </span>**integer**

-----
[itemId]: #itemid
#### [itemId]
The unique identifier of a [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}).  
<span class="type-label">Type: </span>**integer**

-----
[itemPriceId]: #itempriceid
#### [itemPriceId]
The unique identifier of a [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}).  
<span class="type-label">Type: </span>**integer**

-----
[maximumDriveCount]: #maximumdrivecount
#### [maximumDriveCount]
The maximum number of hard drives the server can support.  
<span class="type-label">Type: </span>**integer**

-----
[maximumPortSpeed]: #maximumportspeed
#### [maximumPortSpeed]
The maximum available network speed for the server.  
<span class="type-label">Type: </span>**decimal**

-----
[maximumRamCapacity]: #maximumramcapacity
#### [maximumRamCapacity]
The maximum amount of RAM the server can support.  
<span class="type-label">Type: </span>**decimal**

-----
[minimumPortSpeed]: #minimumportspeed
#### [minimumPortSpeed]
The minimum available network speed for the server.  
<span class="type-label">Type: </span>**decimal**

-----
[networkGatewayApplianceRoleFlag]: #networkgatewayapplianceroleflag
#### [networkGatewayApplianceRoleFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[outletFlag]: #outletflag
#### [outletFlag]
DEPRECATED. Indicates whether or not the server is being sold as part of an outlet package.  
<span class="type-label">Type: </span>**boolean**

-----
[packageId]: #packageid
#### [packageId]
The unique identifier of a [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}).  
<span class="type-label">Type: </span>**integer**

-----
[packageType]: #packagetype
#### [packageType]
The type of service offering/package.  
<span class="type-label">Type: </span>**string**

-----
[powerServerFlag]: #powerserverflag
#### [powerServerFlag]
Flag to indicate if the server is an IBM Power server.  
<span class="type-label">Type: </span>**boolean**

-----
[presetId]: #presetid
#### [presetId]
The unique identifier of a [SoftLayer_Product_Package_Preset]({{<ref "reference/datatypes/SoftLayer_Product_Package_Preset">}}).  
<span class="type-label">Type: </span>**integer**

-----
[privateNetworkOnlyFlag]: #privatenetworkonlyflag
#### [privateNetworkOnlyFlag]
Indicates whether or not the server can only be configured with a private network.  
<span class="type-label">Type: </span>**boolean**

-----
[processorBusSpeed]: #processorbusspeed
#### [processorBusSpeed]
The processor's bus speed.  
<span class="type-label">Type: </span>**string**

-----
[processorCache]: #processorcache
#### [processorCache]
The amount of cache the processor has.  
<span class="type-label">Type: </span>**string**

-----
[processorCores]: #processorcores
#### [processorCores]
The number of cores in each processor.  
<span class="type-label">Type: </span>**integer**

-----
[processorCount]: #processorcount
#### [processorCount]
The number of processors the server has.  
<span class="type-label">Type: </span>**integer**

-----
[processorManufacturer]: #processormanufacturer
#### [processorManufacturer]
The manufacturer of the server's processor.  
<span class="type-label">Type: </span>**string**

-----
[processorModel]: #processormodel
#### [processorModel]
The model of the server's processor.  
<span class="type-label">Type: </span>**string**

-----
[processorName]: #processorname
#### [processorName]
The name of the server's processor.  
<span class="type-label">Type: </span>**string**

-----
[processorSpeed]: #processorspeed
#### [processorSpeed]
The processor speed.  
<span class="type-label">Type: </span>**string**

-----
[productName]: #productname
#### [productName]
The name of the server product.  
<span class="type-label">Type: </span>**string**

-----
[redundantPowerFlag]: #redundantpowerflag
#### [redundantPowerFlag]
Indicates whether or not the server has the capability to support a redundant power supply.  
<span class="type-label">Type: </span>**boolean**

-----
[sapCertifiedServerFlag]: #sapcertifiedserverflag
#### [sapCertifiedServerFlag]
Flag to indicate if the server is SAP certified.  
<span class="type-label">Type: </span>**boolean**

-----
[startingHourlyPrice]: #startinghourlyprice
#### [startingHourlyPrice]
The hourly starting price for the server. This includes a sum of all the minimum required items, including RAM and hard drives. Not all servers are available hourly.   
<span class="type-label">Type: </span>**decimal**

-----
[startingMonthlyPrice]: #startingmonthlyprice
#### [startingMonthlyPrice]
The monthly starting price for the server. This includes a sum of all the minimum required items, including RAM and hard drives.  
<span class="type-label">Type: </span>**decimal**

-----
[totalCoreCount]: #totalcorecount
#### [totalCoreCount]
The total number of processor cores available for the server.  
<span class="type-label">Type: </span>**integer**

-----
[txtTpmFlag]: #txttpmflag
#### [txtTpmFlag]
Flag to indicate if the server configuration supports TXT/TPM.  
<span class="type-label">Type: </span>**boolean**

-----
[unitSize]: #unitsize
#### [unitSize]
The size of the server.  
<span class="type-label">Type: </span>**integer**

-----
[vmwareVsanNodeFlag]: #vmwarevsannodeflag
#### [vmwareVsanNodeFlag]
Flag to indicate if the server is a VMware vSAN Node configuration.  
<span class="type-label">Type: </span>**boolean**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[catalog]: #catalog
#### [catalog]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Catalog'>SoftLayer_Product_Catalog </a>**

-----
[item]: #item
#### [item]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[itemPrice]: #itemprice
#### [itemPrice]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**

-----
[package]: #package
#### [package]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**

-----
[preset]: #preset
#### [preset]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a>**


## Count
</div>


