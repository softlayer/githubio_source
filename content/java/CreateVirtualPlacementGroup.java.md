---
title: "CreatePlacementGroup.java"
description: "Add a placement group to your account for use during VSI provisioning."
date: "2018-11-23"
classes: 
    - "SoftLayer_Virtual_PlacementGroup"
tags:
    - "PlacementGroup"
---

```
package com.softlayer.api.test;
/*
 Create Object

 Add a placement group to your account for use during VSI provisioning.

 Important manual pages:
 https://softlayer.github.io/reference/services/SoftLayer_Virtual_PlacementGroup/createObject/
 https://softlayer.github.io/reference/datatypes/SoftLayer_Virtual_PlacementGroup/

 License: http://sldn.softlayer.com/article/License
 Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.PlacementGroup;

public class CreateVirtualPlacementGroup {
    public static void main(String []arg){
        String username = "set me";
        String apiKey = "set me";

        PlacementGroup placement = new PlacementGroup();
        placement.setName("fotest");
        placement.setBackendRouterId(11111L);
        placement.setRuleId(1L);

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        PlacementGroup.Service placementGroup = PlacementGroup.service(client);

        try {

            PlacementGroup result = placementGroup.createObject(placement);
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
