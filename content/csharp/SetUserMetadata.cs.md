---
title: "SetUserMetadata.cs"
description: "SetUserMetadata.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_GuestInitParameters"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_Virtual_GuestInitParametersValue"
tags:
    - "metadata"
---


```
//-----------------------------------------------------------------------
// <copyright file="SetUserMetadata.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace SetUserMetadataNamespace
{
    using System;

    class SetUserMetadata
    {
        /// <summary>
        /// Set the user data for a VSI.
        /// The script sets the user metadata for a VSI we make a simple
        /// call the setUserMetadata() in the SoftLayer_Virtual_Guest API service
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setUserMetadata
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username key.            
            string username = "set me";

            // Your SoftLayer API key.
            string apiKey = "set me";

            // The user data you wish to set
            string[] userData = new string[1] { "this is my user data." };

            // The id of the VSI where you want to set the user data
            int virtualGuestId = 7370502;

            // Creating a connection to the SoftLayer_Virtual_GuestService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declare the API client
            SoftLayer_Virtual_GuestService virtualGuestService = new SoftLayer_Virtual_GuestService();
            virtualGuestService.authenticateValue = authenticate;

            // Setting the init parameter in the virtual guest service.
            virtualGuestService.SoftLayer_Virtual_GuestInitParametersValue = new SoftLayer_Virtual_GuestInitParameters();
            virtualGuestService.SoftLayer_Virtual_GuestInitParametersValue.id = virtualGuestId;

            try
            {
                virtualGuestService.setUserMetadata(userData);
                Console.WriteLine("The user data was set successfully. ");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to set the user data. " + e.Message);
            }
        }
    }
}

```
