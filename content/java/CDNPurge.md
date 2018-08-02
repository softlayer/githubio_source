---
title: "CDN Purge"
description: "Purge content on Akamai and Verizon CDN"
date: "2018-08-02"
classes: 
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"
    - "SoftLayer_Cointainer_Network_CdnMarketplace_Configuration_Cache_Purge"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Container_Network_ContentDelivery_PurgeService_Response"
tags:
    - "cdn"
---

**Akamai CDN**

```java
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.network.cdnmarketplace.configuration.cache.Purge;

public class AkamaiCDNPurge{
    public static void main(String[] args) {        
        // Your SoftLayer API username and key.
        String user = "set me";
        String apiKey = "set me";
                
        // ID of Akamai CDN
        String cdnId = "11334422425697";
        // Standard Unix path syntax to reach the file you wish to purge.
        String path = "/folderPath/file";

        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge service
        com.softlayer.api.service.network.cdnmarketplace.configuration.cache.Purge.Service purgeService = 
        com.softlayer.api.service.network.cdnmarketplace.configuration.cache.Purge.service(client);
		
        try {
            // Purge and retrieve list of SoftLayer_Cointainer_Network_CdnMarketplace_Configuration_Cache_Purge
            List<Purge> container = purgeService.createPurge(cdnId, path);
            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
**Verizon  CDN**

To purge stale content from the CDN, enter up to 15 URLs on the list. Within 3-5 minutes, the content will be removed from all points.

```java
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.network.contentdelivery.purgeservice.Response;


public class CDNPurge{
    public static void main(String[] args) {        
        // Your SoftLayer API username and key.
        String user = "set me";
        String apiKey = "set me";
                
        // ID of CDN
        Long cdnId = new Long(1166);
        // List of URL contents
        List<String> urlContents = new ArrayList<>();
        urlContents.add("http://1122.http.cdn.softlayer.net/00001/");

        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Network_ContentDelivery_Account service
        com.softlayer.api.service.network.contentdelivery.Account.Service cdnService = 
        com.softlayer.api.service.network.contentdelivery.Account.service(client, cdnId);
		
        try {
            // Purge and retrieve list of SoftLayer_Container_Network_ContentDelivery_PurgeService_Response
            List<Response> response = cdnService.purgeCache(urlContents);
            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(response));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```