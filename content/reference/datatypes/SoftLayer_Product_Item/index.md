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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capacity" name=capacity>capacity</a></span>
            <div class='views-field-body'>Some Product Items have capacity information such as RAM and bandwidth, and others. This provides the numerical representation of the capacity given in the description of this product item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>A product's description </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A product's internal identification number </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemTaxCategoryId" name=itemTaxCategoryId>itemTaxCategoryId</a></span>
            <div class='views-field-body'>A products tax category internal identification number </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>A unique key name for the product. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#longDescription" name=longDescription>longDescription</a></span>
            <div class='views-field-body'>Detailed product description </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#softwareDescriptionId" name=softwareDescriptionId>softwareDescriptionId</a></span>
            <div class='views-field-body'>The unique identifier of the SoftLayer_Software_Description tied to this item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#units" name=units>units</a></span>
            <div class='views-field-body'>The unit of measurement that a product item is measured in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#upgradeItemId" name=upgradeItemId>upgradeItemId</a></span>
            <div class='views-field-body'>A products upgrade item's internal identification number </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activePresaleEvents" name=activePresaleEvents>activePresaleEvents</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeUsagePrices" name=activeUsagePrices>activeUsagePrices</a></span>
            <div class='views-field-body'>Active usage based prices. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attributes" name=attributes>attributes</a></span>
            <div class='views-field-body'>The attribute values for a product item. These are additional properties that give extra information about the product being sold. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Attribute'>SoftLayer_Product_Item_Attribute[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#availabilityAttributes" name=availabilityAttributes>availabilityAttributes</a></span>
            <div class='views-field-body'>Attributes that govern when an item may no longer be available. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Attribute'>SoftLayer_Product_Item_Attribute[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingType" name=billingType>billingType</a></span>
            <div class='views-field-body'>An item's special billing type, if applicable. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bundle" name=bundle>bundle</a></span>
            <div class='views-field-body'>An item's included product item references. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item_Bundles objects. See the SoftLayer_Product_Item::bundleItems property for bundle of SoftLayer_Product_Item of objects. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Bundles'>SoftLayer_Product_Item_Bundles[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bundleItems" name=bundleItems>bundleItems</a></span>
            <div class='views-field-body'>An item's included products. Some items have other items included in them that we specifically detail. They are here called Bundled Items. An example is Plesk unlimited. It as a bundled item labeled 'SiteBuilder'. These are the SoftLayer_Product_Item objects. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capacityMaximum" name=capacityMaximum>capacityMaximum</a></span>
            <div class='views-field-body'>When the product capacity is best described as a range, this holds the ceiling of the range. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capacityMinimum" name=capacityMinimum>capacityMinimum</a></span>
            <div class='views-field-body'>When the product capacity is best described as a range, this holds the floor of the range. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capacityRestrictedProductFlag" name=capacityRestrictedProductFlag>capacityRestrictedProductFlag</a></span>
            <div class='views-field-body'>This flag indicates that this product is restricted by a capacity on a related product. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#categories" name=categories>categories</a></span>
            <div class='views-field-body'>An item's associated item categories. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#configurationTemplates" name=configurationTemplates>configurationTemplates</a></span>
            <div class='views-field-body'>Some product items have configuration templates which can be used to during provisioning of that product. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#conflicts" name=conflicts>conflicts</a></span>
            <div class='views-field-body'>An item's conflicts. For example, McAfee LinuxShield cannot be ordered with Windows. It was not meant for that operating system and as such is a conflict. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#coreRestrictedItemFlag" name=coreRestrictedItemFlag>coreRestrictedItemFlag</a></span>
            <div class='views-field-body'>This flag indicates that this product is restricted by the number of cores on the compute instance. This is deprecated. Use [[SoftLayer_Product_Item/getCapacityRestrictedProductFlag|getCapacityRestrictedProductFlag]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downgradeItem" name=downgradeItem>downgradeItem</a></span>
            <div class='views-field-body'>Some product items have a downgrade path. This is the first product item in the downgrade path. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downgradeItems" name=downgradeItems>downgradeItems</a></span>
            <div class='views-field-body'>Some product items have a downgrade path. These are those product items. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#globalCategoryConflicts" name=globalCategoryConflicts>globalCategoryConflicts</a></span>
            <div class='views-field-body'>An item's category conflicts. For example, 10 Gbps redundant network functionality cannot be ordered with a secondary GPU and as such is a conflict. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareGenericComponentModel" name=hardwareGenericComponentModel>hardwareGenericComponentModel</a></span>
            <div class='views-field-body'>The generic hardware component that this item represents. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hideFromPortalFlag" name=hideFromPortalFlag>hideFromPortalFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#inventory" name=inventory>inventory</a></span>
            <div class='views-field-body'>DEPRECATED. An item's inventory status per datacenter. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Inventory'>SoftLayer_Product_Package_Inventory[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isEngineeredServerProduct" name=isEngineeredServerProduct>isEngineeredServerProduct</a></span>
            <div class='views-field-body'>Flag to indicate the server product is engineered for a multi-server solution. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemCategory" name=itemCategory>itemCategory</a></span>
            <div class='views-field-body'>An item's primary item category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#localDiskFlag" name=localDiskFlag>localDiskFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationConflicts" name=locationConflicts>locationConflicts</a></span>
            <div class='views-field-body'>An item's location conflicts. For example, Dual Path network functionality cannot be ordered in WDC and as such is a conflict. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Resource_Conflict'>SoftLayer_Product_Item_Resource_Conflict[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#objectStorageClusterGeolocationType" name=objectStorageClusterGeolocationType>objectStorageClusterGeolocationType</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#objectStorageItemFlag" name=objectStorageItemFlag>objectStorageItemFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#objectStorageServiceClass" name=objectStorageServiceClass>objectStorageServiceClass</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packages" name=packages>packages</a></span>
            <div class='views-field-body'>A collection of all the SoftLayer_Product_Package(s) in which this item exists. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#physicalCoreCapacity" name=physicalCoreCapacity>physicalCoreCapacity</a></span>
            <div class='views-field-body'>The number of cores that a processor has. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#presaleEvents" name=presaleEvents>presaleEvents</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#prices" name=prices>prices</a></span>
            <div class='views-field-body'>A product item's prices. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#requirements" name=requirements>requirements</a></span>
            <div class='views-field-body'>If an item must be ordered with another item, it will have a requirement item here. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Requirement'>SoftLayer_Product_Item_Requirement[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#rules" name=rules>rules</a></span>
            <div class='views-field-body'>An item's rules. This includes the requirements and conflicts to resources that an item has. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule'>SoftLayer_Product_Item_Rule[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#softwareDescription" name=softwareDescription>softwareDescription</a></span>
            <div class='views-field-body'>The SoftLayer_Software_Description tied to this item. This will only be populated for software items. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#taxCategory" name=taxCategory>taxCategory</a></span>
            <div class='views-field-body'>An item's tax category, if applicable. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Tax_Category'>SoftLayer_Product_Item_Tax_Category </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#thirdPartyPolicyAssignments" name=thirdPartyPolicyAssignments>thirdPartyPolicyAssignments</a></span>
            <div class='views-field-body'>Third-party policy assignments for this product. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Policy_Assignment'>SoftLayer_Product_Item_Policy_Assignment[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#thirdPartySupportVendor" name=thirdPartySupportVendor>thirdPartySupportVendor</a></span>
            <div class='views-field-body'>The 3rd party vendor for a support subscription item. (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalPhysicalCoreCapacity" name=totalPhysicalCoreCapacity>totalPhysicalCoreCapacity</a></span>
            <div class='views-field-body'>The total number of physical processing cores (excluding virtual cores / hyperthreads) for this server. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalPhysicalCoreCount" name=totalPhysicalCoreCount>totalPhysicalCoreCount</a></span>
            <div class='views-field-body'>Shows the total number of cores. This is deprecated. Use [[SoftLayer_Product_Item/getCapacity|getCapacity]] for guest_core products and [[SoftLayer_Product_Item/getTotalPhysicalCoreCapacity|getTotalPhysicalCoreCapacity]] for server products </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalProcessorCapacity" name=totalProcessorCapacity>totalProcessorCapacity</a></span>
            <div class='views-field-body'>The total number of processors for this server. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#upgradeItem" name=upgradeItem>upgradeItem</a></span>
            <div class='views-field-body'>Some product items have an upgrade path. This is the next product item in the upgrade path. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#upgradeItems" name=upgradeItems>upgradeItems</a></span>
            <div class='views-field-body'>Some product items have an upgrade path. These are those upgrade product items. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p></div>
        </div>
            </div>
</div>


