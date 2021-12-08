---
title: "getObjectTypes"
description: "This method returns a collection of [SoftLayer_Container_Search_ObjectType]({{<ref 'reference/datatypes/SoftLayer_Contai... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Search"
classes:
    - "SoftLayer_Search"
aliases:
    - "/reference/services/softlayer_search/getObjectTypes"
---
# [SoftLayer_Search](/reference/services/SoftLayer_Search)::getObjectTypes


Return a collection of indexed object types. 


## Overview 
This method returns a collection of [SoftLayer_Container_Search_ObjectType]({{<ref "reference/datatypes/SoftLayer_Container_Search_ObjectType">}}) containers that specify which indexed object types and properties are exposed for the current user.  These object types can be used to discover searchable data and to create or validate object index search strings. 



Refer to the [SoftLayer_Search::search]({{<ref "reference/services/SoftLayer_Search/search">}}) and [SoftLayer_Search::advancedSearch]({{<ref "reference/services/SoftLayer_Search/advancedSearch">}}) methods for information on using object types and properties in search strings. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Search_ObjectType'>SoftLayer_Container_Search_ObjectType[] </a>


### Associated Methods

*  [SoftLayer_Search::search](/reference/services/SoftLayer_Search/search )
*  [SoftLayer_Search::advancedSearch](/reference/services/SoftLayer_Search/advancedSearch )




