---
title: "SoftLayer_Ticket_Status"
description: "The SoftLayer_Ticket_Status data type models the state of a ticket as it is worked by SoftLayer and its customers. Tickets exist in one of three states: 
*'''OPEN''': Open tickets are considered unresolved issues by SoftLayer and can be assigned to a SoftLayer employee for work. Tickets created by portal or API users are created in the Open state.
*'''ASSIGNED''': Assigned tickets are identical to open tickets, but are assigned to an individual SoftLayer employee. An assigned ticket is actively being worked by SoftLayer.
*'''CLOSED''': Tickets are closed when the issue at hand is considered resolved. A SoftLayer employee can change a ticket's status from Closed to Open or Assigned if the need arises.


A ticket usually goes from the Open to Assigned to Closed states during its life cycle. If a ticket is forwarded from one department to another it may change from the Assigned state back to Open until it is assigned to a member of the new department. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Status"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Ticket_Status"
---
