---
title: "SoftLayer_Container_Authentication_Response_Common"
description: "The SoftLayer_Container_Authentication_Response_Common data type contains common information for responses from the getP... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Response_Common"
---

# SoftLayer_Container_Authentication_Response_Common
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Common' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Authentication_Response_Common data type contains common information for responses from the getPortalLogin API. This is an abstract class that serves as a base that more specialized classes will derive from. For example, a response class that is specific to a successful response from the getPortalLogin API. 





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
            <span class='views-field-title'><a href="#accounts" name=accounts>accounts</a></span>
            <div class='views-field-body'>The list of linked accounts for the authenticated SoftLayer customer portal user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Account'>SoftLayer_Container_Authentication_Response_Account[] </a></p></div>
        </div>
            </div>
    </div>


