---
title: "SoftLayer_Product_Item_Rule"
description: "The item rule data type represents a rule that must be followed when the item assigned to the rule is ordered. The type... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Rule"
---

# SoftLayer_Product_Item_Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The item rule data type represents a rule that must be followed when the item assigned to the rule is ordered. The type and operation applied to the resources of the rule will affect how the rule is checked during ordering. 





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
[itemId]: #itemid
#### [itemId]
The unique identifier of the item that the rule applies to.  
<span class="type-label">Type: </span>**integer**

-----
[message]: #message
#### [message]
An optional message shown for when the rule is found to be invalid when ordering.  
<span class="type-label">Type: </span>**string**

-----
[operation]: #operation
#### [operation]
  
<span class="type-label">Type: </span>**string**

-----
[packageId]: #packageid
#### [packageId]
The unique identifier of the service offering that is associated with the rule.  
<span class="type-label">Type: </span>**integer**

-----
[typeId]: #typeid
#### [typeId]
The unique identifier of the type of resource rule.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[item]: #item
#### [item]
The product item that a rule applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[itemCategoryResources]: #itemcategoryresources
#### [itemCategoryResources]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a>**

-----
[itemResources]: #itemresources
#### [itemResources]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a>**

-----
[locationResources]: #locationresources
#### [locationResources]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a>**

-----
[package]: #package
#### [package]
The package that a rule is applicable to when ordering. If no package exists, the rule applies to any package.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**

-----
[permissionResources]: #permissionresources
#### [permissionResources]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a>**

-----
[resources]: #resources
#### [resources]
Resources for this rule that are validated when ordering.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a>**

-----
[type]: #type
#### [type]
The type a rule is. The type affects how the rule is validated when ordering.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Type'>SoftLayer_Product_Item_Rule_Type </a>**


## Count

-----
[itemCategoryResourceCount]: #itemcategoryresourcecount
#### [itemCategoryResourceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[itemResourceCount]: #itemresourcecount
#### [itemResourceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[locationResourceCount]: #locationresourcecount
#### [locationResourceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[permissionResourceCount]: #permissionresourcecount
#### [permissionResourceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[resourceCount]: #resourcecount
#### [resourceCount]
A count of resources for this rule that are validated when ordering.   
<span class="type-label">Type: </span>**unsigned long**

</div>


