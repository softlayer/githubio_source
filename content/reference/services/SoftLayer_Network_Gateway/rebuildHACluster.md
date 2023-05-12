---
title: "rebuildHACluster"
description: "Rebuild a virtual gateway with HA cluster by destroying existing member gateway os and installing new os on both gateway members, then creating HA cluster between 2 members. This is a destructive process which will remove existing configuration and stop all gateway capabilities. vSRX will need to be re-configured after this operation. 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---
