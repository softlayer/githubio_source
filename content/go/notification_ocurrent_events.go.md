---
title: "Managing Notification Occurrence Events services"
description: "How to interact with the Notification Ocurrence Events services. The SoftLayer_Notification_Occurrence_Event service represents all events with potential to cause a disruption in service.."
date: "2022-01-13"
classes: 
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "Notification Ocurrence Event "    
---

# Setup
Each of these snippets below will share basically the same initialization code, so to save some space we will include the initialization code here, and assume you can setup the SoftLayer client before running each example.

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	username := "Set - me"
	apikey := "Set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	notificationService := services.GetNotificationOccurrenceEventService(sess)
	fmt.Println(getAllObjects(notificationService))
	// Notificacion ocurrent event id = 123456
	fmt.Println(getObject(notificationService,123456))
}

func getAcknowledgeNotification(service services.Notification_Occurrence_Event, notificationId int) bool {
	result, err := service.Id(notificationId).AcknowledgeNotification()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)

	}
	return result
}

func getAllObjects(service services.Notification_Occurrence_Event) string {
	receipt, err := service.limit(50).GetAllObjects()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getAttachments(service services.Notification_Occurrence_Event, notificationId int) string {
	result, err := service.Id(notificationId).GetAttachments()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(result, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getFirstUpdate(service services.Notification_Occurrence_Event, notificationId int) string {
	receipt, err := service.Id(notificationId).GetFirstUpdate()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getObject(service services.Notification_Occurrence_Event, notificationId int) string {
	service.Options.Mask="impactedAccounts"
	receipt, err := service.Id(notificationId).GetObject()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getImpactedAccounts(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetImpactedAccounts()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getImpactedDevices(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetImpactedDevices()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getImpactedResources(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetImpactedResources()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getImpactedUsers(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetImpactedUsers()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getLastUpdate(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetLastUpdate()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getNotificationOcurrentEventType(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetNotificationOccurrenceEventType()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getStatusCode(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetStatusCode()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getUpdates(service services.Notification_Occurrence_Event,  notificationId int) string {
	receipt, err := service.Id(notificationId).GetUpdates()
	if err != nil {
		fmt.Printf("SoftLayer API Error: %s", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
```