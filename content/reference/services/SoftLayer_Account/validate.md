---
title: "validate"
description: "This method will validate the following account fields. Included are the allowed characters for each field.<br> <strong>Company Name (required):</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, comma, colon, at sign, ampersand, underscore, apostrophe, parenthesis, exclamation point. Maximum length: 100 characters. (Note: may not contain an email address)<br> <strong>First Name (required):</strong> alphabet, space, period, dash, comma, apostrophe. Maximum length: 30 characters.<br> <strong>Last Name (required):</strong> alphabet, space, period, dash, comma, apostrophe. Maximum length: 30 characters.<br> <strong>Email (required):</strong> Validates e-mail addresses against the syntax in RFC 822.<br> <strong>Address 1 (required):</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, comma, colon, at sign, ampersand, underscore, apostrophe, parentheses. Maximum length: 100 characters. (Note: may not contain an email address)<br> <strong>Address 2:</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, comma, colon, at sign, ampersand, underscore, apostrophe, parentheses. Maximum length: 100 characters. (Note: may not contain an email address)<br> <strong>City (required):</strong> alphabet, numbers, space, period, dash, apostrophe, forward slash, comma, parenthesis. Maximum length: 100 characters.<br> <strong>State (required if country is US, Brazil, Canada or India):</strong> Must be valid Alpha-2 ISO 3166-1 state code for that country.<br> <strong>Postal Code (required if country is US or Canada):</strong> Accepted characters are alphabet, numbers, dash, space. Maximum length: 50 characters.<br> <strong>Country (required):</strong> alphabet, numbers. Must be valid Alpha-2 ISO 3166-1 country code.<br> <strong>Office Phone (required):</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign. Maximum length: 100 characters.<br> <strong>Alternate Phone:</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign. Maximum length: 100 characters.<br> <strong>Fax Phone:</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign. Maximum length: 20 characters.<br> "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### [REST Example](#validate-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validate-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/validate'
```
