---
title: "Manage (Create, Add Permissions, Delete) User"
description: "Example application which 1) creates a user, 2) Adds some portal permissions, and 3) Deletes the user"
date: "2016-09-19"
tags:
    - "UserCustomer"
    - "addBulkPortalPermissions"
---

```go
package main

import (
    "fmt"
    "log"

    "github.com/softlayer/softlayer-go/datatypes"
    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
    "github.com/softlayer/softlayer-go/sl"
)

var sess *session.Session

func main() {
    sess = session.New()

    newUser := datatypes.User_Customer{
        Username:     sl.String("johnsmith"),
        FirstName:    sl.String("John"),
        LastName:     sl.String("Smith"),
        Email:        sl.String("johnsmith@example.com"),
        CompanyName:  sl.String("Example Co."),
        Address1:     sl.String("123 Oak St."),
        City:         sl.String("Champaign"),
        State:        sl.String("IL"),
        Country:      sl.String("US"),
        TimezoneId:   getTimezoneID("EST"),
        UserStatusId: getUserStatusID("ACTIVE"),
    }

    password := "password"

    userID, err := createUser(&newUser, password)
    if err != nil {
        log.Fatal("Could not create user:", err)
    }

    fmt.Printf("New user ID: %d\n", userID)

    // For permissions, it's sufficient to send just the keynames to SoftLayer
    permissions := []datatypes.User_Customer_CustomerPermission_Permission{
        {KeyName: sl.String("TICKET_ADD")},
        {KeyName: sl.String("TICKET_VIEW")},
        {KeyName: sl.String("SERVER_ADD")},
        {KeyName: sl.String("VIRTUAL_GUEST_VIEW")},
    }

    err = addUserPermissions(userID, permissions)
    if err != nil {
        log.Fatal("Could not add user permissions:", err)
    }

    fmt.Println("Portal permissions added")

    err = deleteUser(userID)
    if err != nil {
        log.Fatal("Could not delete user:", err)
    }

    fmt.Printf("User %d deleted", userID)

}

func createUser(user *datatypes.User_Customer, password string) (int, error) {
    // Create the user, specifying the portal password (3rd argument - VPN
    // password - is optional, and not specified here)
    obj, err := services.GetUserCustomerService(sess).
        CreateObject(
            user,
            &password,
            nil)

    if err != nil {
        return -1, err
    }

    return *obj.Id, nil
}

func addUserPermissions(userID int, permissions []datatypes.User_Customer_CustomerPermission_Permission) error {
    _, err := services.GetUserCustomerService(sess).
        Id(userID).
        AddBulkPortalPermission(permissions)

    return err
}

// Delete user is accomplished by setting the user's status to CANCEL_PENDING
func deleteUser(userID int) error {
    _, err := services.GetUserCustomerService(sess).
        Id(userID).
        EditObject(&datatypes.User_Customer{
            UserStatusId: getUserStatusID("CANCEL_PENDING"),
        })

    return err
}

// helper function to get a user status ID from a keyname (e.g., ACTIVE)
func getUserStatusID(key string) *int {
    statuses, err := services.GetUserCustomerStatusService(sess).GetAllObjects()
    if err != nil {
        log.Fatal(err)
    }

    for _, status := range statuses {
        if *status.KeyName == key {
            return status.Id
        }
    }

    log.Fatal("Unable to locate user status matching [%s]", key)

    return nil
}

// helper function to get a timezone ID from a keyname (e.g., EST)
func getTimezoneID(key string) *int {
    timezones, err := services.GetLocaleTimezoneService(sess).GetAllObjects()
    if err != nil {
        log.Fatal(err)
    }

    for _, tz := range timezones {
        if *tz.ShortName == key {
            return tz.Id
        }
    }

    log.Fatal("Unable to locate timezone matching [%s]", key)

    return nil
}
```
