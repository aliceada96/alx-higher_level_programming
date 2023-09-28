#!/bin/bash
# Sends a Json post request, URL as argument, displays response body
curl -X -s -H "Content-Type: application/json" -d @"$2" "$1"
