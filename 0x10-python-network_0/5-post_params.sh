#!/bin/bash
# post request with variable email and subject
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
