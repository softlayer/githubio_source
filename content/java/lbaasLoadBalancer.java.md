---
title: "Working with Lbaas loadBalancer"
description: "A few examples on interacting with lbaas loadBalancer"

date: "2020-07-08"

classes: 
    - "SoftLayer_Network_LBaaS_LoadBalancer"    
tags:
    - "lbaas_loadbalancer"
---

[Lbaas_LoadBalancer](https://sldn.softlayer.com/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/)

### LBaaS loadBalancer examples

#### Some examples use the most important methods. 

```java
package loadbalancer;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Location;
import com.softlayer.api.service.network.lbaas.*;
import com.softlayer.api.service.network.lbaas.LoadBalancer.Service;

import java.util.List;

public class LoadBalancers {

    ApiClient client;
    Service service;

    /**
     * method constructor sent the package Id and get the package items
     * @param user user name credential.
     * @param apiKey api key credential.
     */
    public LoadBalancers(String user, String apiKey) {
        client = (new RestApiClient()).withCredentials(user, apiKey);
        service = LoadBalancer.service(client);

    }

    /**
     * method constructor sent the package Id and get the package items
     * @param user user name credential.
     * @param apiKey api key credential.
     * @param loadBalancerId lBaaS loadbalancer identifier.
     */
    public LoadBalancers(String user, String apiKey, long loadBalancerId) {
        client = (new RestApiClient()).withCredentials(user, apiKey);
        service = LoadBalancer.service(client, loadBalancerId);
    }

    public Boolean cancelLoadBalancer(String uuid) {
        return service.cancelLoadBalancer(uuid);
    }

    public LoadBalancer enableOrDisableDataLogs(String uuid, boolean enable) {
        return service.enableOrDisableDataLogs(uuid, enable);
    }

    public List<LoadBalancer> getAllLoadBalancers() {
        return service.getAllObjects();
    }

    public Location getDatacenter() {
        return service.getDatacenter();
    }

    public List<HealthMonitor> getHealthMonitor() {
        return service.getHealthMonitors();
    }

    public List<L7Pool> getL7Pools() {
        return service.getL7Pools();
    }

    public List<Listener> getListeners() {
        return service.getListeners();
    }

    public LoadBalancer getLoadBalancer(String uuid){
        return service.getLoadBalancer(uuid);
    }

    public List<Member> getMembers(){
        return service.getMembers();
    }

    public LoadBalancer getObject(){
        return service.getObject();
    }

    public static void main(String[] Args){
        String user = "set - me";
        String apiKey = "set - me";
        long loadBalancerId = new Long(123456);
        String uuid = "set - me";
        LoadBalancers loadBalancers = new LoadBalancers(user,apiKey);
        Gson gson = (new GsonBuilder()).setPrettyPrinting().create();
        System.out.println(gson.toJson(loadBalancers.getAllLoadBalancers()));
        loadBalancers = new LoadBalancers(user,apiKey,loadBalancerId);
        System.out.println(gson.toJson(loadBalancers.getLoadBalancer(uuid)));
    }
}
```