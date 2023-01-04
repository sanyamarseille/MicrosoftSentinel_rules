#!/usr/bin/python3
#coding:UTF-8

import os
import re
import sys
import subprocess
import datetime

## variable
today = str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S'))
cwd = os.getcwd()

severity_pattern = re.compile(r'^severity:\s(?P<rule_severity>.+)$')
name_pattern = re.compile(r'^name:\s(?P<rule_name>.+)$')
version_pattern = re.compile(r'^version:\s(?P<rule_version>[\d.]+)$') 
rule_pattern = re.compile(r'^kind:\s(?P<rule_type>.+)$') 

## files
make_rule_list_script = cwd + '/makeSigmaFiles.sh'
rule_list =  cwd + '/SigmaFiles.txt'
result_file = cwd + '/results/' + today + '.log'

def make_rule_list():
	result = subprocess.run([make_rule_list_script])
	if result.returncode != 0:
		print('failed to make rule list')
		sys.exit()

def make_result_file():
	try:
		with open(result_file, mode='x') as f:
			pass
		with open(result_file, mode='a') as f:
			f.write('severity;ruleName;kind;version;sigmaFile\n')

	except FileExistsError:
		print('File exists: ' + result_file)
		sys.exit()


make_rule_list()
make_result_file()

with open(rule_list) as rule:
	rule_file = rule.readline()

	while rule_file:
		rule_file = rule_file.replace("\n","")

		with open(rule_file) as sigma:
			data = sigma.readline()

			while data:
				data = data.replace("\n","")

				severity_result = severity_pattern.search(data)
				name_result = name_pattern.search(data)
				version_result = version_pattern.search(data)
				rule_result = rule_pattern.search(data)

				if severity_result is not None:
					rule_severity = severity_result.group('rule_severity')
				if name_result is not None:
					rule_name = name_result.group('rule_name')
				if version_result is not None:
					rule_version = version_result.group('rule_version')
				if rule_result is not None:
					rule_type = rule_result.group('rule_type')

				# read next line at rule file
				data = sigma.readline()
		
		with open(result_file, mode='a') as rf:
			rf.write(rule_severity + ';' + rule_name + ';' + rule_type + ';' + rule_version + ';' + rule_file.replace(cwd + '/', '') + '\n')

		#break
		# read next line at rule list
		rule_file = rule.readline()
