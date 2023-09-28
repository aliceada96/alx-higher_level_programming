#!/bin/bash
# Sends a Json post request, URL as argument, displays response body
curl -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$1"