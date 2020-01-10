---
title: "SoftLayer_Ticket"
description: "Tickets are SoftLayer's primary way to keep in touch with its customers. A ticket is an entity that describes a problem... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# SoftLayer_Ticket
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Ticket' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket' >Datatype</a></li>
    </ul>
</div>

## Description
Tickets are SoftLayer's primary way to keep in touch with its customers. A ticket is an entity that describes a problem or request and tracks a conversation between you, your account users, and SoftLayer employees relating to your problem or request. Tickets can be assigned to one of your account users, and SoftLayer can assign a ticket to a particular department (also called a ticket group) or employee. The SoftLayer_Ticket service controls your interaction with SoftLayer's ticketing system. 

Every ticket object has at least one ticket update. Ticket updates may be created by either a user or SoftLayer employee. These ticket updates record the conversation between SoftLayer and you about the issue at hand. You may only add new updates to a ticket. Once an update is created you may not edit or delete it. 

Tickets exist in one of three states: open, assigned, and closed. Open tickets are considered a current issue, but are not yet assigned to a specific SoftLayer employee. Assigned issues are open issues that are assigned to a SoftLayer employee. You can safely assume that your ticket is being handled if it is in the Assigned state. Closed tickets are considered resolved issues and allow no further updates. Please contact SoftLayer if you need to re-open a ticket, as you may only create ticket updates on open or assigned tickets. 

It is possible to attach files and associate hardware with a ticket. Associating your ticket with more than one pieces of hardware helps SoftLayer's support team localize issues to certain servers. Attachments are a good way to illustrate a point, such as adding a screen shot of a problem or attaching a driver or configuration file that you'd like investigated. 

Typically the only tickets an account user may create are technical support tickets. Technical support tickets are divided into two categories: standard tickets and administrative tickets. A standard support ticket describes an issue with your SoftLayer server or services. Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the [SoftLayer_Ticket_Subject]({{<ref "reference/datatypes/SoftLayer_Ticket_Subject">}}) service. If you need a little help from SoftLayer's support staff to manage your server then open an administrative support ticket. Administrative tickets add a one-time $3USD charge to your account, and you may specify your ticket's title as needed. 



### seeAlso

* [SoftLayer_Ticket_Update_Customer](/reference/datatypes/SoftLayer_Ticket_Update_Customer )


* [SoftLayer_Ticket_Update_Employee](/reference/services/SoftLayer_Ticket_Update_Employee )


* [SoftLayer_Ticket_Attachment_Hardware](/reference/datatypes/SoftLayer_Ticket_Attachment_Hardware )


* [SoftLayer_Ticket_Attachment_File](/reference/services/SoftLayer_Ticket_Attachment_File )


* [SoftLayer_Ticket_Group](/reference/datatypes/SoftLayer_Ticket_Group )


* [SoftLayer_Ticket_Status](/reference/datatypes/SoftLayer_Ticket_Status )


* [SoftLayer_Ticket_Subject](/reference/services/SoftLayer_Ticket_Subject )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [addAssignedAgent](/reference/services/SoftLayer_Ticket/addAssignedAgent)
Assign an Agent to a ticket.
</div>

<div class="method-row">

#### [addAttachedAdditionalEmails](/reference/services/SoftLayer_Ticket/addAttachedAdditionalEmails)
Add non-user email addresses to a ticket's email notify list.
</div>

<div class="method-row">

#### [addAttachedDedicatedHost](/reference/services/SoftLayer_Ticket/addAttachedDedicatedHost)
Attach a Dedicated Host to a ticket.
</div>

<div class="method-row">

#### [addAttachedFile](/reference/services/SoftLayer_Ticket/addAttachedFile)
Attach a file to a ticket.
</div>

<div class="method-row">

#### [addAttachedHardware](/reference/services/SoftLayer_Ticket/addAttachedHardware)
Attach hardware to a ticket.
</div>

<div class="method-row">

#### [addAttachedVirtualGuest](/reference/services/SoftLayer_Ticket/addAttachedVirtualGuest)
Attach a CloudLayer Computing Instance to a ticket.
</div>

<div class="method-row">

#### [addFinalComments](/reference/services/SoftLayer_Ticket/addFinalComments)
Add final comments to a closed ticket.
</div>

<div class="method-row">

#### [addScheduledAlert](/reference/services/SoftLayer_Ticket/addScheduledAlert)

</div>

<div class="method-row">

#### [addScheduledAutoClose](/reference/services/SoftLayer_Ticket/addScheduledAutoClose)

</div>

<div class="method-row">

#### [addUpdate](/reference/services/SoftLayer_Ticket/addUpdate)
Add an update to a ticket.
</div>

<div class="method-row">

