---
title: "enableEuSupport"
description: "<p> If you select the EU Supported option, the most common Support issues will be limited to IBM Cloud staff located in the EU.  In the event your issue requires non-EU expert assistance, it will be reviewed and approval given prior to any non-EU intervention.  Additionally, in order to support and update the services, cross-border Processing of your data may still occur.  Please ensure you take the necessary actions to allow this Processing, as detailed in the <strong><a href='http://www-03.ibm.com/software/sla/sladb.nsf/sla/bm-6605-12'>Cloud Service Terms</a></strong>. A standard Data Processing Addendum is available <strong><a href='https://www-05.ibm.com/support/operations/zz/en/dpa.html'>here</a></strong>. </p> 

<p> <strong>Important note (you will only see this once):</strong> Orders using the API will proceed without additional notifications. The terms related to selecting products, services, or locations outside the EU apply to API orders. Users you create and API keys you generate will have the ability to order products, services, and locations outside of the EU. It is your responsibility to educate anyone you grant access to your account on the consequences and requirements if they make a selection that is not in the EU Supported option.  In order to meet EU Supported requirements, the current PPTP VPN solution will no longer be offered or supported. </p> 

<p> If PPTP has been selected as an option for any users in your account by itself (or in combination with another VPN offering), you will need to disable PPTP before selecting the EU Supported account feature. For more information on VPN changes, click <strong><a href='http://knowledgelayer.softlayer.com/procedure/activate-or-deactivate-pptp-vpn-access-user'> here</a></strong>. </p> "
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

### [REST Example](#enableEuSupport-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#enableEuSupport-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/enableEuSupport'
```
