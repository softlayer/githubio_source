---
title: "Working with placement groups"
description: "A few examples on interacting with placement group"
date: "2018-11-30"
classes: 
    - "SoftLayer_Virtual_PlacementGroup"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Account"
tags:
    - "order"
    - "Account"
    - "Virtual"
---

Create Placement Group

```java
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

Delete Placement Group

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.PlacementGroup;

public class Delete {
    public static void main(String[] arg) {
        String username = "set me";
        String apiKey = "set me";

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        PlacementGroup.Service placementGroup = PlacementGroup.service(client, 11111L);

        try {
            Boolean result = placementGroup.deleteObject();
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

Get Guests from a Placement Group

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.PlacementGroup;

import java.util.List;

public class GetObject {
    public static void main(String []arg){
        String username = "set me";
        String apiKey = "set me";

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        PlacementGroup.Service placementGroup = PlacementGroup.service(client, 11111L);

        try {

            List<Guest> result = placementGroup.getGuests();
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

Get Placement Groups of the Account

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.PlacementGroup;

import java.util.List;

public class GetPlacementGroup {
    public static void main(String []arg){
        String username = "set me";
        String apiKey = "set me";

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        Account.Service account = Account.service(client);

        try {
            List<PlacementGroup> result = account.getPlacementGroups();
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

Order a Virtual Guest into a specific Placement Group

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.product.order.Receipt;
import com.softlayer.api.service.container.product.order.virtual.Guest;
import com.softlayer.api.service.product.Order;
import com.softlayer.api.service.product.item.Price;

import java.util.ArrayList;

public class OrderVSInPlacementGroup {
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

Get the Placement Group from a Virtual Guest

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.PlacementGroup;

public class VSPG {
    public static void main(String[] arg) {
        String username = "set me";
        String apiKey = "set me";

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        Guest.Service service = Guest.service(client, 11111L);

        try {

            PlacementGroup result = service.getPlacementGroup();
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
