---
title: "edit_firewall_rule_from_vsi.go"
description: "edit_firewall_rule_from_vsi.go"
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


```
/*
Edit a firewall rule from a  VSI.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
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
	"reflect"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of Virtual server you wish to retrieve it firewall rules
	vsiId := 33051333

	/*
	Data of firewall rule you want to edit/update. If you want to edit rules which don't have
	attributes like destinationPortRangeStart and DestinationPortRangeEnd, case for icmp
	protocol, just put 'nil' next to the attribute.
	*/
	oldRule := datatypes.Network_Component_Firewall_Rule {
		Action                    : sl.String("permit"),
		Protocol                  : sl.String("tcp"),
		Version 	          : sl.Int(4),
		SourceIpAddress           : sl.String("10.10.0.0"),
		DestinationIpAddress      : sl.String("169.57.65.166"),
		SourceIpCidr              : sl.Int(32),
		DestinationPortRangeStart : sl.Int(8081),
		DestinationPortRangeEnd   : sl.Int(8085),
	}

	// New data values of firewall rule that will be edited
	newRule := datatypes.Network_Firewall_Update_Request_Rule {
		Action                    : sl.String("deny"),
		Protocol                  : sl.String("tcp"),
		Version 	          : sl.Int(4),
		SourceIpAddress           : sl.String("10.10.0.0"),
		DestinationIpAddress      : sl.String("169.57.65.166"),
		SourceIpCidr              : sl.Int(32),
		DestinationPortRangeStart : sl.Int(8081),
		DestinationPortRangeEnd   : sl.Int(8085),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest and SoftLayer_Network_Component_Firewall services
	guestService := services.GetVirtualGuestService(sess)
	firewallService := services.GetNetworkComponentFirewallService(sess)
	firewallUpdateService := services.GetNetworkFirewallUpdateRequestService(sess)

	// 1. Get the Firewall Service Component
  	firewall, err := guestService.Id(vsiId).GetFirewallServiceComponent()
	if err != nil {
		fmt.Printf("\n Unable to get firewall component:\n - %s\n", err)
		return
	}

	// The following mask is to get specific data of firewall rules, retrieved data will be
	// compared in order to retrieve the rule we want to update.
	mask := "orderValue;action;protocol;sourceIpAddress;sourceIpCidr;version;" +
		"destinationIpAddress;destinationPortRangeStart;destinationPortRangeEnd"

	// 2. Retrieve all current firewall rules
  	currentRules, err := firewallService.Id(*firewall.Id).Mask(mask).GetRules()
	if err != nil {
		fmt.Printf("\n Unable to get firewall rules:\n - %s\n", err)
		return
	}

	// This variable will be used to save current rules and rule you wan to update, this into
	// an array object SoftLayer_Network_Firewall_Update_Request_Rule
  	firewallRules := []datatypes.Network_Firewall_Update_Request_Rule {}

	// 4. If some rule matches with values into 'oldRule', we'll changed it with the new values
	// into object 'newRule'. And we'll save current rules if it doesn't matches.
	for _, rule := range currentRules {
		ruleOrder := *rule.OrderValue
		rule.OrderValue = nil
		if reflect.DeepEqual(rule, oldRule) {
			newRule.OrderValue = sl.Int(ruleOrder)
			firewallRules = append(firewallRules, newRule)
    		} else {
			currentRule := convertToFirewallRule(rule)
			currentRule.OrderValue = sl.Int(ruleOrder)
			firewallRules = append(firewallRules, currentRule)
		}
  	}

	// 5. Build the Network_Firewall_Update_Request_Rule object with the firewall rules.
  	template := datatypes.Network_Firewall_Update_Request {
		NetworkComponentFirewallId : sl.Int(*firewall.Id),
		Rules                      : firewallRules,
	}

	// 6. Call to createObject() method in order to set firewall rules with all changes.
  	updateRequest, err := firewallUpdateService.CreateObject(&template)
	if err != nil {
		fmt.Printf("\n Unable to replace/update all firewall rules:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(updateRequest,"","     ")
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
func convertToFirewallRule(object interface{}) datatypes.Network_Firewall_Update_Request_Rule {

	var result datatypes.Network_Firewall_Update_Request_Rule

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
