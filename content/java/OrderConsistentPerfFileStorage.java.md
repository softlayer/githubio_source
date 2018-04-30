---
title: "OrderConsistentPerfFileStorage.java"
description: "OrderConsistentPerfFileStorage.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Location_Group_Pricing"
    - "SoftLayer_Location"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs"
tags:
    - "networkstorage"
---


```
package api.storage;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Location;
import com.softlayer.api.service.container.product.order.network.performancestorage.Nfs;
import com.softlayer.api.service.location.Group;
import com.softlayer.api.service.location.group.Pricing;
import com.softlayer.api.service.product.Item;
import com.softlayer.api.service.product.Order;
import com.softlayer.api.service.product.Package;
import com.softlayer.api.service.product.item.Price;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * Order a consistent file storage (performance NFS).
 *
 * This example shows how to order a SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs
 * by sending following data:
 *      quantity - Quantity of "File Storages" to order
 *      location - Location where storage will be hosted
 *      storageSize - The size in GB of the File Storage
 *      iops - Number of IOPS between "100" and "6000" by intervals of 100.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems
 * http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Pricing
 * http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Pricing/getAllObjects
 * http://sldn.softlayer.com/reference/services/SoftLayer_Location
 * http://sldn.softlayer.com/reference/services/SoftLayer_Location/getDatacenters
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
 * http://sldn.softlayer.com/blog/cmporter/Location-based-Pricing-and-You
 * http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-3
 * http://sldn.softlayer.com/article/Object-Masks
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 *
 * Required Java version: JDK 8 or higher.
 */
public class OrderConsistentPerfFileStorage {

    private static final String USER_NAME = "set-me";
    private static final String API_KEY = "set-me";

    // The quantity
    public Long quantity = new Long(1);

    // Values "ams01", "ams03", "che01", "dal05", "dal06" "fra02", "hkg02", "lon02", etc.
    public String location = "dal06";

    // Values "20", "40", "80", "100", "200", "250", "500" etc.
    public BigDecimal storageSize = new BigDecimal(250);

    // Values between "100" and "6000" by intervals of 100.
    public BigDecimal iops = new BigDecimal(100);

    // The package id to order a network storage is 222
    private static final Long packageId = new Long(222);

    // Storage types - required to find item prices
    private static final String STORAGE_NFS = "performance_storage_nfs";
    private static final String STORAGE_SPACE = "performance_storage_space";
    private static final String STORAGE_IOPS = "performance_storage_iops";

    public OrderConsistentPerfFileStorage(){

        // Create and instantiate the Api Client object
        ApiClient client = new RestApiClient().withCredentials(USER_NAME, API_KEY);

        // Call to following SoftLayer Services
        Order.Service productOrderService = Order.service(client);
        Package.Service packageService = Package.service(client, packageId);
        Pricing.Service locationGroupPricingService = Pricing.service(client);
        Location.Service locationGroupService = Location.service(client);

        // Now we can delete the Scale Group
        try {
            // Getting the datacenter of location
            locationGroupService.withMask().regions();
            Location datacenter = locationGroupService.getDatacenters().stream()
                    .filter( x -> location.equals(x.getName()))
                    .findFirst()
                    .get();

            // Getting Performance Storage NFS item.
            System.out.println("Getting Performance Storage NFS item price");
            packageService.withMask().items().prices();
            List<Item> itemsStorageNfs = packageService.getObject().getItems().stream()
                    .filter( x -> x.getItemCategory().getCategoryCode().equals(STORAGE_NFS))
                    .collect(Collectors.toList());

            // Getting the SoftLayer_Location_Group_Pricing which contains the configured
            // location.
            locationGroupPricingService.withMask().locations();
            Group locationGroup = locationGroupPricingService.getAllObjects().stream()
                    .filter( gp -> gp.getLocations().stream()
                                .anyMatch( x -> x.getName().equals(location)))
                    .findFirst()
                    .orElse(null);

            Long locationId = (locationGroup != null) ? locationGroup.getId() : null;

            /*
             * Getting the storage space prices which match the configured storage space,
             * and are valid for the configured location. In case we did not get a
             * location group for the configured location, we are going to search for
             * standard prices.
             */

            // Use object-mask to get items, categories and avoid a lot of unnecessary data
            packageService.withMask().itemPrices().id();
            packageService.withMask().itemPrices().locationGroupId();
            packageService.withMask().itemPrices().capacityRestrictionMaximum();
            packageService.withMask().itemPrices().capacityRestrictionMinimum();
            packageService.withMask().itemPrices().item().id();
            packageService.withMask().itemPrices().item().capacity();
            packageService.withMask().itemPrices().categories().id();
            packageService.withMask().itemPrices().categories().categoryCode();

            // Get all item prices
            System.out.println("Getting available prices in specified package");
            List<Price> itemPrices = packageService.getObject().getItemPrices();

            // As Java don't support object-filter feature, the following is an useful
            // alternative to get performance_storage_space objects
            System.out.println("Getting prices of Performance Storage Space objects");
            List<Price> pricesStorageSpace = filterStoragePrices(itemPrices,
                                                                 STORAGE_SPACE,
                                                                 locationId);
            if (pricesStorageSpace.isEmpty()){
                System.out.println("Error: The storage space value " + storageSize +
                        " GB is not valid or it doesn't exists in specified location");
            }else{
                System.out.println("\tStorage Space price: " +
                        pricesStorageSpace.get(0).getId());
            }

            // Following is to get performance_storage_iops objects prices
            System.out.println("Getting prices of Performance Storage IOPS objects");
            List<Price> pricesStorageIops = filterStoragePrices(itemPrices,
                                                                STORAGE_IOPS,
                                                                locationId);
            if (pricesStorageIops.isEmpty()){
                System.out.println("Error: The IOPS value " + iops +
                        " is not valid for storage space " + storageSize + " GB and "+
                        "location '" + location + "'.");
            }else{
                System.out.println("\tStorage IOPS price: " +
                        pricesStorageIops.get(0).getId());
            }

            // Set prices that will be used
            System.out.println("Building the order of network storage");
            List<Price> orderPrices = new ArrayList<Price>(){{
                add(itemsStorageNfs.get(0).getPrices().get(0));
                add(pricesStorageSpace.get(0));
                add(pricesStorageIops.get(0));
            }};

            // Build the order template
            Nfs orderData = new Nfs();
            orderData.setPackageId(packageId);
            orderData.setLocation(datacenter.getRegions().get(0).getKeyname());
            orderData.setQuantity(quantity);
            orderData.getPrices().addAll(orderPrices);

            /*
             * verifyOrder() will check your order for errors. Replace this with a call to
             * placeOrder() when you're ready to order. Both calls return a receipt object
             * that you can use for your records.
             */
            System.out.println("Verifying the order....");
            com.softlayer.api.service.container.product.Order order;
            order = productOrderService.verifyOrder(orderData);
            System.out.println("Verified!! \n\t" + order.toString());

        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    // Following function filter the item prices in order to get all available according
    // to entered arguments
    private  List<Price> filterStoragePrices(List<Price> itemPrices,
                                          String storageType,
                                          Long locationId){
        List<Price> prices = itemPrices.stream()
                .filter(storagePredicate(storageType, locationId))
                .collect(Collectors.toList());
        if (prices.isEmpty()){
            prices = itemPrices.stream()
                    .filter(storagePredicate(storageType, null))
                    .collect(Collectors.toList());
        }
        return  prices;
    }

    // Following function returns the Predicate that will be used during filter
    private Predicate<Price> storagePredicate(String storageType, Long locationId){
        Predicate<Price> predicate = null;

        switch (storageType){
            case STORAGE_SPACE:
                if (locationId == null){
                    predicate = price -> price.getItem().getCapacity().equals(storageSize)
                            && price.getLocationGroupId() == null
                            && price.getCategories().stream()
                                .anyMatch( category -> category.getCategoryCode()
                                        .equals(storageType));
                }else{
                    predicate = price -> price.getItem().getCapacity().equals(storageSize)
                            && price.getLocationGroupId() != null
                            && price.getLocationGroupId().equals(locationId)
                            && price.getCategories().stream()
                                .anyMatch( category -> category.getCategoryCode()
                                        .equals(storageType));
                }
                break;
            case STORAGE_IOPS:
                if (locationId == null){
                    predicate = price -> price.getItem().getCapacity().equals(iops)
                            && price.getLocationGroupId() == null
                            && price.getCategories().stream()
                                .anyMatch( category -> category.getCategoryCode()
                                        .equals(storageType))
                            && Integer.parseInt(price.getCapacityRestrictionMinimum())
                                        <= storageSize.intValue()
                            && Integer.parseInt(price.getCapacityRestrictionMaximum())
                                        >= storageSize.intValue();

                }else{
                    predicate = price -> price.getItem().getCapacity().equals(iops)
                            && price.getLocationGroupId() != null
                            && price.getLocationGroupId().equals(locationId)
                            && price.getCategories().stream()
                                .anyMatch( category -> category.getCategoryCode()
                                        .equals(storageType))
                            && Integer.parseInt(price.getCapacityRestrictionMinimum())
                                        <= storageSize.intValue()
                            && Integer.parseInt(price.getCapacityRestrictionMaximum())
                                        >= storageSize.intValue();
                }
                break;
        }
        return predicate;
    }

    public static void main(String args[]){
        new OrderConsistentPerfFileStorage();
    }
}

```
