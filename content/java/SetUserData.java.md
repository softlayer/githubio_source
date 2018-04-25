---
title: "SetUserData.java"
description: "SetUserData.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "metadata"
---


```
package api.examples;

import java.util.ArrayList;
import java.util.List;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.Guest;

public class SetUserData {

	/**
	 * Set the user data for a VSI.
	 * 
	 * The script sets the user metadata for a VSI we make a simple call th the
	 * setUserMetadata() in the SoftLayer_Virtual_Guest API service
	 *
	 * Manual pages see
	 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest see
	 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/
	 * setUserMetadata license <http://sldn.softlayer.com/article/License>
	 * author SoftLayer Technologies, Inc. <sldn@softlayer.com>
	 */
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";

		// The user data you wish to set
		List<String> userData = new ArrayList<String>();
		userData.add("this is my user data");

		// The id of the VSI where you want to set the user data
		Long virtualGuestId = new Long(7370502);

		// Declare the API client.
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Guest.Service virtualGuestService = Guest.service(client,
				virtualGuestId);

		try {
			virtualGuestService.setUserMetadata(userData);
			System.out.println("The user data was set successfully. ");

		} catch (Exception e) {
			System.out
					.println("Unable to set the user data. " + e.getMessage());
		}

	}

}

```
