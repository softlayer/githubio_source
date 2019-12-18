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
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Package' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package' >Datatype</a></li>
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

## Local
-----
[description]: #description
#### [description]
A generic description of the processor type and count. This includes HTML, so you may want to strip these tags if you plan to use it.  
<span class="type-label">Type: </span>**string**

-----
[firstOrderStepId]: #firstorderstepid
#### [firstOrderStepId]
This is only needed for step-based order verification. We use this for the order forms, but it is not required. This step is the first SoftLayer_Product_Package_Step for this package. Use this for for filtering which item categories are returned as a part of SoftLayer_Product_Package_Order_Configuration.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A package's internal identifier. Everything regarding a SoftLayer_Product_Package is tied back to this id.   
<span class="type-label">Type: </span>**integer**

-----
[isActive]: #isactive
#### [isActive]
  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
A unique key name for the package.  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
The description of the package. For server packages, this is usually a detailed description of processor type and count.  
<span class="type-label">Type: </span>**string**

-----
[subDescription]: #subdescription
#### [subDescription]
This currently contains no information but is here for future use.  
<span class="type-label">Type: </span>**string**

-----
[unitSize]: #unitsize
#### [unitSize]
The server unit size this package will match to.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[accountRestrictedActivePresets]: #accountrestrictedactivepresets
#### [accountRestrictedActivePresets]
The preset configurations available only for the authenticated account and this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset[] </a>**

-----
[accountRestrictedCategories]: #accountrestrictedcategories
#### [accountRestrictedCategories]
The results from this call are similar to [SoftLayer_Product_Package::getCategories]({{<ref "reference/services/SoftLayer_Product_Package/getCategories">}}), but these ONLY include account-restricted prices. Not all accounts have restricted pricing.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**

-----
[accountRestrictedPricesFlag]: #accountrestrictedpricesflag
#### [accountRestrictedPricesFlag]
The flag to indicate if there are any restricted prices in a package for the currently-active account.  
<span class="type-label">Type: </span>**boolean**

-----
[activePresets]: #activepresets
#### [activePresets]
The available preset configurations for this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset[] </a>**

-----
[activeRamItems]: #activeramitems
#### [activeRamItems]
A collection of valid RAM items available for purchase in this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[activeServerItems]: #activeserveritems
#### [activeServerItems]
A collection of valid server items available for purchase in this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[activeSoftwareItems]: #activesoftwareitems
#### [activeSoftwareItems]
A collection of valid software items available for purchase in this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[activeUsagePrices]: #activeusageprices
#### [activeUsagePrices]
A collection of [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) objects for pay-as-you-go usage.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[additionalServiceFlag]: #additionalserviceflag
#### [additionalServiceFlag]
This flag indicates that the package is an additional service.  
<span class="type-label">Type: </span>**boolean**

-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Attribute'>SoftLayer_Product_Package_Attribute[] </a>**

-----
[availableLocations]: #availablelocations
#### [availableLocations]
A collection of valid locations for this package. (Deprecated - Use [SoftLayer_Product_Package::getRegions]({{<ref "reference/services/SoftLayer_Product_Package/getRegions">}}))  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Locations'>SoftLayer_Product_Package_Locations[] </a>**

-----
[availableStorageUnits]: #availablestorageunits
#### [availableStorageUnits]
The maximum number of available disk storage units associated with the servers in a package.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[categories]: #categories
#### [categories]
This is a collection of categories ([SoftLayer_Product_Item_Category]({{<ref "reference/datatypes/SoftLayer_Product_Item_Category">}})) associated with a package which can be used for ordering. These categories have several objects prepopulated which are useful when determining the available products for purchase. The categories contain groups ([SoftLayer_Product_Package_Item_Category_Group]({{<ref "reference/datatypes/SoftLayer_Product_Package_Item_Category_Group">}})) that organize the products and prices by similar features. For example, operating systems will be grouped by their manufacturer and virtual server disks will be grouped by their disk type (SAN vs. local). Each group will contain prices ([SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}})) which you can use determine the cost of each product. Each price has a product ([SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}})) which provides the name and other useful information about the server, service or software you may purchase.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**

-----
[configuration]: #configuration
#### [configuration]
The item categories associated with a package, including information detailing which item categories are required as part of a SoftLayer product order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration'>SoftLayer_Product_Package_Order_Configuration[] </a>**

-----
[defaultRamItems]: #defaultramitems
#### [defaultRamItems]
A collection of valid RAM items available for purchase in this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[deploymentNodeType]: #deploymentnodetype
#### [deploymentNodeType]
The node type for a package in a solution deployment.  
<span class="type-label">Type: </span>**string**

-----
[deploymentPackages]: #deploymentpackages
#### [deploymentPackages]
The packages that are allowed in a multi-server solution. (Deprecated)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>**

-----
[deploymentType]: #deploymenttype
#### [deploymentType]
The solution deployment type.  
<span class="type-label">Type: </span>**string**

