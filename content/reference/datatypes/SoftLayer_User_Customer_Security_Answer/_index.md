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

## Local
-----
[answer]: #answer
#### [answer]
A user's answer.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A user's answer identifying number.  
<span class="type-label">Type: </span>**integer**

-----
[questionId]: #questionid
#### [questionId]
A user's question identifying number.  
<span class="type-label">Type: </span>**integer**

-----
[userId]: #userid
#### [userId]
A user's identifying number.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[question]: #question
#### [question]
The question the security answer is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question </a>**

-----
[user]: #user
#### [user]
The user who the security answer belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count
</div>


