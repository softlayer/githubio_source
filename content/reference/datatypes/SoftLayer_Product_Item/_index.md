---
title: "SoftLayer_Product_Item"
description: "The SoftLayer_Product_Item data type contains general information relating to a single SoftLayer product."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item"
---

# SoftLayer_Product_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Item data type contains general information relating to a single SoftLayer product. 





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
[capacity]: #capacity
#### [capacity]
Some Product Items have capacity information such as RAM and bandwidth, and others. This provides the numerical representation of the capacity given in the description of this product item.  
<span class="type-label">Type: </span>**decimal**

-----
[description]: #description
#### [description]
A product's description  
<span class="type-label">Type: </span>**string**

-----
[hardwareGenericComponentId]: #hardwaregenericcomponentid
#### [hardwareGenericComponentId]
The hardware generic component model ID of the product.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A product's internal identification number  
<span class="type-label">Type: </span>**integer**

-----
[itemTaxCategoryId]: #itemtaxcategoryid
#### [itemTaxCategoryId]
A products tax category internal identification number  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
A unique key name for the product.  
<span class="type-label">Type: </span>**string**

-----
[longDescription]: #longdescription
#### [longDescription]
Detailed product description  
<span class="type-label">Type: </span>**string**

-----
[softwareDescriptionId]: #softwaredescriptionid
#### [softwareDescriptionId]
The unique identifier of the SoftLayer_Software_Description tied to this item.  
<span class="type-label">Type: </span>**integer**

-----
[units]: #units
#### [units]
The unit of measurement that a product item is measured in.  
<span class="type-label">Type: </span>**string**

-----
[upgradeItemId]: #upgradeitemid
#### [upgradeItemId]
A products upgrade item's internal identification number  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[activePresaleEvents]: #activepresaleevents
#### [activePresaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**

-----
[activeUsagePrices]: #activeusageprices
#### [activeUsagePrices]
Active usage based prices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[attributes]: #attributes
#### [attributes]
The attribute values for a product item. These are additional properties that give extra information about the product being sold.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Attribute'>SoftLayer_Product_Item_Attribute[] </a>**

-----
[availabilityAttributes]: #availabilityattributes
#### [availabilityAttributes]
Attributes that govern when an item may no longer be available.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Attribute'>SoftLayer_Product_Item_Attribute[] </a>**

-----
[billingType]: #billingtype
#### [billingType]
An item's special billing type, if applicable.  
<span class="type-label">Type: </span>**string**

-----
[bundle]: #bundle
#### [bundle]
An item's included product item references. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item_Bundles objects. See the SoftLayer_Product_Item::bundleItems property for bundle of SoftLayer_Product_Item of objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Bundles'>SoftLayer_Product_Item_Bundles[] </a>**

-----
[bundleItems]: #bundleitems
#### [bundleItems]
An item's included products. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[capacityMaximum]: #capacitymaximum
#### [capacityMaximum]
When the product capacity is best described as a range, this holds the ceiling of the range.  
<span class="type-label">Type: </span>**string**

-----
[capacityMinimum]: #capacityminimum
#### [capacityMinimum]
When the product capacity is best described as a range, this holds the floor of the range.  
<span class="type-label">Type: </span>**string**

-----
[capacityRestrictedProductFlag]: #capacityrestrictedproductflag
#### [capacityRestrictedProductFlag]
This flag indicates that this product is restricted by a capacity on a related product.  
<span class="type-label">Type: </span>**boolean**

-----
[categories]: #categories
#### [categories]
An item's associated item categories.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**

-----
[configurationTemplates]: #configurationtemplates
#### [configurationTemplates]
Some product items have configuration templates which can be used to during provisioning of that product.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template[] </a>**

-----
[conflicts]: #conflicts
#### [conflicts]
An item's conflicts. For example, McAfee LinuxShield cannot be ordered with Windows. It was not meant for that operating system and as such is a conflict.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**