-----
[deployments]: #deployments
#### [deployments]
The package that represents a multi-server solution. (Deprecated)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>**

-----
[disallowCustomDiskPartitions]: #disallowcustomdiskpartitions
#### [disallowCustomDiskPartitions]
This flag indicates the package does not allow custom disk partitions.  
<span class="type-label">Type: </span>**boolean**

-----
[firstOrderStep]: #firstorderstep
#### [firstOrderStep]
The Softlayer order step is optionally step-based. This returns the first SoftLayer_Product_Package_Order_Step in the step-based order process.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step'>SoftLayer_Product_Package_Order_Step </a>**

-----
[gatewayApplianceFlag]: #gatewayapplianceflag
#### [gatewayApplianceFlag]
Whether the package is a specialized network gateway appliance package.  
<span class="type-label">Type: </span>**boolean**

-----
[gpuFlag]: #gpuflag
#### [gpuFlag]
This flag indicates that the package supports GPUs.  
<span class="type-label">Type: </span>**boolean**

-----
[hourlyBillingAvailableFlag]: #hourlybillingavailableflag
#### [hourlyBillingAvailableFlag]
Determines whether the package contains prices that can be ordered hourly.  
<span class="type-label">Type: </span>**boolean**

-----
[hourlyOnlyOrders]: #hourlyonlyorders
#### [hourlyOnlyOrders]
Packages with this flag do not allow monthly orders.  
<span class="type-label">Type: </span>**boolean**

-----
[itemConflicts]: #itemconflicts
#### [itemConflicts]
The item-item conflicts associated with a package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**

-----
[itemLocationConflicts]: #itemlocationconflicts
#### [itemLocationConflicts]
The item-location conflicts associated with a package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**

-----
[itemPriceReferences]: #itempricereferences
#### [itemPriceReferences]
cross reference for item prices  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Item_Prices'>SoftLayer_Product_Package_Item_Prices[] </a>**

-----
[itemPrices]: #itemprices
#### [itemPrices]
A collection of SoftLayer_Product_Item_Prices that are valid for this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[items]: #items
#### [items]
A collection of valid items available for purchase in this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[locations]: #locations
#### [locations]
A collection of valid locations for this package. (Deprecated - Use [SoftLayer_Product_Package::getRegions]({{<ref "reference/services/SoftLayer_Product_Package/getRegions">}}))  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**

-----
[lowestServerPrice]: #lowestserverprice
#### [lowestServerPrice]
The lowest server [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) related to this package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**

-----
[maximumPortSpeed]: #maximumportspeed
#### [maximumPortSpeed]
The maximum available network speed associated with the package.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[minimumPortSpeed]: #minimumportspeed
#### [minimumPortSpeed]
The minimum available network speed associated with the package.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[mongoDbEngineeredFlag]: #mongodbengineeredflag
#### [mongoDbEngineeredFlag]
This flag indicates that this is a MongoDB engineered package. (Deprecated)  
<span class="type-label">Type: </span>**boolean**

-----
[nonEuCompliantFlag]: #noneucompliantflag
#### [nonEuCompliantFlag]
Whether the package is not in compliance with EU support.  
<span class="type-label">Type: </span>**boolean**

-----
[orderPremiums]: #orderpremiums
#### [orderPremiums]
The premium price modifiers associated with the [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) and [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) objects in a package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price_Premium'>SoftLayer_Product_Item_Price_Premium[] </a>**

-----
[popLocationAvailabilityFlag]: #poplocationavailabilityflag
#### [popLocationAvailabilityFlag]
This flag indicates if the package may be available in PoP locations in addition to Datacenters.  
<span class="type-label">Type: </span>**boolean**

-----
[preconfiguredFlag]: #preconfiguredflag
#### [preconfiguredFlag]
This flag indicates the package is pre-configured. (Deprecated)  
<span class="type-label">Type: </span>**boolean**

-----
[presetConfigurationRequiredFlag]: #presetconfigurationrequiredflag
#### [presetConfigurationRequiredFlag]
Whether the package requires the user to define a preset configuration.  
<span class="type-label">Type: </span>**boolean**

-----
[preventVlanSelectionFlag]: #preventvlanselectionflag
#### [preventVlanSelectionFlag]
Whether the package prevents the user from specifying a Vlan.  
<span class="type-label">Type: </span>**boolean**

-----
[privateHostedCloudPackageFlag]: #privatehostedcloudpackageflag
#### [privateHostedCloudPackageFlag]
This flag indicates the package is for a private hosted cloud deployment. (Deprecated)  
<span class="type-label">Type: </span>**boolean**

-----
[privateHostedCloudPackageType]: #privatehostedcloudpackagetype
#### [privateHostedCloudPackageType]
The server role of the private hosted cloud deployment. (Deprecated)  
<span class="type-label">Type: </span>**string**

-----
[privateNetworkOnlyFlag]: #privatenetworkonlyflag
#### [privateNetworkOnlyFlag]
Whether the package only has access to the private network.  
<span class="type-label">Type: </span>**boolean**

