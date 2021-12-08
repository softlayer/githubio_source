---
title: "SoftLayer_Container_User_Customer_PasswordSet"
description: "Container for holding information necessary for the setting and resetting of customer passwords"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_User_Customer_PasswordSet"
---

# SoftLayer_Container_User_Customer_PasswordSet
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_User_Customer_PasswordSet' >Datatype</a></li>
    </ul>
</div>

## Description 


Container for holding information necessary for the setting and resetting of customer passwords 





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
[answeredSecurityQuestionId]: #answeredsecurityquestionid
#### [answeredSecurityQuestionId]
Id of SoftLayer_User_Security_Question.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[authenticationMethods]: #authenticationmethods
#### [authenticationMethods]
The authentication methods required.  
<span class="type-label">Type: </span>**array of integers**  



</div>
<div class="prop-row">

-----
[digitCountRequirement]: #digitcountrequirement
#### [digitCountRequirement]
The number of digits required.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[key]: #key
#### [key]
The password key provided to user in the password set url link sent via email.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[lowercaseCountRequirement]: #lowercasecountrequirement
#### [lowercaseCountRequirement]
The number of lowercase letters required.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[maximumPasswordLengthRequirement]: #maximumpasswordlengthrequirement
#### [maximumPasswordLengthRequirement]
The maximum password length requirement.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[minimumPasswordLengthRequirement]: #minimumpasswordlengthrequirement
#### [minimumPasswordLengthRequirement]
The minimum password length requirement.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
The user's new password.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[securityAnswer]: #securityanswer
#### [securityAnswer]
Answer to security question provided by the user.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[securityQuestions]: #securityquestions
#### [securityQuestions]
Array of SoftLayer_User_Security_Question.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Security_Question'>SoftLayer_User_Security_Question[] </a>**  



</div>
<div class="prop-row">

-----
[specialCharacterCountRequirement]: #specialcharactercountrequirement
#### [specialCharacterCountRequirement]
The number of special characters required.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[specialCharactersAllowed]: #specialcharactersallowed
#### [specialCharactersAllowed]
List of the allowed special characters.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[uppercaseCountRequirement]: #uppercasecountrequirement
#### [uppercaseCountRequirement]
The number of uppercase letters required.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
The id of the user to authenticate.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


