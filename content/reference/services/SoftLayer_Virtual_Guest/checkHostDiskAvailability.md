---
title: "checkHostDiskAvailability"
description: "Checks the associated host for available disk space to determine if guest migration is necessary. This method is only used with local disks. If this method returns false, calling attachDiskImage($imageId) will automatically migrate the destination guest to a new host before attaching the portable volume. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "checkHostDiskAvailability"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---
