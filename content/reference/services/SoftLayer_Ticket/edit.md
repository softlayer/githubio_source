---
title: "edit"
description: "Edit a SoftLayer ticket. The edit method is two-fold. You may either edit a ticket itself, add an update to a ticket, attach up to two files to a ticket, or perform all of these tasks. The SoftLayer API ignores changes made to the ''userEditableFlag''  and ''accountId'' properties. You may not assign a ticket to a user that your API account does not have access to. You may not enter a custom title for standard support tickets, buy may do so when editing an administrative ticket. Finally, you may not close a ticket using this method. Please contact SoftLayer if you need a ticket closed. 

If you need to only add an update to a ticket then please use the [SoftLayer_Ticket::addUpdate](/reference/datatypes/$1/#$2) method in this service. Likewise if you need to only attach a file to a ticket then use the [SoftLayer_Ticket::addAttachedFile](/reference/datatypes/$1/#$2) method. The edit method exists as a convenience if you need to perform all these tasks at once. "
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
