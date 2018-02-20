---
title: "placeOrder"
description: "Use this method to place bare metal server, virtual server and additional service orders with SoftLayer. Upon success, y... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
---
# SoftLayer_Product_Order::placeOrder
## Overview 

Use this method to place bare metal server, virtual server and additional service orders with SoftLayer. Upon success, your credit card or PayPal account will incur charges for the monthly order total (or prorated value if ordered mid billing cycle). If all products on the order are only billed hourly, you will be charged on your billing anniversary date, which occurs monthly on the day you ordered your first service with SoftLayer. For new customers, you are required to provide billing information when you place an order. For existing customers, the credit card on file will be charged. If you're a PayPal customer, a URL will be returned from the call to [[SoftLayer_Product_Order/placeOrder|placeOrder]] which is to be used to finish the authorization process. This authorization tells PayPal that you indeed want to place an order with SoftLayer. From PayPal's web site, you will be redirected back to SoftLayer for your order receipt.<br/><br/> 


When an order is placed, your order will be in a "pending approval" state. When all internal checks pass, your order will be automatically approved. For orders that may need extra attention, a Sales representative will review the order and contact you if necessary. Once the order is approved, your server or service will be provisioned and available to you shortly thereafter. Depending on the type of server or service ordered, provisioning times will vary.<br/><br/> 


<h2>Order Containers</h2> 


When placing API orders, it's important to order your server and services on the appropriate [[SoftLayer_Container_Product_Order (type)|order container]]. Failing to provide the correct container may delay your server or service from being provisioned in a timely manner. Some common order containers are included below.<br/><br/> 


<strong>Note:</strong> <code>SoftLayer_Container_Product_Order_</code> has been removed from the containers in the table below for readability.<br/><br/> 


