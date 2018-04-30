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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#catalogId" name=catalogId>catalogId</a>
            </span>
            <div class='views-field-body'>The unique identifier of a [[SoftLayer_Product_Catalog]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#datacenters" name=datacenters>datacenters</a>
            </span>
            <div class='views-field-body'>Comma-separated list of datacenter names this server is available in </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#defaultRamCapacity" name=defaultRamCapacity>defaultRamCapacity</a>
            </span>
            <div class='views-field-body'>The minimum amount of RAM the server is configured with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#dualPathNetworkFlag" name=dualPathNetworkFlag>dualPathNetworkFlag</a>
            </span>
            <div class='views-field-body'>Flag to indicate if the server configuration supports dual path network routing. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#flexCoreServerFlag" name=flexCoreServerFlag>flexCoreServerFlag</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#gpuFlag" name=gpuFlag>gpuFlag</a>
            </span>
            <div class='views-field-body'>Indicates whether or not the server contains a GPU. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hourlyBillingFlag" name=hourlyBillingFlag>hourlyBillingFlag</a>
            </span>
            <div class='views-field-body'>Flag to determine if a server is available for hourly billing. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of a [[SoftLayer_Product_Package_Server]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemId" name=itemId>itemId</a>
            </span>
            <div class='views-field-body'>The unique identifier of a [[SoftLayer_Product_Item]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPriceId" name=itemPriceId>itemPriceId</a>
            </span>
            <div class='views-field-body'>The unique identifier of a [[SoftLayer_Product_Item_Price]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maximumDriveCount" name=maximumDriveCount>maximumDriveCount</a>
            </span>
            <div class='views-field-body'>The maximum number of hard drives the server can support. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maximumPortSpeed" name=maximumPortSpeed>maximumPortSpeed</a>
            </span>
            <div class='views-field-body'>The maximum available network speed for the server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maximumRamCapacity" name=maximumRamCapacity>maximumRamCapacity</a>
            </span>
            <div class='views-field-body'>The maximum amount of RAM the server can support. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#minimumPortSpeed" name=minimumPortSpeed>minimumPortSpeed</a>
            </span>
            <div class='views-field-body'>The minimum available network speed for the server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkGatewayApplianceRoleFlag" name=networkGatewayApplianceRoleFlag>networkGatewayApplianceRoleFlag</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#outletFlag" name=outletFlag>outletFlag</a>
            </span>
            <div class='views-field-body'>DEPRECATED. Indicates whether or not the server is being sold as part of an outlet package. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageId" name=packageId>packageId</a>
            </span>
            <div class='views-field-body'>The unique identifier of a [[SoftLayer_Product_Package]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageType" name=packageType>packageType</a>
            </span>
            <div class='views-field-body'>The type of service offering/package. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#powerServerFlag" name=powerServerFlag>powerServerFlag</a>
            </span>
            <div class='views-field-body'>Flag to indicate if the server is an IBM Power server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#presetId" name=presetId>presetId</a>
            </span>
            <div class='views-field-body'>The unique identifier of a [[SoftLayer_Product_Package_Preset]]. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#privateNetworkOnlyFlag" name=privateNetworkOnlyFlag>privateNetworkOnlyFlag</a>
            </span>
            <div class='views-field-body'>Indicates whether or not the server can only be configured with a private network. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorBusSpeed" name=processorBusSpeed>processorBusSpeed</a>
            </span>
            <div class='views-field-body'>The processor's bus speed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorCache" name=processorCache>processorCache</a>
            </span>
            <div class='views-field-body'>The amount of cache the processor has. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorCores" name=processorCores>processorCores</a>
            </span>
            <div class='views-field-body'>The number of cores in each processor. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorCount" name=processorCount>processorCount</a>
            </span>
            <div class='views-field-body'>The number of processors the server has. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorManufacturer" name=processorManufacturer>processorManufacturer</a>
            </span>
            <div class='views-field-body'>The manufacturer of the server's processor. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorModel" name=processorModel>processorModel</a>
            </span>
            <div class='views-field-body'>The model of the server's processor. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorName" name=processorName>processorName</a>
            </span>
            <div class='views-field-body'>The name of the server's processor. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processorSpeed" name=processorSpeed>processorSpeed</a>
            </span>
            <div class='views-field-body'>The processor speed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productName" name=productName>productName</a>
            </span>
            <div class='views-field-body'>The name of the server product. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#redundantPowerFlag" name=redundantPowerFlag>redundantPowerFlag</a>
            </span>
            <div class='views-field-body'>Indicates whether or not the server has the capability to support a redundant power supply. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sapCertifiedServerFlag" name=sapCertifiedServerFlag>sapCertifiedServerFlag</a>
            </span>
            <div class='views-field-body'>Flag to indicate if the server is SAP certified. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#startingHourlyPrice" name=startingHourlyPrice>startingHourlyPrice</a>
            </span>
            <div class='views-field-body'>The hourly starting price for the server. This includes a sum of all the minimum required items, including RAM and hard drives. Not all servers are available hourly.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#startingMonthlyPrice" name=startingMonthlyPrice>startingMonthlyPrice</a>
            </span>
            <div class='views-field-body'>The monthly starting price for the server. This includes a sum of all the minimum required items, including RAM and hard drives. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalCoreCount" name=totalCoreCount>totalCoreCount</a>
            </span>
            <div class='views-field-body'>The total number of processor cores available for the server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#txtTpmFlag" name=txtTpmFlag>txtTpmFlag</a>
            </span>
            <div class='views-field-body'>Flag to indicate if the server configuration supports TXT/TPM. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#unitSize" name=unitSize>unitSize</a>
            </span>
            <div class='views-field-body'>The size of the server. </div>
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
                <a href="#catalog" name=catalog>catalog</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Catalog'>SoftLayer_Product_Catalog </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#item" name=item>item</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPrice" name=itemPrice>itemPrice</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#package" name=package>package</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preset" name=preset>preset</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


