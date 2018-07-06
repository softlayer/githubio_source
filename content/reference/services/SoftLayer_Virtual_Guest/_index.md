---
title: "SoftLayer_Virtual_Guest"
description: "The virtual guest service provides a common interface to any virtualization platform supported by SoftLayer. The interac... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Guest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest' >Datatype</a></li>
    </ul>
</div>

## Description
The virtual guest service provides a common interface to any virtualization platform supported by SoftLayer. The interaction with various third party APIs is not needed when implementing this service to administer your guests. The SoftLayer_Virtual_Guest service also controls individual CloudLayer Computing Instances purchased from SoftLayer in a way that is analogous to the [[SoftLayer_Hardware_Server]] service's control over physical hardware purchased form SoftLayer. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/activatePrivatePort'> activatePrivatePort</a> </span>
            <div class='views-field-body'>Activate the private port</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/activatePublicPort'> activatePublicPort</a> </span>
            <div class='views-field-body'>Activate the public port</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/allowAccessToNetworkStorage'> allowAccessToNetworkStorage</a> </span>
            <div class='views-field-body'>Allow access to a SoftLayer_Network_Storage volume from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/allowAccessToNetworkStorageList'> allowAccessToNetworkStorageList</a> </span>
            <div class='views-field-body'>Allow access to multiple SoftLayer_Network_Storage volumes from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/attachDiskImage'> attachDiskImage</a> </span>
            <div class='views-field-body'>Attaches a disk image.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/cancelIsolationForDestructiveAction'> cancelIsolationForDestructiveAction</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/captureImage'> captureImage</a> </span>
            <div class='views-field-body'>Captures a Flex Image of the hard disk on the virtual machine.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/checkHostDiskAvailability'> checkHostDiskAvailability</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/closeAlarm'> closeAlarm</a> </span>
            <div class='views-field-body'>Returns monitoring alarm detailed history</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/configureMetadataDisk'> configureMetadataDisk</a> </span>
            <div class='views-field-body'>Configures the guest's metadata disk.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction'> createArchiveTransaction</a> </span>
            <div class='views-field-body'>[[SoftLayer_Virtual_Guest_Block_Devices|Block Devices]] can be grouped together in and backed up in an archive for later use. This method generates a transaction to perform an archive of the provided block devices. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new computing instance</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/createObjects'> createObjects</a> </span>
            <div class='views-field-body'>Create new computing instances</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/createPostSoftwareInstallTransaction'> createPostSoftwareInstallTransaction</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a computing instance</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/deleteTransientWebhook'> deleteTransientWebhook</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/detachDiskImage'> detachDiskImage</a> </span>
            <div class='views-field-body'>Detaches a disk image.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a computing instance's properties</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/executeIderaBareMetalRestore'> executeIderaBareMetalRestore</a> </span>
            <div class='views-field-body'>Reboot a guest into the Idera Bare Metal Restore image.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/executeR1SoftBareMetalRestore'> executeR1SoftBareMetalRestore</a> </span>
            <div class='views-field-body'>Reboot a guest into the R1Soft Bare Metal Restore image.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/executeRemoteScript'> executeRemoteScript</a> </span>
            <div class='views-field-body'>Download and run remote script from uri on the virtual guest. Requires https for script to be executed after download. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/executeRescueLayer'> executeRescueLayer</a> </span>
            <div class='views-field-body'>Reboot a Linux guest into the Xen rescue image.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/findByIpAddress'> findByIpAddress</a> </span>
            <div class='views-field-body'>Find CCI by its primary public or private IP (ipv4) address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate'> generateOrderTemplate</a> </span>
            <div class='views-field-body'>Obtain an order container for a given template object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account that a virtual guest belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAccountOwnedPoolFlag'> getAccountOwnedPoolFlag</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getActiveNetworkMonitorIncident'> getActiveNetworkMonitorIncident</a> </span>
            <div class='views-field-body'>Retrieve a virtual guest's currently active network monitoring incidents.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getActiveTickets'> getActiveTickets</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getActiveTransaction'> getActiveTransaction</a> </span>
            <div class='views-field-body'>Retrieve a transaction that is still be performed on a cloud server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getActiveTransactions'> getActiveTransactions</a> </span>
            <div class='views-field-body'>Retrieve any active transaction(s) that are currently running for the server (example: os reload).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAdditionalRequiredPricesForOsReload'> getAdditionalRequiredPricesForOsReload</a> </span>
            <div class='views-field-body'>Return a collection of SoftLayer_Item_Price objects for an OS reload</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAlarmHistory'> getAlarmHistory</a> </span>
            <div class='views-field-body'>Returns monitoring alarm detailed history</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAllowedHost'> getAllowedHost</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this Virtual Guest to Network Storage volumes that require access control lists.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAllowedNetworkStorage'> getAllowedNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Virtual_Guest has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAllowedNetworkStorageReplicas'> getAllowedNetworkStorageReplicas</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Virtual_Guest has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAntivirusSpywareSoftwareComponent'> getAntivirusSpywareSoftwareComponent</a> </span>
            <div class='views-field-body'>Retrieve a antivirus / spyware software component object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getApplicationDeliveryController'> getApplicationDeliveryController</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAttachedNetworkStorages'> getAttachedNetworkStorages</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Storage volumes authorized to this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAttributes'> getAttributes</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAvailableBlockDevicePositions'> getAvailableBlockDevicePositions</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAvailableMonitoring'> getAvailableMonitoring</a> </span>
            <div class='views-field-body'>Retrieve an object that stores the maximum level for the monitoring query types and response types.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAvailableNetworkStorages'> getAvailableNetworkStorages</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAverageDailyPrivateBandwidthUsage'> getAverageDailyPrivateBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the average daily private bandwidth usage for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getAverageDailyPublicBandwidthUsage'> getAverageDailyPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the average daily public bandwidth usage for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBackendNetworkComponents'> getBackendNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve a guests's backend network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBackendRouters'> getBackendRouters</a> </span>
            <div class='views-field-body'>Retrieve a guest's backend or private router.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBandwidthAllocation'> getBandwidthAllocation</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's allotted bandwidth (measured in GB).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBandwidthAllotmentDetail'> getBandwidthAllotmentDetail</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's allotted detail record. Allotment details link bandwidth allocation with allotments.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBandwidthDataByDate'> getBandwidthDataByDate</a> </span>
            <div class='views-field-body'>Retrieve the amount of network traffic that occurred for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBandwidthForDateRange'> getBandwidthForDateRange</a> </span>
            <div class='views-field-body'>Retrieve bandwidth data from a tracking object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBandwidthImage'> getBandwidthImage</a> </span>
            <div class='views-field-body'>Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBandwidthImageByDate'> getBandwidthImageByDate</a> </span>
            <div class='views-field-body'>Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBandwidthTotal'> getBandwidthTotal</a> </span>
            <div class='views-field-body'>Retrieve total amount of network traffic that was in use during the time specified by the input parameters for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBillingCycleBandwidthUsage'> getBillingCycleBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBillingCyclePrivateBandwidthUsage'> getBillingCyclePrivateBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the raw private bandwidth usage data for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBillingCyclePublicBandwidthUsage'> getBillingCyclePublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the raw public bandwidth usage data for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the billing item for a CloudLayer Compute Instance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBlockCancelBecauseDisconnectedFlag'> getBlockCancelBecauseDisconnectedFlag</a> </span>
            <div class='views-field-body'>Retrieve determines whether the instance is ineligible for cancellation because it is disconnected.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBlockDeviceTemplateGroup'> getBlockDeviceTemplateGroup</a> </span>
            <div class='views-field-body'>Retrieve the global identifier for the image template that was used to provision or reload a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBlockDevices'> getBlockDevices</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's block devices. Block devices link [[SoftLayer_Virtual_Disk_Image|disk images]] to computing instances.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBootMode'> getBootMode</a> </span>
            <div class='views-field-body'>Retrieves the boot mode of the VSI.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getBootOrder'> getBootOrder</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getConsoleAccessLog'> getConsoleAccessLog</a> </span>
            <div class='views-field-body'>get console access logs</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getConsoleIpAddressFlag'> getConsoleIpAddressFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating a computing instance's console IP address is assigned.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getConsoleIpAddressRecord'> getConsoleIpAddressRecord</a> </span>
            <div class='views-field-body'>Retrieve a record containing information about a computing instance's console IP and port number.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getContinuousDataProtectionSoftwareComponent'> getContinuousDataProtectionSoftwareComponent</a> </span>
            <div class='views-field-body'>Retrieve a continuous data protection software component object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getControlPanel'> getControlPanel</a> </span>
            <div class='views-field-body'>Retrieve a guest's control panel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCoreRestrictedOperatingSystemPrice'> getCoreRestrictedOperatingSystemPrice</a> </span>
            <div class='views-field-body'>Return the associated core-restricted operating system item price for the virtual server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCpuMetricDataByDate'> getCpuMetricDataByDate</a> </span>
            <div class='views-field-body'>Retrieve records containing the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCpuMetricImage'> getCpuMetricImage</a> </span>
            <div class='views-field-body'>Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCpuMetricImageByDate'> getCpuMetricImageByDate</a> </span>
            <div class='views-field-body'>Retrieve a visual representation of the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions'> getCreateObjectOptions</a> </span>
            <div class='views-field-body'>Determine options available when creating a computing instance</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCurrentBandwidthSummary'> getCurrentBandwidthSummary</a> </span>
            <div class='views-field-body'>Retrieve an object that provides commonly used bandwidth summary components for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCurrentBillingDetail'> getCurrentBillingDetail</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's upgradeable items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCurrentBillingTotal'> getCurrentBillingTotal</a> </span>
            <div class='views-field-body'>Get the total billing price for this instance's hourly usage up to this point. This includes total includes all bandwidth charges.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCustomBandwidthDataByDate'> getCustomBandwidthDataByDate</a> </span>
            <div class='views-field-body'>Retrieve bandwidth graph by date.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getCustomMetricDataByDate'> getCustomMetricDataByDate</a> </span>
            <div class='views-field-body'>Retrieve bandwidth graph by date.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>Retrieve the datacenter that a virtual guest resides in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getDedicatedHost'> getDedicatedHost</a> </span>
            <div class='views-field-body'>Retrieve the dedicated host associated with this guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getDriveRetentionItemPrice'> getDriveRetentionItemPrice</a> </span>
            <div class='views-field-body'>Return a drive retention SoftLayer_Item_Price object for a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getEvaultNetworkStorage'> getEvaultNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve a guest's associated EVault network storage service account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getFirewallProtectableSubnets'> getFirewallProtectableSubnets</a> </span>
            <div class='views-field-body'>Get the subnets associated with this CloudLayer computing instance that are protectable by a network component firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent'> getFirewallServiceComponent</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's hardware firewall services.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getFirstAvailableBlockDevicePosition'> getFirstAvailableBlockDevicePosition</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getFrontendNetworkComponents'> getFrontendNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve a guest's frontend network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getFrontendRouters'> getFrontendRouters</a> </span>
            <div class='views-field-body'>Retrieve a guest's frontend or public router.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getGcPassword'> getGcPassword</a> </span>
            <div class='views-field-body'>Retrieve the encrypted Windows user password.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getGlobalIdentifier'> getGlobalIdentifier</a> </span>
            <div class='views-field-body'>Retrieve a guest's universally unique identifier.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getGuestBootParameter'> getGuestBootParameter</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getHost'> getHost</a> </span>
            <div class='views-field-body'>Retrieve the virtual host on which a virtual guest resides (available only on private clouds).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getHostIpsSoftwareComponent'> getHostIpsSoftwareComponent</a> </span>
            <div class='views-field-body'>Retrieve a host IPS software component object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getHourlyBillingFlag'> getHourlyBillingFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a computing instance is billed hourly instead of monthly.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getInboundPrivateBandwidthUsage'> getInboundPrivateBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total private inbound bandwidth for this computing instance for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getInboundPublicBandwidthUsage'> getInboundPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total public inbound bandwidth for this computing instance for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getInternalTagReferences'> getInternalTagReferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getIsoBootImage'> getIsoBootImage</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getItemPricesFromSoftwareDescriptions'> getItemPricesFromSoftwareDescriptions</a> </span>
            <div class='views-field-body'>Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getLastKnownPowerState'> getLastKnownPowerState</a> </span>
            <div class='views-field-body'>Retrieve the last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getLastOperatingSystemReload'> getLastOperatingSystemReload</a> </span>
            <div class='views-field-body'>Retrieve the last transaction that a cloud server's operating system was loaded.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getLastTransaction'> getLastTransaction</a> </span>
            <div class='views-field-body'>Retrieve the last transaction a cloud server had performed.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getLatestNetworkMonitorIncident'> getLatestNetworkMonitorIncident</a> </span>
            <div class='views-field-body'>Retrieve a virtual guest's latest network monitoring incident.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getLocalDiskFlag'> getLocalDiskFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that the virtual guest has at least one disk which is local to the host it runs on. This does not include a SWAP device.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getLocation'> getLocation</a> </span>
            <div class='views-field-body'>Retrieve where guest is located within SoftLayer's location hierarchy.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getManagedResourceFlag'> getManagedResourceFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that the virtual guest is a managed resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricDataByDate'> getMemoryMetricDataByDate</a> </span>
            <div class='views-field-body'>Retrieve records containing the amount memory that was used for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricImage'> getMemoryMetricImage</a> </span>
            <div class='views-field-body'>Retrieve a visual representation of the amount of memory used for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMemoryMetricImageByDate'> getMemoryMetricImageByDate</a> </span>
            <div class='views-field-body'>Retrieve a visual representation of the amount of memory used for the specified time frame for a computing instance. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMetricTrackingObject'> getMetricTrackingObject</a> </span>
            <div class='views-field-body'>Retrieve a guest's metric tracking object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMetricTrackingObjectId'> getMetricTrackingObjectId</a> </span>
            <div class='views-field-body'>Retrieve the metric tracking object id for this guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringActiveAlarms'> getMonitoringActiveAlarms</a> </span>
            <div class='views-field-body'>Returns open monitoring alarms for a given time period</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringAgents'> getMonitoringAgents</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringClosedAlarms'> getMonitoringClosedAlarms</a> </span>
            <div class='views-field-body'>Returns closed monitoring alarms for a given time period</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringRobot'> getMonitoringRobot</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceComponent'> getMonitoringServiceComponent</a> </span>
            <div class='views-field-body'>Retrieve a virtual guest's network monitoring services.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceEligibilityFlag'> getMonitoringServiceEligibilityFlag</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringServiceFlag'> getMonitoringServiceFlag</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getMonitoringUserNotification'> getMonitoringUserNotification</a> </span>
            <div class='views-field-body'>Retrieve the monitoring notification objects for this guest. Each object links this guest instance to a user account that will be notified if monitoring on this guest object fails</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getNetworkComponentFirewallProtectableIpAddresses'> getNetworkComponentFirewallProtectableIpAddresses</a> </span>
            <div class='views-field-body'>Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network component firewall.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getNetworkComponents'> getNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve a guests's network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getNetworkMonitorIncidents'> getNetworkMonitorIncidents</a> </span>
            <div class='views-field-body'>Retrieve all of a virtual guest's network monitoring incidents.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getNetworkMonitors'> getNetworkMonitors</a> </span>
            <div class='views-field-body'>Retrieve a guests's network monitors.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getNetworkStorage'> getNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve a guest's associated network storage accounts.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getNetworkVlans'> getNetworkVlans</a> </span>
            <div class='views-field-body'>Retrieve the network Vlans that a guest's network components are associated with.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Virtual_Guest record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOpenCancellationTicket'> getOpenCancellationTicket</a> </span>
            <div class='views-field-body'>Retrieve an open ticket requesting cancellation of this server, if one exists.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOperatingSystem'> getOperatingSystem</a> </span>
            <div class='views-field-body'>Retrieve a guest's operating system.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOperatingSystemReferenceCode'> getOperatingSystemReferenceCode</a> </span>
            <div class='views-field-body'>Retrieve a guest's operating system software description.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOrderTemplate'> getOrderTemplate</a> </span>
            <div class='views-field-body'>Obtain an order container that is ready to be sent to the [[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder]] method.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOrderedPackageId'> getOrderedPackageId</a> </span>
            <div class='views-field-body'>Retrieve the original package id provided with the order for a Cloud Computing Instance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOutboundPrivateBandwidthUsage'> getOutboundPrivateBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total private outbound bandwidth for this computing instance for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOutboundPublicBandwidthUsage'> getOutboundPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total public outbound bandwidth for this computing instance for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getOverBandwidthAllocationFlag'> getOverBandwidthAllocationFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the bandwidth usage for this computing instance for the current billing cycle exceeds the allocation.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getPendingMigrationFlag'> getPendingMigrationFlag</a> </span>
            <div class='views-field-body'>Retrieve when true this virtual guest must be migrated using SoftLayer_Virtual_Guest::migrate.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getPowerState'> getPowerState</a> </span>
            <div class='views-field-body'>Retrieve the current power state of a virtual guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getPrimaryBackendIpAddress'> getPrimaryBackendIpAddress</a> </span>
            <div class='views-field-body'>Retrieve a guest's primary private IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getPrimaryBackendNetworkComponent'> getPrimaryBackendNetworkComponent</a> </span>
            <div class='views-field-body'>Retrieve a guest's primary backend network component.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getPrimaryIpAddress'> getPrimaryIpAddress</a> </span>
            <div class='views-field-body'>Retrieve the guest's primary public IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getPrimaryNetworkComponent'> getPrimaryNetworkComponent</a> </span>
            <div class='views-field-body'>Retrieve a guest's primary public network component.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getPrivateNetworkOnlyFlag'> getPrivateNetworkOnlyFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the computing instance only has access to the private network.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getProjectedOverBandwidthAllocationFlag'> getProjectedOverBandwidthAllocationFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the bandwidth usage for this computing instance for the current billing cycle is projected to exceed the allocation.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getProjectedPublicBandwidthUsage'> getProjectedPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the projected public outbound bandwidth for this computing instance for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getProvisionDate'> getProvisionDate</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getRecentEvents'> getRecentEvents</a> </span>
            <div class='views-field-body'>Retrieve recent events that impact this computing instance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getRecentMetricData'> getRecentMetricData</a> </span>
            <div class='views-field-body'>Recent metric data for a guest </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getRegionalGroup'> getRegionalGroup</a> </span>
            <div class='views-field-body'>Retrieve the regional group this guest is in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getRegionalInternetRegistry'> getRegionalInternetRegistry</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getRemoteMonitoringActiveAlarms'> getRemoteMonitoringActiveAlarms</a> </span>
            <div class='views-field-body'>Returns open monitoring alarms for a given time period</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getRemoteMonitoringClosedAlarms'> getRemoteMonitoringClosedAlarms</a> </span>
            <div class='views-field-body'>Returns closed monitoring alarms for a given time period</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getReverseDomainRecords'> getReverseDomainRecords</a> </span>
            <div class='views-field-body'>Retrieve the reverse domain records associated with a server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getScaleAssets'> getScaleAssets</a> </span>
            <div class='views-field-body'>Retrieve collection of scale assets this guest corresponds to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getScaleMember'> getScaleMember</a> </span>
            <div class='views-field-body'>Retrieve the scale member for this guest, if applicable.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getScaledFlag'> getScaledFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not this guest is a member of a scale group and was automatically created as part of a scale group action.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getSecurityScanRequests'> getSecurityScanRequests</a> </span>
            <div class='views-field-body'>Retrieve a guest's vulnerability scan requests.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getServerRoom'> getServerRoom</a> </span>
            <div class='views-field-body'>Retrieve the server room that a guest is located at. There may be more than one server room for every data center.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getSoftwareComponents'> getSoftwareComponents</a> </span>
            <div class='views-field-body'>Retrieve a guest's installed software.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getSshKeys'> getSshKeys</a> </span>
            <div class='views-field-body'>Retrieve sSH keys to be installed on the server during provisioning or an OS reload.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getTagReferences'> getTagReferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getTransientGuestFlag'> getTransientGuestFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a computing instance is a Transient Instance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getTransientWebhookURI'> getTransientWebhookURI</a> </span>
            <div class='views-field-body'>Retrieve the endpoint used to notify customers their transient guest is terminating.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve the type of this virtual guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getUpgradeItemPrices'> getUpgradeItemPrices</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's upgradeable items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getUpgradeRequest'> getUpgradeRequest</a> </span>
            <div class='views-field-body'>Retrieve a computing instance's associated upgrade request object if any.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getUserData'> getUserData</a> </span>
            <div class='views-field-body'>Retrieve a base64 encoded string containing custom user data for a Cloud Computing Instance order.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getUsers'> getUsers</a> </span>
            <div class='views-field-body'>Retrieve a list of users that have access to this computing instance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getValidBlockDeviceTemplateGroups'> getValidBlockDeviceTemplateGroups</a> </span>
            <div class='views-field-body'>Return a list of valid block device template groups based on this host</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getVirtualRack'> getVirtualRack</a> </span>
            <div class='views-field-body'>Retrieve the name of the bandwidth allotment that a hardware belongs too.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getVirtualRackId'> getVirtualRackId</a> </span>
            <div class='views-field-body'>Retrieve the id of the bandwidth allotment that a computing instance belongs too.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/getVirtualRackName'> getVirtualRackName</a> </span>
            <div class='views-field-body'>Retrieve the name of the bandwidth allotment that a computing instance belongs too.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/isBackendPingable'> isBackendPingable</a> </span>
            <div class='views-field-body'>Verifies if a guest's backend ip address is pingable.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/isPingable'> isPingable</a> </span>
            <div class='views-field-body'>Verifies if guest is pingable.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/isolateInstanceForDestructiveAction'> isolateInstanceForDestructiveAction</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/migrate'> migrate</a> </span>
            <div class='views-field-body'>Creates a transaction to migrate a virtual guest to a new host. NOTE: Will only migrate if SoftLayer_Virtual_Guest property pendingMigrationFlag = true </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/migrateDedicatedHost'> migrateDedicatedHost</a> </span>
            <div class='views-field-body'>Migrate a dedicated instance from one dedicated host to another dedicated host </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/mountIsoImage'> mountIsoImage</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/pause'> pause</a> </span>
            <div class='views-field-body'>Pause a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/powerCycle'> powerCycle</a> </span>
            <div class='views-field-body'>Power cycle a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/powerOff'> powerOff</a> </span>
            <div class='views-field-body'>Power off a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/powerOffSoft'> powerOffSoft</a> </span>
            <div class='views-field-body'>Cleanly shut down a guest and disable power</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/powerOn'> powerOn</a> </span>
            <div class='views-field-body'>Power on a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/rebootDefault'> rebootDefault</a> </span>
            <div class='views-field-body'>Power cycle a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/rebootHard'> rebootHard</a> </span>
            <div class='views-field-body'>Power cycle a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/rebootSoft'> rebootSoft</a> </span>
            <div class='views-field-body'>Attempt to complete a soft reboot of a guest by shutting down the operating system.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/reloadCurrentOperatingSystemConfiguration'> reloadCurrentOperatingSystemConfiguration</a> </span>
            <div class='views-field-body'>Perform an OS reload</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/reloadOperatingSystem'> reloadOperatingSystem</a> </span>
            <div class='views-field-body'>Reloads operating system configuration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/removeAccessToNetworkStorage'> removeAccessToNetworkStorage</a> </span>
            <div class='views-field-body'>Remove access to a SoftLayer_Network_Storage volume from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/removeAccessToNetworkStorageList'> removeAccessToNetworkStorageList</a> </span>
            <div class='views-field-body'>Remove access to multiple SoftLayer_Network_Storage volumes from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/resume'> resume</a> </span>
            <div class='views-field-body'>Resume a guest.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/setPrivateNetworkInterfaceSpeed'> setPrivateNetworkInterfaceSpeed</a> </span>
            <div class='views-field-body'>Updates the private network interface (eth0) speed.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/setPublicNetworkInterfaceSpeed'> setPublicNetworkInterfaceSpeed</a> </span>
            <div class='views-field-body'>Updates the public network interface (eth1) speed.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/setTags'> setTags</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/setTransientWebhook'> setTransientWebhook</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/setUserMetadata'> setUserMetadata</a> </span>
            <div class='views-field-body'>Configures the guest's metadata disk.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/shutdownPrivatePort'> shutdownPrivatePort</a> </span>
            <div class='views-field-body'>Shuts down the private port</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/shutdownPublicPort'> shutdownPublicPort</a> </span>
            <div class='views-field-body'>Shuts down the public port</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/unmountIsoImage'> unmountIsoImage</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/validateImageTemplate'> validateImageTemplate</a> </span>
            <div class='views-field-body'>Validates an image template for OS Reload</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest/verifyReloadOperatingSystem'> verifyReloadOperatingSystem</a> </span>
            <div class='views-field-body'>Verify that a virtual server can go through the operating system reload process.</div>
        </div>
        </div>
</div>

