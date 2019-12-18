---
title: "SoftLayer_Product_Item_Category_Question_Xref"
description: "The SoftLayer_Product_Item_Category_Question_Xref data type represents a link between an item category and an item categ... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Category_Question_Xref"
---

# SoftLayer_Product_Item_Category_Question_Xref
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question_Xref' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Item_Category_Question_Xref data type represents a link between an item category and an item category question.  It also contains a 'required' field that designates if the question is required to be answered for the given item category. 





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
[id]: #id
#### [id]
Identifier for category question xref record.  
<span class="type-label">Type: </span>**integer**

-----
[itemCategoryId]: #itemcategoryid
#### [itemCategoryId]
Identifier for item category.  
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
Identifier for the question.  
<span class="type-label">Type: </span>**integer**

-----
[questionId]: #questionid
#### [questionId]
Identifier for the question.  
<span class="type-label">Type: </span>**integer**

-----
[required]: #required
#### [required]
Flag to indicate whether an answer is required for the question..  
<span class="type-label">Type: </span>**boolean**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[itemCategory]: #itemcategory
#### [itemCategory]
The product item category that this reference points to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**

-----
[question]: #question
#### [question]
The item category question that this reference points to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question'>SoftLayer_Product_Item_Category_Question </a>**


## Count
</div>


