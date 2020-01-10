---
title: "SoftLayer_Container_KnowledgeLayer_QuestionAnswer"
description: "SoftLayer_Container_KnowledgeLayer_QuestionAnswer models a single question and answer pair from SoftLayer's KnowledgeLay... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_KnowledgeLayer_QuestionAnswer"
---

# SoftLayer_Container_KnowledgeLayer_QuestionAnswer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_KnowledgeLayer_QuestionAnswer' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_KnowledgeLayer_QuestionAnswer models a single question and answer pair from SoftLayer's KnowledgeLayer knowledge base. SoftLayer's backend network interfaces with the KnowledgeLayer to recommend helpful articles when support tickets are created. 

### External Links


* [The SoftLayer Knowledge Layer](http://knowledgelayer.softlayer.com/)



### associatedMethods

*  [SoftLayer_Ticket_Subject::getTopFiveKnowledgeLayerQuestions](/reference/services/SoftLayer_Ticket_Subject/getTopFiveKnowledgeLayerQuestions )





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
[answer]: #answer
#### [answer]
The answer to a question asked on the SoftLayer KnowledgeLayer.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[link]: #link
#### [link]
The link to a question asked on the SoftLayer KnowledgeLayer.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[question]: #question
#### [question]
A question asked on the SoftLayer KnowledgeLayer.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


