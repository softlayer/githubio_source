---
title: "Managing CDN accounts"
description: "How to interact with the CdnMarketplace services. Order CDN, manage mappings and other related functions"
date: "2021-01-02"
classes: 
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Input"
tags:
    - "cdn"    
---

# Setup
Each of these snippets below will share basically the same initialization code, so to save some space we will include the initialization code here, and assume you can setup the SoftLayer client before running each example.

```java
package networkcdnMarketplaceconfigurationmapping;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.cdnmarketplace.configuration.Mapping;
import com.softlayer.api.service.network.cdnmarketplace.configuration.mapping.Path;
import com.softlayer.api.service.network.cdnmarketplace.configuration.cache.Purge;
import com.softlayer.api.service.container.network.cdnmarketplace.configuration.*;

import java.util.AbstractMap;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CdnServices {
    Path.Service servicePath;
    Mapping.Service service;
    Purge.Service serviceCachePurge;

    public CdnServices() {
        String user = "set - me";
        String apiKey = "set - me";
        ApiClient client = (new RestApiClient()).withCredentials(user, apiKey);
        service = Mapping.service(client);
        servicePath = Path.service(client);
        serviceCachePurge =  Purge.service(client);
    }

    public static void main(String[] args) {
        // Json example
        String param ="{'certificateType':'SHARED_SAN_CERT'," +
                "'httpPort':80," +
                "'originType':'HOST_SERVER','" +
                "vendor Name':'akamai'," +
                "'origin':'10.32.12.125'," +
                "'header':'www.techsuppottest.com'," +
                "'path':'/'," +
                "'domain':'www.techsupporttest3.com'," +
                "'protocol':'HTTP'}";
        try {
            CdnServices cdnService = new CdnServices();
            Gson gson = (new GsonBuilder()).setPrettyPrinting().create();
            System.out.println(gson.toJson(cdnService.createDomainMapping(param)));
        } catch (Exception var8) {
            System.out.println("Error: " + var8);
        }
    }

    /**
     * createDomainMapping method
     * @param parameters - Json template in String form
     * @return List<Mapping>
     */
    public List<com.softlayer.api.service.container.network.cdnmarketplace.configuration.Mapping> createDomainMapping(String parameters) {

        parameters = parameters.replaceAll("[{'}]","");
        Map<String, String> paramObject = new HashMap<String, String>();
        for(final String entry : parameters.split(",")) {
            final String[] parts = entry.split(":");
            assert(parts.length == 2) : "Invalid entry: " + entry;
            paramObject.put(parts[0], parts[1]);
        }
        Input input = new Input();
        input.setCertificateType(paramObject.get("certificateType"));
        input.setHttpPort(Long.valueOf(paramObject.get("httpPort")));
        input.setOriginType(paramObject.get("originType"));
        input.setVendorName(paramObject.get("vendor Name"));
        input.setOrigin(paramObject.get("origin"));
        input.setHeader(paramObject.get("header"));
        input.setPath(paramObject.get("path"));
        input.setDomain(paramObject.get("domain"));
        input.setProtocol(paramObject.get("protocol"));

        return service.createDomainMapping(input);
    }

    /**
     *  createOriginPath method
     * @param parameters - Json template in String form
     * @return List<Path>
     */
    public List<com.softlayer.api.service.container.network.cdnmarketplace.configuration.mapping.Path> createOriginPath(String parameters) {

        parameters = parameters.replaceAll("[{'}]","");
        Map<String, String> paramObject = new HashMap<String, String>();
        for(final String entry : parameters.split(",")) {
            final String[] parts = entry.split(":");
            assert(parts.length == 2) : "Invalid entry: " + entry;
            paramObject.put(parts[0], parts[1]);
        }
        Input input = new Input();
        input.setCertificateType(String.valueOf(paramObject.get("certificateType")));
        input.setHttpPort(Long.valueOf(paramObject.get("httpPort")));
        input.setOriginType(String.valueOf(paramObject.get("originType")));
        input.setVendorName(String.valueOf(paramObject.get("vendor Name")));
        input.setOrigin(String.valueOf(paramObject.get("origin")));
        input.setHeader(String.valueOf(paramObject.get("header")));
        input.setPath(String.valueOf(paramObject.get("path")));
        input.setPath(String.valueOf(paramObject.get("domain")));
        input.setProtocol(String.valueOf(paramObject.get("protocol")));
        input.setPerformanceConfiguration(String.valueOf(paramObject.get("performanceConfiguration")));
        input.setUniqueId(String.valueOf(paramObject.get("uniqueId")));
        return servicePath.createOriginPath(input);
    }

    public List<com.softlayer.api.service.container.network.cdnmarketplace.configuration.Mapping> listDomainMapping() {
        return service.listDomainMappings();
    }

    /**
     * listDomainMappingByUniqueId method
     * @param unique - Unique id DomainMapping
     * @return  List<Mapping>
     */
    public List<com.softlayer.api.service.container.network.cdnmarketplace.configuration.Mapping> listDomainMappingByUniqueId(String unique){
        return service.listDomainMappingByUniqueId(unique);
    }

    /**
     *  listOriginPath method
     * @param path - Domain Path 
     * @return List<Path>
     */
    public List<com.softlayer.api.service.container.network.cdnmarketplace.configuration.mapping.Path> listOriginPath(String path){
        return servicePath.listOriginPath(path);
    }

    /**
     * createPurge
     * @param uniqueId - Unique id DomainMapping
     * @param path - Domain Path
     * @return List<Purge>
     */
    public List<com.softlayer.api.service.container.network.cdnmarketplace.configuration.cache.Purge> createPurge(String uniqueId, String path){
        return serviceCachePurge.createPurge(uniqueId,path);
    }

    /**
     * deleteOriginPath method
     * @param uniqueId - Unique id DomainMapping
     * @param path - Domain Path
     * @return String
     */
    public String deleteOriginPath(String uniqueId, String path){
        return servicePath.deleteOriginPath(uniqueId,path);
    }

}
```
