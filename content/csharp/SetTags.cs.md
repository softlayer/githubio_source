---
title: "SetTags.cs"
description: "SetTags.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_GuestInitParameters"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_Virtual_GuestInitParametersValue"
tags:
    - "tags"
---


```
//-----------------------------------------------------------------------
// <copyright file="SetTags.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace SetTagsNamespace
{
    using System;

    class SetTags
    {
        static void Main(string[] args)
        {
            // Your SoftLayer username key.            
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // The id of the VSI you wish to set the tags
            int virtualGuestId = 7844984;

            // The tags you wish to set in the VSI
            string tags = "mytag1,mytag2,mytag3";

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
                bool result = virtualGuestService.setTags(tags);
                Console.WriteLine("The tags has been set successfully. ");
            }

            catch (Exception e)
            {
                Console.WriteLine("Unable to set the tags. ");
            }

        }
    }
}

```
