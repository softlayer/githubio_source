---
title: "SoftLayer_Container_Account_ProofOfConcept_Review_History"
description: "Summary of review activity for a proof of concept request."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_ProofOfConcept_Review_History"
---

# SoftLayer_Container_Account_ProofOfConcept_Review_History
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review_History' >Datatype</a></li>
    </ul>
</div>

## Description 
Summary of review activity for a proof of concept request. 





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
                <a href="#accountCreatedFlag" name=accountCreatedFlag>accountCreatedFlag</a>
            </span>
            <div class='views-field-body'>True for approved requests associated with a new account and false otherwise. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#deniedFlag" name=deniedFlag>deniedFlag</a>
            </span>
            <div class='views-field-body'>True for denied requests and false otherwise. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#events" name=events>events</a>
            </span>
            <div class='views-field-body'>List of events occurring during the review. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review_Event'>SoftLayer_Container_Account_ProofOfConcept_Review_Event[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#reviewCompleteFlag" name=reviewCompleteFlag>reviewCompleteFlag</a>
            </span>
            <div class='views-field-body'>True for fully reviewed requests and false otherwise. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
    </div>


