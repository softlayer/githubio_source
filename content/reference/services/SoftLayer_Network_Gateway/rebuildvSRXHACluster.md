---
title: "rebuildvSRXHACluster"
description: "Rebuild a vSRX gateway with HA cluster by destroying existing vSRX and installing new vSRX on both gateway servers, then creating HA cluster between 2 vSRX. This is a destructive process which will remove existing vSRX configuration and stop all gateway capabilities. vSRX will need to be re-configured after this operation. 

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
