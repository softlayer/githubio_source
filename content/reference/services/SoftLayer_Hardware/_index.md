---
title: "SoftLayer_Hardware"
description: "Every SoftLayer hardware is defined in the SoftLayer_Hardware service. SoftLayer hardware has network components, softwa... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# SoftLayer_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer hardware is defined in the SoftLayer_Hardware service. SoftLayer hardware has network components, software, monitoring services such as network monitoring, and hardware components such as hard drives. The SoftLayer_Hardware service is a convenient way to obtain general information about your SoftLayer hardware. Use the data returned by these methods with other API services to get more detailed information about your services and to make changes to your servers and services. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/allowAccessToNetworkStorage'> allowAccessToNetworkStorage</a> </span>
            <div class='views-field-body'>Allow access to a SoftLayer_Network_Storage volume from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/allowAccessToNetworkStorageList'> allowAccessToNetworkStorageList</a> </span>
            <div class='views-field-body'>Allow access to multiple SoftLayer_Network_Storage volumes from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/captureImage'> captureImage</a> </span>
            <div class='views-field-body'>Captures a Flex Image of the hard disk on the physical machine.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/closeAlarm'> closeAlarm</a> </span>
            <div class='views-field-body'>Returns monitoring alarm detailed history</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new server</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a server</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/deleteSoftwareComponentPasswords'> deleteSoftwareComponentPasswords</a> </span>
            <div class='views-field-body'>Delete software component passwords.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/deleteTag'> deleteTag</a> </span>
            <div class='views-field-body'>Delete a tag</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/editSoftwareComponentPasswords'> editSoftwareComponentPasswords</a> </span>
            <div class='views-field-body'>Edit the properties of software component passwords.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/executeRemoteScript'> executeRemoteScript</a> </span>
            <div class='views-field-body'>Download and run remote script from uri on the hardware. Requires https for script to be executed after download. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/findByIpAddress'> findByIpAddress</a> </span>
            <div class='views-field-body'>Find hardware by its primary public or private IP (ipv4) address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/generateOrderTemplate'> generateOrderTemplate</a> </span>
            <div class='views-field-body'>Obtain an order container for a given template object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account associated with a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getActiveComponents'> getActiveComponents</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's active physical components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getActiveNetworkMonitorIncident'> getActiveNetworkMonitorIncident</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's active network monitoring incidents.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAlarmHistory'> getAlarmHistory</a> </span>
            <div class='views-field-body'>Returns monitoring alarm detailed history</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAllPowerComponents'> getAllPowerComponents</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAllowedHost'> getAllowedHost</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this server to Network Storage volumes that require access control lists.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAllowedNetworkStorage'> getAllowedNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAllowedNetworkStorageReplicas'> getAllowedNetworkStorageReplicas</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAntivirusSpywareSoftwareComponent'> getAntivirusSpywareSoftwareComponent</a> </span>
            <div class='views-field-body'>Retrieve information regarding an antivirus/spyware software component object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAttachedNetworkStorages'> getAttachedNetworkStorages</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Storage volumes authorized to this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAttributes'> getAttributes</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's specific attributes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAvailableNetworkStorages'> getAvailableNetworkStorages</a> </span>
            <div class='views-field-body'>Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getAverageDailyPublicBandwidthUsage'> getAverageDailyPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the average daily public bandwidth usage for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBackendIncomingBandwidth'> getBackendIncomingBandwidth</a> </span>
            <div class='views-field-body'>Retrieve the amount of incoming private network bandwidth used by a server over a period of time. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBackendNetworkComponents'> getBackendNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's back-end or private network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBackendOutgoingBandwidth'> getBackendOutgoingBandwidth</a> </span>
            <div class='views-field-body'>Retrieve the amount of outgoing private network bandwidth used by a server over a period of time. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBackendRouters'> getBackendRouters</a> </span>
            <div class='views-field-body'>Retrieve a hardware's backend or private router.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBandwidthAllocation'> getBandwidthAllocation</a> </span>
            <div class='views-field-body'>Retrieve a hardware's allotted bandwidth (measured in GB).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBandwidthAllotmentDetail'> getBandwidthAllotmentDetail</a> </span>
            <div class='views-field-body'>Retrieve a hardware's allotted detail record. Allotment details link bandwidth allocation with allotments.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBenchmarkCertifications'> getBenchmarkCertifications</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's benchmark certifications.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve information regarding the billing item for a server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBillingItemFlag'> getBillingItemFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that a billing item exists.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBlockCancelBecauseDisconnectedFlag'> getBlockCancelBecauseDisconnectedFlag</a> </span>
            <div class='views-field-body'>Retrieve determines whether the hardware is ineligible for cancellation because it is disconnected.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getBusinessContinuanceInsuranceFlag'> getBusinessContinuanceInsuranceFlag</a> </span>
            <div class='views-field-body'>Retrieve status indicating whether or not a piece of hardware has business continuance insurance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getChildrenHardware'> getChildrenHardware</a> </span>
            <div class='views-field-body'>Retrieve child hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getComponentDetailsXML'> getComponentDetailsXML</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getComponents'> getComponents</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getContinuousDataProtectionSoftwareComponent'> getContinuousDataProtectionSoftwareComponent</a> </span>
            <div class='views-field-body'>Retrieve a continuous data protection/server backup software component object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getCreateObjectOptions'> getCreateObjectOptions</a> </span>
            <div class='views-field-body'>Determine options available when creating a server</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getCurrentBillableBandwidthUsage'> getCurrentBillableBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the current billable public outbound bandwidth for this hardware for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getCurrentBillingDetail'> getCurrentBillingDetail</a> </span>
            <div class='views-field-body'><< EOT</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getCurrentBillingTotal'> getCurrentBillingTotal</a> </span>
            <div class='views-field-body'>Get the billing total for this instance's usage up to this point. This total includes all bandwidth charges. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDailyAverage'> getDailyAverage</a> </span>
            <div class='views-field-body'>calculate the average daily network traffic used by a server in gigabytes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>Retrieve information regarding the datacenter in which a piece of hardware resides.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDatacenterName'> getDatacenterName</a> </span>
            <div class='views-field-body'>Retrieve the name of the datacenter in which a piece of hardware resides.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDaysInSparePool'> getDaysInSparePool</a> </span>
            <div class='views-field-body'>Retrieve number of day(s) a server have been in spare pool.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownlinkHardware'> getDownlinkHardware</a> </span>
            <div class='views-field-body'>Retrieve all hardware that has uplink network connections to a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownlinkNetworkHardware'> getDownlinkNetworkHardware</a> </span>
            <div class='views-field-body'>Retrieve all hardware that has uplink network connections to a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownlinkServers'> getDownlinkServers</a> </span>
            <div class='views-field-body'>Retrieve information regarding all servers attached to a piece of network hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownlinkVirtualGuests'> getDownlinkVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve information regarding all virtual guests attached to a piece of network hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownstreamHardwareBindings'> getDownstreamHardwareBindings</a> </span>
            <div class='views-field-body'>Retrieve all hardware downstream from a network device.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownstreamNetworkHardware'> getDownstreamNetworkHardware</a> </span>
            <div class='views-field-body'>Retrieve all network hardware downstream from the selected piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownstreamNetworkHardwareWithIncidents'> getDownstreamNetworkHardwareWithIncidents</a> </span>
            <div class='views-field-body'>Retrieve all network hardware with monitoring warnings or errors that are downstream from the selected piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownstreamServers'> getDownstreamServers</a> </span>
            <div class='views-field-body'>Retrieve information regarding all servers attached downstream to a piece of network hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDownstreamVirtualGuests'> getDownstreamVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve information regarding all virtual guests attached to a piece of network hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getDriveControllers'> getDriveControllers</a> </span>
            <div class='views-field-body'>Retrieve the drive controllers contained within a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getEvaultNetworkStorage'> getEvaultNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's associated EVault network storage service account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getFirewallServiceComponent'> getFirewallServiceComponent</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's firewall services.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getFixedConfigurationPreset'> getFixedConfigurationPreset</a> </span>
            <div class='views-field-body'>Retrieve defines the fixed components in a fixed configuration bare metal server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getFrontendIncomingBandwidth'> getFrontendIncomingBandwidth</a> </span>
            <div class='views-field-body'>Retrieve the amount of incoming public network bandwidth used by a server over a period of time. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getFrontendNetworkComponents'> getFrontendNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's front-end or public network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getFrontendOutgoingBandwidth'> getFrontendOutgoingBandwidth</a> </span>
            <div class='views-field-body'>Retrieve the amount of outgoing public network bandwidth used by a server over a period of time. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getFrontendRouters'> getFrontendRouters</a> </span>
            <div class='views-field-body'>Retrieve a hardware's frontend or public router.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getGlobalIdentifier'> getGlobalIdentifier</a> </span>
            <div class='views-field-body'>Retrieve a hardware's universally unique identifier.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHardDrives'> getHardDrives</a> </span>
            <div class='views-field-body'>Retrieve the hard drives contained within a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHardwareChassis'> getHardwareChassis</a> </span>
            <div class='views-field-body'>Retrieve the chassis that a piece of hardware is housed in.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHardwareFunction'> getHardwareFunction</a> </span>
            <div class='views-field-body'>Retrieve a hardware's function.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHardwareFunctionDescription'> getHardwareFunctionDescription</a> </span>
            <div class='views-field-body'>Retrieve a hardware's function.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHardwareStatus'> getHardwareStatus</a> </span>
            <div class='views-field-body'>Retrieve a hardware's status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHasTrustedPlatformModuleBillingItemFlag'> getHasTrustedPlatformModuleBillingItemFlag</a> </span>
            <div class='views-field-body'>Retrieve determine in hardware object has TPM enabled.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHostIpsSoftwareComponent'> getHostIpsSoftwareComponent</a> </span>
            <div class='views-field-body'>Retrieve information regarding a host IPS software component object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHourlyBandwidth'> getHourlyBandwidth</a> </span>
            <div class='views-field-body'>Retrieves bandwidth hourly over a 24-hour period for the specified hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getHourlyBillingFlag'> getHourlyBillingFlag</a> </span>
            <div class='views-field-body'>Retrieve a server's hourly billing status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getInboundBandwidthUsage'> getInboundBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the sum of all the inbound network traffic data for the last 30 days.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getInboundPublicBandwidthUsage'> getInboundPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total public inbound bandwidth for this hardware for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getLastTransaction'> getLastTransaction</a> </span>
            <div class='views-field-body'>Retrieve information regarding the last transaction a server performed.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getLatestNetworkMonitorIncident'> getLatestNetworkMonitorIncident</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's latest network monitoring incident.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getLocation'> getLocation</a> </span>
            <div class='views-field-body'>Retrieve where a piece of hardware is located within SoftLayer's location hierarchy.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getLocationPathString'> getLocationPathString</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getLockboxNetworkStorage'> getLockboxNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve information regarding a lockbox account associated with a server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getManagedResourceFlag'> getManagedResourceFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that the hardware is a managed resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMemory'> getMemory</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's memory.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMemoryCapacity'> getMemoryCapacity</a> </span>
            <div class='views-field-body'>Retrieve the amount of memory a piece of hardware has, measured in gigabytes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMetricTrackingObject'> getMetricTrackingObject</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's metric tracking object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getModules'> getModules</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMonitoringActiveAlarms'> getMonitoringActiveAlarms</a> </span>
            <div class='views-field-body'>Returns open monitoring alarms for a given time period</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMonitoringAgents'> getMonitoringAgents</a> </span>
            <div class='views-field-body'>Retrieve information regarding the monitoring agents associated with a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMonitoringClosedAlarms'> getMonitoringClosedAlarms</a> </span>
            <div class='views-field-body'>Returns closed monitoring alarms for a given time period</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMonitoringRobot'> getMonitoringRobot</a> </span>
            <div class='views-field-body'>Retrieve information regarding the hardware's monitoring robot.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMonitoringServiceComponent'> getMonitoringServiceComponent</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's network monitoring services.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMonitoringServiceEligibilityFlag'> getMonitoringServiceEligibilityFlag</a> </span>
            <div class='views-field-body'>Retrieve the monitoring service flag eligibility status for a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMonitoringServiceFlag'> getMonitoringServiceFlag</a> </span>
            <div class='views-field-body'>Retrieve the service flag status for a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getMotherboard'> getMotherboard</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's motherboard.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkCards'> getNetworkCards</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's network cards.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkComponents'> getNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve returns a hardware's network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkGatewayMember'> getNetworkGatewayMember</a> </span>
            <div class='views-field-body'>Retrieve the gateway member if this device is part of a network gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkGatewayMemberFlag'> getNetworkGatewayMemberFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not this device is part of a network gateway.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkManagementIpAddress'> getNetworkManagementIpAddress</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's network management IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkMonitorAttachedDownHardware'> getNetworkMonitorAttachedDownHardware</a> </span>
            <div class='views-field-body'>Retrieve all servers with failed monitoring that are attached downstream to a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkMonitorAttachedDownVirtualGuests'> getNetworkMonitorAttachedDownVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve virtual guests that are attached downstream to a hardware that have failed monitoring</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkMonitorIncidents'> getNetworkMonitorIncidents</a> </span>
            <div class='views-field-body'>Retrieve the status of all of a piece of hardware's network monitoring incidents.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkMonitors'> getNetworkMonitors</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's network monitors.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkStatus'> getNetworkStatus</a> </span>
            <div class='views-field-body'>Retrieve the value of a hardware's network status attribute.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkStatusAttribute'> getNetworkStatusAttribute</a> </span>
            <div class='views-field-body'>Retrieve the hardware's related network status attribute.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkStorage'> getNetworkStorage</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's associated network storage service account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNetworkVlans'> getNetworkVlans</a> </span>
            <div class='views-field-body'>Retrieve the network virtual LANs (VLANs) associated with a piece of hardware's network components.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNextBillingCycleBandwidthAllocation'> getNextBillingCycleBandwidthAllocation</a> </span>
            <div class='views-field-body'>Retrieve a hardware's allotted bandwidth for the next billing cycle (measured in GB).</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getNotesHistory'> getNotesHistory</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Hardware record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getOperatingSystem'> getOperatingSystem</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's operating system.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getOperatingSystemReferenceCode'> getOperatingSystemReferenceCode</a> </span>
            <div class='views-field-body'>Retrieve a hardware's operating system software description.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getOutboundBandwidthUsage'> getOutboundBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the sum of all the outbound network traffic data for the last 30 days.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getOutboundPublicBandwidthUsage'> getOutboundPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total public outbound bandwidth for this hardware for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getParentBay'> getParentBay</a> </span>
            <div class='views-field-body'>Retrieve blade Bay</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getParentHardware'> getParentHardware</a> </span>
            <div class='views-field-body'>Retrieve parent Hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPointOfPresenceLocation'> getPointOfPresenceLocation</a> </span>
            <div class='views-field-body'>Retrieve information regarding the Point of Presence (PoP) location in which a piece of hardware resides.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPowerComponents'> getPowerComponents</a> </span>
            <div class='views-field-body'>Retrieve the power components for a hardware object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPowerSupply'> getPowerSupply</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's power supply.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPrimaryBackendIpAddress'> getPrimaryBackendIpAddress</a> </span>
            <div class='views-field-body'>Retrieve the hardware's primary private IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPrimaryBackendNetworkComponent'> getPrimaryBackendNetworkComponent</a> </span>
            <div class='views-field-body'>Retrieve information regarding the hardware's primary back-end network component.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPrimaryIpAddress'> getPrimaryIpAddress</a> </span>
            <div class='views-field-body'>Retrieve the hardware's primary public IP address.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPrimaryNetworkComponent'> getPrimaryNetworkComponent</a> </span>
            <div class='views-field-body'>Retrieve information regarding the hardware's primary public network component.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPrivateBandwidthData'> getPrivateBandwidthData</a> </span>
            <div class='views-field-body'>Retrieve a graph of a server's private network usage.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPrivateNetworkOnlyFlag'> getPrivateNetworkOnlyFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the hardware only has access to the private network.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getProcessorCoreAmount'> getProcessorCoreAmount</a> </span>
            <div class='views-field-body'>Retrieve the total number of processor cores, summed from all processors that are attached to a piece of hardware</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getProcessorPhysicalCoreAmount'> getProcessorPhysicalCoreAmount</a> </span>
            <div class='views-field-body'>Retrieve the total number of physical processor cores, summed from all processors that are attached to a piece of hardware</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getProcessors'> getProcessors</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's processors.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getPublicBandwidthData'> getPublicBandwidthData</a> </span>
            <div class='views-field-body'>Retrieve a graph of a server's public network usage.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getRack'> getRack</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getRaidControllers'> getRaidControllers</a> </span>
            <div class='views-field-body'>Retrieve the RAID controllers contained within a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getRecentEvents'> getRecentEvents</a> </span>
            <div class='views-field-body'>Retrieve recent events that impact this hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getRemoteManagementAccounts'> getRemoteManagementAccounts</a> </span>
            <div class='views-field-body'>Retrieve user credentials to issue commands and/or interact with the server's remote management card.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getRemoteManagementComponent'> getRemoteManagementComponent</a> </span>
            <div class='views-field-body'>Retrieve a hardware's associated remote management component. This is normally IPMI.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getResourceConfigurations'> getResourceConfigurations</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getResourceGroupMemberReferences'> getResourceGroupMemberReferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getResourceGroupRoles'> getResourceGroupRoles</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getResourceGroups'> getResourceGroups</a> </span>
            <div class='views-field-body'>Retrieve the resource groups in which this hardware is a member.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getRouters'> getRouters</a> </span>
            <div class='views-field-body'>Retrieve a hardware's routers.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getScaleAssets'> getScaleAssets</a> </span>
            <div class='views-field-body'>Retrieve collection of scale assets this hardware corresponds to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getSecurityScanRequests'> getSecurityScanRequests</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's vulnerability scan requests.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getSensorData'> getSensorData</a> </span>
            <div class='views-field-body'>Retrieve a server's hardware state via its internal sensors</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getSensorDataWithGraphs'> getSensorDataWithGraphs</a> </span>
            <div class='views-field-body'>Retrieve server's temperature and fan speed graphs as well the sensor raw data.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getServerFanSpeedGraphs'> getServerFanSpeedGraphs</a> </span>
            <div class='views-field-body'>Retrieve a server's fan speed graphs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getServerPowerState'> getServerPowerState</a> </span>
            <div class='views-field-body'>Retrieves a server's power state.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getServerRoom'> getServerRoom</a> </span>
            <div class='views-field-body'>Retrieve information regarding the server room in which the hardware is located.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getServerTemperatureGraphs'> getServerTemperatureGraphs</a> </span>
            <div class='views-field-body'>Retrieve server's temperature graphs</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getServiceProvider'> getServiceProvider</a> </span>
            <div class='views-field-body'>Retrieve information regarding the piece of hardware's service provider.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getSoftwareComponents'> getSoftwareComponents</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's installed software.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getSparePoolBillingItem'> getSparePoolBillingItem</a> </span>
            <div class='views-field-body'>Retrieve information regarding the billing item for a spare pool server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getSshKeys'> getSshKeys</a> </span>
            <div class='views-field-body'>Retrieve sSH keys to be installed on the server during provisioning or an OS reload.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getStorageNetworkComponents'> getStorageNetworkComponents</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getTagReferences'> getTagReferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getTopLevelLocation'> getTopLevelLocation</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getTransactionHistory'> getTransactionHistory</a> </span>
            <div class='views-field-body'>Get transaction history for a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getUpgradeItemPrices'> getUpgradeItemPrices</a> </span>
            <div class='views-field-body'>Retrieve a list of upgradable items available to a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getUpgradeRequest'> getUpgradeRequest</a> </span>
            <div class='views-field-body'>Retrieve an account's associated upgrade request object, if any.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getUplinkHardware'> getUplinkHardware</a> </span>
            <div class='views-field-body'>Retrieve the network device connected to a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getUplinkNetworkComponents'> getUplinkNetworkComponents</a> </span>
            <div class='views-field-body'>Retrieve information regarding the network component that is one level higher than a piece of hardware on the network infrastructure.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getUserData'> getUserData</a> </span>
            <div class='views-field-body'>Retrieve an array containing a single string of custom user data for a hardware order. Max size is 16 kb.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualChassis'> getVirtualChassis</a> </span>
            <div class='views-field-body'>Retrieve information regarding the virtual chassis for a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualChassisSiblings'> getVirtualChassisSiblings</a> </span>
            <div class='views-field-body'>Retrieve information regarding the virtual chassis siblings for a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualHost'> getVirtualHost</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's virtual host record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualLicenses'> getVirtualLicenses</a> </span>
            <div class='views-field-body'>Retrieve information regarding a piece of hardware's virtual software licenses.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualRack'> getVirtualRack</a> </span>
            <div class='views-field-body'>Retrieve information regarding the bandwidth allotment to which a piece of hardware belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualRackId'> getVirtualRackId</a> </span>
            <div class='views-field-body'>Retrieve the name of the bandwidth allotment belonging to a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualRackName'> getVirtualRackName</a> </span>
            <div class='views-field-body'>Retrieve the name of the bandwidth allotment belonging to a piece of hardware.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/getVirtualizationPlatform'> getVirtualizationPlatform</a> </span>
            <div class='views-field-body'>Retrieve a piece of hardware's virtualization platform software.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/importVirtualHost'> importVirtualHost</a> </span>
            <div class='views-field-body'>attempt to import the host record for the virtualization platform running on a server</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/isPingable'> isPingable</a> </span>
            <div class='views-field-body'>Verifies whether or not a server is pingable.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/ping'> ping</a> </span>
            <div class='views-field-body'>Issues ping command.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/powerCycle'> powerCycle</a> </span>
            <div class='views-field-body'>Issues power cycle to server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/powerOff'> powerOff</a> </span>
            <div class='views-field-body'>Power off server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/powerOn'> powerOn</a> </span>
            <div class='views-field-body'>Power on server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/rebootDefault'> rebootDefault</a> </span>
            <div class='views-field-body'>Reboot the server via the default method.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/rebootHard'> rebootHard</a> </span>
            <div class='views-field-body'>Reboot the server via "hard" reboot.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/rebootSoft'> rebootSoft</a> </span>
            <div class='views-field-body'>Execute a soft reboot to the server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/removeAccessToNetworkStorage'> removeAccessToNetworkStorage</a> </span>
            <div class='views-field-body'>Remove access to a SoftLayer_Network_Storage volume from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/removeAccessToNetworkStorageList'> removeAccessToNetworkStorageList</a> </span>
            <div class='views-field-body'>Remove access to multiple SoftLayer_Network_Storage volumes from this device. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/removeTags'> removeTags</a> </span>
            <div class='views-field-body'>Remove a tag reference</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/setTags'> setTags</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Hardware/updateIpmiPassword'> updateIpmiPassword</a> </span>
            <div class='views-field-body'>Update the root IPMI user password </div>
        </div>
        </div>
</div>

