---
title: "SoftLayer_Ticket"
description: "The SoftLayer_Ticket data type models a single SoftLayer customer support or notification ticket. Each ticket object con... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_Ticket data type models a single SoftLayer customer support or notification ticket. Each ticket object contains references to it's updates, the user it's assigned to, the SoftLayer department and employee that it's assigned to, and any hardware objects or attached files associated with the ticket. Tickets are described in further detail on the [SoftLayer_Ticket]({{<ref "reference/datatypes/SoftLayer_Ticket">}}) service page. 

To create a support ticket execute the [SoftLayer_Ticket::createStandardTicket]({{<ref "reference/services/SoftLayer_Ticket/createStandardTicket">}}). 


### associatedMethods

*  [SoftLayer_Account::getTickets](/reference/services/SoftLayer_Account/getTickets )
*  [SoftLayer_Account::getOpenTickets](/reference/services/SoftLayer_Account/getOpenTickets )
*  [SoftLayer_Account::getClosedTickets](/reference/services/SoftLayer_Account/getClosedTickets )
*  [SoftLayer_Account::getLastFiveClosedTickets](/reference/services/SoftLayer_Account/getLastFiveClosedTickets )
*  [SoftLayer_Account::getLastFiveClosedAbuseTickets](/reference/services/SoftLayer_Account/getLastFiveClosedAbuseTickets )
*  [SoftLayer_Account::getLastFiveClosedAccountingTickets](/reference/services/SoftLayer_Account/getLastFiveClosedAccountingTickets )
*  [SoftLayer_Account::getLastFiveClosedSalesTickets](/reference/services/SoftLayer_Account/getLastFiveClosedSalesTickets )
*  [SoftLayer_Account::getLastFiveClosedSupportTickets](/reference/services/SoftLayer_Account/getLastFiveClosedSupportTickets )
*  [SoftLayer_Account::getLastFiveClosedOtherTickets](/reference/services/SoftLayer_Account/getLastFiveClosedOtherTickets )
*  [SoftLayer_Ticket::getObject](/reference/services/SoftLayer_Ticket/getObject )
*  [SoftLayer_Ticket::getTicketsClosedSinceDate](/reference/services/SoftLayer_Ticket/getTicketsClosedSinceDate )
*  [SoftLayer_Ticket::createStandardTicket](/reference/services/SoftLayer_Ticket/createStandardTicket )
*  [SoftLayer_Ticket::createAdministrativeTicket](/reference/services/SoftLayer_Ticket/createAdministrativeTicket )
*  [SoftLayer_Ticket::createUpgradeTicket](/reference/services/SoftLayer_Ticket/createUpgradeTicket )





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
An internal identifier of the SoftLayer customer account that a ticket is associated with.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[assignedUserId]: #assigneduserid
#### [assignedUserId]
An internal identifier of the portal user that a ticket is assigned to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[billableFlag]: #billableflag
#### [billableFlag]
Whether a ticket has a one-time charge associated with it. Standard tickets are free while administrative tickets typically cost $3 USD.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[bnppSupportedLocationId]: #bnppsupportedlocationid
#### [bnppSupportedLocationId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[changeOwnerFlag]: #changeownerflag
#### [changeOwnerFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that a ticket was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[euSupportedLocationId]: #eusupportedlocationid
#### [euSupportedLocationId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[finalComments]: #finalcomments
#### [finalComments]
Feedback left by a portal or API user on their experiences in a ticket. Final comments may be created after a ticket is closed.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[groupId]: #groupid
#### [groupId]
The internal identifier of the SoftLayer department that a ticket is assigned to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A ticket's internal identifier. Each ticket is defined by a unique identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[lastEditDate]: #lasteditdate
#### [lastEditDate]
The date that a ticket was last modified. A modification does not necessarily mean that an update was added.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[lastEditType]: #lastedittype
#### [lastEditType]
The type of user who last edited or updated a ticket. This is either "EMPLOYEE" or "USER".  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[lastResponseDate]: #lastresponsedate
#### [lastResponseDate]
The date that the last ticket update was made  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[locationId]: #locationid
#### [locationId]
The internal identifier of the location associated with a ticket.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that a ticket was last updated.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[notifyUserOnUpdateFlag]: #notifyuseronupdateflag
#### [notifyUserOnUpdateFlag]
Whether or not the user who owns a ticket is notified via email when a ticket is updated.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[originatingIpAddress]: #originatingipaddress
#### [originatingIpAddress]
The IP address of the user who opened a ticket.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[priority]: #priority
#### [priority]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[responsibleBrandId]: #responsiblebrandid
#### [responsibleBrandId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serverAdministrationBillingAmount]: #serveradministrationbillingamount
#### [serverAdministrationBillingAmount]
The amount of money in US Dollars ($USD) that a ticket has charged to an account. A ticket's administrative billing amount is a one time charge and only applies to administrative support tickets.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serverAdministrationBillingInvoiceId]: #serveradministrationbillinginvoiceid
#### [serverAdministrationBillingInvoiceId]
The internal identifier of the invoice associated with a ticket's administrative charge. Only tickets with an administrative charge have an associated invoice.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serverAdministrationFlag]: #serveradministrationflag
#### [serverAdministrationFlag]
Whether a ticket is a standard or an administrative support ticket. Administrative support tickets typically incur a $3 USD charge.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serverAdministrationRefundInvoiceId]: #serveradministrationrefundinvoiceid
#### [serverAdministrationRefundInvoiceId]
The internal identifier of the refund invoice associated with a ticket. Only tickets with an account refund associated with them have an associated refund invoice.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serviceProviderResourceId]: #serviceproviderresourceid
#### [serviceProviderResourceId]
A ticket's internal identifier at its service provider. Each ticket is defined by a unique identifier.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
A ticket status' internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[subjectId]: #subjectid
#### [subjectId]
An internal identifier of the pre-set subject that a ticket is associated with. Standard support tickets have a subject set while administrative tickets have a null subject. A standard support ticket's title is the name of it's associated subject.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[title]: #title
#### [title]
A ticket's title. This is typically a brief summary of the issue described in the ticket.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[totalUpdateCount]: #totalupdatecount
#### [totalUpdateCount]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[userEditableFlag]: #usereditableflag
#### [userEditableFlag]
Whether a user is able to update a ticket.  
<span class="type-label">Type: </span>**boolean**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The SoftLayer customer account associated with a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[assignedAgents]: #assignedagents
#### [assignedAgents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**


