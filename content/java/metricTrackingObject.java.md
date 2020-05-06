---
title: "Working with Metric_Tracking_Object"
description: "A few examples on interacting with Metric tracking object using java"

date: "2020-01-27"
classes: 
    - "SoftLayer_Metric_Tracking_Object"    
tags:
    - "metric_tracking"
---

[Metric_Tracking_Object](https://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/)

### Get the all metric tracking ids

```Java
import java.util.List;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.virtual.Guest;

public class GetMetricTracking {

    public static void main(String[] args) {

        // Your SoftLayer API username and key.
        String user = "set - me";
        String apiKey = "set - me";


        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Account
        Account.Service account= Account.service(client);
  
        account.withMask().virtualGuests().id();
        account.withMask().virtualGuests().metricTrackingObjectId();

        try {
            // Retrieve the all metric tracking object Id with Virtual guest attribute in false
            List<Guest> container = account.getObject().getVirtualGuests();

            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

### Get back bone bandwidth graph

```Java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.Graph;
import com.softlayer.api.service.container.metric.data.Type;
import com.softlayer.api.service.metric.tracking.Object;

public class GetCustomGraphData {

    public static void main(String[] args) {
        // Your SoftLayer API username and key.
        String user = "set - me";
        String apiKey = "set - me";


        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Metric_Tracking_Object_id
        String metricId = "set - me"
        Object.Service metric= Object.service(client, Long.valueOf(metricId));
        
        Graph graph = new Graph();
        graph.setEndDatetime("2019-07-09T19:06:11-06:00");
        Type type= new Type();
        type.setKeyName("VIRTUAL_DEDICATED_RACK");
        type.setName("Bandwidth Allotment");
        type.setUnit("unit");
        graph.getMetrics().add(type);

        try {
            Graph container = metric.getCustomGraphData(graph);

            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

### Get bandwidth data

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.metric.tracking.Object;
import com.softlayer.api.service.metric.tracking.object.*;
import java.util.GregorianCalendar;
import java.util.List;

public class GetBandwithData {
    public static void main(String[] args) {
        // Your SoftLayer API username and key.
        String user = "set - me";
        String apiKey = "set - me";


        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Metric_Tracking_Object Id
        String metricId = "set - me"
        Object.Service metric= Object.service(client, Long.valueOf(metricId));

        GregorianCalendar start =
                new GregorianCalendar(2019, 8, 12, 22, 00, 10);
        GregorianCalendar end =
                new GregorianCalendar(2019, 9, 12, 22, 00, 10);

        long timer = new Long(600);
        String typeString = "public"

        try {
            List<Data> container = metric.getBandwidthData(start,end,
                       typeString,timer);

            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

Get metric data types

```java
package softlayer.metrictracking;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.metric.data.Type;
import com.softlayer.api.service.metric.tracking.Object;

import java.util.List;

public class GetMetricDataTypes {
    public static void main(String[] args) {
        // Your SoftLayer API username and key.
        String user = "set - me";
        String apiKey = "set - me";

        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Metric_Tracking_Object Id
        String metricId = "set - me"
        Object.Service metric= Object.service(client, Long.valueOf(metricId));

        try {
            List<Type> container = metric.getMetricDataTypes();

            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

Get object

```java
package softlayer.metrictracking;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.metric.tracking.Object;
import com.softlayer.api.service.metric.tracking.object.Data;

import java.util.GregorianCalendar;
import java.util.List;

public class getObject {
    public static void main(String[] args) {
        // Your SoftLayer API username and key.
        String user = "set - me";
        String apiKey = "set - me";

        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Metric_Tracking_Object Id
        String metricId = "set - me"
        Object.Service metric= Object.service(client, Long.valueOf(metricId));

        try {
            Object container = metric.getObject();
            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```

Get summary data

```java
package softlayer.metrictracking;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.container.metric.data.Type;
import com.softlayer.api.service.metric.tracking.Object;
import com.softlayer.api.service.metric.tracking.object.Data;

import java.util.ArrayList;
import java.util.GregorianCalendar;
import java.util.List;

public class GetSummaryData {
    public static void main(String[] args) {
        // Your SoftLayer API username and key.
        String user = "set-mee";
        String apiKey = "set-me";

        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Metric_Tracking_Object Id
        String metricId = "set - me"
        Object.Service metric= Object.service(client, Long.valueOf(metricId));

        GregorianCalendar start =
                new GregorianCalendar(2019, 8, 12, 22, 00, 10);
        GregorianCalendar end =
                new GregorianCalendar(2019, 9, 12, 22, 00, 10);

        long tim = new Long(600);
        List<Type> typeList= new ArrayList<>();
        Type typeObject= new Type();
        typeObject.setKeyName("CPU0");
        typeObject.setSummaryType("max");
        typeList.add(typeObject);

        try {
            List<Data> container = metric.getSummaryData(start,end,typeList,tim);
            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
Get Metric Tracking Object type

```java
package softlayer.metrictracking;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.metric.tracking.Object;
import com.softlayer.api.service.metric.tracking.object.Type;

public class GetType {
    public static void main(String[] args) {
        // Your SoftLayer API username and key.
        String user = "set-me";
        String apiKey = "set-me";

        // API client
        ApiClient client = new RestApiClient().withCredentials(user, apiKey);
        // SoftLayer_Metric_Tracking_Object Id
        String metricId = "set - me"
        Object.Service metric= Object.service(client, Long.valueOf(metricId));

        try {
            Type container = metric.getType();
            // Print results
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(container));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
