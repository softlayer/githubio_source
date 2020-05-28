---
title: "Date Handling in the SoftLayer API"
description: "Working with datatypes from the SoftLayer API"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---


Most of the data presented in the SoftLayer API is date-sensitive. Servers have provision dates, tickets have modify dates, and nearly everything has a creation date. To maintain compliancy and consistency standards for all of our users worldwide, SoftLayer presents its dates in [http://www.iso.org/iso/date_and_time_format ISO 8601] format under the data type ''dateTime''. ISO 8601 represents a complete date including date, time and time zone. Every data type property in the SoftLayer API that ends with the string "Date" is represented by the ''dateTime'' format.

## The dateTime Datatype
The `dateTime` data type uses the following format:  `<YYYY>-<MM>-<DD>T<HH>:<MM>:<SS>-<TZ>`

For example the `dateTime` value `'2007-07-19T15:21:48-05:00'` translates to:
`July 19, 2007, 3:21:48 P.M., GMT -0500`

Refer to the information below for more information regarding the data represented in the dateTime data type:

+ `YYYY`:  A four digit representation of the year
+ `MM`:  A two digit representation of the month, including a leading zero, if applicable.  (Acceptable range of 01 to 12)
+ `DD`:  A two digit representation of the day, including a leading zero, if applicable.  (Acceptable range of 01 to 31)
+ `HH`:  A two digit representation of the hour in 24-hour format, including a leading zero, if applicable.  (Acceptable range of 00 to 23)
+ `MM`:  A two digit representation of the minute, including a leading zero, if applicable.  (Acceptable range of 00-59)</li>
+ `SS`:  A two digit representation of the second, including a leading zero, if applicable.  (Acceptable range of 00-59)</li>
+ `TZ`:  The time zone, represented as the different between the current time zone and GMT in +/-HH:MM format.




## Setting Your Time Zone
If your API calls return incorrect times for your location, you likely need to set (or reset) the time zone and/or Daylight Savings Time options for the user making API calls. 

Data in the API is centric to the Central time zone (CST/CDT). Which means that unless you specify a timezone in your request, CST/CDT will be assumed. 


### API
To set your user's time zone using a direct API call, complete the following steps:

+ Make an api call to [SoftLayer_User_Customer::editObject](/reference/services/SoftLayer_User_Customer/editObject/)
+ Set the `timeZoneId` property in the template object passed to the call
    *Note*: Retrieve a list of time zones from[[SoftLayer_Locale_Timezone::getAllObjects](/reference/services/SoftLayer_Locale_Timezone/getAllObjects/)
+ Determine if `Daylight Savings Time` should be active for the user
    *Note*: The system defaults to an active Daylight Savings Time return
+ If Daylight Savings Time should be `active` for the user enter `1` under the `daylightSavingsTimeFlag` property
+ If Daylight Savings Time should be `inactive` for the user enter `0`under the `daylightSavingsTimeFlag` property



## External Links
[ISO 8601 Format](http://www.iso.org/iso/date_and_time_format )