<table style="word-wrap:break-word;"> 
  <tr style="text-align:left;"> 
    <th>Product</th> 
    <th>Order container</th> 
    <th>Package type</th> 
  </tr> 
  <tr> 
    <td>Bare metal server by CPU</td> 
    <td>[[SoftLayer_Container_Product_Order_Hardware_Server (type)|Hardware_Server]]</td> 
    <td>BARE_METAL_CPU</td> 
  </tr> 
  <tr> 
    <td>Bare metal server by core</td> 
    <td>[[SoftLayer_Container_Product_Order_Hardware_Server (type)|Hardware_Server]]</td> 
    <td>BARE_METAL_CORE</td> 
  </tr> 
  <tr> 
    <td>Virtual server</td> 
    <td>[[SoftLayer_Container_Product_Order_Virtual_Guest (type)|Virtual_Guest]]</td> 
    <td>VIRTUAL_SERVER_INSTANCE</td> 
  </tr> 
  <tr> 
    <td>DNS domain registration</td> 
    <td>[[SoftLayer_Container_Product_Order_Dns_Domain_Registration (type)|Dns_Domain_Registration]]</td> 
    <td>ADDITIONAL_SERVICES</td> 
  </tr> 
  <tr> 
    <td>Local & dedicated load balancers</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_LoadBalancer (type)|Network_LoadBalancer]]</td> 
    <td>ADDITIONAL_SERVICES_LOAD_BALANCER</td> 
  </tr> 
  <tr> 
    <td>Content delivery network</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_ContentDelivery_Account (type)|Network_ContentDelivery_Account]]</td> 
    <td>ADDITIONAL_SERVICES_CDN</td> 
  </tr> 
  <tr> 
    <td>Content delivery network Addon</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_ContentDelivery_Account_Addon (type)|Network_ContentDelivery_Account_Addon]]</td> 
    <td>ADDITIONAL_SERVICES_CDN_ADDON</td> 
  </tr> 
  <tr> 
    <td>Hardware & software firewalls</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Protection_Firewall (type)|Network_Protection_Firewall]]</td> 
    <td>ADDITIONAL_SERVICES_FIREWALL</td> 
  </tr> 
  <tr> 
    <td>Dedicated firewall</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated (type)|Network_Protection_Firewall_Dedicated]]</td> 
    <td>ADDITIONAL_SERVICES_FIREWALL</td> 
  </tr> 
  <tr> 
    <td>Object storage</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Storage_Object (type)|Network_Storage_Object]]</td> 
    <td>ADDITIONAL_SERVICES_OBJECT_STORAGE</td> 
  </tr> 
  <tr> 
    <td>Object storage (hub)</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Storage_Hub (type)|Network_Storage_Hub]]</td> 
    <td>ADDITIONAL_SERVICES_OBJECT_STORAGE</td> 
  </tr> 
  <tr> 
    <td>Network attached storage</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Storage_Nas (type)|Network_Storage_Nas]]</td> 
    <td>ADDITIONAL_SERVICES_NETWORK_ATTACHED_STORAGE</td> 
  </tr> 
  <tr> 
    <td>Iscsi storage</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Storage_Iscsi (type)|Network_Storage_Iscsi]]</td> 
    <td>ADDITIONAL_SERVICES_ISCSI_STORAGE</td> 
  </tr> 
  <tr> 
    <td>Evault</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault (type)|Network_Storage_Backup_Evault_Vault]]</td> 
    <td>ADDITIONAL_SERVICES</td> 
  </tr> 
  <tr> 
    <td>Evault Plugin</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Plugin (type)|Network_Storage_Backup_Evault_Plugin]]</td> 
    <td>ADDITIONAL_SERVICES</td> 
  </tr> 
  <tr> 
    <td>Application delivery appliance</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Application_Delivery_Controller (type)|Network_Application_Delivery_Controller]]</td> 
    <td>ADDITIONAL_SERVICES_APPLICATION_DELIVERY_APPLIANCE</td> 
  </tr> 
  <tr> 
    <td>Network subnet</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Subnet (type)|Network_Subnet]]</td> 
    <td>ADDITIONAL_SERVICES</td> 
  </tr> 
  <tr> 
    <td>Global IPv4</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Subnet (type)|Network_Subnet]]</td> 
    <td>ADDITIONAL_SERVICES_GLOBAL_IP_ADDRESSES</td> 
  </tr> 
  <tr> 
    <td>Global IPv6</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Subnet (type)|Network_Subnet]]</td> 
    <td>ADDITIONAL_SERVICES_GLOBAL_IP_ADDRESSES</td> 
  </tr> 
  <tr> 
    <td>Network VLAN</td> 
    <td>[[SoftLayer_Container_Product_Order_Network_Vlan (type)|Network_Vlan]]</td> 
    <td>ADDITIONAL_SERVICES_NETWORK_VLAN</td> 
  </tr> 
  <tr> 
    <td>Portable storage</td> 
    <td>[[SoftLayer_Container_Product_Order_Virtual_Disk_Image (type)|Virtual_Disk_Image]]</td> 
    <td>ADDITIONAL_SERVICES_PORTABLE_STORAGE</td> 
  </tr> 
  <tr> 
    <td>SSL certificate</td> 
    <td>[[SoftLayer_Container_Product_Order_Security_Certificate (type)|Security_Certificate]]</td> 
    <td>ADDITIONAL_SERVICES_SSL_CERTIFICATE</td> 
  </tr> 
  <tr> 
    <td>External authentication</td> 
    <td>[[SoftLayer_Container_Product_Order_User_Customer_External_Binding (type)|User_Customer_External_Binding]]</td> 
    <td>ADDITIONAL_SERVICES</td> 
  </tr> 
  <tr> 
    <td>Dedicated Host</td> 
    <td>[[SoftLayer_Container_Product_Order_Virtual_DedicatedHost (type)|Virtual_DedicatedHosts]]</td> 
    <td>DEDICATED_HOST</td> 
  </tr> 
</table> 


<h2>Server example</h2> 


This example includes a single bare metal server being ordered with monthly billing.<br/><br/> 


