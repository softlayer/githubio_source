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


This example deals with a few ways of pulling data from [SoftLayer_Event_Log](https://sldn.softlayer.com/reference/services/SoftLayer_Event_Log/). There can be quite a few Logs here, therefore it is recommended to use a filter like in `getRecentLogs` to limit how far back your search for Events, otherwise you will be paging through Events for a long time.

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

func main() {
	sess := session.New()
	sess.Debug = true
	getSystemLogs(sess)
	getLoginLogs(sess)
	getRecentLogs(sess)
	getEventUserTypes(sess)
	getEventNames(sess)

}

/**
Shows the SYSTEM Logs.
Request URL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"userType":{"operation":"SYSTEM"}}&
objectMask=mask[userType,eventName,eventCreateDate]&
resultLimit=0,50
 */
func getSystemLogs(sess *session.Session){
	filter := filter.Build(filter.Path("userType").Eq("SYSTEM"))
	mask:="userType,eventName,eventCreateDate"
	systemEvents:=getAllEvents(sess,filter,mask)
	printLogs(systemEvents)
}

/**
Shows the Login Logs
RequestURL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"eventName":{"operation":"^=+Login"}}&
objectMask=mask[userType;eventName,eventCreateDate]&
resultLimit=0,50
 */
func getLoginLogs(sess *session.Session){
	filter := filter.Build(filter.Path("eventName").Eq("^= Login"))
	mask:="userType;eventName,eventCreateDate"
	eventLogs :=getAllEvents(sess,filter,mask)
	printLogs(eventLogs)
}

/**
Shows the recent Logs
Request URL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter={"eventCreateDate":{"operation":"greaterThanDate",
	"options":[{"name":"date","value":["2021-04-24T00:00:00.0000-06:00"]}]}}&
objectMask=mask[userType;eventName,eventCreateDate]&
resultLimit=0,50
 */
func getRecentLogs(sess *session.Session){
	offsetDate :=getDateString(-10)
	filterObject:=filter.Build(filter.Path("eventCreateDate").DateAfter(offsetDate))
	mask:="userType;eventName,eventCreateDate"
	recentEvents:=getAllEvents(sess, filterObject,mask)
	printLogs(recentEvents)
}

/**
Pages through all results from the Event_Log. This might take long time.
*/
func getAllEvents(
	sess *session.Session,
	filter string,
	mask string,
) (resp []datatypes.Event_Log) {
	limit:=50
	offset:=0
	eventsSize:=limit
	var allEvents []datatypes.Event_Log
	for limit==eventsSize {
		events := getAllObjects(sess, limit,offset,filter,mask)
		allEvents=append(allEvents, events...)
		eventsSize=len(events)
		eventsSize=0 // comment this line to get all events
	}
	return allEvents
}

/**
Request URL:
GET https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
objectFilter= filter &
objectMask= mask &
resultLimit=0,50
 */
func getAllObjects(
	sess *session.Session,
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
func getEventNames(sess *session.Session){
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
func getEventUserTypes(	sess *session.Session) {
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
 Prints the data as format JSON
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
Prints the Event Logs
*/
func printLogs(logs []datatypes.Event_Log){
	fmt.Printf("| %20s | %25s |%10s |\n","Event Name","Event Create Date","User Type")
		for _, log := range logs {
			if log!=(datatypes.Event_Log{}){
				fmt.Printf("| %20s ", *log.EventName)
				fmt.Printf("| %25s ", log.EventCreateDate)
				fmt.Printf("| %10s |\n", *log.UserType)
			}
	}
}

```