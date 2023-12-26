---
title: "getTopFiveKnowledgeLayerQuestions"
description: "SoftLayer maintains relationships between the generic subjects for standard administration and the top five commonly asked questions about these subjects. getTopFileKnowledgeLayerQuestions() retrieves the top five questions and answers from the SoftLayer KnowledgeLayer related to the given ticket subject. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Subject"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket_Subject"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket_Subject/{SoftLayer_Ticket_SubjectID}/getTopFiveKnowledgeLayerQuestions'
```
