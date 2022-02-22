---
title: "SoftLayer_Scale_Group_Status"
description: "The status of a scale group. This status affects what actions can occur on a group. The values can be: 


* ACTIVE - There are no actions execution for any members or assets of any type.
* BUSY - There is an action executing for one of the members or assets, but that action is not a scaling action.
* SCALING - At least one of the members is in the process of being created or destroyed.
* SUSPENDED - The group has been placed in a suspended state by a user. It may only be resumed by a user. While in a
suspended state, a scale group cannot have any members added or deleted, or change settings of that group that would invoke such an action. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group_Status"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Scale_Group_Status"
---
