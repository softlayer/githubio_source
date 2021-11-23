---
title: "getHistoricalUptimeGraph"
description: "The graph image is returned as a base64 PNG string. Start and end dates should be formatted using the ISO 8601 date standard. If there is an error retrieving graph data or generating the graph string a graphError attribute will be returned. The graphError attribute may contain any of the following error messages: SoftLayer_Exception_Public Thrown if an invalid start or end date is provided. SoftLayer_Exception Thrown if there is an error connecting to HBase. SoftLayer_Exception Thrown if there is no data available for the specified date range. SoftLayer_Exception Thrown if there is an error retrieving data or generating the graph. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "getHistoricalUptimeGraph"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---
