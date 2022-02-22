---
title: "detachDiskImage"
description: "Creates a transaction to detach a guest's disk image. If the disk image is already detached it will be ignored. 

WARNING: The transaction created by this service will shut down the guest while the disk image is attached. The guest will be turned back on once this process is complete. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---