-----
[coreRestrictedItemFlag]: #corerestricteditemflag
#### [coreRestrictedItemFlag]
This flag indicates that this product is restricted by the number of cores on the compute instance. This is deprecated. Use [SoftLayer_Product_Item::getCapacityRestrictedProductFlag]({{<ref "reference/services/SoftLayer_Product_Item/getCapacityRestrictedProductFlag">}})  
<span class="type-label">Type: </span>**boolean**

-----
[downgradeItem]: #downgradeitem
#### [downgradeItem]
Some product items have a downgrade path. This is the first product item in the downgrade path.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[downgradeItems]: #downgradeitems
#### [downgradeItems]
Some product items have a downgrade path. These are those product items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[globalCategoryConflicts]: #globalcategoryconflicts
#### [globalCategoryConflicts]
An item's category conflicts. For example, 10 Gbps redundant network functionality cannot be ordered with a secondary GPU and as such is a conflict.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**

-----
[hardwareGenericComponentModel]: #hardwaregenericcomponentmodel
#### [hardwareGenericComponentModel]
The generic hardware component that this item represents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a>**

-----
[hideFromPortalFlag]: #hidefromportalflag
#### [hideFromPortalFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[ineligibleForAccountDiscountFlag]: #ineligibleforaccountdiscountflag
#### [ineligibleForAccountDiscountFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[inventory]: #inventory
#### [inventory]
DEPRECATED. An item's inventory status per datacenter.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Inventory'>SoftLayer_Product_Package_Inventory[] </a>**

-----
[isEngineeredServerProduct]: #isengineeredserverproduct
#### [isEngineeredServerProduct]
Flag to indicate the server product is engineered for a multi-server solution. (Deprecated)  
<span class="type-label">Type: </span>**boolean**

-----
[itemCategory]: #itemcategory
#### [itemCategory]
An item's primary item category.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**

-----
[localDiskFlag]: #localdiskflag
#### [localDiskFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[locationConflicts]: #locationconflicts
#### [locationConflicts]
An item's location conflicts. For example, Dual Path network functionality cannot be ordered in WDC and as such is a conflict.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**

-----
[minimumNvmeBays]: #minimumnvmebays
#### [minimumNvmeBays]
The minimum number of bays that support NVMe SSDs.  
<span class="type-label">Type: </span>**integer**

-----
[nvmeDiskFlag]: #nvmediskflag
#### [nvmeDiskFlag]
Indicates whether an item is a NVMe SSD.  
<span class="type-label">Type: </span>**boolean**

-----
[objectStorageClusterGeolocationType]: #objectstorageclustergeolocationtype
#### [objectStorageClusterGeolocationType]
  
<span class="type-label">Type: </span>**string**

-----
[objectStorageItemFlag]: #objectstorageitemflag
#### [objectStorageItemFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[objectStorageServiceClass]: #objectstorageserviceclass
#### [objectStorageServiceClass]
  
<span class="type-label">Type: </span>**string**

-----
[packages]: #packages
#### [packages]
A collection of all the SoftLayer_Product_Package(s) in which this item exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>**

-----
[physicalCoreCapacity]: #physicalcorecapacity
#### [physicalCoreCapacity]
The number of cores that a processor has.  
<span class="type-label">Type: </span>**string**

-----
[presaleEvents]: #presaleevents
#### [presaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**

-----
[prices]: #prices
#### [prices]
A product item's prices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[requirements]: #requirements
#### [requirements]
If an item must be ordered with another item, it will have a requirement item here.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Requirement'>SoftLayer_Product_Item_Requirement[] </a>**

-----
[rules]: #rules
#### [rules]
An item's rules. This includes the requirements and conflicts to resources that an item has.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule'>SoftLayer_Product_Item_Rule[] </a>**

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The SoftLayer_Software_Description tied to this item. This will only be populated for software items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**

-----
[taxCategory]: #taxcategory
#### [taxCategory]
An item's tax category, if applicable.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Tax_Category'>SoftLayer_Product_Item_Tax_Category </a>**

-----
[thirdPartyPolicyAssignments]: #thirdpartypolicyassignments
#### [thirdPartyPolicyAssignments]
Third-party policy assignments for this product.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Policy_Assignment'>SoftLayer_Product_Item_Policy_Assignment[] </a>**

