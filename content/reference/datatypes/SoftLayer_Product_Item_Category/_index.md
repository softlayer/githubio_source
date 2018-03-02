---
title: "SoftLayer_Product_Item_Category"
description: "The SoftLayer_Product_Item_Category data type contains general category information for prices."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Category"
---

# SoftLayer_Product_Item_Category
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Category' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Item_Category data type contains general category information for prices. 





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
            <span class='views-field-title'><a href="#categoryCode" name=categoryCode>categoryCode</a></span>
            <div class='views-field-body'>The code used to identify this category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>identifier for category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The friendly, descriptive name of the category as seen on the order forms and on invoices. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#quantityLimit" name=quantityLimit>quantityLimit</a></span>
            <div class='views-field-body'>Quantity that can be ordered. If 0, it will inherit the quantity from the server quantity ordered. Otherwise it can be specified with the order separately </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sortOrder" name=sortOrder>sortOrder</a></span>
            <div class='views-field-body'>The sort order of the category. It may be used to affect the order in which the category may appear in lists (on order forms and invoices). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItems" name=billingItems>billingItems</a></span>
            <div class='views-field-body'>The billing items associated with an account that share a category code with an item category's category code. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#group" name=group>group</a></span>
            <div class='views-field-body'>This invoice item's "item category group".  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Group'>SoftLayer_Product_Item_Category_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#groups" name=groups>groups</a></span>
            <div class='views-field-body'>A collection of service offering category groups. Each group contains a collection of items associated with this category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Item_Category_Group'>SoftLayer_Product_Package_Item_Category_Group[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderOptions" name=orderOptions>orderOptions</a></span>
            <div class='views-field-body'>Any unique options associated with an item category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Order_Option_Type'>SoftLayer_Product_Item_Category_Order_Option_Type[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageConfigurations" name=packageConfigurations>packageConfigurations</a></span>
            <div class='views-field-body'>A list of configuration available in this category.' </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration'>SoftLayer_Product_Package_Order_Configuration[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#presetConfigurations" name=presetConfigurations>presetConfigurations</a></span>
            <div class='views-field-body'>A list of preset configurations this category is used in.' </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Configuration'>SoftLayer_Product_Package_Preset_Configuration[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#questionReferences" name=questionReferences>questionReferences</a></span>
            <div class='views-field-body'>The question references that are associated with an item category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question_Xref'>SoftLayer_Product_Item_Category_Question_Xref[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#questions" name=questions>questions</a></span>
            <div class='views-field-body'>The questions that are associated with an item category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question'>SoftLayer_Product_Item_Category_Question[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItemCount" name=billingItemCount>billingItemCount</a></span>
            <div class='views-field-body'>A count of the billing items associated with an account that share a category code with an item category's category code. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#groupCount" name=groupCount>groupCount</a></span>
            <div class='views-field-body'>A count of a collection of service offering category groups. Each group contains a collection of items associated with this category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderOptionCount" name=orderOptionCount>orderOptionCount</a></span>
            <div class='views-field-body'>A count of any unique options associated with an item category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageConfigurationCount" name=packageConfigurationCount>packageConfigurationCount</a></span>
            <div class='views-field-body'>A count of a list of configuration available in this category.' </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#presetConfigurationCount" name=presetConfigurationCount>presetConfigurationCount</a></span>
            <div class='views-field-body'>A count of a list of preset configurations this category is used in.' </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#questionCount" name=questionCount>questionCount</a></span>
            <div class='views-field-body'>A count of the questions that are associated with an item category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#questionReferenceCount" name=questionReferenceCount>questionReferenceCount</a></span>
            <div class='views-field-body'>A count of the question references that are associated with an item category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