-----
[quantaStorPackageFlag]: #quantastorpackageflag
#### [quantaStorPackageFlag]
Whether the package is a specialized mass storage QuantaStor package. (Deprecated)  
<span class="type-label">Type: </span>**boolean**

-----
[raidDiskRestrictionFlag]: #raiddiskrestrictionflag
#### [raidDiskRestrictionFlag]
This flag indicates the package does not allow different disks with RAID.  
<span class="type-label">Type: </span>**boolean**

-----
[redundantPowerFlag]: #redundantpowerflag
#### [redundantPowerFlag]
This flag determines if the package contains a redundant power supply product.  
<span class="type-label">Type: </span>**boolean**

-----
[regions]: #regions
#### [regions]
The regional locations that a package is available in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Region'>SoftLayer_Location_Region[] </a>**

-----
[resourceGroupTemplate]: #resourcegrouptemplate
#### [resourceGroupTemplate]
The resource group template that describes a multi-server solution. (Deprecated)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Template'>SoftLayer_Resource_Group_Template </a>**

-----
[topLevelItemCategoryCode]: #toplevelitemcategorycode
#### [topLevelItemCategoryCode]
The top level category code for this service offering.  
<span class="type-label">Type: </span>**string**

-----
[type]: #type
#### [type]
The type of service offering. This property can be used to help filter packages.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Type'>SoftLayer_Product_Package_Type </a>**


## Count

-----
[accountRestrictedActivePresetCount]: #accountrestrictedactivepresetcount
#### [accountRestrictedActivePresetCount]
A count of the preset configurations available only for the authenticated account and this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[accountRestrictedCategoryCount]: #accountrestrictedcategorycount
#### [accountRestrictedCategoryCount]
A count of the results from this call are similar to [SoftLayer_Product_Package::getCategories]({{<ref "reference/services/SoftLayer_Product_Package/getCategories">}}), but these ONLY include account-restricted prices. Not all accounts have restricted pricing.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activePresetCount]: #activepresetcount
#### [activePresetCount]
A count of the available preset configurations for this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeRamItemCount]: #activeramitemcount
#### [activeRamItemCount]
A count of a collection of valid RAM items available for purchase in this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeServerItemCount]: #activeserveritemcount
#### [activeServerItemCount]
A count of a collection of valid server items available for purchase in this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeSoftwareItemCount]: #activesoftwareitemcount
#### [activeSoftwareItemCount]
A count of a collection of valid software items available for purchase in this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[activeUsagePriceCount]: #activeusagepricecount
#### [activeUsagePriceCount]
A count of a collection of [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) objects for pay-as-you-go usage.   
<span class="type-label">Type: </span>**unsigned long**


-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[availableLocationCount]: #availablelocationcount
#### [availableLocationCount]
A count of a collection of valid locations for this package. (Deprecated - Use [SoftLayer_Product_Package::getRegions]({{<ref "reference/services/SoftLayer_Product_Package/getRegions">}}))   
<span class="type-label">Type: </span>**unsigned long**


-----
[configurationCount]: #configurationcount
#### [configurationCount]
A count of the item categories associated with a package, including information detailing which item categories are required as part of a SoftLayer product order.   
<span class="type-label">Type: </span>**unsigned long**


-----
[defaultRamItemCount]: #defaultramitemcount
#### [defaultRamItemCount]
A count of a collection of valid RAM items available for purchase in this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[deploymentCount]: #deploymentcount
#### [deploymentCount]
A count of the package that represents a multi-server solution. (Deprecated)   
<span class="type-label">Type: </span>**unsigned long**


-----
[deploymentPackageCount]: #deploymentpackagecount
#### [deploymentPackageCount]
A count of the packages that are allowed in a multi-server solution. (Deprecated)   
<span class="type-label">Type: </span>**unsigned long**


-----
[itemCount]: #itemcount
#### [itemCount]
A count of a collection of valid items available for purchase in this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[itemPriceCount]: #itempricecount
#### [itemPriceCount]
A count of a collection of SoftLayer_Product_Item_Prices that are valid for this package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[itemPriceReferenceCount]: #itempricereferencecount
#### [itemPriceReferenceCount]
A count of cross reference for item prices   
<span class="type-label">Type: </span>**unsigned long**


-----
[locationCount]: #locationcount
#### [locationCount]
A count of a collection of valid locations for this package. (Deprecated - Use [SoftLayer_Product_Package::getRegions]({{<ref "reference/services/SoftLayer_Product_Package/getRegions">}}))   
<span class="type-label">Type: </span>**unsigned long**


-----
[orderPremiumCount]: #orderpremiumcount
#### [orderPremiumCount]
A count of the premium price modifiers associated with the [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) and [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) objects in a package.   
<span class="type-label">Type: </span>**unsigned long**


-----
[regionCount]: #regioncount
#### [regionCount]
A count of the regional locations that a package is available in.   
<span class="type-label">Type: </span>**unsigned long**

</div>


