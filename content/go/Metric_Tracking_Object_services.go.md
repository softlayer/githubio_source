---
title: "Managing Metric Tracking Object services"
description: "How to interact with the Metric Tracking Object services. How to get summary and graph data."
date: "2020-10-07"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "metric tracking object "    
---

# Setup
Each of these snippets below will share basically the same initialization code, so to save some space we will include the initialization code here, and assume you can setup the SoftLayer client before running each example.

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
	"time"
)

func main() {
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	virtualService := services.GetVirtualGuestService(sess)
	metricService := services.GetMetricTrackingObjectService(sess)

	start := datatypes.Time{time.Date(2020, 10, 1, 0, 0, 0, 0, time.UTC)}
	end := datatypes.Time{time.Date(2020, 11, 1, 0, 0, 0, 0, time.UTC)}
	typ := []datatypes.Container_Metric_Data_Type{
		{KeyName: sl.String("CPU0"), SummaryType: sl.String("max")},
	}
	timevar := sl.Int(600)

	metricService.Options.Id = sl.Int(getMetricId(virtualService, 1233456))
	fmt.Println(getSummaryData(metricService, start, end, typ, timevar))
	fmt.Println(getObject(metricService))
}

func getMetricId(service services.Virtual_Guest, virtualId int) int {
	service.Options.Mask = "metricTrackingObjectId"
	service.Options.Id = sl.Int(virtualId)
	result, err := service.GetObject()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)

	}
	return *result.MetricTrackingObjectId
}

func getCustomGraphData(service services.Metric_Tracking_Object, graph datatypes.Container_Graph) string {
	receipt, err := service.GetCustomGraphData(&graph)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getBandwidthData(service services.Metric_Tracking_Object, start datatypes.Time, end datatypes.Time, typ *string, timevar *int) string {
	receipt, err := service.GetBandwidthData(&start, &end, typ, timevar)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getType(service services.Metric_Tracking_Object) string {
	receipt, err := service.GetType()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getMetricDataType(service services.Metric_Tracking_Object) string {
	receipt, err := service.GetMetricDataTypes()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}

	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return (string(jsonFormat1))
}

func getObject(service services.Metric_Tracking_Object) string {
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
func getSummaryData(service services.Metric_Tracking_Object, start datatypes.Time, end datatypes.Time, typ []datatypes.Container_Metric_Data_Type, timevar *int) string {
	receipt, err := service.GetSummaryData(&start, &end, typ, timevar)
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
