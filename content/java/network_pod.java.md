---
title: "Working with Network_Pod"
description: "A few examples on interacting with Network Pod"

date: "2020-06-09"

classes: 
    - "SoftLayer_Network_Pod"    
tags:
    - "network_pod"
---

[Network_Pod](https://https://sldn.softlayer.com/reference/services/SoftLayer_Network_Pod/)

### Get the all Metric Pods

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Pod;

import java.util.List;

public class getAllObjects {
    public static void main(String[] args) {
        String user = "set-me";
        String apiKey = "set-me";
        ApiClient client = (new RestApiClient()).withCredentials(user, apiKey);
        Pod.Service service = Pod.service(client);

        try {
            List<Pod> allHW = service.getAllObjects();
            Gson gson = (new GsonBuilder()).setPrettyPrinting().create();
            System.out.println(gson.toJson(allHW));
        } catch (Exception var8) {
            System.out.println("Error: " + var8);
        }
    }
}

```

### Get the network pod object

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Pod;


public class getObject {
    public static void main(String[] args) {
        String user = "set-me";
        String apiKey = "setme";
        ApiClient client = (new RestApiClient()).withCredentials(user, apiKey);
        Pod.Service service = Pod.service(client);
        // network pod name
        String name = "set-me";
        try {
            Pod resultPod = new Pod();
            for (Pod p : service.getAllObjects()) {
                if (p.getName().equals(name)) {
                    resultPod = p;
                    break;
                }
            }
            Gson gson = (new GsonBuilder()).setPrettyPrinting().create();
            System.out.println(gson.toJson(resultPod));
        } catch (Exception var8) {
            System.out.println("Error: " + var8);
        }
    }
}

```

### List capabilities of the Network Pod

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Pod;
import java.util.List;

public class ListCapabilities {
    public static void main(String[] args) {
        String user = "set-me";
        String apiKey = "set-me";
        ApiClient client = (new RestApiClient()).withCredentials(user, apiKey);
        Pod.Service service = Pod.service(client);

        try {
            List<String> allPodCap = service.listCapabilities();
            Gson gson = (new GsonBuilder()).setPrettyPrinting().create();
            System.out.println(gson.toJson(allPodCap));
        } catch (Exception var8) {
            System.out.println("Error: " + var8);
        }
    }
}

```
