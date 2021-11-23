---
title: "SoftLayer_Ticket"
description: "Tickets are SoftLayer's primary way to keep in touch with its customers. A ticket is an entity that describes a problem or request and tracks a conversation between you, your account users, and SoftLayer employees relating to your problem or request. Tickets can be assigned to one of your account users, and SoftLayer can assign a ticket to a particular department (also called a ticket group) or employee. The SoftLayer_Ticket service controls your interaction with SoftLayer's ticketing system. 

Every ticket object has at least one ticket update. Ticket updates may be created by either a user or SoftLayer employee. These ticket updates record the conversation between SoftLayer and you about the issue at hand. You may only add new updates to a ticket. Once an update is created you may not edit or delete it. 

Tickets exist in one of three states: open, assigned, and closed. Open tickets are considered a current issue, but are not yet assigned to a specific SoftLayer employee. Assigned issues are open issues that are assigned to a SoftLayer employee. You can safely assume that your ticket is being handled if it is in the Assigned state. Closed tickets are considered resolved issues and allow no further updates. Please contact SoftLayer if you need to re-open a ticket, as you may only create ticket updates on open or assigned tickets. 

It is possible to attach files and associate hardware with a ticket. Associating your ticket with more than one pieces of hardware helps SoftLayer's support team localize issues to certain servers. Attachments are a good way to illustrate a point, such as adding a screen shot of a problem or attaching a driver or configuration file that you'd like investigated. 

Typically the only tickets an account user may create are technical support tickets. Technical support tickets are divided into two categories: standard tickets and administrative tickets. A standard support ticket describes an issue with your SoftLayer server or services. Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the [[SoftLayer_Ticket_Subject]] service. If you need a little help from SoftLayer's support staff to manage your server then open an administrative support ticket. Administrative tickets add a one-time $3USD charge to your account, and you may specify your ticket's title as needed. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
type: "reference"
layout: "service"
mainService : "SoftLayer_Ticket"
---
