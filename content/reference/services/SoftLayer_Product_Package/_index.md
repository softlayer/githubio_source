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

#### [getAccountRestrictedActivePresets](/reference/services/SoftLayer_Product_Package/getAccountRestrictedActivePresets)
Retrieve the preset configurations available only for the authenticated account and this package.
</div>

<div class="method-row">

#### [getAccountRestrictedCategories](/reference/services/SoftLayer_Product_Package/getAccountRestrictedCategories)
Retrieve the results from this call are similar to [SoftLayer_Product_Package::getCategories]({{<ref "reference/services/SoftLayer_Product_Package/getCategories">}}), but these ONLY include account-restricted prices. Not all accounts have restricted pricing.
</div>

<div class="method-row">

#### [getAccountRestrictedPricesFlag](/reference/services/SoftLayer_Product_Package/getAccountRestrictedPricesFlag)
Retrieve the flag to indicate if there are any restricted prices in a package for the currently-active account.
</div>

<div class="method-row">

#### [getActiveItems](/reference/services/SoftLayer_Product_Package/getActiveItems)
Retrieve the active items, as well as their prices and categories for this package
</div>

<div class="method-row">

#### [getActivePackagesByAttribute](/reference/services/SoftLayer_Product_Package/getActivePackagesByAttribute)
[<strong>DEPRECATED</strong>] Retrieve the active [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) objects from which you can order a server, service or software filtered by an attribute type ([SoftLayer_Product_Package_Attribute_Type]({{<ref "reference/datatypes/SoftLayer_Product_Package_Attribute_Type">}})) on the package. 
</div>

<div class="method-row">

#### [getActivePresets](/reference/services/SoftLayer_Product_Package/getActivePresets)
Retrieve the available preset configurations for this package.
</div>

<div class="method-row">

#### [getActivePrivateHostedCloudPackages](/reference/services/SoftLayer_Product_Package/getActivePrivateHostedCloudPackages)
[DEPRECATED] Get the Active SoftLayer_Product_Packages from which one can order private hosted cloud configurations.
</div>

<div class="method-row">

#### [getActiveRamItems](/reference/services/SoftLayer_Product_Package/getActiveRamItems)
Retrieve a collection of valid RAM items available for purchase in this package.
</div>

<div class="method-row">

#### [getActiveServerItems](/reference/services/SoftLayer_Product_Package/getActiveServerItems)
Retrieve a collection of valid server items available for purchase in this package.
</div>

<div class="method-row">

#### [getActiveSoftwareItems](/reference/services/SoftLayer_Product_Package/getActiveSoftwareItems)
Retrieve a collection of valid software items available for purchase in this package.
</div>

<div class="method-row">

#### [getActiveUsagePrices](/reference/services/SoftLayer_Product_Package/getActiveUsagePrices)
Retrieve a collection of [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) objects for pay-as-you-go usage.
</div>

<div class="method-row">

#### [getActiveUsageRatePrices](/reference/services/SoftLayer_Product_Package/getActiveUsageRatePrices)
Return the active usage rate prices for the current package. 
</div>

<div class="method-row">

#### [getAdditionalServiceFlag](/reference/services/SoftLayer_Product_Package/getAdditionalServiceFlag)
Retrieve this flag indicates that the package is an additional service.
</div>

<div class="method-row">

#### [getAllObjects](/reference/services/SoftLayer_Product_Package/getAllObjects)
Get the Active SoftLayer_Product_Packages
</div>

<div class="method-row">

#### [getAttributes](/reference/services/SoftLayer_Product_Package/getAttributes)

</div>

<div class="method-row">

#### [getAvailableLocations](/reference/services/SoftLayer_Product_Package/getAvailableLocations)
Retrieve a collection of valid locations for this package. (Deprecated - Use [SoftLayer_Product_Package::getRegions]({{<ref "reference/services/SoftLayer_Product_Package/getRegions">}}))
</div>