#### [createAdministrativeTicket](/reference/services/SoftLayer_Ticket/createAdministrativeTicket)
Create an administrative support ticket.
</div>

<div class="method-row">

#### [createCancelServerTicket](/reference/services/SoftLayer_Ticket/createCancelServerTicket)
Create a sales cancel server ticket to be cancelled on next bill date.
</div>

<div class="method-row">

#### [createCancelServiceTicket](/reference/services/SoftLayer_Ticket/createCancelServiceTicket)
Create a sales cancel service ticket.
</div>

<div class="method-row">

#### [createStandardTicket](/reference/services/SoftLayer_Ticket/createStandardTicket)
Create a standard support ticket.
</div>

<div class="method-row">

#### [createUpgradeTicket](/reference/services/SoftLayer_Ticket/createUpgradeTicket)
Create an upgrade request ticket for the SoftLayer sales team.
</div>

<div class="method-row">

#### [edit](/reference/services/SoftLayer_Ticket/edit)
Edit or update a SoftLayer ticket.
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Ticket/getAccount)
Retrieve the SoftLayer customer account associated with a ticket.
</div>

<div class="method-row">

#### [getAllTicketGroups](/reference/services/SoftLayer_Ticket/getAllTicketGroups)
Retrieve all available ticket groups. 
</div>

<div class="method-row">

#### [getAllTicketStatuses](/reference/services/SoftLayer_Ticket/getAllTicketStatuses)
Retrieve all available ticket statuses. 
</div>

<div class="method-row">

#### [getAssignedAgents](/reference/services/SoftLayer_Ticket/getAssignedAgents)

</div>

<div class="method-row">

#### [getAssignedUser](/reference/services/SoftLayer_Ticket/getAssignedUser)
Retrieve the portal user that a ticket is assigned to.
</div>

<div class="method-row">

#### [getAttachedAdditionalEmails](/reference/services/SoftLayer_Ticket/getAttachedAdditionalEmails)
Retrieve the list of additional emails to notify when a ticket update is made.
</div>

<div class="method-row">

#### [getAttachedDedicatedHosts](/reference/services/SoftLayer_Ticket/getAttachedDedicatedHosts)
Retrieve the Dedicated Hosts associated with a ticket. This is used in cases where a ticket is directly associated with one or more Dedicated Hosts.
</div>

<div class="method-row">

#### [getAttachedFile](/reference/services/SoftLayer_Ticket/getAttachedFile)
Retrieve a file attached to a ticket.
</div>

<div class="method-row">

#### [getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles)
Retrieve the files attached to a ticket.
</div>

<div class="method-row">

#### [getAttachedHardware](/reference/services/SoftLayer_Ticket/getAttachedHardware)
Retrieve the hardware associated with a ticket. This is used in cases where a ticket is directly associated with one or more pieces of hardware.
</div>

<div class="method-row">

#### [getAttachedHardwareCount](/reference/services/SoftLayer_Ticket/getAttachedHardwareCount)

</div>

<div class="method-row">

#### [getAttachedResources](/reference/services/SoftLayer_Ticket/getAttachedResources)

</div>

<div class="method-row">

#### [getAttachedVirtualGuests](/reference/services/SoftLayer_Ticket/getAttachedVirtualGuests)
Retrieve the virtual guests associated with a ticket. This is used in cases where a ticket is directly associated with one or more virtualized guests installations or Virtual Servers.
</div>

<div class="method-row">

#### [getAwaitingUserResponseFlag](/reference/services/SoftLayer_Ticket/getAwaitingUserResponseFlag)
Retrieve ticket is waiting on a response from a customer flag.
</div>

<div class="method-row">

#### [getCancellationRequest](/reference/services/SoftLayer_Ticket/getCancellationRequest)
Retrieve a service cancellation request.
</div>

<div class="method-row">

#### [getEmployeeAttachments](/reference/services/SoftLayer_Ticket/getEmployeeAttachments)

</div>

<div class="method-row">

#### [getEuSupportedFlag](/reference/services/SoftLayer_Ticket/getEuSupportedFlag)
Retrieve a ticket's associated EU compliant record
</div>

<div class="method-row">

#### [getFirstAttachedResource](/reference/services/SoftLayer_Ticket/getFirstAttachedResource)
Retrieve the first physical or virtual server attached to a ticket.
</div>

<div class="method-row">

#### [getFirstUpdate](/reference/services/SoftLayer_Ticket/getFirstUpdate)
Retrieve the first update made to a ticket. This is typically the contents of a ticket when it's created.
</div>

<div class="method-row">

#### [getGroup](/reference/services/SoftLayer_Ticket/getGroup)
Retrieve the SoftLayer department that a ticket is assigned to.
</div>

