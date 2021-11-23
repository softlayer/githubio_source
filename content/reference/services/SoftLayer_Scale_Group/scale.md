---
title: "scale"
description: "Scale this group up or down by the amount given. If the number is negative, the given amount of guest members are removed. Similarly, if the number is positive, the given amount of guest members are added. Note, this call will add or remove as much as asked for, but will NOT go beyond the limits set by minimumMemberCount and maximumMemberCount. The result is a collection of SoftLayer_Scale_Member instances that were either removed or added. This call can only be invoked on an active group and does not respect cooldown (i.e. even if in a cooldown period, the scaling will still occur). "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "scale"
type: "reference"
layout: "method"
mainService : "SoftLayer_Scale_Group"
---
