---
title: "SoftLayer_User_Customer"
description: "Every SoftLayer account has one or more portal users which are defined by the SoftLayer_User_Customer service. Every SoftLayer customer account has a master user account whose name corresponds to their account id preceded by the letters 'SL'. Users exist in a parent-child relationship. Child users inherit the properties and permissions of their parent user while conversely a user may have more than one child users. 

API users have full access to their own portal user account and they could also have access to other users under their SoftLayer customer account, if they have 'Manage Users' permission in the customer portal. 

There are two relational properties that contain the permissions assigned to a customer user; permissions and actions.  These are simply two different representations of the same information. The permissions ORM key creates a SoftLayer_Container_Collection_Permissions collection from SoftLayer_User_Customer_CustomerPermission_Permission objects which is populated from the same data source as the actions ORM key which creates a SoftLayer_Container_Collection_Permissions collection from SoftLayer_User_Permission_Action objects. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_User_Customer"
---