<strong>Warning:</strong> the price ids provided below may be outdated or unavailable, so you will need to determine the available prices from the bare metal server [[SoftLayer_Product_Package/getAllObjects|packages]], which have a [[SoftLayer_Product_Package_Type (type)|package type]] of '''BARE_METAL_CPU''' or '''BARE_METAL_CORE'''. You can get a full list of [[SoftLayer_Product_Package_Type/getAllObjects|package types]] to see other potentially available server packages.<br/><br/> 


<http title="Bare metal server"> 
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type="ns1:SoftLayer_Container_Product_Order_Hardware_Server"> 
        <hardware SOAP-ENC:arrayType="ns1:SoftLayer_Hardware[1]" xsi:type="ns1:SoftLayer_HardwareArray"> 
          <item xsi:type="ns1:SoftLayer_Hardware"> 
            <domain xsi:type="xsd:string">example.com</domain> 
            <hostname xsi:type="xsd:string">server1</hostname> 
          </item> 
        </hardware> 
        <location xsi:type="xsd:string">138124</location> 
        <packageId xsi:type="xsd:int">142</packageId> 
        <prices SOAP-ENC:arrayType="ns1:SoftLayer_Product_Item_Price[14]" xsi:type="ns1:SoftLayer_Product_Item_PriceArray"> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">58</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">22337</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">21189</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">876</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">57</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">55</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">21190</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">36381</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">21</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">22013</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">906</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">420</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">418</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">342</id> 
          </item> 
        </prices> 
        <useHourlyPricing xsi:type="xsd:boolean">false</useHourlyPricing> 
      </orderData> 
      <saveAsQuote xsi:nil="true" /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
</http><br/><br/> 


<h2>Virtual server example</h2> 


This example includes 2 identical virtual servers (except for hostname) being ordered for hourly billing. It includes an optional image template id and VLAN data specified on the virtualGuest objects - <code>primaryBackendNetworkComponent</code> and <code>primaryNetworkComponent</code>.<br/><br/> 


<strong>Warning:</strong> the price ids provided below may be outdated or unavailable, so you will need to determine the available prices from the virtual server [[SoftLayer_Product_Package/getAllObjects|package]], which has a [[SoftLayer_Product_Package_Type (type)|package type]] of '''VIRTUAL_SERVER_INSTANCE'''.<br/><br/> 


<http title="Virtual server"> 
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type="ns1:SoftLayer_Container_Product_Order_Virtual_Guest"> 
        <imageTemplateId xsi:type="xsd:int">13251</imageTemplateId> 
        <location xsi:type="xsd:string">37473</location> 
        <packageId xsi:type="xsd:int">46</packageId> 
        <prices SOAP-ENC:arrayType="ns1:SoftLayer_Product_Item_Price[13]" xsi:type="ns1:SoftLayer_Product_Item_PriceArray"> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">2159</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">55</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">13754</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">1641</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">905</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">1800</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">58</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">21</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">1645</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">272</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">57</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">418</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">420</id> 
          </item> 
        </prices> 
        <quantity xsi:type="xsd:int">2</quantity> 
        <useHourlyPricing xsi:type="xsd:boolean">true</useHourlyPricing> 
        <virtualGuests SOAP-ENC:arrayType="ns1:SoftLayer_Virtual_Guest[1]" xsi:type="ns1:SoftLayer_Virtual_GuestArray"> 
          <item xsi:type="ns1:SoftLayer_Virtual_Guest"> 
            <domain xsi:type="xsd:string">example.com</domain> 
            <hostname xsi:type="xsd:string">server1</hostname> 
            <primaryBackendNetworkComponent xsi:type="ns1:SoftLayer_Virtual_Guest_Network_Component"> 
              <networkVlan xsi:type="ns1:SoftLayer_Network_Vlan"> 
                <id xsi:type="xsd:int">12345</id> 
              </networkVlan> 
            </primaryBackendNetworkComponent> 
            <primaryNetworkComponent xsi:type="ns1:SoftLayer_Virtual_Guest_Network_Component"> 
              <networkVlan xsi:type="ns1:SoftLayer_Network_Vlan"> 
                <id xsi:type="xsd:int">67890</id> 
              </networkVlan> 
            </primaryNetworkComponent> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Virtual_Guest"> 
            <domain xsi:type="xsd:string">example.com</domain> 
            <hostname xsi:type="xsd:string">server2</hostname> 
            <primaryBackendNetworkComponent xsi:type="ns1:SoftLayer_Virtual_Guest_Network_Component"> 
              <networkVlan xsi:type="ns1:SoftLayer_Network_Vlan"> 
                <id xsi:type="xsd:int">12345</id> 
              </networkVlan> 
            </primaryBackendNetworkComponent> 
            <primaryNetworkComponent xsi:type="ns1:SoftLayer_Virtual_Guest_Network_Component"> 
              <networkVlan xsi:type="ns1:SoftLayer_Network_Vlan"> 
                <id xsi:type="xsd:int">67890</id> 
              </networkVlan> 
            </primaryNetworkComponent> 
          </item> 
        </virtualGuests> 
      </orderData> 
      <saveAsQuote xsi:nil="true" /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
