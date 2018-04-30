---
title: "CreateObjectWithTemplate.java"
description: "CreateObjectWithTemplate.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Location"
tags:
    - "virtualguest"
---


```
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Location;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.guest.block.device.template.Group;

/**
 * Create a Virtual Server with Image Template
 *
 * This script creates a VSI order in a simplified way using the minimum required properties that
 * SoftLayer_Virtual_Guest::createObject method specifies and setting an Image Template to be used to provision
 * on Computing Instance. The execution of this script will incur charges on your account. For testing input parameters
 * before ordering a VSI use SoftLayer_Virtual_Guest::generateOrderTemplate method instead.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 * http://sldn.softlayer.com/reference/services/SoftLayer_Location
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 0.2.4
 */


public class CreateObjectWithTemplate {
    
    public static void main(String [] args)
    {
        String username = "set-me";
        String apiKey = "set-me";

        //declare Variables
        String hostname = "SimpleVSI2";
        String domain = "techs.com";
        Long startCpus = 2L;
        Long maxMemory = 8L;
        String datacenterName = "ams03";
        boolean hourlyBillingFlag = false;
        boolean localDiskFlag = true;

        // Get Api Client and service
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Guest.Service guestService = Guest.service(client);

        // Create a SoftLayer_Virtual_Guest object
        Guest templateObject = new Guest();

        // Declare properties for Skeleton input SoftLayer_Virtual_Guest datatype
        templateObject.setHostname(hostname);
        templateObject.setDomain(domain);
        templateObject.setStartCpus(startCpus);
        templateObject.setMaxMemory(maxMemory);
        templateObject.setHourlyBillingFlag(hourlyBillingFlag);
        templateObject.setLocalDiskFlag(localDiskFlag);

        templateObject.setNotes("This is an optional property: " +
                "This script creates a VSI order with the minimum properties required and using an image Template, " +
                "it is required that operatingSystemReferenceCode property shouldn't be set");
        // Setting location to the skeleton
        Location newLocation = new Location();
        newLocation.setName(datacenterName);
        templateObject.setDatacenter(newLocation);

        // Setting image template to the skeleton
        Group blockDevice = new Group();
        blockDevice.setGlobalIdentifier("ce3f5ea3-893a-4992-ad14-5bcd99d9b32a");
        templateObject.setBlockDeviceTemplateGroup(blockDevice);

        try{
            com.softlayer.api.service.container.product.Order result = guestService.generateOrderTemplate(templateObject);
            // Comment above generateOrderTemplate method and use the createObject below instead when you are ready to order
            // the server.
            // Guest result = guestService.createObject(templateObject);

            //Print result
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e)
        {
            System.out.println("Error: " + e);
        }
    }
}

```
