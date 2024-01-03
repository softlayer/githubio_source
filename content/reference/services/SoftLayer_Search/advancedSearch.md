---
title: "advancedSearch"
description: "This method allows for searching for SoftLayer resources by simple terms and operators.  Fields that are used for searching will be available at sldn.softlayer.com. It returns a collection or array of [SoftLayer_Container_Search_Result](/reference/datatypes/SoftLayer_Container_Search_Result) objects that have search metadata for each result and the resulting resource found. 

The advancedSearch() method recognizes the special <code>_objectType:</code></b> quantifier in search strings.  See the documentation for the [SoftLayer_Search::search](/reference/services/SoftLayer_Search/search) method on how to restrict searches using object types. 

The advancedSearch() method recognizes [SoftLayer_Container_Search_ObjectType_Property](/reference/datatypes/SoftLayer_Container_Search_ObjectType_Property), which can also be used to limit searches.  Example: 

<code>_objectType:Type_1 propertyA:</code><i><code>value</code></i> 

A search string can specify multiple properties, separated with spaces. Example: 

<code>_objectType:Type_1 propertyA:</code><i><code>value</code></i> <code>propertyB:</code><i><code>value</code></i> 

A collection of available object types and their properties can be retrieved by calling the [SoftLayer_Search::getObjectTypes](/reference/services/SoftLayer_Search/getObjectTypes) method. 


#### Exact Match on Text Fields
To enforce an exact match on text fields, encapsulate the term in double quotes. For example, given a set of device host names: 

<ul> <li>baremetal-a</li> <li>baremetal-b</li> <li>a-virtual-guest</li> <li>b-virtual-guest</li> <li>edge-router</li> </ul> 

An exact search (double-quote) for 'baremetal-a' will return only the exact match of <u>baremetal-a</u>. 

A fuzzy search (no double-quote) for baremetal-a will return <u>baremetal</u>-<u>a</u>, <u>baremetal</u>-b, <u>a</u>-virtu<u>a</u>l-guest, b-virtu<u>a</u>l-guest but will omit edge-router. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Search"
classes:
    - "SoftLayer_Search"
type: "reference"
layout: "method"
mainService : "SoftLayer_Search"
---

# [REST Example](#advancedSearch-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#advancedSearch-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch'
```
