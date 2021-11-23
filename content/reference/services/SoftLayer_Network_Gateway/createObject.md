---
title: "createObject"
description: "Create and return a new gateway. This object can be created with any number of members or VLANs, but they all must be in the same pod. By creating a gateway with members and/or VLANs attached, it is the equivalent of individually calling their createObject methods except this will start a single asynchronous process to setup the gateway. The status of this process can be checked using the status field. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "createObject"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---
