---
title: "search"
description: "This method allows for searching for SoftLayer resources by simple phrase. It returns a collection or array of <b>[[Soft... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Search"
classes:
    - "SoftLayer_Search"
aliases:
    - "/reference/services/softlayer_search/search"
---
# [SoftLayer_Search](/reference/services/SoftLayer_Search)::search

Search for SoftLayer Resources by simple phrase.


## Overview 
This method allows for searching for SoftLayer resources by simple phrase. It returns a collection or array of <b>[[SoftLayer_Container_Search_Result (type)|SoftLayer_Container_Search_Result]]</b> objects that have search metadata for each result and the resulting resource found. 

This method recognizes the special <b><code>_objectType:</code></b> quantifier in search strings.  This quantifier can be used to restrict a search to specific object types.  Example usage: 

<code>_objectType:Type_1 </code><i><code>(other search terms...)</code></i> 

A search string can specify multiple object types, separated by commas (no spaces are permitted between the type names).  Example: 

<code>_objectType:Type_1,Type_2,Type_3 </code><i><code>(other search terms...)</code></i> 

If the list of object types is prefixed with a hyphen or minus sign (-), then the specified types are excluded from the search.  Example: 

<code>_objectType:-Type_4,Type_5 </code><i><code>(other search terms...)</code></i> 

A collection of available object types can be retrieved by calling the <b>[[SoftLayer_Search/getObjectTypes|getObjectTypes()]]</b> method. 

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

