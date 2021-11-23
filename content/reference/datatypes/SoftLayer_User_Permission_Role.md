---
title: "SoftLayer_User_Permission_Role"
description: "The SoftLayer_User_Permission_Role class is one of several classes that make up the customer permission system.  The system is a role-based system that includes defined actions which can be 'grouped' together using a SoftLayer_User_Permission_Group class.  These groups of actions are then used to define roles, and the roles are assigned to users. 

When a [[SoftLayer_User_Customer]] is created, a SoftLayer_User_Permission_Role is created for the user with a group type of SYSTEM.  This role is linked to the SYSTEM SoftLayer_User_Permission_Group that was also created specifically for this user.  When the UI is used to alter the permissions of a customer user, the actions are added or removed from this group.  The api can not be used to alter the permissions in this group.  If an account wants to create their own unique permission groups and roles, the UI can not be used to manage them. 

User Customers can be assigned to multiple roles but it is recommended to either use the UI for managing account users permissions or only use the api.  Mixing the two will lead to confusing results as the UI will not show any permissions assigned to a user via a customer created role/group combination. 

Proceed with caution. 

One or more [[SoftLayer_User_Permission_Action]] are assigned to one or more [[SoftLayer_User_Permission_Group]] Objects. One ore more SoftLayer_User_Permission_Group objects can be linked to a [[SoftLayer_User_Permission_Role]]. A single SoftLayer_User_Permission_Group object can be linked to multiple SoftLayer_User_Permission_Role objects. The SoftLayer_User_Permission_Role is assigned to one or more [[SoftLayer_User_Customer]].  A single SoftLayer_User_Customer can be assigned to one or more roles. 

The SoftLayer_User_Permission_Action class defines the permissions that are required in order for a SoftLayer_User_Customer to perform certain actions within IMS. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_User_Permission_Role"
---
