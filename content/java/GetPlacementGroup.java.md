---
title: "GetPlacementGroup.java"
description: "Retrieve a SoftLayer_Virtual_PlacementGroup record."
date: "2018-11-23"
classes: 
    - "SoftLayer_Virtual_PlacementGroup"
tags:
    - "PlacementGroup"
---

```
package com.softlayer.api.test;

/*
 Get Object

 Retrieve a SoftLayer_Virtual_PlacementGroup record.

 Important manual pages:
 https://softlayer.github.io/reference/services/SoftLayer_Virtual_PlacementGroup/getObject/

 License: http://sldn.softlayer.com/article/License
 Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.PlacementGroup;

import java.util.List;

public class GetPlacementGroup {
    public static void main(String []arg){
        String username = "set me";
        String apiKey = "set me";

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        PlacementGroup.Service placementGroup = PlacementGroup.service(client, 11111L);

        try {

            List<Guest> result = placementGroup.getObject();
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
