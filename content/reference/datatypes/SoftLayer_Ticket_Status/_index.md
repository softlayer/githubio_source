---
title: "SoftLayer_Ticket_Status"
description: "The SoftLayer_Ticket_Status data type models the state of a ticket as it is worked by SoftLayer and its customers. Ticke... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Status"
---

# SoftLayer_Ticket_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Ticket_Status data type models the state of a ticket as it is worked by SoftLayer and its customers. Tickets exist in one of three states: 
*'''OPEN''': Open tickets are considered unresolved issues by SoftLayer and can be assigned to a SoftLayer employee for work. Tickets created by portal or API users are created in the Open state.
*'''ASSIGNED''': Assigned tickets are identical to open tickets, but are assigned to an individual SoftLayer employee. An assigned ticket is actively being worked by SoftLayer.
*'''CLOSED''': Tickets are closed when the issue at hand is considered resolved. A SoftLayer employee can change a ticket's status from Closed to Open or Assigned if the need arises.


A ticket usually goes from the Open to Assigned to Closed states during its life cycle. If a ticket is forwarded from one department to another it may change from the Assigned state back to Open until it is assigned to a member of the new department. 



### seeAlso

* [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket )




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
[id]: #id
#### [id]
A ticket status' internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A ticket status' name.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


