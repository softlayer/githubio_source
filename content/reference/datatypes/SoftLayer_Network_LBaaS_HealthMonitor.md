---
title: "SoftLayer_Network_LBaaS_HealthMonitor"
description: "The SoftLayer_Network_LBaaS_HealthMonitor type presents a structure containing attributes of a health monitor object associated with load balancer instance. Note that the relationship between backend (pool) and health monitor is N-to-1, especially that the pools object associated with a health monitor must have the same pair of protocol and port. Example: frontend FA: http, 80   - backend BA: tcp, 3456 - healthmonitor HM_tcp3456 frontend FB: https, 443 - backend BB: tcp, 3456 - healthmonitor HM_tcp3456 In above example both backends BA and BB share the same healthmonitor HM_tcp3456 "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_HealthMonitor"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Network_LBaaS_HealthMonitor"
---
