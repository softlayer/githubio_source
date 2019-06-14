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

Typically the only tickets an account user may create are technical support tickets. Technical support tickets are divided into two categories: standard tickets and administrative tickets. A standard support ticket describes an issue with your SoftLayer server or services. Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the [[SoftLayer_Ticket_Subject]] service. If you need a little help from SoftLayer's support staff to manage your server then open an administrative support ticket. Administrative tickets add a one-time $3USD charge to your account, and you may specify your ticket's title as needed. 



### seeAlso

* [SoftLayer_Ticket_Update_Customer](/reference/datatypes/SoftLayer_Ticket_Update_Customer )


* [SoftLayer_Ticket_Update_Employee](/reference/datatypes/SoftLayer_Ticket_Update_Employee )


* [SoftLayer_Ticket_Attachment_Hardware](/reference/datatypes/SoftLayer_Ticket_Attachment_Hardware )


* [SoftLayer_Ticket_Attachment_File](/reference/datatypes/SoftLayer_Ticket_Attachment_File )


* [SoftLayer_Ticket_Group](/reference/datatypes/SoftLayer_Ticket_Group )


* [SoftLayer_Ticket_Status](/reference/datatypes/SoftLayer_Ticket_Status )


* [SoftLayer_Ticket_Subject](/reference/datatypes/SoftLayer_Ticket_Subject )


        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addAssignedAgent'> addAssignedAgent</a> </span>
            <div class='views-field-body'>Assign an Agent to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addAttachedAdditionalEmails'> addAttachedAdditionalEmails</a> </span>
            <div class='views-field-body'>Add non-user email addresses to a ticket's email notify list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addAttachedDedicatedHost'> addAttachedDedicatedHost</a> </span>
            <div class='views-field-body'>Attach a Dedicated Host to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addAttachedFile'> addAttachedFile</a> </span>
            <div class='views-field-body'>Attach a file to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addAttachedHardware'> addAttachedHardware</a> </span>
            <div class='views-field-body'>Attach hardware to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addAttachedVirtualGuest'> addAttachedVirtualGuest</a> </span>
            <div class='views-field-body'>Attach a CloudLayer Computing Instance to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addFinalComments'> addFinalComments</a> </span>
            <div class='views-field-body'>Add final comments to a closed ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addScheduledAlert'> addScheduledAlert</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addScheduledAutoClose'> addScheduledAutoClose</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/addUpdate'> addUpdate</a> </span>
            <div class='views-field-body'>Add an update to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/createAdministrativeTicket'> createAdministrativeTicket</a> </span>
            <div class='views-field-body'>Create an administrative support ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/createCancelServerTicket'> createCancelServerTicket</a> </span>
            <div class='views-field-body'>Create a sales cancel server ticket to be cancelled on next bill date.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/createCancelServiceTicket'> createCancelServiceTicket</a> </span>
            <div class='views-field-body'>Create a sales cancel service ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/createStandardTicket'> createStandardTicket</a> </span>
            <div class='views-field-body'>Create a standard support ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/createUpgradeTicket'> createUpgradeTicket</a> </span>
            <div class='views-field-body'>Create an upgrade request ticket for the SoftLayer sales team.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/edit'> edit</a> </span>
            <div class='views-field-body'>Edit or update a SoftLayer ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer customer account associated with a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAllTicketGroups'> getAllTicketGroups</a> </span>
            <div class='views-field-body'>Retrieve all available ticket groups. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAllTicketStatuses'> getAllTicketStatuses</a> </span>
            <div class='views-field-body'>Retrieve all available ticket statuses. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAssignedAgents'> getAssignedAgents</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAssignedUser'> getAssignedUser</a> </span>
            <div class='views-field-body'>Retrieve the portal user that a ticket is assigned to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedAdditionalEmails'> getAttachedAdditionalEmails</a> </span>
            <div class='views-field-body'>Retrieve the list of additional emails to notify when a ticket update is made.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedDedicatedHosts'> getAttachedDedicatedHosts</a> </span>
            <div class='views-field-body'>Retrieve the Dedicated Hosts associated with a ticket. This is used in cases where a ticket is directly associated with one or more Dedicated Hosts.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedFile'> getAttachedFile</a> </span>
            <div class='views-field-body'>Retrieve a file attached to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedFiles'> getAttachedFiles</a> </span>
            <div class='views-field-body'>Retrieve the files attached to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedHardware'> getAttachedHardware</a> </span>
            <div class='views-field-body'>Retrieve the hardware associated with a ticket. This is used in cases where a ticket is directly associated with one or more pieces of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedHardwareCount'> getAttachedHardwareCount</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedResources'> getAttachedResources</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAttachedVirtualGuests'> getAttachedVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve the virtual guests associated with a ticket. This is used in cases where a ticket is directly associated with one or more virtualized guests installations or Virtual Servers.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getAwaitingUserResponseFlag'> getAwaitingUserResponseFlag</a> </span>
            <div class='views-field-body'>Retrieve ticket is waiting on a response from a customer flag.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getCancellationRequest'> getCancellationRequest</a> </span>
            <div class='views-field-body'>Retrieve a service cancellation request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getEmployeeAttachments'> getEmployeeAttachments</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getEuSupportedFlag'> getEuSupportedFlag</a> </span>
            <div class='views-field-body'>Retrieve a ticket's associated EU compliant record</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getFirstAttachedResource'> getFirstAttachedResource</a> </span>
            <div class='views-field-body'>Retrieve the first physical or virtual server attached to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getFirstUpdate'> getFirstUpdate</a> </span>
            <div class='views-field-body'>Retrieve the first update made to a ticket. This is typically the contents of a ticket when it's created.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getGroup'> getGroup</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer department that a ticket is assigned to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getInvoiceItems'> getInvoiceItems</a> </span>
            <div class='views-field-body'>Retrieve the invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee that has been invoiced.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getLastActivity'> getLastActivity</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getLastEditor'> getLastEditor</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getLastUpdate'> getLastUpdate</a> </span>
            <div class='views-field-body'>Retrieve the last update made to a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getLastViewedDate'> getLastViewedDate</a> </span>
            <div class='views-field-body'>Retrieve a timestamp of the last time the Ticket was viewed by the active user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getLocation'> getLocation</a> </span>
            <div class='views-field-body'>Retrieve a ticket's associated location within the SoftLayer location hierarchy.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getNewUpdatesFlag'> getNewUpdatesFlag</a> </span>
            <div class='views-field-body'>Retrieve true if there are new, unread updates to this ticket for the current user, False otherwise.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Ticket record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getScheduledActions'> getScheduledActions</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getServerAdministrationBillingInvoice'> getServerAdministrationBillingInvoice</a> </span>
            <div class='views-field-body'>Retrieve the invoice associated with a ticket. Only tickets with an associated administrative charge have an invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getServerAdministrationRefundInvoice'> getServerAdministrationRefundInvoice</a> </span>
            <div class='views-field-body'>Retrieve the refund invoice associated with a ticket. Only tickets with a refund applied in them have an associated refund invoice.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getServiceProvider'> getServiceProvider</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getState'> getState</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve a ticket's status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getSubject'> getSubject</a> </span>
            <div class='views-field-body'>Retrieve a ticket's subject. Only standard support tickets have an associated subject. A standard support ticket's title corresponds with it's subject's name.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getTagReferences'> getTagReferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getTicketsClosedSinceDate'> getTicketsClosedSinceDate</a> </span>
            <div class='views-field-body'>Retrieve tickets closed since a given date. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getUpdateRatingFlag'> getUpdateRatingFlag</a> </span>
            <div class='views-field-body'>Retrieve whether employees' updates of this ticket could be rated by customer</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/getUpdates'> getUpdates</a> </span>
            <div class='views-field-body'>Retrieve a ticket's updates.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/markAsViewed'> markAsViewed</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/removeAssignedAgent'> removeAssignedAgent</a> </span>
            <div class='views-field-body'>Remove an assigned agent from a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/removeAttachedAdditionalEmails'> removeAttachedAdditionalEmails</a> </span>
            <div class='views-field-body'>Detaches non-user additional email addresses from a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/removeAttachedHardware'> removeAttachedHardware</a> </span>
            <div class='views-field-body'>detach hardware from a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/removeAttachedVirtualGuest'> removeAttachedVirtualGuest</a> </span>
            <div class='views-field-body'>Detach a CloudLayer Computing Instance from a ticket.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/removeScheduledAlert'> removeScheduledAlert</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/removeScheduledAutoClose'> removeScheduledAutoClose</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/setTags'> setTags</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/surveyEligible'> surveyEligible</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Ticket/updateAttachedAdditionalEmails'> updateAttachedAdditionalEmails</a> </span>
            <div class='views-field-body'>Update non-user email addresses attached to a ticket's email notify list.</div>
        </div>
        </div>
</div>

