---
title: "Order Evault"
description: "The example shows how to order a evault storage device in a virtual server"
date: "2019-02-26"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "evault"
    - "order"
---


```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace OrderEvault
{
    class Program
    {
        static void Main(string[] args)
        {
            // Your SoftLayer username and API username.
            authenticate authenticate = new authenticate()
            {   
                username = "set me",
                apiKey = "set me"
            };

            // Evault prices are on this package
            string package = "ADDITIONAL_SERVICES";
            string location = "DALLAS06";

            // KeyName format usually is EVAULT_##_GB and the values could be: 10, 20, 30, 40, 50, 
            // 60, 100, 175, 250, 350, 500, 750, 1000, 1500, 2000, 4000
            string itemKeyName = "EVAULT_10_GB";
            
            // Virtual server ID to which the evault will be added
            int guestID = 123456789;
            IList<SoftLayer_Virtual_Guest> guestList = new List<SoftLayer_Virtual_Guest>()
            {
                new SoftLayer_Virtual_Guest(){id=guestID, idSpecified=true}
            };

            // Initialize the Evault object
            Evault evault = new Evault(authenticate);
            
            // Remove the 'verify' param or set it to false to place the order
            evault.placeOrder(package, itemKeyName, location, guestList, verify: true);
        }
    }

    class Evault
    {        
        SoftLayer_Product_PackageService packageService;
        SoftLayer_Product_OrderService orderService;

        public Evault(authenticate auth)
        {
            packageService = new SoftLayer_Product_PackageService();
            packageService.authenticateValue = auth;

            orderService = new SoftLayer_Product_OrderService();
            orderService.authenticateValue = auth;
        }

        // Verify or Place the order and prints the results
        public void placeOrder(string packageType, string evaultKeyName, string datacenter,
            IList<SoftLayer_Virtual_Guest> guests, int quantity = 1, Boolean verify = false)
        {
            // Retrieve packageId and the evault price
            int packageId = (int) getPackage(packageType).id;
            List<SoftLayer_Product_Item_Price> itemPrices = getItemPrices(packageId, evaultKeyName);

            // Build the order template
            SoftLayer_Container_Product_Order orderTemplate = new SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault()
            {
                location = datacenter,
                packageId = packageId,
                packageIdSpecified = true,
                prices = itemPrices.ToArray(),
                virtualGuests = guests.ToArray(),
                quantity = quantity,
                quantitySpecified = true
            };
            
            try
            {
                // Call to the verifyOrder method if TRUE, to placeOrder if FALSE
                if (verify)
                {
                    Console.WriteLine("Wait while verifying the order...");

                    SoftLayer_Container_Product_Order order = orderService.verifyOrder(orderTemplate);

                    Console.WriteLine("\nOrder verified!\n");
                    Console.WriteLine("\tItem Description: " + order.prices[0].item.description);
                    Console.WriteLine("\tVirtual Guest FQDN: " + order.virtualGuests[0].fullyQualifiedDomainName);
                }
                else
                {
                    Console.WriteLine("Wait while placing the order...");

                    SoftLayer_Container_Product_Order_Receipt receipt = orderService.placeOrder(orderTemplate, false);

                    Console.WriteLine("\nOrder approved!\n");
                    Console.WriteLine("\tOrder ID: " + receipt.orderId);
                    Console.WriteLine("\tOrder Date: " + receipt.orderDate);
                    Console.WriteLine("\tOrder Status: " + receipt.placedOrder.status);
                    Console.WriteLine("\tItem Description: " + receipt.orderDetails.prices[0].item.description);
                    Console.WriteLine("\tVirtual Server Hostname: " + receipt.orderDetails.virtualGuests[0].fullyQualifiedDomainName);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Invalid order: " + e.Message);
            }
            Console.ReadLine();
        }

        // Use object-filter to retrieve the Product_Package object
        private SoftLayer_Product_Package getPackage(String type)
        {
            // Filter to find the packageId
            packageService.SoftLayer_Product_PackageObjectFilterValue = new SoftLayer_Product_PackageObjectFilter();
            packageService.SoftLayer_Product_PackageObjectFilterValue.type = new SoftLayer_Product_Package_TypeObjectFilter();
            packageService.SoftLayer_Product_PackageObjectFilterValue.type.keyName = new SoftLayer_Utility_ObjectFilter_Operation();
            packageService.SoftLayer_Product_PackageObjectFilterValue.type.keyName.operation = type;
            
            Console.WriteLine("Retrieving the package id...");
            SoftLayer_Product_Package package = new SoftLayer_Product_Package();
            try
            {
                SoftLayer_Product_Package[] packages = packageService.getAllObjects();
                package = packages[0];
            }
            catch(Exception e)
            {
                Console.WriteLine("Unable to get package list: " + e.Message);
            }

            return package;
        }

        // Use object-filter to retrieve the price id, it is added to a list
        // which will be used in the order template
        private List<SoftLayer_Product_Item_Price> getItemPrices(int packageId, string keyName)
        {
            // Filter to find the item through its keyName
            packageService.SoftLayer_Product_PackageObjectFilterValue = new SoftLayer_Product_PackageObjectFilter();
            packageService.SoftLayer_Product_PackageObjectFilterValue.items = new SoftLayer_Product_ItemObjectFilter();
            packageService.SoftLayer_Product_PackageObjectFilterValue.items.keyName = new SoftLayer_Utility_ObjectFilter_Operation();
            packageService.SoftLayer_Product_PackageObjectFilterValue.items.keyName.operation = keyName;

            Console.WriteLine("Retrieving the item price ...");
            List<SoftLayer_Product_Item_Price> itemPrices = new List<SoftLayer_Product_Item_Price>();

            try
            {
                SoftLayer_Product_PackageInitParameters packageInitParameters = new SoftLayer_Product_PackageInitParameters();
                packageInitParameters.id = packageId;

                packageService.SoftLayer_Product_PackageInitParametersValue = packageInitParameters;

                SoftLayer_Product_Item[] items = packageService.getItems();

                // Looks for the standard price and add it to the list
                foreach (SoftLayer_Product_Item_Price iPrice in items[0].prices)
                {
                    if (iPrice.locationGroupId == null)
                    {
                        itemPrices.Add(iPrice);
                        break;
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get the Evault price: " + e.Message);
            }            
            return itemPrices;
        }        
    }   
}

```
