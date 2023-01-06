#!/usr/bin/python3
#coding:UTF-8

import os
import sys
import datetime
import traceback
import modules.sigmafiles
import argparse

## variable
today = str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S'))
cwd = os.path.dirname(__file__)

## files
result_file = cwd + '/results/' + today + '.log'

def ERROR_EXIT():
	print('[ERROR]Tool exit...')
	sys.exit()

def make_resultFile():
	try:
		with open(result_file, mode='x') as f:
			pass
		with open(result_file, mode='a') as f:
			f.write('"ruleName","severity","version","kind","filePath"\n')
		return result_file

	except FileExistsError:
		print('File exists: ' + result_file)
		traceback.print_exc()
		ERROR_EXIT()

##
# Help menu
##
parser = argparse.ArgumentParser(description='Generate sigma file path for Azure Sentinel Repository. Build by Python 3.10.9.')

parser.add_argument('-s', '--severity', type=str, default='All',\
					help='Specify for rule severity. default is All, severity of High, Medium, Low, Informational')

parser.add_argument('-k', '--kind', type=str, default='Scheduled',\
					help='Specify for rule kind. default is Scheduled, kind of Scheduled, ...')

parser.add_argument('-v', '--verbose', action='store_true', help='Output debug level messages.')
args = parser.parse_args()


sigmas = modules.sigmafiles.sigma(args.verbose)

if sigmas.CheckRepo(args.verbose) == 1:
	ERROR_EXIT()

# Generate result file.
result_filePath = make_resultFile()

# Generate list.
sigmas.MakeList(result_filePath, args.severity, args.verbose)

print('Tool exec end.')