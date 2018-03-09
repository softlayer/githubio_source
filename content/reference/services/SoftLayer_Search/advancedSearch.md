---
title: "advancedSearch"
description: "This method allows for searching for SoftLayer resources by simple terms and operators.  Fields that are used for search... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Search"
classes:
    - "SoftLayer_Search"
---
# [SoftLayer_Search](/reference/services/SoftLayer_Search)::advancedSearch

Search for SoftLayer Resources by simple terms.


## Overview 
This method allows for searching for SoftLayer resources by simple terms and operators.  Fields that are used for searching will be available at sldn.softlayer.com. It returns a collection or array of <b>[[SoftLayer_Container_Search_Result (type)|SoftLayer_Container_Search_Result]]</b> objects that have search metadata for each result and the resulting resource found. 

The advancedSearch() method recognizes the special <b><code>_objectType:</code></b> quantifier in search strings.  See the documentation for the <b>[[SoftLayer_Search/search|search()]]</b> method on how to restrict searches using object types. 

The advancedSearch() method recognizes <b>[[SoftLayer_Container_Search_ObjectType_Property (type)|object properties]]</b>, which can also be used to limit searches.  Example: 

<code>_objectType:Type_1 propertyA:</code><i><code>value</code></i> 

A search string can specify multiple properties, separated with spaces. Example: 

<code>_objectType:Type_1 propertyA:</code><i><code>value</code></i> <code>propertyB:</code><i><code>value</code></i> 

A collection of available object types and their properties can be retrieved by calling the <b>[[SoftLayer_Search/getObjectTypes|getObjectTypes()]]</b> method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|searchString| string| A string with search terms.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Search_Result'>SoftLayer_Container_Search_Result[] </a>