<div class="method-row">

#### [getAvailablePackagesForImageTemplate](/reference/services/SoftLayer_Product_Package/getAvailablePackagesForImageTemplate)

</div>

<div class="method-row">

#### [getAvailableStorageUnits](/reference/services/SoftLayer_Product_Package/getAvailableStorageUnits)
Retrieve the maximum number of available disk storage units associated with the servers in a package.
</div>

<div class="method-row">

#### [getCategories](/reference/services/SoftLayer_Product_Package/getCategories)
Retrieve this is a collection of categories ([SoftLayer_Product_Item_Category]({{<ref "reference/datatypes/SoftLayer_Product_Item_Category">}})) associated with a package which can be used for ordering. These categories have several objects prepopulated which are useful when determining the available products for purchase. The categories contain groups ([SoftLayer_Product_Package_Item_Category_Group]({{<ref "reference/datatypes/SoftLayer_Product_Package_Item_Category_Group">}})) that organize the products and prices by similar features. For example, operating systems will be grouped by their manufacturer and virtual server disks will be grouped by their disk type (SAN vs. local). Each group will contain prices ([SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}})) which you can use determine the cost of each product. Each price has a product ([SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}})) which provides the name and other useful information about the server, service or software you may purchase.
</div>

<div class="method-row">

#### [getCdnItems](/reference/services/SoftLayer_Product_Package/getCdnItems)

</div>

<div class="method-row">

#### [getCloudStorageItems](/reference/services/SoftLayer_Product_Package/getCloudStorageItems)

</div>

<div class="method-row">

#### [getConfiguration](/reference/services/SoftLayer_Product_Package/getConfiguration)
Retrieve the item categories associated with a package, including information detailing which item categories are required as part of a SoftLayer product order.
</div>

<div class="method-row">

#### [getDefaultBootCategoryCode](/reference/services/SoftLayer_Product_Package/getDefaultBootCategoryCode)
Retrieve the default boot category code for the package.
</div>

<div class="method-row">

#### [getDefaultRamItems](/reference/services/SoftLayer_Product_Package/getDefaultRamItems)
Retrieve a collection of valid RAM items available for purchase in this package.
</div>

<div class="method-row">

#### [getDeploymentNodeType](/reference/services/SoftLayer_Product_Package/getDeploymentNodeType)
Retrieve the node type for a package in a solution deployment.
</div>

<div class="method-row">

#### [getDeploymentPackages](/reference/services/SoftLayer_Product_Package/getDeploymentPackages)
Retrieve the packages that are allowed in a multi-server solution. (Deprecated)
</div>

<div class="method-row">

#### [getDeploymentType](/reference/services/SoftLayer_Product_Package/getDeploymentType)
Retrieve the solution deployment type.
</div>

<div class="method-row">

#### [getDeployments](/reference/services/SoftLayer_Product_Package/getDeployments)
Retrieve the package that represents a multi-server solution. (Deprecated)
</div>

<div class="method-row">

#### [getDisallowCustomDiskPartitions](/reference/services/SoftLayer_Product_Package/getDisallowCustomDiskPartitions)
Retrieve this flag indicates the package does not allow custom disk partitions.
</div>

<div class="method-row">

#### [getFirstOrderStep](/reference/services/SoftLayer_Product_Package/getFirstOrderStep)
Retrieve the Softlayer order step is optionally step-based. This returns the first SoftLayer_Product_Package_Order_Step in the step-based order process.
</div>

<div class="method-row">

#### [getGatewayApplianceFlag](/reference/services/SoftLayer_Product_Package/getGatewayApplianceFlag)
Retrieve whether the package is a specialized network gateway appliance package.
</div>

<div class="method-row">

#### [getGpuFlag](/reference/services/SoftLayer_Product_Package/getGpuFlag)
Retrieve this flag indicates that the package supports GPUs.
</div>

