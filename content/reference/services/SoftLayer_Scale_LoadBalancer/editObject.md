---
title: "editObject"
description: "Edit this load balancer configuration. Note, this does not affect existing scaled members. Once edited however, future s... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_LoadBalancer"
aliases:
    - "/reference/services/softlayer_scale_loadbalancer/editObject"
---
# [SoftLayer_Scale_LoadBalancer](/reference/services/SoftLayer_Scale_LoadBalancer)::editObject

Edit this load balancer configuration. 


## Overview 
Edit this load balancer configuration. Note, this does not affect existing scaled members. Once edited however, future scaled members will be load balanced with this configuration. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer </a>| A skeleton SoftLayer_Scale_LoadBalancer object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Scale_LoadBalancerInitParameters


### Return Values
* boolean




