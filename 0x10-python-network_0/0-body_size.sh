#!/bin/bash
# Displays the size of the response body
curl -sI "$1" | wc -c
