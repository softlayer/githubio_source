---
title: "Event Logs"
description: "Working with Event Log, with pagination support"
date: "2021-05-04"
classes: 
    - "SoftLayer_Event_Log"
tags:
    - "eventlogs"
    - "objectfilter"
    - "objectmask"
    - "resultlimit"
---


This example deals with a few ways of pulling data from [SoftLayer_Event_Log](https://sldn.softlayer.com/reference/services/SoftLayer_Event_Log/). There can be quite a few Logs here, therefore it is recommended to use a filter like in `getRecentLogs` to limit how far back your search for Events, otherwise you will be paging through Events for a long time. Moreover, this example uses the `maxNumberOfEvents` value to limit the number of event logs that will be retrieved.

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"time"
)

// Session created using values set in the environment, or from the local configuration file (i.e. ~/.softlayer).
var sess = session.New()

// Set the limit number of events that the API retrieves in each SoftLayer_Event_Log::getAllObjects  method call.
var pagination = 50

// Set the max number of events to retrieve in each log example function.
var maxNumberOfEvents =200

func main() {

	sess.Debug = true

	//shows the all user type events
	getEventUserTypes()
	userType:="EMPLOYEE"
	//shows the events with names is a userType value
	getLogsByUserType(userType)

	//shows the all user type events
	getEventNames()
	eventName:="Authentication"
	//shows the events which names contain the eventName value
	getLogsByName(eventName)

	//shows the events created from a specific number of days ago
	daysAgo:=30
	getRecentLogs(daysAgo)

	//shows the system logs
	getSystemLogs()

	//shows the login logs
	getLoginLogs()
}

/**
Shows the Event Logs by user type.
Request URL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"userType":{"operation":"userType"}}&
objectMask=mask[userType,eventName,eventCreateDate]&
resultLimit=0,50
*/
func getLogsByUserType(eventUserType string) {
	filter := filter.Build(filter.Path("userType").Eq(eventUserType))
	mask:="userType,eventName,eventCreateDate"
	systemEvents:=getAllEvents(filter,mask,pagination,maxNumberOfEvents)
	printLogs(systemEvents)
}

/**
Shows the Event Logs which eventName contains nameQuery value
RequestURL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"eventName":{"operation":"^=+nameQuery"}}&
objectMask=mask[userType;eventName,eventCreateDate]&
resultLimit=0,50
*/
func
getLogsByName(nameQuery string){
	filterQuery:=fmt.Sprintf("^= %s",nameQuery)
	filter := filter.Build(filter.Path("eventName").Eq(filterQuery))
	mask:="userType;eventName,eventCreateDate"
	eventLogs :=getAllEvents(filter,mask,pagination,maxNumberOfEvents)
	printLogs(eventLogs)
}


/**
Shows the SYSTEM Logs.
Request URL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"userType":{"operation":"SYSTEM"}}&
objectMask=mask[userType,eventName,eventCreateDate]&
resultLimit=0,50
*/
func getSystemLogs(){
	getLogsByUserType("SYSTEM")
}

/**
Shows the Login Logs
RequestURL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"eventName":{"operation":"^=+Login"}}&
objectMask=mask[userType;eventName,eventCreateDate]&
resultLimit=0,50
*/
func getLoginLogs(){
	getLogsByName("Login")
}

/**
Shows the recent Logs, based on a number of days ago.
Request URL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"eventCreateDate":{"operation":"greaterThanDate",
	"options":[{"name":"date","value":["2021-04-24T00:00:00.0000-06:00"]}]}}&
objectMask=mask[userType;eventName,eventCreateDate]&
resultLimit=0,50
*/
func getRecentLogs(daysAgo int){
	offsetDate :=getDateString(-daysAgo)
	filterObject:=filter.Build(filter.Path("eventCreateDate").DateAfter(offsetDate))
	mask:="userType;eventName,eventCreateDate"
	recentEvents:=getAllEvents(filterObject,mask,pagination,maxNumberOfEvents)
	printLogs(recentEvents)
}

/**
Pages through all results from the Event_Log. This might take long time.
*/
func getAllEvents(
	filter string,
	mask string,
	pagination int,
	maxNumberOfEvents int,
) (resp []datatypes.Event_Log) {
	limit:=pagination
	offset:=0
	eventsSize:=limit
	var allEvents []datatypes.Event_Log
	for eventsSize<=maxNumberOfEvents {
		events := getAllObjects(limit,offset,filter,mask)
		// return if the events are a list of empty structure like [{}]
		if events[0]==(datatypes.Event_Log{}){
			return allEvents
		}
		allEvents=append(allEvents, events...)
		eventsSize=eventsSize+pagination
	}
	return allEvents
}

/**
Request URL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter= filter &
objectMask= mask &
resultLimit=0,50

It returns an array of Event_Log encountered.
*/
func getAllObjects(
	limit int,
	offset int,
	filter string,
	mask string,
) (resp []datatypes.Event_Log) {
	var service = services.GetEventLogService(sess)
	result, err := service.
		Limit(limit).
		Offset(offset).
		Filter(filter).
		Mask(mask).
		GetAllObjects()
	if err != nil {
		fmt.Printf("\n Unable to get Events:\n - %s\n", err)
		return
	}

	return result
}

/**
Shows the Event Logs Names.
*/
func getEventNames(){
	var service = services.GetEventLogService(sess)
	result, err := service.GetAllEventObjectNames()
	if err != nil {
		fmt.Printf("\n Unable to get Events:\n - %s\n", err)
		return
	}
	printAsJsonFormat(result)
}

/**
Shows the Event Logs User Types.
*/
func getEventUserTypes() {
	var service = services.GetEventLogService(sess)
	result, err := service.GetAllUserTypes()
	if err != nil {
		fmt.Printf("\n Unable to get User types:\n - %s\n", err)
		return
	}
	printAsJsonFormat(result)
}

/**
Gets a date offset in days determined by offsetDays value.
It returns a string date with SL API date filtering format.
*/
func getDateString(offsetDays int) (resp string) {
	years:=0
	months:=0
	days:= offsetDays
	offsetTime:=time.Now().AddDate(years,months,days)
	return fmt.Sprintf(
		"%d-%02d-%02dT00:00:00.0000-06:00",
		offsetTime.Year(),
		offsetTime.Month(),
		offsetTime.Day())
}

/**
Prints the data as format JSON.
*/
func printAsJsonFormat(data interface{}){
	jsonData, jsonErr := json.MarshalIndent(data, "", "    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	println(string(jsonData))
}

/**
Prints the Event Logs.
*/
func printLogs(logs []datatypes.Event_Log){
	fmt.Printf("| %35s | %25s |%10s |\n","Event Name","Event Create Date","User Type")
	for _, log := range logs {
		if log!=(datatypes.Event_Log{}){
			fmt.Printf("| %35s ", *log.EventName)
			fmt.Printf("| %25s ", log.EventCreateDate)
			fmt.Printf("| %10s |\n", *log.UserType)
		}
	}
}
```