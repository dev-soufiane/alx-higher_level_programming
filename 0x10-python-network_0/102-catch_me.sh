#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!"
curl -sX PUT -L -d "user_id=98" --header "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
