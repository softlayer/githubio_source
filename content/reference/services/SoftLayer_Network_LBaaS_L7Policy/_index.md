---
title: "SoftLayer_Network_LBaaS_L7Policy"
description: "The SoftLayer_Network_LBaaS_L7Policy service allows consumers to manage the Policies associated with a Listener. A Listener can have multiple policies. Polices are associated with priorities. The priorities indicate the order in which policies are evaluated. Each policy is configured with an action which is applied when http traffic matches rules associated with the policy. A policy can be configured with one of the following actions: redirect to pool, redirect to url, or reject. Policies configured with reject are always evaluated first irrespective of the priority followed by redirect to url, after which policies with action set to redirect to pool are evaluated. if policies are configured with redirect to https and reject also, then reject always evaluated first. Polices have multiple rules, each rule is evaluated to true or false. If all the rules of the policy evaluate to true then the action associated with that policy is applied to the request. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Policy"
type: "reference"
layout: "service"
mainService : "SoftLayer_Network_LBaaS_L7Policy"
---
