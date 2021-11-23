---
title: "editObject"
description: "Edit this group. The name can be edited at any time. The minimumMemberCount and maximumMemberCount fields can also be edited at any time provided they don't force a scale up or scale down to bring the group into the proper range. Otherwise, the group's status must be active to set those fields. If the group member count is less than the new minimumMemberCount and the group is active, it will scale up the group members to reach the new minimum. Similarly if the group member count is greater than the new maximumMemberCount and the group is active, it will scale down the group members to reach the new maximum. 

When editing an active group, a special field can be provided: desiredMemberCount. When given, the group members are automatically scaled up or down to reach that number. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "editObject"
type: "reference"
layout: "method"
mainService : "SoftLayer_Scale_Group"
---
