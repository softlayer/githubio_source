---
title: "PlaceOrder.java"
description: "PlaceOrder.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
tags:
    - "virtualguest"
---


```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.product.Order;
import com.softlayer.api.service.container.product.order.Receipt;
import com.softlayer.api.service.product.item.Price;
import com.softlayer.api.service.virtual.Guest;
import java.util.ArrayList;
import java.util.List;

/**
 * Order Virtual Server
 *
 * The script makes a order for a VSI, it uses the SoftLayer_Product_Order::placeOrder method
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/verifyOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/placeOrder
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 0.2.4
 */

public class placeOrder {

    public static void main(String [] args)
    {
        // Declare username and api key
        String API_USERNAME = "set-me";
        String API_KEY = "set-me";

        //declare Variables
        long quantity = 1;
        String location = "DALLAS09";
        long packageId = 46;
        String hostname = "vsiHostname";
        String domain = "domain.com";

        long[] pricesIds ={
                1643, // guest_core: 8 x 2.0 GHz Cores
                1646, // ram: 4 GB
                45466, // os: CentOS 7.x - Minimal Install (64 bit)
                2202, // guest_disk0: 25 GB (SAN)
                50367, // bandwith: 250 GB Bandwidth
                273, // service_port: 100 Mbps Public & Private Network Uplinks
                55, // monitoring: Host Ping
                57, // notification: Email and Ticket
                58, // response: Automated Notification
                21, // pri_ip_addresses: 1 IP Address
                418, // vulnerability_scanner: Nessus Vulnerability Assessment & Reporting
                420, // vpn_management: Unlimited SSL VPN Users & 1 PPTP VPN User per account
                905}; //remote_management: Reboot / Remote console

        List<Price> prices = new ArrayList<Price>();
        for (long pricesId : pricesIds) {
            Price p = new Price();
            p.setId(pricesId);
            prices.add(p);
        }

        // Get Api Client and service
        ApiClient client = new RestApiClient(API_ENDPOINT).withCredentials(API_USERNAME, API_KEY);
        com.softlayer.api.service.product.Order.Service orderService = com.softlayer.api.service.product.Order.service(client);

        // Build a skeleton array of SoftLayer_Virtual_Guest objects.
        List<Guest> guestObjects = new ArrayList<Guest>();
        Guest guestsTemplate = new Guest();
        guestsTemplate.setHostname(hostname);
        guestsTemplate.setDomain(domain);
        guestObjects.add(guestsTemplate);

        // Build a skeleton SoftLayer_Container_Product_Order object that has details required to order.
        Order orderData = new Order();
        orderData.setLocation(location);
        orderData.setPackageId(packageId);
        orderData.setQuantity(quantity);
        List<Price> priceList = orderData.getPrices();
        priceList.addAll(prices);
        orderData.getVirtualGuests().addAll(guestObjects);

        try{
            // verifyOrder() will check your order for errors. Replace this with a call to placeOrder() when you're ready to order
            // as it will incur in billing charges to your account. Once your order is placed it'll go through SoftLayer's
            // provisioning process. When it's done you'll have a new SoftLayer_Virtual_Guest object and CCI ready to use.
             Order result = orderService.verifyOrder(orderData);

            // Comment verifyOrder method call and use placeOrder method below once ready to order, change boolean (saveAsQuote) value
            // and set to "true" if the order data is to be saved as a quote.
//            Receipt result = orderService.placeOrder(orderData, false);


            //prettyformat Json response
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));

        } catch (Exception e)
        {
            System.out.println("Error: " + e);
        }
    }
}

```
