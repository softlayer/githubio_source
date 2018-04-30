---
title: "SoftLayer_Network_ContentDelivery_Account"
description: "SoftLayer_Network_ContentDelivery_Account controls a single CDN user account and that account's content hosted on SoftLa... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_ContentDelivery_Account' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Account' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer_Network_ContentDelivery_Account controls a single CDN user account and that account's content hosted on SoftLayer's CDN hosting infrastructure. Individual customer accounts can have more than one CDN account. 

Every CDN account has the capability to configure and upload content to SoftLayer's CDN infrastructure. When a user requests content from the CDN they retrieve data from the node in closest physical proximity to them, assuring failover in the case of single node failure and the lowest network latency possible. 

CDN supports three distinct types of content, streaming Flash, streaming Windows Media and traditional HTTP. Each of these types of service are automatically set depending on the folder you upload your content to. Each of these types of content are accessed from different URLs. URL examples can be found on the [https://manage.softlayer.com customer portal]. 

CDN supports directory creation, [[SoftLayer_Network_ContentDelivery_Account::getBandwidthData|bandwidth reporting]], and an [[SoftLayer_Network_ContentDelivery_Account::createOriginPullRule|Origin Pull]] rule if you wish to manage your content directly on one of your servers. Files uploaded to CDN are accessed by users in directories relative to your account's root directory. For instance, if the file "/images/header.jpg" exists in your CDN space then it can be accessed at the URL "<nowiki>http://<your CDN username>.http.cdn.softlayer.net/00<your CDN username>/images/header.jpg</nowiki>" 

CDN accounts support FTP transfers in addition to API-based uploads. To access a CDN account's FTP space on the SoftLayer private network, log into '''ftp.cdnlayer.service.softlayer.com''' with an FTP client using your CDN account name and a password set either in the SoftLayer [https://manage.softlayer.com customer portal] or by via the [[SoftLayer_Network_ContentDelivery_Account::setFtpPassword|setFtpPassword]] method 

CDN supports the content authentication service. CDN's content authentication service is the technology that allows only authorized user to access your content. It performs a token based authentication before delivering content. An authentication token can be obtained from the SoftLayer customer portal or API and it needs to be appended to the CDN URL. When an end-user requests a file, CDN server will check the validity of the token passed via HTTP GET string with a remote web service provided by SoftLayer. Then the content will be delivered if the value returned from the web service is good otherwise the connection will be rejected. The token authentication web service call is made in real time and it will hold the incoming connection until receiving a value returned from the website. 

There are several scenarios where this authentication capability could be useful. Websites can prevent other rogue websites from linking to their videos. Content owners can prevent users from passing around HTTP links, thus forcing them to login to view contents. See [[SoftLayer_Network_ContentDelivery_Authentication_Token|SoftLayer_Network_ContentDelivery_Authentication_Token]] and [[SoftLayer_Network_ContentDelivery_Authentication_Address|SoftLayer_Network_ContentDelivery_Authentication_Address]] for more details on the content authentication service. 



### External Links


* [Content delivery network at Wikipedia](http://en.wikipedia.org/wiki/Content_delivery_network)


* [CDN Services at softlayer.com](http://knowledgelayer.softlayer.com/topic/cdn)




        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/authenticateResourceRequest'> authenticateResourceRequest</a> </span>
            <div class='views-field-body'>Validates an authentication token</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/createDirectory'> createDirectory</a> </span>
            <div class='views-field-body'>Creates a directory on the CDN FTP server</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/createFtpUser'> createFtpUser</a> </span>
            <div class='views-field-body'>Create a CDN FTP user record</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullMapping'> createOriginPullMapping</a> </span>
            <div class='views-field-body'>Sets up an Origin Pull domain rule</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullRule'> createOriginPullRule</a> </span>
            <div class='views-field-body'>Sets up an Origin Pull domain rule</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/createTokenAuthenticationDirectory'> createTokenAuthenticationDirectory</a> </span>
            <div class='views-field-body'>Adds a token authentication directory</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/deleteFtpUser'> deleteFtpUser</a> </span>
            <div class='views-field-body'>Deletes a CDN FTP user record</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/deleteOriginPullRule'> deleteOriginPullRule</a> </span>
            <div class='views-field-body'>Removes an Origin Pull domain rule</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/disableLogging'> disableLogging</a> </span>
            <div class='views-field-body'>Disables CDN access log</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/enableLogging'> enableLogging</a> </span>
            <div class='views-field-body'>Enables CDN access log</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the customer account that a CDN account belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getAllPopsBandwidthData'> getAllPopsBandwidthData</a> </span>
            <div class='views-field-body'>Returns bandwidth data for each POP</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getAllPopsBandwidthImage'> getAllPopsBandwidthImage</a> </span>
            <div class='views-field-body'>Returns an object with bandwidth graph data for each POP</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getAssociatedCdnAccountId'> getAssociatedCdnAccountId</a> </span>
            <div class='views-field-body'>Retrieve the CDN account id that this CDN account is associated with.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getAuthenticationIpAddresses'> getAuthenticationIpAddresses</a> </span>
            <div class='views-field-body'>Retrieve the IP addresses that are used for the content authentication service.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getAuthenticationServiceEndpoints'> getAuthenticationServiceEndpoints</a> </span>
            <div class='views-field-body'>Returns all token validation web service endpoints</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthData'> getBandwidthData</a> </span>
            <div class='views-field-body'>Returns bandwidth data for a time range</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthDataWithTypes'> getBandwidthDataWithTypes</a> </span>
            <div class='views-field-body'>Returns bandwidth data for a time range, separated by types and regions</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthImage'> getBandwidthImage</a> </span>
            <div class='views-field-body'>Returns an object with bandwidth graph data</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for a CDN account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getCdnAccountName'> getCdnAccountName</a> </span>
            <div class='views-field-body'>Retrieve the name of a CDN account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getCdnAccountNote'> getCdnAccountNote</a> </span>
            <div class='views-field-body'>Retrieve a brief note on a CDN account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getCdnSolutionName'> getCdnSolutionName</a> </span>
            <div class='views-field-body'>Retrieve the solution type of a CDN account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getCustomerOrigins'> getCustomerOrigins</a> </span>
            <div class='views-field-body'>Returns customer origins</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getDependantServiceFlag'> getDependantServiceFlag</a> </span>
            <div class='views-field-body'>Retrieve indicates if CDN account is dependent on other service. If set, this CDN account is limited to these services: createOriginPullMapping, deleteOriginPullRule, getOriginPullMappingInformation, getCdnUrls, purgeCache, loadContent, manageHttpCompression</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getDirectoryInformation'> getDirectoryInformation</a> </span>
            <div class='views-field-body'>Returns a directory list</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getDiskSpaceUsageDataByDate'> getDiskSpaceUsageDataByDate</a> </span>
            <div class='views-field-body'>Returns a CDN FTP disk space usage</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getDiskSpaceUsageImageByDate'> getDiskSpaceUsageImageByDate</a> </span>
            <div class='views-field-body'>Returns an object with FTP disk usage graph data</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getFtpAttributes'> getFtpAttributes</a> </span>
            <div class='views-field-body'>Returns CDN FTP login credentials</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getLegacyCdnFlag'> getLegacyCdnFlag</a> </span>
            <div class='views-field-body'>Retrieve indicates if it is a legacy CDN or not</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getLogEnabledFlag'> getLogEnabledFlag</a> </span>
            <div class='views-field-body'>Retrieve indicates if CDN logging is enabled.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getMediaUrls'> getMediaUrls</a> </span>
            <div class='views-field-body'>Returns CDN supported URLs</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_ContentDelivery_Account record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getOriginPullMappingInformation'> getOriginPullMappingInformation</a> </span>
            <div class='views-field-body'>Gets Origin Pull domain information</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getOriginPullSupportedMediaUrls'> getOriginPullSupportedMediaUrls</a> </span>
            <div class='views-field-body'>Returns media URLs that support Origin Pull mapping</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getOriginPullUrl'> getOriginPullUrl</a> </span>
            <div class='views-field-body'>Gets Origin Pull domain information</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getPopNames'> getPopNames</a> </span>
            <div class='views-field-body'>Returns all CDN POPs (Points of Presence).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getProviderPortalAccessFlag'> getProviderPortalAccessFlag</a> </span>
            <div class='views-field-body'>Retrieve indicates if customer is allowed to access the CDN provider's management portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getProviderPortalCredentials'> getProviderPortalCredentials</a> </span>
            <div class='views-field-body'>Returns login credentials to the CDN provider portal</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve a CDN account's status presented in a more detailed data type.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getTokenAuthenticationDirectories'> getTokenAuthenticationDirectories</a> </span>
            <div class='views-field-body'>Returns token authentication directories</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getTokenAuthenticationEnabledFlag'> getTokenAuthenticationEnabledFlag</a> </span>
            <div class='views-field-body'>Retrieve indicates if the token authentication service is enabled or not.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/getVendorFtpAttributes'> getVendorFtpAttributes</a> </span>
            <div class='views-field-body'>Returns login credentials to CDN FTP server</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/loadContent'> loadContent</a> </span>
            <div class='views-field-body'>Loads content to all CDN nodes</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/manageHttpCompression'> manageHttpCompression</a> </span>
            <div class='views-field-body'>Enable or disable CDN edge compression</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/purgeCache'> purgeCache</a> </span>
            <div class='views-field-body'>Purges content on POP</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/removeAuthenticationDirectory'> removeAuthenticationDirectory</a> </span>
            <div class='views-field-body'>Deletes a token authentication directory</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/removeFile'> removeFile</a> </span>
            <div class='views-field-body'>Removes a file or a directory on the CDN FTP server</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/setAuthenticationServiceEndpoint'> setAuthenticationServiceEndpoint</a> </span>
            <div class='views-field-body'>Sets the token validation web service endpoint</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/setFtpPassword'> setFtpPassword</a> </span>
            <div class='views-field-body'>Updates a CDN FTP user password</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/updateNote'> updateNote</a> </span>
            <div class='views-field-body'>Updates CDN account note</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_ContentDelivery_Account/uploadStream'> uploadStream</a> </span>
            <div class='views-field-body'>Uploads binary data to the CDN FTP server</div>
        </div>
        </div>
</div>

