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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemId" name=itemId>itemId</a></span>
            <div class='views-field-body'>The unique identifier of the item that the rule applies to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#message" name=message>message</a></span>
            <div class='views-field-body'>An optional message shown for when the rule is found to be invalid when ordering. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#operation" name=operation>operation</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageId" name=packageId>packageId</a></span>
            <div class='views-field-body'>The unique identifier of the service offering that is associated with the rule. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#typeId" name=typeId>typeId</a></span>
            <div class='views-field-body'>The unique identifier of the type of resource rule. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#item" name=item>item</a></span>
            <div class='views-field-body'>The product item that a rule applies to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemCategoryResources" name=itemCategoryResources>itemCategoryResources</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemResources" name=itemResources>itemResources</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationResources" name=locationResources>locationResources</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#package" name=package>package</a></span>
            <div class='views-field-body'>The package that a rule is applicable to when ordering. If no package exists, the rule applies to any package. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#permissionResources" name=permissionResources>permissionResources</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resources" name=resources>resources</a></span>
            <div class='views-field-body'>Resources for this rule that are validated when ordering. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Resource'>SoftLayer_Product_Item_Rule_Resource[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>The type a rule is. The type affects how the rule is validated when ordering. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Rule_Type'>SoftLayer_Product_Item_Rule_Type </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemCategoryResourceCount" name=itemCategoryResourceCount>itemCategoryResourceCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemResourceCount" name=itemResourceCount>itemResourceCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationResourceCount" name=locationResourceCount>locationResourceCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#permissionResourceCount" name=permissionResourceCount>permissionResourceCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceCount" name=resourceCount>resourceCount</a></span>
            <div class='views-field-body'>A count of resources for this rule that are validated when ordering. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


