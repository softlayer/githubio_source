---
title: "Managing Notification Occurrence Events services"
description: "How to interact with the Notification Ocurrence Events services. The SoftLayer_Notification_Occurrence_Event service represents all events with potential to cause a disruption in service.."
date: "2020-10-07"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "Metric Tracking Object "    
---

# Setup
Each of these snippets below will share basically the same initialization code, so to save some space we will include the initialization code here, and assume you can setup the SoftLayer client before running each example.

```Go
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
	service.Options.Id = sl.Int(notificationId)
	result, err := service.AcknowledgeNotification()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)

	}
	return result
}

func getAllObjects(service services.Notification_Occurrence_Event) string {
	receipt, err := service.GetAllObjects()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getAttachments(service services.Notification_Occurrence_Event, notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetAttachments()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getFirstUpdate(service services.Notification_Occurrence_Event, notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetFirstUpdate()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getImpactedAccountCount(service services.Notification_Occurrence_Event, notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetImpactedAccountCount()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getObject(service services.Notification_Occurrence_Event, notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetObject()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getImpactedAccounts(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetImpactedAccounts()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getImpactedDeviceCount(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetImpactedDeviceCount()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getImpactedDevices(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetImpactedDevices()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getImpactedResources(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetImpactedResources()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getImpactedUsers(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetImpactedUsers()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getLastUpdate(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetLastUpdate()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getNotificationOcurrentEventType(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetNotificationOccurrenceEventType()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getStatusCode(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetStatusCode()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
func getUpdates(service services.Notification_Occurrence_Event,  notificationId int) string {
	service.Options.Id = sl.Int(notificationId)
	receipt, err := service.GetUpdates()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}
```