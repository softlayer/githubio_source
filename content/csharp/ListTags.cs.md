---
title: "ListTags.cs"
description: "ListTags.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Tag_Reference"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_GuestInitParameters"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_Virtual_GuestInitParametersValue"
tags:
    - "tags"
---


```
//-----------------------------------------------------------------------
// <copyright file="ListTags.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace ListTagsNamespace
{
    using System;

    class ListTags
    {
        /// <summary>
        /// List the tags for a VSI
        /// The script list all the tags set in an arbitrary  VSI,
        /// it uses the SoftLayer_Virtual_Guest::getTagReferences method
        /// to get the tags. For more information please see below
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getTagReferences
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username key.            
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // The Id of the VSI you wish to retrieve the tags
            int virtualGuestId = 7844984;

            // Creating a connection to the SoftLayer_Virtual_GuestService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_Virtual_GuestService virtualGuestService = new SoftLayer_Virtual_GuestService();
            virtualGuestService.authenticateValue = authenticate;

            virtualGuestService.SoftLayer_Virtual_GuestInitParametersValue = new SoftLayer_Virtual_GuestInitParameters();
            virtualGuestService.SoftLayer_Virtual_GuestInitParametersValue.id = virtualGuestId;
            
            try
            {
                SoftLayer_Tag_Reference[] result = virtualGuestService.getTagReferences();
                Console.WriteLine("The tags has been retrieved successfully. ");
                Console.WriteLine(result.Length);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the tags. " + e);
            }
        }
    }
}

```
