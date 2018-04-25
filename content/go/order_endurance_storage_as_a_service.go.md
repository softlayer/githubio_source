---
title: "order_endurance_storage_as_a_service.go"
description: "order_endurance_storage_as_a_service.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Network_Storage_As"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Network_Storage_Iscsi_"
tags:
    - "blockstorage"
---


```
/*
Order a block storage (endurance) As a Service

The script orders a block storage (endurance) device As a Service, with 80GB storage and 0.25 IOPS.
Since softlayer-go client doesn't have the new datatype containers used in control portal, to order
a SoftLayer_Container_Product_Order_Network_Storage_AsAService object we will make a REST request
by using the source code located in /utils/slapi/softlayer_service_request.go file.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_AsAService
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

// Change imports depending where is located the file softlayer_service_request.go
import "../utils/slapi"

func main() {

	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Build the SoftLayer request you want to send to the API by using REST
	slRequest :=  slapi.SoftLayerServiceRequest{
		Endpoint: "https://api.softlayer.com/rest/v3",
		ServiceName: "SoftLayer_Product_Order",
		Method: "verifyOrder",
	}

	// Build the Parameters object that will be send in the Body request
	parameters := `{"parameters" : [
				{
					"complexType": "SoftLayer_Container_Product_Order_Network_Storage_AsAService",
    					"location": "MEXICO",
    					"quantity": 1,
					"packageId": 759,
					"prices": [
        					{ "id": 189443 },
        					{ "id": 189433 },
        					{ "id": 192043 },
						{ "id": 192233 },
						{ "id": 192053 }
    					],
					"volumeSize": 80,
    					"osFormatType": {
        					"keyName": "LINUX",
        					"complexType": "SoftLayer_Network_Storage_Iscsi_OS_Type"
    					}
        			}
		    	]}`

	// Send API request
	response := slapi.RestRequest(slapi.UrlRequest(slRequest), username, apikey, &parameters, "POST")

	// Following prints the result in a pretty json format
	slapi.PrintJsonFormat(response,true)
}

```
