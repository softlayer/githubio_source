---
title: "addUpdate"
description: "Add an update to a ticket. A ticket update's entry has a maximum length of 4000 characters, so ''addUpdate()'' splits the ''entry'' property in the ''templateObject'' parameter into 3900 character blocks and creates one entry per 3900 character block. Once complete ''addUpdate()'' emails the ticket's owner and additional email addresses with an update message if the ticket's ''notifyUserOnUpdateFlag'' is set. If the ticket is a Legal or Abuse ticket, then the account's abuse emails are also notified when the updates are processed. Finally, ''addUpdate()'' returns an array of the newly created ticket updates. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "addUpdate"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket"
---
