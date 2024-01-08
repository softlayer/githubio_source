---
title: "runPassmarkCertificationBenchmark"
description: "You can launch a new Passmark hardware test by selecting from your server list. It will bring your server offline for approximately 20 minutes while the testing is in progress, and will publish a certificate with the results to your hardware details page. 

While the hard drives are tested for the initial deployment, the Passmark Certificate utility will not test the hard drives on your live server. This is to ensure that no data is overwritten. If you would like to test the server's hard drives, you can have the full Passmark suite installed to your server free of charge through a new Support ticket. 

While the test itself does not overwrite any data on the server, it is recommended that you make full off-server backups of all data prior to launching the test. The Passmark hardware test is designed to force any latent hardware issues to the surface, so hardware failure is possible. 

In the event of a hardware failure during this test our datacenter engineers will be notified of the problem automatically. They will then replace any failed components to bring your server back online, and will be contacting you to ensure that impact on your server is minimal. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

### [REST Example](#runPassmarkCertificationBenchmark-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#runPassmarkCertificationBenchmark-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/runPassmarkCertificationBenchmark'
```
