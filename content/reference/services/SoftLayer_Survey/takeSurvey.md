---
title: "takeSurvey"
description: "Response to a SoftLayer survey's questions. "
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

# [REST Example](#takeSurvey-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#takeSurvey-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Survey_Response]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Survey/{SoftLayer_SurveyID}/takeSurvey'
```
