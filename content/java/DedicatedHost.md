---
title: "Working with DedicatedHost"
description: "This example below lists a few of the common ways of interacting with DedicatedHost, 
including how to order, list, order a virtual guest on DedicatedHost."

date: "2020-07-03"

classes: 
    - "SoftLayer_Virtual_DedicatedHost"
    - "SoftLayer_Virtual_Guest"    
    - "SoftLayer_Product_Order"
tags:
    - "dedicatedhost"
    - "virtualguest"
    - "order"
---


```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.Entity;
import com.softlayer.api.service.Location;
import com.softlayer.api.service.container.product.Order;
import com.softlayer.api.service.container.product.order.virtual.DedicatedHost;
import com.softlayer.api.service.container.product.order.virtual.Guest;
import com.softlayer.api.service.product.Item;
import com.softlayer.api.service.product.Package;
import com.softlayer.api.service.product.item.Price;
import com.softlayer.api.service.product.pkg.Preset;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;


public class DedicatedHostExample {

  private static final String PACKAGE = "packageKeyname";
  private static final String HOST = "hostname";
  private static final String DOMAIN = "domain";
  private static final String DATACENTER = "datacenter";
  private static final String FLAVOR = "flavor";

  private final ApiClient client;
  Properties properties;

  public DedicatedHostExample() {
    String username = "set me";
    String apiKey = "set me";
    client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
  }

  public static void main(String[] args) {

    DedicatedHostExample dedicatedHostExample = new DedicatedHostExample();
    dedicatedHostExample.orderDedicated();
    dedicatedHostExample.printAllDedicatedHost();
    dedicatedHostExample.orderGuestOnDedicatedHost(1111L);
  }

  public void orderDedicated() {
    properties = new Properties() {
      {
        put(HOST, "dedicated-test");
        put(DOMAIN, "example.local");
        put(PACKAGE, "DEDICATED_HOST");
        put(DATACENTER, "dal13");
      }
    };
    String[] orderItems = {
        "56_CORES_X_242_RAM_X_1_4_TB"
    };
    Order order = buildDedicatedTemplate(orderItems);
    placeOrder(order, true);
  }

  public void orderGuestOnDedicatedHost(Long hostId) {
    properties = new Properties() {
      {
        put(HOST, "virtual-test");
        put(DOMAIN, "example.local");
        put(PACKAGE, "SUSPEND_CLOUD_SERVER");
        put(FLAVOR, "M1_1X8X25");
        put(DATACENTER, "dal13");
      }
    };

    String[] orderItems = {
        "REBOOT_REMOTE_CONSOLE",
        "100_MBPS_PRIVATE_NETWORK_UPLINK",
        "BANDWIDTH_0_GB_2",
        "1_IP_ADDRESS",
        "OS_CENTOS_7_X_MINIMAL_64_BIT",
        "MONITORING_HOST_PING_AND_TCP_SERVICE",
        "NOTIFICATION_EMAIL_AND_TICKET",
        "AUTOMATED_REBOOT_FROM_MONITORING",
        "UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT",
        "NESSUS_VULNERABILITY_ASSESSMENT_REPORTING",
    };
    Order order = buildGuestTemplate(orderItems, hostId);
    placeOrder(order, true);

  }

  public Order buildDedicatedTemplate(String[] items) {

    final Long packageId = getPackageId(properties.getProperty(PACKAGE));
    final List<Price> prices = gatherStandardPrices(packageId, items);

    Order order = new DedicatedHost();
    order.setLocation(getLocationId(properties.getProperty(DATACENTER)).toString());
    order.setPackageId(packageId);
    order.setQuantity(1L);
    order.getPrices().addAll(prices);

    return order;
  }

  public Order buildGuestTemplate(String[] items, Long hostId) {

    final Long packageId = getPackageId(properties.getProperty(PACKAGE));
    final List<Price> prices = gatherStandardPrices(packageId, items);
    Guest order = new Guest();
    order.setLocation(getLocationId(properties.getProperty(DATACENTER)).toString());
    order.setPackageId(packageId);
    order.setQuantity(1L);
    order.setUseHourlyPricing(true);
    order.setPresetId(getPresetId(packageId, properties.getProperty(FLAVOR)));
    order.getPrices().addAll(prices);
    order.setHostId(hostId);

    // Build a skeleton SoftLayer_Virtual_Guest object.

    com.softlayer.api.service.virtual.Guest guestsTemplate;
    guestsTemplate = new com.softlayer.api.service.virtual.Guest();
    guestsTemplate.setHostname(properties.getProperty(HOST));
    guestsTemplate.setDomain(properties.getProperty(DOMAIN));
    order.getVirtualGuests().add(guestsTemplate);

    return order;
  }

  private Long getLocationId(String locationName) {
    Long locationId = 0L;
    Location.Service locationService = Location.service(client);
    List<Location> locations = locationService.getDatacenters();
    for (Location location : locations) {
      if (locationName.equals(location.getName())) {
        locationId = location.getId();
        break;
      }
    }
    return locationId;
  }


  private Long getPresetId(Long packageId, String flavor) {
    Long presetId = 0L;
    Package.Service productPackage = Package.service(client, packageId);

    List<Preset> result = productPackage.getActivePresets();
    for (Preset preset : result) {
      if (preset.getKeyName().equals(flavor)) {
        presetId = preset.getId();
        break;
      }
    }
    return presetId;
  }

  public Long getPackageId(String packageName) {
    Long packageId = 0L;
    Package.Service productPackage = Package.service(client);
    List<Package> result = productPackage.getAllObjects();
    for (Package packageData : result) {
      if (packageData.getKeyName().equals(packageName)) {
        packageId = packageData.getId();
        break;
      }
    }
    return packageId;
  }

  public List<Price> gatherStandardPrices(long packageID, String[] itemKeyNames) {
    List<Price> prices = new ArrayList<>();
    Package.Service productPackage = Package.service(client, packageID);
    List<Item> items = productPackage.getItems();
    for (String itemKeyName : itemKeyNames) {
      for (Item item : items) {
        if (itemKeyName.equals(item.getKeyName())) {
          List<Price> itemPrices = item.getPrices();
          for (Price price : itemPrices) {
            if (price.getLocationGroupId() == null) {
              prices.add(price);
            }
          }
        }
      }
    }
    return prices;
  }

  public void placeOrder(Order orderTemplate, boolean verify) {
    com.softlayer.api.service.product.Order.Service productOrder;
    productOrder = com.softlayer.api.service.product.Order.service(client);
    Entity result;
    if (verify) {
      result = productOrder.verifyOrder(orderTemplate);
    } else {
      result = productOrder.placeOrder(orderTemplate, false);
    }
    print(result);
  }

  public void printAllDedicatedHost() {
    Account.Service accountService = Account.service(client);
    print(accountService.getDedicatedHosts());
  }

  void print(Object object) {
    Gson gson = new GsonBuilder().setPrettyPrinting().create();
    String json;
    json = gson.toJson(object);
    System.out.println(json);
  }
}

```
