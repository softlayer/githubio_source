---
title: "SoftLayer_Product_Package"
description: "The SoftLayer_Product_Package data type contains information about packages from which orders can be generated. Packages... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
---

# SoftLayer_Product_Package
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Package data type contains information about packages from which orders can be generated. Packages contain general information regarding what is in them, where they are currently sold, availability, and pricing. 


### associatedMethods

*  [SoftLayer_Product_Package_Items::getObject](/reference/services/SoftLayer_Product_Package_Items/getObject )
*  [SoftLayer_Product_Package_Item_Prices::getObject](/reference/services/SoftLayer_Product_Package_Item_Prices/getObject )





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
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>A generic description of the processor type and count. This includes HTML, so you may want to strip these tags if you plan to use it. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firstOrderStepId" name=firstOrderStepId>firstOrderStepId</a></span>
            <div class='views-field-body'>This is only needed for step-based order verification. We use this for the order forms, but it is not required. This step is the first SoftLayer_Product_Package_Step for this package. Use this for for filtering which item categories are returned as a part of SoftLayer_Product_Package_Order_Configuration.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A package's internal identifier. Everything regarding a SoftLayer_Product_Package is tied back to this id.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isActive" name=isActive>isActive</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>A unique key name for the package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The description of the package. For server packages, this is usually a detailed description of processor type and count. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subDescription" name=subDescription>subDescription</a></span>
            <div class='views-field-body'>This currently contains no information but is here for future use. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#unitSize" name=unitSize>unitSize</a></span>
            <div class='views-field-body'>The server unit size this package will match to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountRestrictedActivePresets" name=accountRestrictedActivePresets>accountRestrictedActivePresets</a></span>
            <div class='views-field-body'>The preset configurations available only for the authenticated account and this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountRestrictedCategories" name=accountRestrictedCategories>accountRestrictedCategories</a></span>
            <div class='views-field-body'>The results from this call are similar to [[SoftLayer_Product_Package/getCategories|getCategories]], but these ONLY include account-restricted prices. Not all accounts have restricted pricing. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountRestrictedPricesFlag" name=accountRestrictedPricesFlag>accountRestrictedPricesFlag</a></span>
            <div class='views-field-body'>The flag to indicate if there are any restricted prices in a package for the currently-active account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activePresets" name=activePresets>activePresets</a></span>
            <div class='views-field-body'>The available preset configurations for this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeRamItems" name=activeRamItems>activeRamItems</a></span>
            <div class='views-field-body'>A collection of valid RAM items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeServerItems" name=activeServerItems>activeServerItems</a></span>
            <div class='views-field-body'>A collection of valid server items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeSoftwareItems" name=activeSoftwareItems>activeSoftwareItems</a></span>
            <div class='views-field-body'>A collection of valid software items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeUsagePrices" name=activeUsagePrices>activeUsagePrices</a></span>
            <div class='views-field-body'>A collection of [[SoftLayer_Product_Item_Price]] objects for pay-as-you-go usage. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#additionalServiceFlag" name=additionalServiceFlag>additionalServiceFlag</a></span>
            <div class='views-field-body'>This flag indicates that the package is an additional service. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attributes" name=attributes>attributes</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Attribute'>SoftLayer_Product_Package_Attribute[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#availableLocations" name=availableLocations>availableLocations</a></span>
            <div class='views-field-body'>A collection of valid locations for this package. (Deprecated - Use [[SoftLayer_Product_Package/getRegions|getRegions]]) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Locations'>SoftLayer_Product_Package_Locations[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#availableStorageUnits" name=availableStorageUnits>availableStorageUnits</a></span>
            <div class='views-field-body'>The maximum number of available disk storage units associated with the servers in a package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#categories" name=categories>categories</a></span>
            <div class='views-field-body'>This is a collection of categories ([[SoftLayer_Product_Item_Category]]) associated with a package which can be used for ordering. These categories have several objects prepopulated which are useful when determining the available products for purchase. The categories contain groups ([[SoftLayer_Product_Package_Item_Category_Group]]) that organize the products and prices by similar features. For example, operating systems will be grouped by their manufacturer and virtual server disks will be grouped by their disk type (SAN vs. local). Each group will contain prices ([[SoftLayer_Product_Item_Price]]) which you can use determine the cost of each product. Each price has a product ([[SoftLayer_Product_Item]]) which provides the name and other useful information about the server, service or software you may purchase. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#configuration" name=configuration>configuration</a></span>
            <div class='views-field-body'>The item categories associated with a package, including information detailing which item categories are required as part of a SoftLayer product order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration'>SoftLayer_Product_Package_Order_Configuration[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#defaultRamItems" name=defaultRamItems>defaultRamItems</a></span>
            <div class='views-field-body'>A collection of valid RAM items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deploymentNodeType" name=deploymentNodeType>deploymentNodeType</a></span>
            <div class='views-field-body'>The node type for a package in a solution deployment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deploymentPackages" name=deploymentPackages>deploymentPackages</a></span>
            <div class='views-field-body'>The packages that are allowed in a multi-server solution. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deploymentType" name=deploymentType>deploymentType</a></span>
            <div class='views-field-body'>The solution deployment type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deployments" name=deployments>deployments</a></span>
            <div class='views-field-body'>The package that represents a multi-server solution. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#disallowCustomDiskPartitions" name=disallowCustomDiskPartitions>disallowCustomDiskPartitions</a></span>
            <div class='views-field-body'>This flag indicates the package does not allow custom disk partitions. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firstOrderStep" name=firstOrderStep>firstOrderStep</a></span>
            <div class='views-field-body'>The Softlayer order step is optionally step-based. This returns the first SoftLayer_Product_Package_Order_Step in the step-based order process. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step'>SoftLayer_Product_Package_Order_Step </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#gatewayApplianceFlag" name=gatewayApplianceFlag>gatewayApplianceFlag</a></span>
            <div class='views-field-body'>Whether the package is a specialized network gateway appliance package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#gpuFlag" name=gpuFlag>gpuFlag</a></span>
            <div class='views-field-body'>This flag indicates that the package supports GPUs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hourlyBillingAvailableFlag" name=hourlyBillingAvailableFlag>hourlyBillingAvailableFlag</a></span>
            <div class='views-field-body'>Determines whether the package contains prices that can be ordered hourly. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemConflicts" name=itemConflicts>itemConflicts</a></span>
            <div class='views-field-body'>The item-item conflicts associated with a package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemLocationConflicts" name=itemLocationConflicts>itemLocationConflicts</a></span>
            <div class='views-field-body'>The item-location conflicts associated with a package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemPriceReferences" name=itemPriceReferences>itemPriceReferences</a></span>
            <div class='views-field-body'>cross reference for item prices </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Item_Prices'>SoftLayer_Product_Package_Item_Prices[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemPrices" name=itemPrices>itemPrices</a></span>
            <div class='views-field-body'>A collection of SoftLayer_Product_Item_Prices that are valid for this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#items" name=items>items</a></span>
            <div class='views-field-body'>A collection of valid items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locations" name=locations>locations</a></span>
            <div class='views-field-body'>A collection of valid locations for this package. (Deprecated - Use [[SoftLayer_Product_Package/getRegions|getRegions]]) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lowestServerPrice" name=lowestServerPrice>lowestServerPrice</a></span>
            <div class='views-field-body'>The lowest server [[SoftLayer_Product_Item_Price]] related to this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maximumPortSpeed" name=maximumPortSpeed>maximumPortSpeed</a></span>
            <div class='views-field-body'>The maximum available network speed associated with the package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#minimumPortSpeed" name=minimumPortSpeed>minimumPortSpeed</a></span>
            <div class='views-field-body'>The minimum available network speed associated with the package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#mongoDbEngineeredFlag" name=mongoDbEngineeredFlag>mongoDbEngineeredFlag</a></span>
            <div class='views-field-body'>This flag indicates that this is a MongoDB engineered package. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#nonEuCompliantFlag" name=nonEuCompliantFlag>nonEuCompliantFlag</a></span>
            <div class='views-field-body'>Whether the package is not in compliance with EU support. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderPremiums" name=orderPremiums>orderPremiums</a></span>
            <div class='views-field-body'>The premium price modifiers associated with the [[SoftLayer_Product_Item_Price]] and [[SoftLayer_Location]] objects in a package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price_Premium'>SoftLayer_Product_Item_Price_Premium[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#popLocationAvailabilityFlag" name=popLocationAvailabilityFlag>popLocationAvailabilityFlag</a></span>
            <div class='views-field-body'>This flag indicates if the package may be available in PoP locations in addition to Datacenters. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#preconfiguredFlag" name=preconfiguredFlag>preconfiguredFlag</a></span>
            <div class='views-field-body'>This flag indicates the package is pre-configured. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#presetConfigurationRequiredFlag" name=presetConfigurationRequiredFlag>presetConfigurationRequiredFlag</a></span>
            <div class='views-field-body'>Whether the package requires the user to define a preset configuration. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#preventVlanSelectionFlag" name=preventVlanSelectionFlag>preventVlanSelectionFlag</a></span>
            <div class='views-field-body'>Whether the package prevents the user from specifying a Vlan. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateHostedCloudPackageFlag" name=privateHostedCloudPackageFlag>privateHostedCloudPackageFlag</a></span>
            <div class='views-field-body'>This flag indicates the package is for a private hosted cloud deployment. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateHostedCloudPackageType" name=privateHostedCloudPackageType>privateHostedCloudPackageType</a></span>
            <div class='views-field-body'>The server role of the private hosted cloud deployment. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateNetworkOnlyFlag" name=privateNetworkOnlyFlag>privateNetworkOnlyFlag</a></span>
            <div class='views-field-body'>Whether the package only has access to the private network. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#quantaStorPackageFlag" name=quantaStorPackageFlag>quantaStorPackageFlag</a></span>
            <div class='views-field-body'>Whether the package is a specialized mass storage QuantaStor package. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#raidDiskRestrictionFlag" name=raidDiskRestrictionFlag>raidDiskRestrictionFlag</a></span>
            <div class='views-field-body'>This flag indicates the package does not allow different disks with RAID. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#redundantPowerFlag" name=redundantPowerFlag>redundantPowerFlag</a></span>
            <div class='views-field-body'>This flag determines if the package contains a redundant power supply product. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#regions" name=regions>regions</a></span>
            <div class='views-field-body'>The regional locations that a package is available in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceGroupTemplate" name=resourceGroupTemplate>resourceGroupTemplate</a></span>
            <div class='views-field-body'>The resource group template that describes a multi-server solution. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Template'>SoftLayer_Resource_Group_Template </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#topLevelItemCategoryCode" name=topLevelItemCategoryCode>topLevelItemCategoryCode</a></span>
            <div class='views-field-body'>The top level category code for this service offering. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>The type of service offering. This property can be used to help filter packages. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Type'>SoftLayer_Product_Package_Type </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountRestrictedActivePresetCount" name=accountRestrictedActivePresetCount>accountRestrictedActivePresetCount</a></span>
            <div class='views-field-body'>A count of the preset configurations available only for the authenticated account and this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#accountRestrictedCategoryCount" name=accountRestrictedCategoryCount>accountRestrictedCategoryCount</a></span>
            <div class='views-field-body'>A count of the results from this call are similar to [[SoftLayer_Product_Package/getCategories|getCategories]], but these ONLY include account-restricted prices. Not all accounts have restricted pricing. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activePresetCount" name=activePresetCount>activePresetCount</a></span>
            <div class='views-field-body'>A count of the available preset configurations for this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeRamItemCount" name=activeRamItemCount>activeRamItemCount</a></span>
            <div class='views-field-body'>A count of a collection of valid RAM items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeServerItemCount" name=activeServerItemCount>activeServerItemCount</a></span>
            <div class='views-field-body'>A count of a collection of valid server items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeSoftwareItemCount" name=activeSoftwareItemCount>activeSoftwareItemCount</a></span>
            <div class='views-field-body'>A count of a collection of valid software items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeUsagePriceCount" name=activeUsagePriceCount>activeUsagePriceCount</a></span>
            <div class='views-field-body'>A count of a collection of [[SoftLayer_Product_Item_Price]] objects for pay-as-you-go usage. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attributeCount" name=attributeCount>attributeCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#availableLocationCount" name=availableLocationCount>availableLocationCount</a></span>
            <div class='views-field-body'>A count of a collection of valid locations for this package. (Deprecated - Use [[SoftLayer_Product_Package/getRegions|getRegions]]) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#configurationCount" name=configurationCount>configurationCount</a></span>
            <div class='views-field-body'>A count of the item categories associated with a package, including information detailing which item categories are required as part of a SoftLayer product order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#defaultRamItemCount" name=defaultRamItemCount>defaultRamItemCount</a></span>
            <div class='views-field-body'>A count of a collection of valid RAM items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deploymentCount" name=deploymentCount>deploymentCount</a></span>
            <div class='views-field-body'>A count of the package that represents a multi-server solution. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deploymentPackageCount" name=deploymentPackageCount>deploymentPackageCount</a></span>
            <div class='views-field-body'>A count of the packages that are allowed in a multi-server solution. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemCount" name=itemCount>itemCount</a></span>
            <div class='views-field-body'>A count of a collection of valid items available for purchase in this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemPriceCount" name=itemPriceCount>itemPriceCount</a></span>
            <div class='views-field-body'>A count of a collection of SoftLayer_Product_Item_Prices that are valid for this package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemPriceReferenceCount" name=itemPriceReferenceCount>itemPriceReferenceCount</a></span>
            <div class='views-field-body'>A count of cross reference for item prices </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationCount" name=locationCount>locationCount</a></span>
            <div class='views-field-body'>A count of a collection of valid locations for this package. (Deprecated - Use [[SoftLayer_Product_Package/getRegions|getRegions]]) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderPremiumCount" name=orderPremiumCount>orderPremiumCount</a></span>
            <div class='views-field-body'>A count of the premium price modifiers associated with the [[SoftLayer_Product_Item_Price]] and [[SoftLayer_Location]] objects in a package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#regionCount" name=regionCount>regionCount</a></span>
            <div class='views-field-body'>A count of the regional locations that a package is available in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


