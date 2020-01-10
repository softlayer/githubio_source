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


### associatedMethods

*  [SoftLayer_User_Customer::getSecurityAnswers](/reference/services/SoftLayer_User_Customer/getSecurityAnswers )
*  [SoftLayer_User_Customer_Security_Answer::getObject](/reference/services/SoftLayer_User_Customer_Security_Answer/getObject )



### seeAlso

* [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer )


* [SoftLayer_User_Security_Question](/reference/services/SoftLayer_User_Security_Question )




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
A user's answer.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A user's answer identifying number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[questionId]: #questionid
#### [questionId]
A user's question identifying number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
A user's identifying number.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[question]: #question
#### [question]
The question the security answer is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question </a>**


</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
The user who the security answer belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>

## Count
</div>


