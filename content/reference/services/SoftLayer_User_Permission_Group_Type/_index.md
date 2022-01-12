---
title: "SoftLayer_User_Permission_Group_Type"
description: "The SoftLayer_User_Permission_Group_Type class is one of several classes that make up the customer permission system.  This class defines the valid group types.  The SYSTEM group type is reserved for internal use. 

It is a role-based system that includes defined actions which can be 'grouped' together using a SoftLayer_User_Permission_Group class. These groups of actions are then used to define roles, and the roles are assigned to users. 

When a [SoftLayer_User_Customer](/reference/datatypes/SoftLayer_User_Customer) is created, a SoftLayer_User_Permission_Group and SoftLayer_User_Permission_Role is created specifically for the user with a group type of SYSTEM.  When the UI is used to alter the permissions of a customer user, the actions are added or removed from this group.  The api can not be used to alter the permissions in this group.  If an account wants to create their own unique permission groups and roles, the UI can not be used to manage them. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group_Type"
type: "reference"
layout: "service"
mainService : "SoftLayer_User_Permission_Group_Type"
---
