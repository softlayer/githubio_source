---
title: "Order Load Balancer"
description: "Order a Load Balancer"
date: "2020-05-04"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Account"
tags:
    - "order"
    - "subnet"
    - "package"
---
The following example retrieves the package id, subnet id and prices for a "Load Balancer As A Service(LBaaS)" package, 
builds the order data and place/verify the order.

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.container.product.order.Receipt;
import com.softlayer.api.service.container.product.order.network.loadbalancer.AsAService;
import com.softlayer.api.service.location.Region;
import com.softlayer.api.service.network.Subnet;
import com.softlayer.api.service.network.lbaas.LoadBalancerProtocolConfiguration;
import com.softlayer.api.service.network.vlan.Type;
import com.softlayer.api.service.product.Item;
import com.softlayer.api.service.product.Order;
import com.softlayer.api.service.product.Package;
import com.softlayer.api.service.product.item.Price;

import java.util.ArrayList;
import java.util.List;

public class OrderLoadBalance {

    /*
    Returns the packageId for the LBaaS
    */
    public Long getPackageId(ApiClient client, String pkg_name) {
        Long packageId = 0L;
        Package.Service productPackage = Package.service(client);
        List<Package> result = productPackage.getAllObjects();
        for (Package packageData : result) {
            if (packageData.getName().equals(pkg_name)) {
                packageId = packageData.getId();
                break;
            }
        }
        return packageId;
    }

    /*
    Returns the standard prices
    */
    public List<Long> getItemPrices(ApiClient client, long pkg_id) {
        List<Long> prices = new ArrayList<Long>();
        Package.Service productPackage = Package.service(client, pkg_id);
        List<Item> items = productPackage.getItems();
        for (Item item : items) {
            List<Price> itemPrices = item.getPrices();
            for (Price price : itemPrices) {
                if (price.getLocationGroupId() == null) {
                    Long priceId = price.getId();
                    prices.add(priceId);
                }

            }
        }
        return prices;
    }

    /*
    Find and returns the first subnet in the datacenter
    */
    public Long getSubnetId(ApiClient client, String datacenter) {
        Long subnetId = 0L;
        Account.Service accountService = Account.service(client);
        accountService.withMask().privateSubnets().routingTypeKeyName();
        accountService.withMask().privateSubnets().networkVlan().type();
        accountService.withMask().privateSubnets().networkVlan().primaryRouter().datacenter().regions();

        List<Subnet> subnets = accountService.getObject().getPrivateSubnets();
        for (Subnet subnet : subnets) {
            Type type = subnet.getNetworkVlan().getType();
            String routingTypeKeyName = subnet.getRoutingTypeKeyName();
            List<Region> regions = subnet.getNetworkVlan().getPrimaryRouter().getDatacenter().getRegions();
            for (Region region : regions) {
                if (region.getKeyname().equals(datacenter) && type.getKeyName().equals("STANDARD")
                        && routingTypeKeyName.equals("PRIMARY")) {
                    subnetId = subnet.getId();
                    break;
                }
            }
        }
        if(subnetId == 0L){
            throw new RuntimeException("No subnet found for location provided");
        }
        return subnetId;
    }

    /*
    Allows to order a Load Balancer
    */
    public void orderLbaas(ApiClient client, String pkg_name, String datacenter, String name, String desc,
                           List<LoadBalancerProtocolConfiguration> protocols, Long subnet_id, boolean publicData,
                           boolean verify) {
        Long packageId = getPackageId(client, pkg_name);
        List<Long> prices = getItemPrices(client, packageId);

        // Find and select a subnet id if it was not specified.
        if (subnet_id == null) {
            subnet_id = getSubnetId(client, datacenter);
        }

        // Build the configuration of the order
        AsAService order = new AsAService();
        order.setContainerIdentifier("SoftLayer_Container_Product_Order_Network_LoadBalancer_AsAService");
        order.setName(name);
        order.setDescription(desc);
        order.setLocation(datacenter);
        order.setPackageId(packageId);
        order.setUseHourlyPricing(true);
        for (Long i : prices) {
            Price price = new Price();
            price.setId(new Long(i));
            order.getPrices().add(price);
        }

        for (LoadBalancerProtocolConfiguration protocol : protocols) {
            order.getProtocolConfigurations().add(protocol);
        }

        Subnet subnet = new Subnet();
        subnet.setId(new Long(subnet_id));
        order.getSubnets().add(subnet);

        Order.Service productOrder = Order.service(client);
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        try {
            // If verify=True it will check your order for errors.
            // It will order the lbaas if False.
            if (verify) {
                com.softlayer.api.service.container.product.Order result = productOrder.verifyOrder(order);
                // Print the verify order information.
                System.out.println(gson.toJson(result));
            } else {
                Receipt result = productOrder.placeOrder(order, false);
                // Print the order information.
                System.out.println(gson.toJson(result));
            }

        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }


    public static void main(String arg[]) {
        String username = "set me";
        String apiKey = "set me";
        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();

        OrderLoadBalance orderLoadBalance = new OrderLoadBalance();
        
        String package_name = "Load Balancer As A Service (LBaaS)";
        String location = "DALLAS10";
        String name = "My-LBaaS-name-test";
        String description = "A description sample";
        // Change the subnet_id data if you want to add a specific one, if not just leave it like this.
        Long subnet_id = null;

        // Set False for private network
        boolean is_public = true;

        LoadBalancerProtocolConfiguration loadBalance = new LoadBalancerProtocolConfiguration();
        loadBalance.setBackendPort(80L);
        loadBalance.setBackendProtocol("HTTP");
        loadBalance.setFrontendPort(8080L);
        loadBalance.setFrontendProtocol("HTTP");
        loadBalance.setLoadBalancingMethod("ROUNDROBIN");  // ROUNDROBIN, LEASTCONNECTI
        loadBalance.setMaxConn(1000L);

        List<LoadBalancerProtocolConfiguration> protocols = new ArrayList<LoadBalancerProtocolConfiguration>();
        protocols.add(loadBalance);

        // Change verify = true to false to place the order.
        boolean verify = true;
        orderLoadBalance.orderLbaas(client, package_name, location, name, description, protocols,
                subnet_id, is_public, verify);
    }
}
```