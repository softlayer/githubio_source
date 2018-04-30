---
title: "EditDetails.cs"
description: "EditDetails.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_ServerService"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Hardware"
    - "SoftLayer_Hardware_ServerInitParametersValue"
    - "SoftLayer_Hardware_ServerInitParameters"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="EditDetails.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace EditDetailsNamespace
{
    using System;
    using System.Collections.Generic;

    class EditDetails
    {
        /// <summary>
        /// Editing a server's basic information
        /// Changing the notes property for a single server record to the sentence "This
        /// is my fastest server!" using the editObject() method in the
        /// SoftLayer_Hardware_Server API service. See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/editObject
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username and key.
            string username = "set me";
            string apiKey = "set me";

            // The name of the server we wish to edit.
            string serverName = "test1";

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring a new API service object for the SoftLayer_Account API service.
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            // Calling the getHardware() method from the SoftLayer_Account API service to get
            // a list of hardware on your account, including id numbers.
            SoftLayer_Hardware[] hardwares = null;
            try
            {
                // Making the call to retrieve our hardware records.
                hardwares = accountService.getHardware();
            }
            catch (Exception e)
            {
                // If there was an error returned from the SoftLayer API then bomb out with the
                // error message.
                Console.WriteLine("Unable to retrieve hardware. " + e.Message);
            }

            // Looking for the server name to get its id
            int hardwareId = -1;
            foreach (var hardware in hardwares)
            {
                if (serverName.Equals(hardware.hostname))
                {
                    hardwareId = hardware.id.GetValueOrDefault();
                }
            }

            if (hardwareId == -1)
            {
                throw new Exception("Unable to find the server with the name " + serverName);
            }

            // Declaring a new API service object for the SoftLayer_Account API service.
            SoftLayer_Hardware_ServerService hardwareServerService = new SoftLayer_Hardware_ServerService();
            hardwareServerService.authenticateValue = authenticate;

            // Setting the init parameter with the hardware ID to edit
            SoftLayer_Hardware_ServerInitParameters hardwareInitParameter = new SoftLayer_Hardware_ServerInitParameters();
            hardwareInitParameter.id = hardwareId;
            hardwareServerService.SoftLayer_Hardware_ServerInitParametersValue = hardwareInitParameter;

            // Defining the new local properties to set.
            // A SoftLayer_Hardware_Server record has a few local properties that you can
            // change via the API. Every service's editObject() method takes a single                                                                                                                                              
            // parameter, a skeleton object that only defines the properties we wish to
            // change. While we're only editing a server's notes in this example you can
            // also use editObject() to edit the server's hostname and domain record.
            SoftLayer_Hardware_Server editTemplate = new SoftLayer_Hardware_Server();
            editTemplate.notes = "This is my fastest server!";

            try
            {
                // Editing our server record.
                var result = hardwareServerService.editObject(editTemplate);
                Console.WriteLine("Server edited");
            }
            catch (Exception e)
            {
                // If there was an error returned from the SoftLayer API then bomb out with the
                // error message.
                Console.WriteLine("Unable to retrieve hardware. " + e.Message);
            }
        }
    }
}

```
