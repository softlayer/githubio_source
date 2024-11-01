---
title: "SoftLayer_User_Permission_Group"
description: "The SoftLayer_User_Permission_Group class is one of several classes that make up the customer permission system.  It is a role-based system that includes defined actions which can be 'grouped' together using a SoftLayer_User_Permission_Group class. These groups of actions are then used to define roles, and the roles are assigned to users.  The SoftLayer_User_Permission_Group is also used to track the resources or account devices to which a user has been granted access. The types of resources that users can be granted access is defined in [SoftLayer_User_Permission_Resource_Type](/reference/datatypes/SoftLayer_User_Permission_Resource_Type). 

When a [SoftLayer_User_Customer](/reference/datatypes/SoftLayer_User_Customer) is created, a SoftLayer_User_Permission_Group and SoftLayer_User_Permission_Role is created specifically for the user with a group type of SYSTEM.  When the UI is used to alter the permissions of a customer user, the actions are added or removed from this group.  The api can not be used to alter the permissions in this group.  If an account wants to create their own unique permission groups and roles, the UI can not be used to manage them. 

This is also true for device access.  Either, the UI can be used to track the devices to which users are granted access which will use the SYSTEM group, or the api can be used, making the UI information inaccurate. 

User Customers can be assigned to multiple roles but it is recommended to either use the UI for managing account users permissions or only use the api.  Mixing the two will lead to confusing results as the UI will not show any permissions assigned to a user via a customer created role/group combination. 

Proceed with caution. 

One or more [SoftLayer_User_Permission_Action](/reference/datatypes/SoftLayer_User_Permission_Action) are assigned to one or more SoftLayer_User_Permission_Group Objects. One ore more SoftLayer_User_Permission_Group objects can be linked to a [SoftLayer_User_Permission_Role](/reference/datatypes/SoftLayer_User_Permission_Role). A single SoftLayer_User_Permission_Group object can be linked to multiple SoftLayer_User_Permission_Role objects. The [SoftLayer_User_Permission_Role](/reference/datatypes/SoftLayer_User_Permission_Role) is assigned to one or more [SoftLayer_User_Customer](/reference/datatypes/SoftLayer_User_Customer). 

The [SoftLayer_User_Permission_Action](/reference/datatypes/SoftLayer_User_Permission_Action) class defines the permissions that are required in order for a [SoftLayer_User_Customer](/reference/datatypes/SoftLayer_User_Customer) to perform certain actions within IMS. 

Resources belonging to the user's account can also be linked to permission groups. See [SoftLayer_User_Permission_Resource_Type](/reference/datatypes/SoftLayer_User_Permission_Resource_Type). "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
type: "reference"
layout: "service"
mainService : "SoftLayer_User_Permission_Group"
---
