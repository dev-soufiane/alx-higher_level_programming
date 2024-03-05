#!/bin/bash
# Takes in a URL, sends a GET request to the URL and display response
curl -sfL "$1" -X GET