<div class="method-row">

#### [getHourlyBillingAvailableFlag](/reference/services/SoftLayer_Product_Package/getHourlyBillingAvailableFlag)
Retrieve determines whether the package contains prices that can be ordered hourly.
</div>

<div class="method-row">

#### [getHourlyOnlyOrders](/reference/services/SoftLayer_Product_Package/getHourlyOnlyOrders)
Retrieve packages with this flag do not allow monthly orders.
</div>

<div class="method-row">

#### [getItemAvailabilityTypes](/reference/services/SoftLayer_Product_Package/getItemAvailabilityTypes)
Returns a collection of SoftLayer_Product_Item_Attribute_Type objects.
</div>

<div class="method-row">

#### [getItemConflicts](/reference/services/SoftLayer_Product_Package/getItemConflicts)
Retrieve the item-item conflicts associated with a package.
</div>

<div class="method-row">

#### [getItemLocationConflicts](/reference/services/SoftLayer_Product_Package/getItemLocationConflicts)
Retrieve the item-location conflicts associated with a package.
</div>

<div class="method-row">

#### [getItemPriceReferences](/reference/services/SoftLayer_Product_Package/getItemPriceReferences)
Retrieve cross reference for item prices
</div>

<div class="method-row">

#### [getItemPrices](/reference/services/SoftLayer_Product_Package/getItemPrices)
Retrieve a collection of SoftLayer_Product_Item_Prices that are valid for this package.
</div>

<div class="method-row">

#### [getItemPricesFromSoftwareDescriptions](/reference/services/SoftLayer_Product_Package/getItemPricesFromSoftwareDescriptions)
Returns a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description that are available for the service offering (package). 
</div>

<div class="method-row">

#### [getItems](/reference/services/SoftLayer_Product_Package/getItems)
Retrieve a collection of valid items available for purchase in this package.
</div>

<div class="method-row">

#### [getItemsFromImageTemplate](/reference/services/SoftLayer_Product_Package/getItemsFromImageTemplate)
Return a collection of [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}) objects from a [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}) object
</div>

<div class="method-row">

#### [getLocations](/reference/services/SoftLayer_Product_Package/getLocations)
Retrieve a collection of valid locations for this package. (Deprecated - Use [SoftLayer_Product_Package::getRegions]({{<ref "reference/services/SoftLayer_Product_Package/getRegions">}}))
</div>

<div class="method-row">

#### [getLowestServerPrice](/reference/services/SoftLayer_Product_Package/getLowestServerPrice)
Retrieve the lowest server [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) related to this package.
</div>

<div class="method-row">

#### [getMaximumPortSpeed](/reference/services/SoftLayer_Product_Package/getMaximumPortSpeed)
Retrieve the maximum available network speed associated with the package.
</div>

<div class="method-row">

#### [getMessageQueueItems](/reference/services/SoftLayer_Product_Package/getMessageQueueItems)

</div>

<div class="method-row">

#### [getMinimumPortSpeed](/reference/services/SoftLayer_Product_Package/getMinimumPortSpeed)
Retrieve the minimum available network speed associated with the package.
</div>

<div class="method-row">

#### [getMongoDbEngineeredFlag](/reference/services/SoftLayer_Product_Package/getMongoDbEngineeredFlag)
Retrieve this flag indicates that this is a MongoDB engineered package. (Deprecated)
</div>

<div class="method-row">

#### [getNonEuCompliantFlag](/reference/services/SoftLayer_Product_Package/getNonEuCompliantFlag)
Retrieve whether the package is not in compliance with EU support.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Product_Package/getObject)
Retrieve a SoftLayer_Product_Package record.
</div>

<div class="method-row">

#### [getObjectStorageDatacenters](/reference/services/SoftLayer_Product_Package/getObjectStorageDatacenters)
Returns a collection of datacenters where object storage is available plus the associated active usage rate prices. 
</div>

<div class="method-row">

