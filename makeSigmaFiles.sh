#!/bin/bash

exec_path=`pwd`
repo_path="${exec_path}/Azure-Sentinel"
rule_list="${exec_path}/SigmaFiles.txt"

# Type (kind)
## scheduled rules
`grep -R "kind: Scheduled" ${repo_path} | grep "yaml" | awk -F ":" '{print $1}' > ${rule_list}`

# Severity
## High rules
#`grep -R "severity: High" ${repo_path} | grep "yaml" | awk -F ":" '{print $1}' > ${rule_list}`

## Medium
#`grep -R "severity: Medium" ${repo_path} | grep "yaml" | awk -F ":" '{print $1}' > ${rule_list}`

## Low
#`grep -R "severity: Low" ${repo_path} | grep "yaml" | awk -F ":" '{print $1}' > ${rule_list}`

## Informational
#`grep -R "severity: Informational" ${repo_path} | grep "yaml" | awk -F ":" '{print $1}' > ${rule_list}`

## 
# Status
## Available rules
#`grep -R "status: Available" ${repo_path} | grep "yaml" | awk -F ":" '{print $1}' > ${rule_list}`
