---
title: "SoftLayer_Survey_Answer"
description: "The SoftLayer_Survey_Answer data type contains general information relating to a single SoftLayer survey answer."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Survey"
classes:
    - "SoftLayer_Survey_Answer"
---

# SoftLayer_Survey_Answer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Survey_Answer' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Survey_Answer data type contains general information relating to a single SoftLayer survey answer. 
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
            <div class='views-field-body'>A survey answer's answer that a user can response too. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#answerOrder" name=answerOrder>answerOrder</a></span>
            <div class='views-field-body'>A value indicating the order in when a survey answer will be displayed to a user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A survey answer's Id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#surveyQuestionId" name=surveyQuestionId>surveyQuestionId</a></span>
            <div class='views-field-body'>A survey answer's associated [[SoftLayer_Survey_Question|Survey Question]] Id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#surveyQuestion" name=surveyQuestion>surveyQuestion</a></span>
            <div class='views-field-body'>The survey question that this answer belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Survey_Question'>SoftLayer_Survey_Question </a></p></div>
        </div>
            </div>
</div>


