---
title: "getResultFile"
description: "Attempt to retrieve the file associated with a benchmark certification result, if such a file exists.  If there is no file for this benchmark certification result, calling this method throws an exception. The 'getResultFile' method attempts to retrieve the file associated with a benchmark certification result, if such a file exists. If no file exists for the benchmark certification, an exception is thrown. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Benchmark_Certification"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Benchmark_Certification"
---

# [REST Example](#getResultFile-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getResultFile-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Benchmark_Certification/{SoftLayer_Hardware_Benchmark_CertificationID}/getResultFile'
```
