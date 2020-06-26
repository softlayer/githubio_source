---
title: "Working with Network Vlan"
description: "This example below lists a few of the common ways of interacting with VLANs,  
including how to order, list, cancel Vlan, and list routers by datacenter."

date: "2020-06-25"

classes: 
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Location"    
    - "SoftLayer_Location_Datacenter"
    - "SoftLayer_Hardware"
tags:
    - "vlan"
    - "vlans"
    - "router"
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
import com.softlayer.api.service.container.product.order.network.Vlan;
import com.softlayer.api.service.location.Datacenter;
import com.softlayer.api.service.product.Item;
import com.softlayer.api.service.product.Package;
import com.softlayer.api.service.product.item.Price;
import java.util.List;


public class NetworkVlanExample {

  private final ApiClient client;

  public NetworkVlanExample() {
    String username = "set me";
    String apiKey = "set me";
    client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
  }

  public static void main(String[] args) {
    final String vlanName = "Test Vlan";
    final String packageKeyname = "NETWORK_VLAN";
    final String datacenter = "dal13";
    final String item = "PRIVATE_NETWORK_VLAN";
    final boolean verify = true;

    NetworkVlanExample networkVlan = new NetworkVlanExample();
    networkVlan.orderVlan(packageKeyname, datacenter, vlanName, item, verify);
    networkVlan.printRoutersInDataCenter(datacenter);
    networkVlan.printAllVlans();
    networkVlan.printVlan(11111L);
    networkVlan.cancelVlan(111111L);

  }

  public void orderVlan(
      String packageName,
      String datacenter,
      String name,
      String item,
      boolean verify
  ) {
    Order orderPublicVlanData = buildTemplate(
        packageName,
        datacenter,
        name,
        item);

    placeOrder(orderPublicVlanData, verify);
  }

  public Order buildTemplate(
      String packageName,
      String datacenter,
      String name,
      String item
  ) {

    final Long packageId = getPackageId(packageName);

    final Price itemPrice = getItemPriceStandard(packageId, item);

    Vlan order = new Vlan();
    order.setName(name);
    order.setLocation(getLocationId(datacenter).toString());
    order.setPackageId(packageId);
    // uncomment the line below if you want order the vlan on specific router
    //order.setRouterId(1111111L);
    order.getPrices().add(itemPrice);

    return order;
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

  public Price getItemPriceStandard(long packageID, String itemKeyName) {
    Price itemPrice = new Price();
    Package.Service productPackage = Package.service(client, packageID);
    List<Item> items = productPackage.getItems();
    for (Item item : items) {
      if (itemKeyName.equals(item.getKeyName())) {
        List<Price> itemPrices = item.getPrices();
        for (Price price : itemPrices) {
          if (price.getLocationGroupId() == null) {
            itemPrice = price;
            break;
          }
        }
      }
    }
    return itemPrice;
  }

  public void placeOrder(Order orderTemplate, boolean verify) {
    com.softlayer.api.service.product.Order.Service
        productOrder = com.softlayer.api.service.product.Order.service(client);

    Entity result;
    if (verify) {
      result = productOrder.verifyOrder(orderTemplate);
    } else {
      result = productOrder.placeOrder(orderTemplate, false);
    }
    print(result);

  }

  public void printAllVlans() {
    Account.Service accountService = Account.service(client);
    accountService.setMask("mask[primaryRouter, subnets[ipAddresses]]");
    print(accountService.getNetworkVlans());

  }

  public void printVlan(Long vlanId) {
    com.softlayer.api.service.network.Vlan.Service
        vlanService = com.softlayer.api.service.network.Vlan.service(
        client,
        vlanId);
    vlanService.setMask("mask[primaryRouter, subnets[ipAddresses]]");
    print(vlanService.getObject());
  }

  public void printRoutersInDataCenter(String location) {
    Long locationId = getLocationId(location);
    Datacenter.Service datacenterService = Datacenter.service(client, locationId);
    print(datacenterService.getHardwareRouters());
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

  public void cancelVlan(Long vlanId) {

    com.softlayer.api.service.network.Vlan.Service
        vlanService = com.softlayer.api.service.network.Vlan.service(
        client,
        vlanId);

    vlanService.setMask("mask[billingItem]");

    com.softlayer.api.service.network.Vlan
        vlan = vlanService.getObject();
    Long billingItemId = vlan.getBillingItem().getId();

    com.softlayer.api.service.billing.Item.Service
        itemService = com.softlayer.api.service.billing.Item.service(
        client,
        billingItemId);

    itemService.cancelService();


  }

  void print(Object object) {
    Gson gson = new GsonBuilder().setPrettyPrinting().create();
    String json;
    json = gson.toJson(object);
    System.out.println(json);
  }
}


```
