---
title: "Working with Event Logs"
description: "Some examples of Event Log"
date: "2021-04-14"
classes: 
    - "SoftLayer_Event_Log"
tags:
    - "eventlogs"
    - "resultlimit"
---
# Event Log
This example deals with a few ways of pulling data from [SoftLayer_Event_Log](https://sldn.softlayer.com/reference/services/SoftLayer_Event_Log/). Also, uses the latest version of the SoftLayer API Client for Java (`v0.3.2` at the time of publishing this example), which does not support object filters available in the SoftLayer API, so programmatic filters are used instead.

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.ResultLimit;
import com.softlayer.api.service.event.Log;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;


public class EventLogExample {

  private final ApiClient client;
  private final Log.Service  logService;

  public EventLogExample() {
    String username = "set-me";
    String apiKey = "set-me";
    client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
    logService = Log.service(client);
  }

  public static void main(String[] args) {
    EventLogExample eventLogExample = new EventLogExample();
    eventLogExample.getAllTypes();
    eventLogExample.getUserTypes();
    eventLogExample.allLogs();
    eventLogExample.loginLogs();
    eventLogExample.recentLogs();
    eventLogExample.systemLogs();
  }

  /**
   * Running GET on https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/AllEventObjectNames.json with no body
   */
  private void getAllTypes() {
    print(logService.getAllEventObjectNames());
  }

  /***
   * Running GET on https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/AllUserTypes.json with no body
   */
  private void getUserTypes() {
    print(logService.getAllUserTypes());
  }

  /***
   * Running GET on https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/AllObjects.json?resultLimit=0,50 with no body
   */
  private void systemLogs() {
    List<Log> logs=getAllEvents(false);
    String systemName="SYSTEM";
    List<Log> systemLogs = logs.stream()
            .filter(log -> systemName.equalsIgnoreCase(log.getEventName()))
            .collect(Collectors.toList());
    printEventLogs(systemLogs);
  }

  /**
   * Running GET on https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/AllObjects.json?resultLimit=0,50 with no body
   */
  private void recentLogs() {
    LocalDate daysAgo = LocalDate.now().minusDays(30);
    List<Log> logs=getAllEvents(false);
    List<Log> recentLogs = logs.stream()
            .filter(log -> log.getEventCreateDate()
                    .toZonedDateTime()
                    .toLocalDate()
                    .compareTo(daysAgo)>0)
            .collect(Collectors.toList());
    printEventLogs(recentLogs);
  }

  /**
   * Running GET on https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/AllObjects.json?resultLimit=0,50 with no body
   */
  private void loginLogs() {
    List<Log> logs=getAllEvents(false);
    String loginName="login";
    List<Log> loginLogs = logs.stream()
            .filter(log -> log
                    .getEventName()
                    .toLowerCase()
                    .contains(loginName))
            .collect(Collectors.toList());
    printEventLogs(loginLogs);
  }

  /**
   * Running GET on https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/AllObjects.json?resultLimit=0,50 with no body
   */
  private void allLogs() {
    printEventLogs(getAllEvents(false));
  }


  /**
   * Pages through all results from the Event_Log. This might take long time.
   */
  private List<Log> getAllEvents(boolean allEvents) {
    List<Log> result=new ArrayList<>();
    int limit =50;
    int offset =0;
    ResultLimit resultLimit =new ResultLimit(offset,limit);
    boolean iterateEvents=true;

    while(iterateEvents) {
      logService.setResultLimit(resultLimit);
      List<Log> logs = logService.getAllObjects();
      result.addAll(logs);
      if (logs.size() < resultLimit.limit) {
        iterateEvents = false;
      }
      offset+=limit;
      resultLimit=new ResultLimit(offset,limit);
      iterateEvents=iterateEvents&&allEvents;
    }
    return result;
  }

  void print(Object object) {
    Gson gson = new GsonBuilder().setPrettyPrinting().create();
    String json;
    json = gson.toJson(object);
    System.out.println(json);
  }

  void printEventLogs(List<Log> logs){
    for (Log event :logs) {
      System.out.println(String.format("%s - %s - %s",
                      event.getEventName(),
                      event.getEventCreateDate().getTime(),
                      event.getUserType()));
    }
  }
}
```