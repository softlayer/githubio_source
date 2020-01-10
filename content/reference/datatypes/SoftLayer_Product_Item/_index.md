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





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[capacity]: #capacity
#### [capacity]
Some Product Items have capacity information such as RAM and bandwidth, and others. This provides the numerical representation of the capacity given in the description of this product item.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A product's description  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareGenericComponentId]: #hardwaregenericcomponentid
#### [hardwareGenericComponentId]
The hardware generic component model ID of the product.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A product's internal identification number  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemTaxCategoryId]: #itemtaxcategoryid
#### [itemTaxCategoryId]
A products tax category internal identification number  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
A unique key name for the product.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[longDescription]: #longdescription
#### [longDescription]
Detailed product description  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[softwareDescriptionId]: #softwaredescriptionid
#### [softwareDescriptionId]
The unique identifier of the SoftLayer_Software_Description tied to this item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[units]: #units
#### [units]
The unit of measurement that a product item is measured in.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[upgradeItemId]: #upgradeitemid
#### [upgradeItemId]
A products upgrade item's internal identification number  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[activePresaleEvents]: #activepresaleevents
#### [activePresaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**


</div>
<div class="prop-row">

-----
[activeUsagePrices]: #activeusageprices
#### [activeUsagePrices]
Active usage based prices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**


</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
The attribute values for a product item. These are additional properties that give extra information about the product being sold.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Attribute'>SoftLayer_Product_Item_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[availabilityAttributes]: #availabilityattributes
#### [availabilityAttributes]
Attributes that govern when an item may no longer be available.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Attribute'>SoftLayer_Product_Item_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[billingType]: #billingtype
#### [billingType]
An item's special billing type, if applicable.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[bundle]: #bundle
#### [bundle]
An item's included product item references. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item_Bundles objects. See the SoftLayer_Product_Item::bundleItems property for bundle of SoftLayer_Product_Item of objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Bundles'>SoftLayer_Product_Item_Bundles[] </a>**


</div>
<div class="prop-row">

-----
[bundleItems]: #bundleitems
#### [bundleItems]
An item's included products. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**


</div>
<div class="prop-row">

-----
[capacityMaximum]: #capacitymaximum
#### [capacityMaximum]
When the product capacity is best described as a range, this holds the ceiling of the range.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[capacityMinimum]: #capacityminimum
#### [capacityMinimum]
When the product capacity is best described as a range, this holds the floor of the range.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[capacityRestrictedProductFlag]: #capacityrestrictedproductflag
#### [capacityRestrictedProductFlag]
This flag indicates that this product is restricted by a capacity on a related product.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[categories]: #categories
#### [categories]
An item's associated item categories.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**


</div>
<div class="prop-row">

-----
[configurationTemplates]: #configurationtemplates
#### [configurationTemplates]
Some product items have configuration templates which can be used to during provisioning of that product.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template[] </a>**


</div>
<div class="prop-row">

-----
[conflicts]: #conflicts
#### [conflicts]
An item's conflicts. For example, McAfee LinuxShield cannot be ordered with Windows. It was not meant for that operating system and as such is a conflict.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**


</div>
<div class="prop-row">

-----
[coreRestrictedItemFlag]: #corerestricteditemflag
#### [coreRestrictedItemFlag]
This flag indicates that this product is restricted by the number of cores on the compute instance. This is deprecated. Use [SoftLayer_Product_Item::getCapacityRestrictedProductFlag]({{<ref "reference/services/SoftLayer_Product_Item/getCapacityRestrictedProductFlag">}})  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[downgradeItem]: #downgradeitem
#### [downgradeItem]
Some product items have a downgrade path. This is the first product item in the downgrade path.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[downgradeItems]: #downgradeitems
#### [downgradeItems]
Some product items have a downgrade path. These are those product items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**


</div>
<div class="prop-row">

-----
[globalCategoryConflicts]: #globalcategoryconflicts
#### [globalCategoryConflicts]
An item's category conflicts. For example, 10 Gbps redundant network functionality cannot be ordered with a secondary GPU and as such is a conflict.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**


</div>
<div class="prop-row">

-----
[hardwareGenericComponentModel]: #hardwaregenericcomponentmodel
#### [hardwareGenericComponentModel]
The generic hardware component that this item represents.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a>**


</div>
<div class="prop-row">

-----
[hideFromPortalFlag]: #hidefromportalflag
#### [hideFromPortalFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[ineligibleForAccountDiscountFlag]: #ineligibleforaccountdiscountflag
#### [ineligibleForAccountDiscountFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[inventory]: #inventory
#### [inventory]
DEPRECATED. An item's inventory status per datacenter.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Inventory'>SoftLayer_Product_Package_Inventory[] </a>**


</div>
<div class="prop-row">

-----
[isEngineeredServerProduct]: #isengineeredserverproduct
#### [isEngineeredServerProduct]
Flag to indicate the server product is engineered for a multi-server solution. (Deprecated)  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[itemCategory]: #itemcategory
#### [itemCategory]
An item's primary item category.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[localDiskFlag]: #localdiskflag
#### [localDiskFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[locationConflicts]: #locationconflicts
#### [locationConflicts]
An item's location conflicts. For example, Dual Path network functionality cannot be ordered in WDC and as such is a conflict.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a>**


</div>
<div class="prop-row">

