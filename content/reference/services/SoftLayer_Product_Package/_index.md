---
title: "SoftLayer_Product_Package"
description: "Every SoftLayer_Product_Package contains information related products and services that SoftLayer sells. The configurati... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
---
# SoftLayer_Product_Package
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Package' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer_Product_Package contains information related products and services that SoftLayer sells. The configuration of this package reveals which categories are required to place an order for this package. Every package has items, item prices, locations, regions, and a configuration. This service is the starting point for ordering servers, and other services we provide. 



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAccountRestrictedActivePresets'> getAccountRestrictedActivePresets</a> </span>
            <div class='views-field-body'>Retrieve the preset configurations available only for the authenticated account and this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAccountRestrictedCategories'> getAccountRestrictedCategories</a> </span>
            <div class='views-field-body'>Retrieve the results from this call are similar to [[SoftLayer_Product_Package/getCategories|getCategories]], but these ONLY include account-restricted prices. Not all accounts have restricted pricing.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAccountRestrictedPricesFlag'> getAccountRestrictedPricesFlag</a> </span>
            <div class='views-field-body'>Retrieve the flag to indicate if there are any restricted prices in a package for the currently-active account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActiveItems'> getActiveItems</a> </span>
            <div class='views-field-body'>Retrieve the active items, as well as their prices and categories for this package</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActivePackagesByAttribute'> getActivePackagesByAttribute</a> </span>
            <div class='views-field-body'>[<strong>DEPRECATED</strong>] Retrieve the active [[SoftLayer_Product_Package]] objects from which you can order a server, service or software filtered by an attribute type ([[SoftLayer_Product_Package_Attribute_Type]]) on the package. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActivePresets'> getActivePresets</a> </span>
            <div class='views-field-body'>Retrieve the available preset configurations for this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActivePrivateHostedCloudPackages'> getActivePrivateHostedCloudPackages</a> </span>
            <div class='views-field-body'>Get the Active SoftLayer_Product_Packages from which one can order private hosted cloud configurations.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActiveRamItems'> getActiveRamItems</a> </span>
            <div class='views-field-body'>Retrieve a collection of valid RAM items available for purchase in this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActiveServerItems'> getActiveServerItems</a> </span>
            <div class='views-field-body'>Retrieve a collection of valid server items available for purchase in this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActiveSoftwareItems'> getActiveSoftwareItems</a> </span>
            <div class='views-field-body'>Retrieve a collection of valid software items available for purchase in this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActiveUsagePrices'> getActiveUsagePrices</a> </span>
            <div class='views-field-body'>Retrieve a collection of [[SoftLayer_Product_Item_Price]] objects for pay-as-you-go usage.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getActiveUsageRatePrices'> getActiveUsageRatePrices</a> </span>
            <div class='views-field-body'>Return the active usage rate prices for the current package. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAdditionalServiceFlag'> getAdditionalServiceFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates that the package is an additional service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'>Get the Active SoftLayer_Product_Packages</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAttributes'> getAttributes</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAvailableLocations'> getAvailableLocations</a> </span>
            <div class='views-field-body'>Retrieve a collection of valid locations for this package. (Deprecated - Use [[SoftLayer_Product_Package/getRegions|getRegions]])</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAvailablePackagesForImageTemplate'> getAvailablePackagesForImageTemplate</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getAvailableStorageUnits'> getAvailableStorageUnits</a> </span>
            <div class='views-field-body'>Retrieve the maximum number of available disk storage units associated with the servers in a package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getCategories'> getCategories</a> </span>
            <div class='views-field-body'>Retrieve this is a collection of categories ([[SoftLayer_Product_Item_Category]]) associated with a package which can be used for ordering. These categories have several objects prepopulated which are useful when determining the available products for purchase. The categories contain groups ([[SoftLayer_Product_Package_Item_Category_Group]]) that organize the products and prices by similar features. For example, operating systems will be grouped by their manufacturer and virtual server disks will be grouped by their disk type (SAN vs. local). Each group will contain prices ([[SoftLayer_Product_Item_Price]]) which you can use determine the cost of each product. Each price has a product ([[SoftLayer_Product_Item]]) which provides the name and other useful information about the server, service or software you may purchase.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getCdnItems'> getCdnItems</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getCloudStorageItems'> getCloudStorageItems</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getConfiguration'> getConfiguration</a> </span>
            <div class='views-field-body'>Retrieve the item categories associated with a package, including information detailing which item categories are required as part of a SoftLayer product order.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getDefaultRamItems'> getDefaultRamItems</a> </span>
            <div class='views-field-body'>Retrieve a collection of valid RAM items available for purchase in this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getDeploymentNodeType'> getDeploymentNodeType</a> </span>
            <div class='views-field-body'>Retrieve the node type for a package in a solution deployment.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getDeploymentPackages'> getDeploymentPackages</a> </span>
            <div class='views-field-body'>Retrieve the packages that are allowed in a multi-server solution. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getDeploymentType'> getDeploymentType</a> </span>
            <div class='views-field-body'>Retrieve the solution deployment type.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getDeployments'> getDeployments</a> </span>
            <div class='views-field-body'>Retrieve the package that represents a multi-server solution. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getDisallowCustomDiskPartitions'> getDisallowCustomDiskPartitions</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates the package does not allow custom disk partitions.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getFirstOrderStep'> getFirstOrderStep</a> </span>
            <div class='views-field-body'>Retrieve the Softlayer order step is optionally step-based. This returns the first SoftLayer_Product_Package_Order_Step in the step-based order process.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getGatewayApplianceFlag'> getGatewayApplianceFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the package is a specialized network gateway appliance package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getGpuFlag'> getGpuFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates that the package supports GPUs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getHourlyBillingAvailableFlag'> getHourlyBillingAvailableFlag</a> </span>
            <div class='views-field-body'>Retrieve determines whether the package contains prices that can be ordered hourly.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getHourlyOnlyOrders'> getHourlyOnlyOrders</a> </span>
            <div class='views-field-body'>Retrieve packages with this flag do not allow monthly orders.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItemAvailabilityTypes'> getItemAvailabilityTypes</a> </span>
            <div class='views-field-body'>Returns a collection of SoftLayer_Product_Item_Attribute_Type objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItemConflicts'> getItemConflicts</a> </span>
            <div class='views-field-body'>Retrieve the item-item conflicts associated with a package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItemLocationConflicts'> getItemLocationConflicts</a> </span>
            <div class='views-field-body'>Retrieve the item-location conflicts associated with a package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItemPriceReferences'> getItemPriceReferences</a> </span>
            <div class='views-field-body'>Retrieve cross reference for item prices</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItemPrices'> getItemPrices</a> </span>
            <div class='views-field-body'>Retrieve a collection of SoftLayer_Product_Item_Prices that are valid for this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItemPricesFromSoftwareDescriptions'> getItemPricesFromSoftwareDescriptions</a> </span>
            <div class='views-field-body'>Returns a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description that are available for the service offering (package). </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItems'> getItems</a> </span>
            <div class='views-field-body'>Retrieve a collection of valid items available for purchase in this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getItemsFromImageTemplate'> getItemsFromImageTemplate</a> </span>
            <div class='views-field-body'>Return a collection of [[SoftLayer_Product_Item]] objects from a [[SoftLayer_Virtual_Guest_Block_Device_Template_Group]] object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getLocations'> getLocations</a> </span>
            <div class='views-field-body'>Retrieve a collection of valid locations for this package. (Deprecated - Use [[SoftLayer_Product_Package/getRegions|getRegions]])</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getLowestServerPrice'> getLowestServerPrice</a> </span>
            <div class='views-field-body'>Retrieve the lowest server [[SoftLayer_Product_Item_Price]] related to this package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getMaximumPortSpeed'> getMaximumPortSpeed</a> </span>
            <div class='views-field-body'>Retrieve the maximum available network speed associated with the package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getMessageQueueItems'> getMessageQueueItems</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getMinimumPortSpeed'> getMinimumPortSpeed</a> </span>
            <div class='views-field-body'>Retrieve the minimum available network speed associated with the package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getMongoDbEngineeredFlag'> getMongoDbEngineeredFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates that this is a MongoDB engineered package. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getNonEuCompliantFlag'> getNonEuCompliantFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the package is not in compliance with EU support.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Product_Package record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getObjectStorageDatacenters'> getObjectStorageDatacenters</a> </span>
            <div class='views-field-body'>Returns a collection of datacenters where object storage is available plus the associated active usage rate prices. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getObjectStorageLocationGroups'> getObjectStorageLocationGroups</a> </span>
            <div class='views-field-body'>Returns a collection of location groups where object storage is available plus the associated active usage rate prices. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getOrderPremiums'> getOrderPremiums</a> </span>
            <div class='views-field-body'>Retrieve the premium price modifiers associated with the [[SoftLayer_Product_Item_Price]] and [[SoftLayer_Location]] objects in a package.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getPopLocationAvailabilityFlag'> getPopLocationAvailabilityFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates if the package may be available in PoP locations in addition to Datacenters.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getPreconfiguredFlag'> getPreconfiguredFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates the package is pre-configured. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getPresetConfigurationRequiredFlag'> getPresetConfigurationRequiredFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the package requires the user to define a preset configuration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getPreventVlanSelectionFlag'> getPreventVlanSelectionFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the package prevents the user from specifying a Vlan.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getPrivateHostedCloudPackageFlag'> getPrivateHostedCloudPackageFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates the package is for a private hosted cloud deployment. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getPrivateHostedCloudPackageType'> getPrivateHostedCloudPackageType</a> </span>
            <div class='views-field-body'>Retrieve the server role of the private hosted cloud deployment. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getPrivateNetworkOnlyFlag'> getPrivateNetworkOnlyFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the package only has access to the private network.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getQuantaStorPackageFlag'> getQuantaStorPackageFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the package is a specialized mass storage QuantaStor package. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getRaidDiskRestrictionFlag'> getRaidDiskRestrictionFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates the package does not allow different disks with RAID.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getRedundantPowerFlag'> getRedundantPowerFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag determines if the package contains a redundant power supply product.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getRegions'> getRegions</a> </span>
            <div class='views-field-body'>Retrieve the regional locations that a package is available in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getResourceGroupTemplate'> getResourceGroupTemplate</a> </span>
            <div class='views-field-body'>Retrieve the resource group template that describes a multi-server solution. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getStandardCategories'> getStandardCategories</a> </span>
            <div class='views-field-body'>This call is similar to [[SoftLayer_Product_Package/getCategories|getCategories]], except that it does not include account-restricted pricing. Not all accounts have restricted pricing. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getTopLevelItemCategoryCode'> getTopLevelItemCategoryCode</a> </span>
            <div class='views-field-body'>Retrieve the top level category code for this service offering.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Package/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve the type of service offering. This property can be used to help filter packages.</div>
        </div>
        </div>
</div>

