---
title: "Order Server with RAID Config"
description: "It order a hardware server with raid configuration"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server"
tags:
    - "order"
---

```java
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Hardware;
import com.softlayer.api.service.container.product.order.storage.Group;
import com.softlayer.api.service.container.product.order.storage.group.Partition;
import com.softlayer.api.service.product.Order;
import com.softlayer.api.service.product.item.Price;


public class OrderWithDrivePartition {
    public static void main(String[] args) {
        
        String username = "set me";
        String apiKey = "set me";

        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        
        // Required values to place an order
        long quantity = 1;
        long packageId = 257;

        // Declare hostname, domain and network components of guests you want to order, add more
        // guest objects if quantity is greater than 1
        List<Hardware> baremetals = new ArrayList<Hardware>();
        Hardware server = new Hardware();
        server.setHostname("foobar");
        server.setDomain("softlayer.local");

        baremetals.add(server);

        // Declare the list of prices. To get list of all available prices you can use the method
        // SoftLayer_Product_Package::getItemPrices

        long[] pricesIds = {
            77185,    // Single Intel Xeon E3-1270 v3 (4 Cores, 3.50 GHz)
            76165,    // 8 GB RAM
            44988,    // CentOS 7.x (64 bit)
            74995,    // RAID
            69451,    // 1.00 TB SATA
            69451,    // 1.00 TB SATA
            50357,    // 500 GB Bandwidth Allotment
            273,      // 100 Mbps Public & Private Network Uplinks            
            55,       // Host Ping
            58,       // Automated Notification
            420,      // Unlimited SSL VPN Users & 1 PPTP VPN User per account
            418,      // Nessus Vulnerability Assessment & Reporting
            21,       // 1 IP Address
            57,       // Email and Ticket
            906       // Reboot / KVM over IP
        };
        
        // Building the skeleton of SoftLayer_Product_Item_Price objects
        List<Price> prices = new ArrayList<Price>();
        for (int i = 0; i < pricesIds.length; i++) {
            Price p = new Price();
            p.setId(pricesIds[i]);
            prices.add(p);
        }

        // Set StorageGroups of raid configuration
        // Below is a sample
        Group group1 = new Group();
        group1.setArraySize(new BigDecimal("782"));
        group1.setArrayTypeId(1L);
        Long[] hardDrives1 = {0L,1L};
        group1.getHardDrives().addAll(Arrays.asList(hardDrives1));
        group1.setPartitionTemplateId(1L);

        Group group2 = new Group();
        group2.setArraySize(new BigDecimal("609"));
        group2.setArrayTypeId(2L);
        Long[] hardDrives2 = {0L, 1L};
        group2.getHardDrives().addAll(Arrays.asList(hardDrives2));
        
        Partition partition1 = new Partition();
        partition1.setName("/test");
        partition1.setIsGrow(false);
        partition1.setSize(new BigDecimal("100"));

        Partition partition2 = new Partition();
        partition2.setName("/test2");
        partition2.setIsGrow(true);
        partition2.setSize(new BigDecimal("200"));

        group1.getPartitions().add(partition1);
        group2.getPartitions().add(partition2);
        
        List<Group> storageGroups = new ArrayList<>();
        storageGroups.add(group1);
        storageGroups.add(group2);

        // Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest object template
        // that will be used to order VSIs.
        com.softlayer.api.service.container.product.order.hardware.Server orderTemplate;
        orderTemplate = new com.softlayer.api.service.container.product.order.hardware.Server();        
        orderTemplate.setLocation("AMSTERDAM");
        orderTemplate.setPackageId(packageId);
        orderTemplate.setQuantity(quantity);
        orderTemplate.getHardware().addAll(baremetals);
        orderTemplate.getPrices().addAll(prices);
        orderTemplate.setUseHourlyPricing(Boolean.FALSE);        
        orderTemplate.getStorageGroups().addAll(storageGroups);

        Order.Service orderService = Order.service(client);

        try{
            // verifyOrder() will check your order for errors. Replace this with placeOrder() when
            // you're ready to order:
            //    Receipt receipt = orderService.placeOrder(orderTemplate, Boolean.FALSE);
            com.softlayer.api.service.container.product.Order result = orderService.verifyOrder(orderTemplate);

            // Print response in JSON format
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));

        } catch (Exception e)
        {
            System.out.println("Unable to place the order: " + e);
        }
    }
}
```