-----
[minimumNvmeBays]: #minimumnvmebays
#### [minimumNvmeBays]
The minimum number of bays that support NVMe SSDs.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[nvmeDiskFlag]: #nvmediskflag
#### [nvmeDiskFlag]
Indicates whether an item is a NVMe SSD.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[objectStorageClusterGeolocationType]: #objectstorageclustergeolocationtype
#### [objectStorageClusterGeolocationType]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[objectStorageItemFlag]: #objectstorageitemflag
#### [objectStorageItemFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[objectStorageServiceClass]: #objectstorageserviceclass
#### [objectStorageServiceClass]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[packages]: #packages
#### [packages]
A collection of all the SoftLayer_Product_Package(s) in which this item exists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>**


</div>
<div class="prop-row">

-----
[physicalCoreCapacity]: #physicalcorecapacity
#### [physicalCoreCapacity]
The number of cores that a processor has.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[presaleEvents]: #presaleevents
#### [presaleEvents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a>**


</div>
<div class="prop-row">

-----
[prices]: #prices
#### [prices]
A product item's prices.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**


</div>
<div class="prop-row">

-----
[requirements]: #requirements
#### [requirements]
If an item must be ordered with another item, it will have a requirement item here.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Requirement'>SoftLayer_Product_Item_Requirement[] </a>**


</div>
<div class="prop-row">

-----
[rules]: #rules
#### [rules]
An item's rules. This includes the requirements and conflicts to resources that an item has.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule'>SoftLayer_Product_Item_Rule[] </a>**


</div>
<div class="prop-row">

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The SoftLayer_Software_Description tied to this item. This will only be populated for software items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**


</div>
<div class="prop-row">

-----
[taxCategory]: #taxcategory
#### [taxCategory]
An item's tax category, if applicable.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Tax_Category'>SoftLayer_Product_Item_Tax_Category </a>**


</div>
<div class="prop-row">

-----
[thirdPartyPolicyAssignments]: #thirdpartypolicyassignments
#### [thirdPartyPolicyAssignments]
Third-party policy assignments for this product.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Policy_Assignment'>SoftLayer_Product_Item_Policy_Assignment[] </a>**


</div>
<div class="prop-row">

-----
[thirdPartySupportVendor]: #thirdpartysupportvendor
#### [thirdPartySupportVendor]
The 3rd party vendor for a support subscription item. (Deprecated)  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[totalPhysicalCoreCapacity]: #totalphysicalcorecapacity
#### [totalPhysicalCoreCapacity]
The total number of physical processing cores (excluding virtual cores / hyperthreads) for this server.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[totalPhysicalCoreCount]: #totalphysicalcorecount
#### [totalPhysicalCoreCount]
Shows the total number of cores. This is deprecated. Use [SoftLayer_Product_Item::getCapacity]({{<ref "reference/services/SoftLayer_Product_Item/getCapacity">}}) for server products  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[totalProcessorCapacity]: #totalprocessorcapacity
#### [totalProcessorCapacity]
The total number of processors for this server.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[upgradeItem]: #upgradeitem
#### [upgradeItem]
Some product items have an upgrade path. This is the next product item in the upgrade path.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[upgradeItems]: #upgradeitems
#### [upgradeItems]
Some product items have an upgrade path. These are those upgrade product items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**


</div>

## Count
<div class="prop-row">

-----
[activePresaleEventCount]: #activepresaleeventcount
#### [activePresaleEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeUsagePriceCount]: #activeusagepricecount
#### [activeUsagePriceCount]
A count of active usage based prices.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of the attribute values for a product item. These are additional properties that give extra information about the product being sold.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[availabilityAttributeCount]: #availabilityattributecount
#### [availabilityAttributeCount]
A count of attributes that govern when an item may no longer be available.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bundleCount]: #bundlecount
#### [bundleCount]
A count of an item's included product item references. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item_Bundles objects. See the SoftLayer_Product_Item::bundleItems property for bundle of SoftLayer_Product_Item of objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bundleItemCount]: #bundleitemcount
#### [bundleItemCount]
A count of an item's included products. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item objects.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[categoryCount]: #categorycount
#### [categoryCount]
A count of an item's associated item categories.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[configurationTemplateCount]: #configurationtemplatecount
#### [configurationTemplateCount]
A count of some product items have configuration templates which can be used to during provisioning of that product.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downgradeItemCount]: #downgradeitemcount
#### [downgradeItemCount]
A count of some product items have a downgrade path. These are those product items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[inventoryCount]: #inventorycount
#### [inventoryCount]
A count of dEPRECATED. An item's inventory status per datacenter.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[packageCount]: #packagecount
#### [packageCount]
A count of a collection of all the SoftLayer_Product_Package(s) in which this item exists.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[presaleEventCount]: #presaleeventcount
#### [presaleEventCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[priceCount]: #pricecount
#### [priceCount]
A count of a product item's prices.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of an item's rules. This includes the requirements and conflicts to resources that an item has.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[thirdPartyPolicyAssignmentCount]: #thirdpartypolicyassignmentcount
#### [thirdPartyPolicyAssignmentCount]
A count of third-party policy assignments for this product.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[upgradeItemCount]: #upgradeitemcount
#### [upgradeItemCount]
A count of some product items have an upgrade path. These are those upgrade product items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