<div class="method-row">

#### [getInvoiceItems](/reference/services/SoftLayer_Ticket/getInvoiceItems)
Retrieve the invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee that has been invoiced.
</div>

<div class="method-row">

#### [getLastActivity](/reference/services/SoftLayer_Ticket/getLastActivity)

</div>

<div class="method-row">

#### [getLastEditor](/reference/services/SoftLayer_Ticket/getLastEditor)

</div>

<div class="method-row">

#### [getLastUpdate](/reference/services/SoftLayer_Ticket/getLastUpdate)
Retrieve the last update made to a ticket.
</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Ticket/getLocation)
Retrieve a ticket's associated location within the SoftLayer location hierarchy.
</div>

<div class="method-row">

#### [getNewUpdatesFlag](/reference/services/SoftLayer_Ticket/getNewUpdatesFlag)
Retrieve true if there are new, unread updates to this ticket for the current user, False otherwise.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Ticket/getObject)
Retrieve a SoftLayer_Ticket record.
</div>

<div class="method-row">

#### [getScheduledActions](/reference/services/SoftLayer_Ticket/getScheduledActions)

</div>

<div class="method-row">

#### [getServerAdministrationBillingInvoice](/reference/services/SoftLayer_Ticket/getServerAdministrationBillingInvoice)
Retrieve the invoice associated with a ticket. Only tickets with an associated administrative charge have an invoice.
</div>

<div class="method-row">

#### [getServerAdministrationRefundInvoice](/reference/services/SoftLayer_Ticket/getServerAdministrationRefundInvoice)
Retrieve the refund invoice associated with a ticket. Only tickets with a refund applied in them have an associated refund invoice.
</div>

<div class="method-row">

#### [getServiceProvider](/reference/services/SoftLayer_Ticket/getServiceProvider)

</div>

<div class="method-row">

#### [getState](/reference/services/SoftLayer_Ticket/getState)

</div>

<div class="method-row">

#### [getStatus](/reference/services/SoftLayer_Ticket/getStatus)
Retrieve a ticket's status.
</div>

<div class="method-row">

#### [getSubject](/reference/services/SoftLayer_Ticket/getSubject)
Retrieve a ticket's subject. Only standard support tickets have an associated subject. A standard support ticket's title corresponds with it's subject's name.
</div>

<div class="method-row">

#### [getTagReferences](/reference/services/SoftLayer_Ticket/getTagReferences)

</div>

<div class="method-row">

#### [getTicketsClosedSinceDate](/reference/services/SoftLayer_Ticket/getTicketsClosedSinceDate)
Retrieve tickets closed since a given date. 
</div>

<div class="method-row">

#### [getUpdateRatingFlag](/reference/services/SoftLayer_Ticket/getUpdateRatingFlag)
Retrieve whether employees' updates of this ticket could be rated by customer
</div>

<div class="method-row">

#### [getUpdates](/reference/services/SoftLayer_Ticket/getUpdates)
Retrieve a ticket's updates.
</div>

<div class="method-row">

#### [markAsViewed](/reference/services/SoftLayer_Ticket/markAsViewed)

</div>

<div class="method-row">

#### [removeAssignedAgent](/reference/services/SoftLayer_Ticket/removeAssignedAgent)
Remove an assigned agent from a ticket.
</div>

<div class="method-row">

#### [removeAttachedAdditionalEmails](/reference/services/SoftLayer_Ticket/removeAttachedAdditionalEmails)
Detaches non-user additional email addresses from a ticket.
</div>

<div class="method-row">

#### [removeAttachedHardware](/reference/services/SoftLayer_Ticket/removeAttachedHardware)
detach hardware from a ticket.
</div>

<div class="method-row">

#### [removeAttachedVirtualGuest](/reference/services/SoftLayer_Ticket/removeAttachedVirtualGuest)
Detach a CloudLayer Computing Instance from a ticket.
</div>

<div class="method-row">

#### [removeScheduledAlert](/reference/services/SoftLayer_Ticket/removeScheduledAlert)

</div>

<div class="method-row">

#### [removeScheduledAutoClose](/reference/services/SoftLayer_Ticket/removeScheduledAutoClose)

</div>

<div class="method-row">

#### [setTags](/reference/services/SoftLayer_Ticket/setTags)

</div>

<div class="method-row">

#### [surveyEligible](/reference/services/SoftLayer_Ticket/surveyEligible)

</div>

<div class="method-row">

#### [updateAttachedAdditionalEmails](/reference/services/SoftLayer_Ticket/updateAttachedAdditionalEmails)
Update non-user email addresses attached to a ticket's email notify list.
</div>
</div>

</div>

