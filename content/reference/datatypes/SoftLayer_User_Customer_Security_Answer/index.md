---
title: "SoftLayer_User_Customer_Security_Answer"
description: "The SoftLayer_User_Customer_Security_Answer type contains user's answers to security questions."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Security_Answer"
---

# SoftLayer_User_Customer_Security_Answer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_Security_Answer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Security_Answer' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_Customer_Security_Answer type contains user's answers to security questions.
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
            <span class='views-field-title'><a href="#answer" name=answer>answer</a></span>
            <div class='views-field-body'>A user's answer. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A user's answer identifying number. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#questionId" name=questionId>questionId</a></span>
            <div class='views-field-body'>A user's question identifying number. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userId" name=userId>userId</a></span>
            <div class='views-field-body'>A user's identifying number. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#question" name=question>question</a></span>
            <div class='views-field-body'>The question the security answer is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#user" name=user>user</a></span>
            <div class='views-field-body'>The user who the security answer belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
            </div>
</div>


