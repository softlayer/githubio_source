---
title: "OrderVSOnPlacementGroup.java"
description: "Use this method to place bare metal server, virtual server and additional service orders with SoftLayer."
date: "2018-11-23"
classes: 
    - "SoftLayer_Product_Order"
tags:
    - "PlacementGroup"
---

```
package com.softlayer.api.test;

/*
 Place Order

 Use this method to place bare metal server, virtual server and additional service orders with SoftLayer
 Place an order using the [[SoftLayer_Container_Product_Order]] data type.

 Important manual pages:
 https://softlayer.github.io/reference/services/SoftLayer_Product_Order/placeOrder/

 License: http://sldn.softlayer.com/article/License
 Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.product.order.Receipt;
import com.softlayer.api.service.container.product.order.virtual.Guest;
import com.softlayer.api.service.product.Order;
import com.softlayer.api.service.product.item.Price;

import java.util.ArrayList;

public class OrderVSOnPlacementGroup {
    public static void main(String[] arg) {
        String username = "set me";
        String apiKey = "set me";

        String location = "448994";
        Long packageId = 835L;
        Long[] prices = {203967L, 204135L, 45466L, 2202L, 204853L, 1800L, 273L, 17129L, 28L, 55L, 58L, 420L, 418L, 21L,
                57L, 905L};
        Long quantity = 1L;

        java.util.List<com.softlayer.api.service.virtual.Guest> list = new ArrayList<>();
        com.softlayer.api.service.virtual.Guest virtualGuest = new com.softlayer.api.service.virtual.Guest();
        virtualGuest.setHostname("fo.test");
        virtualGuest.setDomain("test.softlayer.com");
        virtualGuest.setPlacementGroupId(31741L);

        list.add(virtualGuest);

        Guest guest = new Guest();
        guest.setLocation(location);
        guest.setPackageId(packageId);
        guest.setPresetId(215L);
        for (Long i : prices) {
            Price price = new Price();
            price.setId(new Long(i));
            guest.getPrices().add(price);
        }
        guest.setQuantity(quantity);
        guest.setUseHourlyPricing(true);
        for (com.softlayer.api.service.virtual.Guest i : list) {
            guest.getVirtualGuests().add(i);
        }

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        Order.Service orderService = Order.service(client);

        try {

            Receipt result = orderService.placeOrder(guest, false);
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));

        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
