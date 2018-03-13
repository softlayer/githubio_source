---
title: "Ordering Bare Metal Servers Using the SoftLayer API "
description: "The ability to order bare metal servers is one of the unique advantages of the SoftLayer cloud. But bare metal servers a"
date: "2015-08-27"
author: "bpotter"
tags:
    - "blog"
---

The ability to order bare metal servers is one of the unique advantages of the SoftLayer cloud. But bare metal servers are inherently more complicated than virtual server infrastructures (VSI) because there are many more choices. A subset of the common bare metal servers can be ordered fairly easily using the [[SoftLayer_Hardware::createObject()]] method. If that’s sufficient for you, you can stop reading this article right here. If you only need to order one type of custom bare metal server, you don't need most of the detail that follows.

However, if you want to use the SoftLayer API in your code to query all bare metal servers that are available to order, this article will show you how. You’ll also learn how you can order them in a way that will work for all locations and accounts.

The pre-set configuration bare metal servers are queried and ordered differently than the custom bare metal servers, so we will discuss those two situations below.

##**Hourly/Pre-set Configuration Bare Metal Servers**
The servers that can be ordered on an hourly basis are pre-set configurations. We have an existing inventory of these servers, so they can be provisioned without human intervention (and therefore provisioned more quickly).

To query and order hourly bare metal servers, do the following:

* Get the simplified hardware options by calling [[SoftLayer_Hardware::getCreateObjectOptions()]] . For example, in Python:

    <python>
hwOptions = client['Hardware'].getCreateObjectOptions()
</python>

     This will return a data structure like [hw-create-options.txt](https://gist.github.com/bmpotter/a0d9a386d8681bdab456). Note that this is just an **example** of the output. Always produce this data structure at runtime by calling getCreateObjectOptions(), because this data could change over time.

* In the structure returned, there is a key called **fixedConfigurationPresets**. All entries under that key are bare metal servers that can be ordered hourly. The properties under each **preset** key give the description and price of that server—although the hourly fee is rounded to the nearest dollar. If you need precise hourly fees, call [[SoftLayer_Product_Package::getActivePresets()]]  for package 200, and add up the hourly fee of each item price in the pre-set configuration. (See <a href="https://gist.github.com/bmpotter/f7791ab08819eafc93e0">calc-preset-hourly-price.py</a> for an example.)

* Under the **fixedConfigurationPresets** key in the data structure returned by getCreateObjectOptions(), you’ll find keys called **template.** This shows the pre-set information to add to the order structure for that pre-set server. You specify the chosen pre-set instead of the keys: processorCoreAmount, memoryCapacity, and hardDrives.

* Select your choices from getCreateObjectOptions() for datacenter, networkComponents, and operatingSystemReferenceCode, adding the corresponding template values into your order structure. Add the hostname, domain, and hourlyBillingFlag into the order structure and pass it to [[SoftLayer_Hardware::createObject()]].  (See [order-preset-bare-metal.py](https://gist.github.com/bmpotter/fe2de7f8028d73ada4e5) for an example.)

* When createObject() returns, it doesn't provide the id of the bare metal server as it does for VSIs. You must query repeatedly for the server with the hostname and domain you specified, and a mask that includes **provisionDate**. When provisionDate is filled in, the server has been provisioned. You may also include **hardwareStatus** and **lastTransaction** in the mask to view the server’s current provisioning phase while you await completion. Including the operating system username and password in the mask is useful so you can log into the server once it is provisioned. (See [get-bare-metal-provision-status.py](https://gist.github.com/bmpotter/0249e838dce1370a7aa0) for an example.)

But that was the easy part.  Querying and ordering monthly, custom, bare metal servers gets more interesting.

##**Monthly/Custom Bare Metal Servers**
SoftLayer has a wider range of bare metal servers that often requires ops personnel to physically reconfigure a server (add memory, disks, etc.) to meet the request. It often takes several hours to provision a custom server, but this means there’s a much wider selection of server models and configurations available for monthly bare metal.

To query and order monthly bare metal servers, do the following:

* Query the product packages that are of type BARE_METAL_CPU and have at least one item with a category of “server.” You can do this by calling [[SoftLayer_Product_Package::getAllObjects()]] and using a filter for these two criteria. (See [get-bare-metal-pkgs.py](https://gist.github.com/bmpotter/664ee9af622ce08da9a4) for an example of this calling and [bare-metal-pkgs.txt](https://gist.github.com/bmpotter/4aeca22d05b0b95732b9) for an example of the output. This gives you the list of monthly processor models that can be ordered.)

* Once a processor model is selected, you can query the associated product package for all items and item prices for that package. With this, you’ll have access to all options available for this package (amount of memory, disk size, port speed, etc.), and the price associated with each.  

    To organize the items into categories, use the item prices that apply to the chosen data center, and filter out duplicate item prices that are still in the system, we wrote the function getOrderItemsDict() in [order-custom-monthly-bare-metal.py](https://gist.github.com/bmpotter/27913e92e9ff7b6b0c54). This will build a data structure of item price objects for a package that’s organized by category. It only includes the item prices for the specified data center and handles several subtleties related to duplicates. (See [pkg.253.tor01.txt](https://gist.github.com/bmpotter/959720c1a2faf8f6e9e3) for an example of the output getOrderItemsDict() produces for package 253 at the Toronto data center.)  

    This data structure is useful in three ways:
    * Printing this data structure gives you an organized view of the options for this server.
    * You can programmatically parse this data structure and display these choices and their prices to the user (if necessary).
    * You can programmatically select choices by the more reliable categoryCode and keyName (rather than the item price id, which can change) and add them to the order structure.

* When you are ready to order or verify an order for a monthly bare metal server, use the data structure produced by getOrderItemsDict() and the getItemPriceId() function to pick specific item price ids out of the structure. Assemble these ids and other meta information into the order structure and call [[SoftLayer_Product_Order::verifyOrder()]] or [[SoftLayer_Product_Order::placeOrder()]]. (Verifying the order first allows you to get the total price and any errors before actually ordering the server. You can see an example of this in [order-custom-monthly-bare-metal.py](https://gist.github.com/bmpotter/27913e92e9ff7b6b0c54).)

* If placeOrder() completes successfully, query the server repeatedly until the provisionDate is filled in. (Refer to the last section of the Hourly/Pre-set discussion above for details.)

-Bruce

