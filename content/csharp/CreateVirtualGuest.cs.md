---
title: "CreateVirtualGuest.cs"
description: "CreateVirtualGuest.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_Virtual_Guest_Attribute"
    - "SoftLayer_Location"
tags:
    - "virtualguests"
---


```
//-----------------------------------------------------------------------
// <copyright file="CreateVirtualGuest.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VirtualGuests
{
    using System;
    class CreateVirtualGuest
    {
        /// <summary>
        ///  Create Virtual Guest
        ///  This method creates a Virtual Server using the simplified way. 
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
        /// </manualPages>
        static void Main(string[] ards)
        {
            // You SoftLayer username
            string username = "set me";
            // Your SoftLayer API key.            
            string apiKey = "set me";
    
            // Creating a connection to the SoftLayer_Virtual_Guest API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Virtual_GuestService guestService = new SoftLayer_Virtual_GuestService();
            guestService.authenticateValue = authenticate;

            // Build the SoftLayer_Virtual_Guest object that you wish to create.
            SoftLayer_Virtual_Guest templateObject = new SoftLayer_Virtual_Guest();
            templateObject.hostname = "rcvtest1";
            templateObject.domain = "softlayer.com";
            templateObject.startCpus = 2;
            templateObject.startCpusSpecified = true;
            templateObject.maxMemory = 2;
            templateObject.maxMemorySpecified = true;
            templateObject.localDiskFlag = true;
            templateObject.localDiskFlagSpecified = true;
            templateObject.operatingSystemReferenceCode = "WIN_LATEST_64";
            // Build a SoftLayer_Location object to define where the server will be ordered.
            SoftLayer_Location location = new SoftLayer_Location();
            location.name = "dal05";
            templateObject.datacenter = location;
            // Build the SoftLayer_Virtual_Guest_Attribute object with user data for a Cloud Computing Instance order.
            SoftLayer_Virtual_Guest_Attribute attribute = new SoftLayer_Virtual_Guest_Attribute();
            attribute.value = "this is for test";
            // Create an array of attributes and add the attribute previously created.
            SoftLayer_Virtual_Guest_Attribute[] attributes = new SoftLayer_Virtual_Guest_Attribute[1] { attribute };
            // Add attributes array to the template
            templateObject.userData = attributes;
            try
            {
                // To test the input parameters call the SoftLayer_Virtual_Guest::generateOrderTemplate method
                // when you are ready to create the server call the SoftLayer_Virtual_Guest::createObject method.
                SoftLayer_Container_Product_Order result = guestService.generateOrderTemplate(templateObject);
                Console.WriteLine(result.packageId);
                Console.WriteLine(result.location);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to create a VSI: " + e.Message);
            }      
        }
    }
}

```