</http><br/><br/> 


<h2>VLAN example</h2> 


<strong>Warning:</strong> the price ids provided below may be outdated or unavailable, so you will need to determine the available prices from the additional services [[SoftLayer_Product_Package/getAllObjects|package]], which has a [[SoftLayer_Product_Package_Type (type)|package type]] of '''ADDITIONAL_SERVICES'''. You can get a full list of [[SoftLayer_Product_Package_Type/getAllObjects|package types]] to find other available additional service packages.<br/><br/> 


<http title="VLAN"> 
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type="ns1:SoftLayer_Container_Product_Order_Network_Vlan"> 
        <location xsi:type="xsd:string">154820</location> 
        <packageId xsi:type="xsd:int">0</packageId> 
        <prices SOAP-ENC:arrayType="ns1:SoftLayer_Product_Item_Price[2]" xsi:type="ns1:SoftLayer_Product_Item_PriceArray"> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">2021</id> 
          </item> 
          <item xsi:type="ns1:SoftLayer_Product_Item_Price"> 
            <id xsi:type="xsd:int">2018</id> 
          </item> 
        </prices> 
        <useHourlyPricing xsi:type="xsd:boolean">true</useHourlyPricing> 
      </orderData> 
      <saveAsQuote xsi:nil="true" /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
</http><br/><br/> 


<h2>Multiple products example</h2> 


This example includes a combination of the above examples in a single order. Note that all the configuration options for each individual order container are the same as above, except now we encapsulate each one within the <code>orderContainers</code> property on the base [[SoftLayer_Container_Product_Order (type)|order container]].<br/><br/> 


<strong>Warning:</strong> not all products are available to be ordered with other products. For example, since SSL certificates require validation from a 3rd party, the approval process may take days or even weeks, and this would not be acceptable when you need your hourly virtual server right now. To better accommodate customers, we restrict several products to be ordered individually.<br/><br/> 


<http title="Bare metal server + virtual server + VLAN"> 
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type="ns1:SoftLayer_Container_Product_Order"> 
        <orderContainers SOAP-ENC:arrayType="ns1:SoftLayer_Container_Product_Order[3]" xsi:type="ns1:SoftLayer_Container_Product_OrderArray"> 
          <item xsi:type="ns1:SoftLayer_Container_Product_Order_Hardware_Server"> 
            ... 
          </item> 
          <item xsi:type="ns1:SoftLayer_Container_Product_Order_Virtual_Guest"> 
            ... 
          </item> 
          <item xsi:type="ns1:SoftLayer_Container_Product_Order_Network_Vlan"> 
            ... 
          </item> 
        </orderContainers> 
      </orderData> 
      <saveAsQuote xsi:nil="true" /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
</http> 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|orderData| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| Details required to order.|
|saveAsQuote| boolean| Set to true if the order data is to be saved as a quote.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Receipt'>SoftLayer_Container_Product_Order_Receipt </a>
