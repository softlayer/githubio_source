---
title: "EditGateway.java"
description: "EditGateway.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
package api.gateway;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;

/**
 * Edit a Network Gateway. Currently, the only value that can be edited is the name.
 * See below for more details.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/editObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class EditGateway {

    public EditGateway(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of gateway you wish to edit
        Long gatewayId = new Long(169563);

        // Get Api client and service SoftLayer_Network_Gateway
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Gateway.Service gatewayService = Gateway.service(client, gatewayId);

        // Build the Gateway object with new data.
        Gateway templateObject = new Gateway();
        templateObject.setName("New Gateway Name");

        try {
            // Edit existing Gateway by passing the template object.
            Boolean edited = gatewayService.editObject(templateObject);

            // Print the result
            System.out.println(edited ? "Gateway was successfully edited!"
                                      : "Gateway could not be edited.");
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new EditGateway();
    }
}

```