</div>
<div class="prop-row">

-----
[assignedUser]: #assigneduser
#### [assignedUser]
The portal user that a ticket is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>
<div class="prop-row">

-----
[attachedAdditionalEmails]: #attachedadditionalemails
#### [attachedAdditionalEmails]
The list of additional emails to notify when a ticket update is made.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_AdditionalEmail'>SoftLayer_User_Customer_AdditionalEmail[] </a>**


</div>
<div class="prop-row">

-----
[attachedDedicatedHosts]: #attacheddedicatedhosts
#### [attachedDedicatedHosts]
The Dedicated Hosts associated with a ticket. This is used in cases where a ticket is directly associated with one or more Dedicated Hosts.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost[] </a>**


</div>
<div class="prop-row">

-----
[attachedFiles]: #attachedfiles
#### [attachedFiles]
The files attached to a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment_File'>SoftLayer_Ticket_Attachment_File[] </a>**


</div>
<div class="prop-row">

-----
[attachedHardware]: #attachedhardware
#### [attachedHardware]
The hardware associated with a ticket. This is used in cases where a ticket is directly associated with one or more pieces of hardware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[attachedHardwareCount]: #attachedhardwarecount
#### [attachedHardwareCount]
  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[attachedResources]: #attachedresources
#### [attachedResources]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment[] </a>**


</div>
<div class="prop-row">

-----
[attachedVirtualGuests]: #attachedvirtualguests
#### [attachedVirtualGuests]
The virtual guests associated with a ticket. This is used in cases where a ticket is directly associated with one or more virtualized guests installations or Virtual Servers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[awaitingUserResponseFlag]: #awaitinguserresponseflag
#### [awaitingUserResponseFlag]
Ticket is waiting on a response from a customer flag.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[bnppSupportedFlag]: #bnppsupportedflag
#### [bnppSupportedFlag]
A ticket's associated BNPP compliant record  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[cancellationRequest]: #cancellationrequest
#### [cancellationRequest]
A service cancellation request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request </a>**


</div>
<div class="prop-row">

-----
[employeeAttachments]: #employeeattachments
#### [employeeAttachments]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee[] </a>**


</div>
<div class="prop-row">

