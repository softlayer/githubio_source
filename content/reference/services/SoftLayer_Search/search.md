---
title: "search"
description: "This method allows for searching for SoftLayer resources by simple phrase. It returns a collection or array of [SoftLayer_Container_Search_Result](/reference/datatypes/SoftLayer_Container_Search_Result) objects that have search metadata for each result and the resulting resource found. 

This method recognizes the special <b><code>_objectType:</code></b> quantifier in search strings.  This quantifier can be used to restrict a search to specific object types.  Example usage: 

<code>_objectType:Type_1 </code><i><code>(other search terms...)</code></i> 

A search string can specify multiple object types, separated by commas (no spaces are permitted between the type names).  Example: 

<code>_objectType:Type_1,Type_2,Type_3 </code><i><code>(other search terms...)</code></i> 

If the list of object types is prefixed with a hyphen or minus sign (-), then the specified types are excluded from the search.  Example: 

<code>_objectType:-Type_4,Type_5 </code><i><code>(other search terms...)</code></i> 

A collection of available object types can be retrieved by calling the [SoftLayer_Search::getObjectTypes](/reference/services/SoftLayer_Search/getObjectTypes) method. 


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

# [REST Example](#search-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#search-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/search'
```
