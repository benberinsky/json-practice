#!/bin/bash

jq -r '.[].receiptTime' aviation.json | head -n 6

