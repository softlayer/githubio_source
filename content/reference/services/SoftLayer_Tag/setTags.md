---
title: "setTags"
description: "Tag an object by passing in one or more tags separated by a comma. Tag references are cleared out every time this method... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Tag"
classes:
    - "SoftLayer_Tag"
aliases:
    - "/reference/services/softlayer_tag/setTags"
---
# [SoftLayer_Tag](/reference/services/SoftLayer_Tag)::setTags


Set the tags for a given object.


## Overview 
Tag an object by passing in one or more tags separated by a comma. Tag references are cleared out every time this method is called. If your object is already tagged you will need to pass the current tags along with any new ones. To remove all tag references pass an empty string. To remove one or more tags omit them from the tag list. The characters permitted are A-Z, 0-9, whitespace, _ (underscore), - (hypen), . (period), and : (colon). All other characters will be stripped away. You must pass 3 string arguments into this method or you will receive an exception. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|tags| string| List of tags.|
|keyName| string| Key name of a tag type.|
|resourceTableId| integer| $resourceTableId ID of the object being tagged.|


### Required Headers
* authenticate


### Return Values
* boolean




