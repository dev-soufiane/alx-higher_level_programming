#!/bin/bash
# takes in a URL sends GET to thr URL, displays response body
curl -sH "X-School-User-Id: 98" "$1"
