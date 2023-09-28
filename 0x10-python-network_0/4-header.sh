#!/bin/bash
# takes in a URL as an argument, has a custom header
curl -s -H "X-School-User-Id: 98" "$1"
