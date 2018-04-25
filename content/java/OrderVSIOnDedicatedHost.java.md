---
title: "OrderVSIOnDedicatedHost.java"
description: "OrderVSIOnDedicatedHost.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
tags:
    - "dedicatedhost"
---


```
package DedicatedHost;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.product.Order;
import com.softlayer.api.service.product.item.Price;
import com.softlayer.api.service.virtual.Guest;

import java.util.ArrayList;
import java.util.List;

/**
 * Order a new Virtual Guest on a Dedicated Host server.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class OrderVSIOnDedicatedHost {

    public static void main(String args[]){
        // Declare username and api key
        String username = "set me";
        String apiKey = "set me";

        // Required values to place an order
        long quantity = 1;
        long packageId = 46;

        // The ID of dedicated host
        long hostId = 48501L;

        // Declare hostname, domain and network components of guests you want to order, add more
        // guest objects if quantity is greater than 1
        List<Guest> virtualGuests = new ArrayList<Guest>();
        Guest guest = new Guest();
        guest.setHostname("vsiOnDedicatedHost");
        guest.setDomain("domaintest.local");

        virtualGuests.add(guest);

        // Declare the list of prices. To get list of all available prices you can use the method
        // SoftLayer_Product_Package::getItemPrices
        long[] pricesIds = {
                200307,    // 1 x 2.0 GHz Cores (Dedicated Host)
                200337,    // 1 GB RAM (Dedicated Host)
                45466,    // CentOS 7.x - Minimal Install (64 bit)
                2202,     // "25 GB (SAN) as First disk
                1800,     // 0 GB Bandwidth
                203857,   // 100 Mbps Public & Private Network Uplinks (Dedicated Host)
                55,       // Monitoring - Host Ping
                57,       // Email and Ticket
                58,       // Automated Notification
                21,       // Primary IP Addresses
                418,      // Nessus Vulnerability Assessment & Reportin
                420,      // VPN Management - Private Network
                905       // Remote Management
        };

        // Building the skeleton of SoftLayer_Product_Item_Price objects
        List<Price> prices = new ArrayList<Price>();
        for (int i = 0; i < pricesIds.length; i++) {
            Price p = new Price();
            p.setId(pricesIds[i]);
            prices.add(p);
        }

        // Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest object template
        // that will be used to order VSIs.
        com.softlayer.api.service.container.product.order.virtual.Guest orderTemplate;
        orderTemplate = new com.softlayer.api.service.container.product.order.virtual.Guest();

        orderTemplate.setHostId(hostId);
        orderTemplate.setPackageId(packageId);
        orderTemplate.setQuantity(quantity);
        orderTemplate.getVirtualGuests().addAll(virtualGuests);
        orderTemplate.getPrices().addAll(prices);
        orderTemplate.setUseHourlyPricing(Boolean.TRUE);

        // Get Api Client and service
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Order.Service orderService = Order.service(client);

        try{
            // verifyOrder() will check your order for errors. Replace this with placeOrder() when
            // you're ready to order:
            //             Receipt receipt = orderService.placeOrder(orderTemplate, Boolean.FALSE);
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