-----
[euSupportedFlag]: #eusupportedflag
#### [euSupportedFlag]
A ticket's associated EU compliant record  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[firstAttachedResource]: #firstattachedresource
#### [firstAttachedResource]
The first physical or virtual server attached to a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Attachment'>SoftLayer_Ticket_Attachment </a>**


</div>
<div class="prop-row">

-----
[firstUpdate]: #firstupdate
#### [firstUpdate]
The first update made to a ticket. This is typically the contents of a ticket when it's created.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update </a>**


</div>
<div class="prop-row">

-----
[fsboaSupportedFlag]: #fsboasupportedflag
#### [fsboaSupportedFlag]
A ticket's associated FSBOA compliant record  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[group]: #group
#### [group]
The SoftLayer department that a ticket is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Group'>SoftLayer_Ticket_Group </a>**


</div>
<div class="prop-row">

-----
[invoiceItems]: #invoiceitems
#### [invoiceItems]
The invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee that has been invoiced.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**


</div>
<div class="prop-row">

-----
[lastActivity]: #lastactivity
#### [lastActivity]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Activity'>SoftLayer_Ticket_Activity </a>**


</div>
<div class="prop-row">

-----
[lastEditor]: #lasteditor
#### [lastEditor]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Interface'>SoftLayer_User_Interface </a>**


</div>
<div class="prop-row">

-----
[lastUpdate]: #lastupdate
#### [lastUpdate]
The last update made to a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
A ticket's associated location within the SoftLayer location hierarchy.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[newUpdatesFlag]: #newupdatesflag
#### [newUpdatesFlag]
True if there are new, unread updates to this ticket for the current user, False otherwise.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[scheduledActions]: #scheduledactions
#### [scheduledActions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**


</div>
<div class="prop-row">

-----
[serverAdministrationBillingInvoice]: #serveradministrationbillinginvoice
#### [serverAdministrationBillingInvoice]
The invoice associated with a ticket. Only tickets with an associated administrative charge have an invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**


</div>
<div class="prop-row">

-----
[serverAdministrationRefundInvoice]: #serveradministrationrefundinvoice
#### [serverAdministrationRefundInvoice]
The refund invoice associated with a ticket. Only tickets with a refund applied in them have an associated refund invoice.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**


</div>
<div class="prop-row">

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**


</div>
<div class="prop-row">

-----
[state]: #state
#### [state]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_State'>SoftLayer_Ticket_State[] </a>**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
A ticket's status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Status'>SoftLayer_Ticket_Status </a>**


</div>
<div class="prop-row">

-----
[subject]: #subject
#### [subject]
A ticket's subject. Only standard support tickets have an associated subject. A standard support ticket's title corresponds with it's subject's name.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Subject'>SoftLayer_Ticket_Subject </a>**


</div>
<div class="prop-row">

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**


</div>
<div class="prop-row">

-----
[updateRatingFlag]: #updateratingflag
#### [updateRatingFlag]
Whether employees' updates of this ticket could be rated by customer  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[updates]: #updates
#### [updates]
A ticket's updates.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update[] </a>**


</div>

## Count
<div class="prop-row">

-----
[assignedAgentCount]: #assignedagentcount
#### [assignedAgentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attachedAdditionalEmailCount]: #attachedadditionalemailcount
#### [attachedAdditionalEmailCount]
A count of the list of additional emails to notify when a ticket update is made.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attachedDedicatedHostCount]: #attacheddedicatedhostcount
#### [attachedDedicatedHostCount]
A count of the Dedicated Hosts associated with a ticket. This is used in cases where a ticket is directly associated with one or more Dedicated Hosts.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attachedFileCount]: #attachedfilecount
#### [attachedFileCount]
A count of the files attached to a ticket.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attachedResourceCount]: #attachedresourcecount
#### [attachedResourceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attachedVirtualGuestCount]: #attachedvirtualguestcount
#### [attachedVirtualGuestCount]
A count of the virtual guests associated with a ticket. This is used in cases where a ticket is directly associated with one or more virtualized guests installations or Virtual Servers.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[employeeAttachmentCount]: #employeeattachmentcount
#### [employeeAttachmentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[invoiceItemCount]: #invoiceitemcount
#### [invoiceItemCount]
A count of the invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee that has been invoiced.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[scheduledActionCount]: #scheduledactioncount
#### [scheduledActionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[stateCount]: #statecount
#### [stateCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[updateCount]: #updatecount
#### [updateCount]
A count of a ticket's updates.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


