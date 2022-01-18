---
title: "add_firewall_rule_to_vsi.go"
description: "add_firewall_rule_to_vsi.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Firewall_Update_Request"
    - "SoftLayer_Network_Component_Firewall"
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
    - "SoftLayer_Network_Component_Firewall_Rule"
tags:
    - "firewalls"
---


```go
/*
Add firewall rules to the Firewall in a VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Firewall_Update_Request/createObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of Virtual server you wish to retrieve it firewall rules
	vsiId := 33051333

	// Build the Network_Firewall_Update_Request_Rule object with the rules you want to add.
	rulesToAdd := []datatypes.Network_Firewall_Update_Request_Rule{
		{
			Action                    : sl.String("permit"),
			Protocol                  : sl.String("tcp"),
			Version 	          : sl.Int(4),
			SourceIpAddress           : sl.String("10.10.10.3"),
			DestinationIpAddress      : sl.String("169.57.65.166"),
			SourceIpCidr              : sl.Int(16),
			OrderValue                : sl.Int(3),
			DestinationPortRangeStart : sl.Int(8081),
			DestinationPortRangeEnd   : sl.Int(8085),
		},
		{
			Action                    : sl.String("deny"),
			Protocol                  : sl.String("udp"),
			Version 	          : sl.Int(4),
			SourceIpAddress           : sl.String("10.10.10.3"),
			DestinationIpAddress      : sl.String("169.57.65.166"),
			SourceIpCidr              : sl.Int(16),
			OrderValue                : sl.Int(4),
			DestinationPortRangeStart : sl.Int(8081),
			DestinationPortRangeEnd   : sl.Int(8085),
		},
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest and SoftLayer_Network_Component_Firewall services
	guestService := services.GetVirtualGuestService(sess)
	firewallService := services.GetNetworkComponentFirewallService(sess)
	firewallUpdateService := services.GetNetworkFirewallUpdateRequestService(sess)

	// 1. Get Firewall Component from VSI
	firewall, err := guestService.Id(vsiId).GetFirewallServiceComponent()
	if err != nil {
		fmt.Printf("\n Unable to get firewall component:\n - %s\n", err)
		return
	}

	// 2. Retrieve all current rules
	oldRules, err := firewallService.Id(*firewall.Id).GetRules()
	if err != nil {
		fmt.Printf("\n Unable to get firewall rules:\n - %s\n", err)
		return
	}

	/*
	Previous step returns an array of SoftLayer_Network_Component_Firewall_Rule objects
	and we need to convert it to an array of SoftLayer_Network_Firewall_Update_Request_Rule
	objects in order to join all rules. For that reason the method converTo() was created for
	this script.
	*/
	rules := convertToFirewallRules(oldRules).([]datatypes.Network_Firewall_Update_Request_Rule)

	// 3. Join the existent rules with the new rules to add.
	rulesToAdd = append(rules, rulesToAdd...)

	// 4. Build the skeleton of SoftLayer_Network_Firewall_Update_Request that will be used to
	//    update the firewall rules
	template := datatypes.Network_Firewall_Update_Request {
		NetworkComponentFirewallId : sl.Int(*firewall.Id),
		Rules: rulesToAdd,
	}

	// 5. Call to SoftLayer_Network_Firewall_Update_Request::createObject() method in order to
	//    replace all firewall rules (update)
	updateRequest, err := firewallUpdateService.CreateObject(&template)
	if err != nil {
		fmt.Printf("\n Unable to replace/update all firewall rules:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.Marshal(updateRequest)
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

/*
Following method converts an object type SoftLayer_Network_Component_Firewall_Rule to
SoftLayer_Network_Firewall_Update_Request_Rule
*/
func convertToFirewallRules(object interface{}) interface{} {

	var result []datatypes.Network_Firewall_Update_Request_Rule

	// Get the encoded JSON of object
	encoded, err := json.Marshal(object)
	if err != nil {
		fmt.Println(err)
	}

	// Inverse the encoded JSON and return an Network_Firewall_Update_Request_Rule
	if err := json.Unmarshal(encoded, &result); err != nil {
		fmt.Printf("%s\n", err)
	}

	return result
}

```
