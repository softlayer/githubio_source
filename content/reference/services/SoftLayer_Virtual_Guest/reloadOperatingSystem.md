---
title: "reloadOperatingSystem"
description: "Reloads current operating system configuration. 

This service has a confirmation protocol for proceeding with the reload. To proceed with the reload without confirmation, simply pass in 'FORCE' as the token parameter. To proceed with the reload with confirmation, simply call the service with no parameter. A token string will be returned by this service. The token will remain active for 10 minutes. Use this token as the parameter to confirm that a reload is to be performed for the server. 

As a precaution, we strongly  recommend backing up all data before reloading the operating system. The reload will format the primary disk and will reconfigure the computing instance to the current specifications on record. 

If reloading from an image template, we recommend first getting the list of valid private block device template groups, by calling the getOperatingSystemReloadImages method. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "reloadOperatingSystem"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---
