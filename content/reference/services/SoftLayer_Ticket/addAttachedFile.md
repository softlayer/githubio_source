---
title: "addAttachedFile"
description: "Attach the given file to a SoftLayer ticket. A file attachment is a convenient way to submit non-textual error reports to SoftLayer employees in a ticket. File attachments to tickets must have a unique name. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Utility_File_Attachment]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/addAttachedFile'
```