#### [getObjectStorageLocationGroups](/reference/services/SoftLayer_Product_Package/getObjectStorageLocationGroups)
Returns a collection of location groups where object storage is available plus the associated active usage rate prices. 
</div>

<div class="method-row">

#### [getOrderPremiums](/reference/services/SoftLayer_Product_Package/getOrderPremiums)
Retrieve the premium price modifiers associated with the [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) and [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) objects in a package.
</div>

<div class="method-row">

#### [getPopLocationAvailabilityFlag](/reference/services/SoftLayer_Product_Package/getPopLocationAvailabilityFlag)
Retrieve this flag indicates if the package may be available in PoP locations in addition to Datacenters.
</div>

<div class="method-row">

#### [getPreconfiguredFlag](/reference/services/SoftLayer_Product_Package/getPreconfiguredFlag)
Retrieve this flag indicates the package is pre-configured. (Deprecated)
</div>

<div class="method-row">

#### [getPresetConfigurationRequiredFlag](/reference/services/SoftLayer_Product_Package/getPresetConfigurationRequiredFlag)
Retrieve whether the package requires the user to define a preset configuration.
</div>

<div class="method-row">

#### [getPreventVlanSelectionFlag](/reference/services/SoftLayer_Product_Package/getPreventVlanSelectionFlag)
Retrieve whether the package prevents the user from specifying a Vlan.
</div>

<div class="method-row">

#### [getPrivateHostedCloudPackageFlag](/reference/services/SoftLayer_Product_Package/getPrivateHostedCloudPackageFlag)
Retrieve this flag indicates the package is for a private hosted cloud deployment. (Deprecated)
</div>

<div class="method-row">

#### [getPrivateHostedCloudPackageType](/reference/services/SoftLayer_Product_Package/getPrivateHostedCloudPackageType)
Retrieve the server role of the private hosted cloud deployment. (Deprecated)
</div>

<div class="method-row">

#### [getPrivateNetworkOnlyFlag](/reference/services/SoftLayer_Product_Package/getPrivateNetworkOnlyFlag)
Retrieve whether the package only has access to the private network.
</div>

<div class="method-row">

#### [getQuantaStorPackageFlag](/reference/services/SoftLayer_Product_Package/getQuantaStorPackageFlag)
Retrieve whether the package is a specialized mass storage QuantaStor package. (Deprecated)
</div>

<div class="method-row">

#### [getRaidDiskRestrictionFlag](/reference/services/SoftLayer_Product_Package/getRaidDiskRestrictionFlag)
Retrieve this flag indicates the package does not allow different disks with RAID.
</div>

<div class="method-row">

#### [getRedundantPowerFlag](/reference/services/SoftLayer_Product_Package/getRedundantPowerFlag)
Retrieve this flag determines if the package contains a redundant power supply product.
</div>

<div class="method-row">

#### [getRegions](/reference/services/SoftLayer_Product_Package/getRegions)
Retrieve the regional locations that a package is available in.
</div>

<div class="method-row">

#### [getResourceGroupTemplate](/reference/services/SoftLayer_Product_Package/getResourceGroupTemplate)
Retrieve the resource group template that describes a multi-server solution. (Deprecated)
</div>

<div class="method-row">

#### [getStandardCategories](/reference/services/SoftLayer_Product_Package/getStandardCategories)
This call is similar to [SoftLayer_Product_Package::getCategories]({{<ref "reference/services/SoftLayer_Product_Package/getCategories">}}), except that it does not include account-restricted pricing. Not all accounts have restricted pricing. 
</div>

<div class="method-row">

#### [getTopLevelItemCategoryCode](/reference/services/SoftLayer_Product_Package/getTopLevelItemCategoryCode)
Retrieve the top level category code for this service offering.
</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_Product_Package/getType)
Retrieve the type of service offering. This property can be used to help filter packages.
</div>
</div>

</div>

