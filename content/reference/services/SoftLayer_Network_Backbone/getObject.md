---
title: "getObject"
description: "Retrieve an individual SoftLayer_Network_Backbone record. Use the getAllBackbones() method to retrieve a list of all Sof... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Backbone"
aliases:
    - "/reference/services/softlayer_network_backbone/getObject"
---
# [SoftLayer_Network_Backbone](/reference/services/SoftLayer_Network_Backbone)::getObject


Retrieve a SoftLayer_Network_Backbone record.


## Overview 
Retrieve an individual SoftLayer_Network_Backbone record. Use the getAllBackbones() method to retrieve a list of all SoftLayer network backbones.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_BackboneInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_BackboneObjectMask
* SoftLayer_Network_BackboneObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Backbone'>SoftLayer_Network_Backbone </a>


### Associated Methods

*  [SoftLayer_Network_Backbone::getAllBackbones](/reference/services/SoftLayer_Network_Backbone/getAllBackbones )



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 



