---
title: "SearchTag.cs"
description: "SearchTag.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_Utility_ObjectFilter_Operation_Option"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_Virtual_GuestObjectFilter"
    - "SoftLayer_TagObjectFilter"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Tag_ReferenceObjectFilter"
    - "SoftLayer_AccountObjectFilterValue"
tags:
    - "tags"
---


```
//-----------------------------------------------------------------------
// <copyright file="SearchTag.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace SearchTagNamespace
{
    using System;

    class SearchTag
    {
        /// <summary>
        /// Search VSI by tag
        /// The script retrieves all the VSIs which contain an
        /// arbitrary list of tags
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username key.
            string username = "set me";

            // Your SoftLayer API key.
            string apiKey = "set me";

            // The list of task you want to search
            string[] tags = new string[2] { "tag1", "tag2" };

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.virtualGuests = new SoftLayer_Virtual_GuestObjectFilter();
            filter.virtualGuests.tagReferences = new SoftLayer_Tag_ReferenceObjectFilter();
            filter.virtualGuests.tagReferences.tag = new SoftLayer_TagObjectFilter();
            filter.virtualGuests.tagReferences.tag.name = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.virtualGuests.tagReferences.tag.name.operation = "in";
            filter.virtualGuests.tagReferences.tag.name.options = new SoftLayer_Utility_ObjectFilter_Operation_Option[1];
            filter.virtualGuests.tagReferences.tag.name.options[0] = new SoftLayer_Utility_ObjectFilter_Operation_Option();
            filter.virtualGuests.tagReferences.tag.name.options[0].name = "data";
            filter.virtualGuests.tagReferences.tag.name.options[0].value = tags;

            accountService.SoftLayer_AccountObjectFilterValue = filter;

            try
            {
                SoftLayer_Virtual_Guest[] result = accountService.getVirtualGuests();
                Console.WriteLine("The VSIs has been retrieved successfully ");
                Console.WriteLine(result.Length);
            }
            catch (Exception e)
            {
                Console.WriteLine("There was an error getting the VSIs " + e);
            }
        }
    }
}

```
