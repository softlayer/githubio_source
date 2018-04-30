---
title: "CreateObject.java"
description: "CreateObject.java"
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

/**
 * Create a Virtual Server simplified.
 *
 * This script creates a VSI order in a simplified way using the minimum required properties that
 * SoftLayer_Virtual_Guest::createObject method specifies. The execution of this script will incur charges on your
 * account. For testing input parameters before ordering a VSI use the SoftLayer_Virtual_Guest::generateOrderTemplate
 * method instead.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 * http://sldn.softlayer.com/reference/services/SoftLayer_Location
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 0.2.3
 */

public class CreateObject {

    public CreateObject(){
        // Declare username and api key
        String username = "set-me";
        String apiKey = "set-me";

        //declare Variables
        String hostname = "SimpleVSI1";
        String domain = "techs.com";
        Long startCpus = 4L;
        Long maxMemory = 2L;
        String datacenterName = "ams03";
        boolean hourlyBillingFlag = false;
        boolean localDiskFlag = true;
        String operatingSystemReferenceCode = "UBUNTU_LATEST";
        String notes = "This is an optional property: " +
                "This VSI was created with the minimum properties required using VirtualGuest::createObject";

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
        templateObject.setOperatingSystemReferenceCode(operatingSystemReferenceCode);
        templateObject.setNotes(notes);
        // Setting location to the skeleton
        Location newLocation = new Location();
        newLocation.setName(datacenterName);
        templateObject.setDatacenter(newLocation);

        try{
               com.softlayer.api.service.container.product.Order result = guestService.generateOrderTemplate(templateObject);
            // Comment above generateOrderTemplate method and use createObject below instead when you are ready to order
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
    public static void main(String [] args)
    {
        new CreateObject();
    }
}
```
