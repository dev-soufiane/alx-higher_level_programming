#!/bin/bash
# Takes in a URL, sends request to it while requesting its body-size-response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
