---
title: "getObject"
description: "getObject retrieves the SoftLayer_Survey object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Survey service. You can only retrieve the survey that your portal user has taken. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Survey"
classes:
    - "SoftLayer_Survey"
type: "reference"
layout: "method"
mainService : "SoftLayer_Survey"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Survey/{SoftLayer_SurveyID}/getObject'
```
