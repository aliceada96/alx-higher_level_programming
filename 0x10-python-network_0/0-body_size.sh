#!/bin/bash
# Displays the size of the response body
curl -s "$1" | wc -c
