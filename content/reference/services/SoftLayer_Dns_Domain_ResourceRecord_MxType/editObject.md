---
title: "editObject"
description: "editObject edits an existing MX resource record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for '@', '_', '.', '*', and '-'. The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for '.' and '-'. Editing an MX record updates the serial number of the domain the record is associated with. 

''editObject'' returns Boolean ''true'' on a successful edit or ''false'' if it was unable to edit the resource record. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "editObject"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_ResourceRecord_MxType"
---
