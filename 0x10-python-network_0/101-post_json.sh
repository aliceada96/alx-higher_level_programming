#!/bin/bash
# Sends a Json post request, URL as argument, displays response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