-----
[thirdPartySupportVendor]: #thirdpartysupportvendor
#### [thirdPartySupportVendor]
The 3rd party vendor for a support subscription item. (Deprecated)  
<span class="type-label">Type: </span>**string**

-----
[totalPhysicalCoreCapacity]: #totalphysicalcorecapacity
#### [totalPhysicalCoreCapacity]
The total number of physical processing cores (excluding virtual cores / hyperthreads) for this server.  
<span class="type-label">Type: </span>**integer**

-----
[totalPhysicalCoreCount]: #totalphysicalcorecount
#### [totalPhysicalCoreCount]
Shows the total number of cores. This is deprecated. Use [SoftLayer_Product_Item::getCapacity]({{<ref "reference/services/SoftLayer_Product_Item/getCapacity">}}) for server products  
<span class="type-label">Type: </span>**integer**

-----
[totalProcessorCapacity]: #totalprocessorcapacity
#### [totalProcessorCapacity]
The total number of processors for this server.  
<span class="type-label">Type: </span>**integer**

-----
[upgradeItem]: #upgradeitem
#### [upgradeItem]
Some product items have an upgrade path. This is the next product item in the upgrade path.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[upgradeItems]: #upgradeitems
#### [upgradeItems]
Some product items have an upgrade path. These are those upgrade product items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**


## Count

-----
[activePresaleEventCount]: #activepresaleeventcount
#### [activePresaleEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[activeUsagePriceCount]: #activeusagepricecount
#### [activeUsagePriceCount]
A count of active usage based prices.   
<span class="type-label">Type: </span>**unsigned long**


-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of the attribute values for a product item. These are additional properties that give extra information about the product being sold.   
<span class="type-label">Type: </span>**unsigned long**


-----
[availabilityAttributeCount]: #availabilityattributecount
#### [availabilityAttributeCount]
A count of attributes that govern when an item may no longer be available.   
<span class="type-label">Type: </span>**unsigned long**


-----
[bundleCount]: #bundlecount
#### [bundleCount]
A count of an item's included product item references. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item_Bundles objects. See the SoftLayer_Product_Item::bundleItems property for bundle of SoftLayer_Product_Item of objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[bundleItemCount]: #bundleitemcount
#### [bundleItemCount]
A count of an item's included products. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[categoryCount]: #categorycount
#### [categoryCount]
A count of an item's associated item categories.   
<span class="type-label">Type: </span>**unsigned long**


-----
[configurationTemplateCount]: #configurationtemplatecount
#### [configurationTemplateCount]
A count of some product items have configuration templates which can be used to during provisioning of that product.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downgradeItemCount]: #downgradeitemcount
#### [downgradeItemCount]
A count of some product items have a downgrade path. These are those product items.   
<span class="type-label">Type: </span>**unsigned long**


-----
[inventoryCount]: #inventorycount
#### [inventoryCount]
A count of dEPRECATED. An item's inventory status per datacenter.   
<span class="type-label">Type: </span>**unsigned long**


-----
[packageCount]: #packagecount
#### [packageCount]
A count of a collection of all the SoftLayer_Product_Package(s) in which this item exists.   
<span class="type-label">Type: </span>**unsigned long**


-----
[presaleEventCount]: #presaleeventcount
#### [presaleEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[priceCount]: #pricecount
#### [priceCount]
A count of a product item's prices.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of an item's rules. This includes the requirements and conflicts to resources that an item has.   
<span class="type-label">Type: </span>**unsigned long**


-----
[thirdPartyPolicyAssignmentCount]: #thirdpartypolicyassignmentcount
#### [thirdPartyPolicyAssignmentCount]
A count of third-party policy assignments for this product.   
<span class="type-label">Type: </span>**unsigned long**


-----
[upgradeItemCount]: #upgradeitemcount
#### [upgradeItemCount]
A count of some product items have an upgrade path. These are those upgrade product items.   
<span class="type-label">Type: </span>**unsigned long**

</div>


