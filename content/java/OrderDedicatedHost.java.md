---
title: "OrderDedicatedHost.java"
description: "OrderDedicatedHost.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
tags:
    - "dedicatedhost"
---


```
package DedicatedHost;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Hardware;
import com.softlayer.api.service.hardware.Router;
import com.softlayer.api.service.network.Component;
import com.softlayer.api.service.product.Order;
import com.softlayer.api.service.product.item.Price;

import java.util.ArrayList;
import java.util.List;

/**
 * Order Dedicated Host server.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * http://sldn.softlayer.com/blog/cmporter/Location-based-Pricing-and-You
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class OrderDedicatedHost {

    public static void main(String args[]){
        // Declare username and api key
        String username = "set me";
        String apiKey = "set me";

        // Required variables to place an order
        long quantity = 1;
        String location = "MEXICO";
        long packageId = 813;

        // The backend router you want to use to order the dedicated host.
        Router router = new Router();
        router.setId(329266L);

        // Private network component is required, it must have set a router
        Component primaryBackendNetworkComponent = new Component();
        primaryBackendNetworkComponent.setRouter(router);

        // Set hostname, domain and network components of Dedicated Host you want to order.
        List<Hardware> hardwareList = new ArrayList<Hardware>();
        Hardware hardware = new Hardware();
        hardware.setHostname("dedicatedHost");
        hardware.setDomain("domaintest.local");
        hardware.setPrimaryBackendNetworkComponent(primaryBackendNetworkComponent);

        hardwareList.add(hardware);

        // Build the skeleton of SoftLayer_Product_Item_Price objects
        List<Price> priceList = new ArrayList<Price>();
        Price price = new Price();
        price.setId(200269L);   // 56 Cores X 242 RAM X 1.2 TB

        priceList.add(price);

        // Build a skeleton SoftLayer_Container_Product_Order object template that will be used
        // to order Dedicated Host.
        com.softlayer.api.service.container.product.Order orderTemplate;
        orderTemplate = new com.softlayer.api.service.container.product.Order();

        orderTemplate.setLocation(location);
        orderTemplate.setPackageId(packageId);
        orderTemplate.setQuantity(quantity);
        orderTemplate.getHardware().addAll(hardwareList);
        orderTemplate.getPrices().addAll(priceList);

        // Get Api Client and service
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Order.Service orderService = Order.service(client);

        try{
            // verifyOrder() will check your order for errors. Replace this with placeOrder() when
            // you're ready to order:
            //     Receipt receipt = orderService.placeOrder(orderTemplate, Boolean.FALSE);
            com.softlayer.api.service.container.product.Order receipt = orderService.verifyOrder(orderTemplate);

            // Print response in JSON format
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(receipt));

        } catch (Exception e)
        {
            System.out.println("Unable to place the order: " + e);
        }
    }
}
```
