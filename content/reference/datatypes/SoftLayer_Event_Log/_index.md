---
title: "SoftLayer_Event_Log"
description: "The SoftLayer_Event_Log data type contains an event detail occurred upon various SoftLayer resources."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Event"
classes:
    - "SoftLayer_Event_Log"
---

# SoftLayer_Event_Log
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Event_Log' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Event_Log' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Event_Log data type contains an event detail occurred upon various SoftLayer resources. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
    <div id="localProperties" class="prop-content" >
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>Account id with which the event is associated  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#eventCreateDate" name=eventCreateDate>eventCreateDate</a>
            </span>
            <div class='views-field-body'>Event creation date in millisecond precision  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#eventName" name=eventName>eventName</a>
            </span>
            <div class='views-field-body'>Event name such as "reboot", "cancel", "update host" and so on.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ipAddress" name=ipAddress>ipAddress</a>
            </span>
            <div class='views-field-body'>The remote IP Address that made the request  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#label" name=label>label</a>
            </span>
            <div class='views-field-body'>Label or description of the event object  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#metaData" name=metaData>metaData</a>
            </span>
            <div class='views-field-body'>Meta data for an event in JSON string  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>JSON string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#objectId" name=objectId>objectId</a>
            </span>
            <div class='views-field-body'>Event object id  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#objectName" name=objectName>objectName</a>
            </span>
            <div class='views-field-body'>Event object name such as "server", "dns" and so on.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#openIdConnectUserName" name=openIdConnectUserName>openIdConnectUserName</a>
            </span>
            <div class='views-field-body'>OpenIdConnectUserName of the customer who initiated the event  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resource" name=resource>resource</a>
            </span>
            <div class='views-field-body'>A resource object that is associated with the event </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#traceId" name=traceId>traceId</a>
            </span>
            <div class='views-field-body'>A unique trace id. Multiple event can be grouped by a trace id.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userId" name=userId>userId</a>
            </span>
            <div class='views-field-body'>Id of customer who initiated the event  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userType" name=userType>userType</a>
            </span>
            <div class='views-field-body'>Type of user that triggered the event. User type can be CUSTOMER, EMPLOYEE or SYSTEM.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#username" name=username>username</a>
            </span>
            <div class='views-field-body'>Customer username who initiated the event  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#user" name=user>user</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


