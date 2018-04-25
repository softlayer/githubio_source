---
title: "GetBandwidthGraph.cs"
description: "GetBandwidthGraph.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Bandwidth_GraphOutputs"
    - "SoftLayer_Account"
    - "SoftLayer_Metric_Tracking_Object"
    - "SoftLayer_Metric_Tracking_ObjectInitParametersValue"
    - "SoftLayer_Metric_Tracking_Object_HardwareServer"
    - "SoftLayer_HardwareInitParameters"
    - "SoftLayer_Metric_Tracking_ObjectService"
    - "SoftLayer_Metric_Tracking_ObjectInitParameters"
    - "SoftLayer_HardwareInitParametersValue"
    - "SoftLayer_HardwareService"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetBandwidthGraph.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetBandwidthGraphNamespace
{
    using System;
    using System.Collections.Generic;

    class GetBandwidthGraph
    {
        /// <summary>
        /// Retrieve a bandwidth graph for a single server.
        /// Retrieve a bandwidth graph for a single server for an arbitrary start and
        /// end date, specifying graph size and other graphing options. We can do this
        /// with two calls to the SoftLayer API.
        /// Counter data such as bandwidth counters and VSI resource use are stored in
        /// a server's metric tracking object. Our first call retrieves that server's
        /// tracking object record. The second call is to the tracking object service
        /// which will generate a PNG image of our bandwidth graph.
        /// </summary>
        /// <manualPages>
        /// Important manual pages:
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.           
            string username = "set me";

            // Your SoftLayer API key.                    
            string apiKey = "set me";

            // The id number of the server whose graph you wish to retrieve. Call the
            // getHardware() method in the SoftLayer_Account API service to retrieve a list
            // of the servers on your account.
            int serverId = 153851;

            // The date at which you wish to start graphing bandwidth.
            DateTime startDate = DateTime.Now.Subtract(new TimeSpan(20, 0, 0, 0, 0));

            // The date at which you wish to end graphing bandwidth.
            DateTime endDate = DateTime.Now;

            // Whether to get a graph for 'public' or 'private' bandwidth usage.
            string graphType = "public";

            // The height of the text in the bandwidth graph in pixels.
            int fontSize = 8;

            // The width of the graph to retrieve in pixels.
            int graphWidth = 827;
            int graphHeight = 273;
            bool hideTimeZone = true;

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_HardwareService hardwareService = new SoftLayer_HardwareService();
            hardwareService.authenticateValue = authenticate;

            SoftLayer_Metric_Tracking_ObjectService metricTrackingObjectService = new SoftLayer_Metric_Tracking_ObjectService();
            metricTrackingObjectService.authenticateValue = authenticate;

            // Setting the init parameter for the hardwareService
            hardwareService.SoftLayer_HardwareInitParametersValue = new SoftLayer_HardwareInitParameters();
            hardwareService.SoftLayer_HardwareInitParametersValue.id = serverId;

            SoftLayer_Metric_Tracking_Object_HardwareServer trackingObject = hardwareService.getMetricTrackingObject();

            // Setting the init parameter for the hardwareService
            metricTrackingObjectService.SoftLayer_Metric_Tracking_ObjectInitParametersValue = new SoftLayer_Metric_Tracking_ObjectInitParameters();
            metricTrackingObjectService.SoftLayer_Metric_Tracking_ObjectInitParametersValue.id = trackingObject.id.GetValueOrDefault();

            try
            {
                // getBandwidthGraph() returns a SoftLayer_Container_Bandwidth_GraphOutputs
                // object. The contents of the bandwidth image is in $image->graphImage.
                // From here you can write it to the file system, display it to a web
                // browser, or run other functions on it.
                SoftLayer_Container_Bandwidth_GraphOutputs image = metricTrackingObjectService.getBandwidthGraph(startDate, endDate, graphType, fontSize, graphWidth, graphHeight, hideTimeZone);
                Console.WriteLine("Image retrieved!");
            }
            catch (Exception e)
            {
                // If there was an error returned from the SoftLayer API then bomb out with the
                // error message.
                Console.WriteLine("Unable to get the bandwidth. " + e.Message);
            }
        }
    }
}

```
