#!/usr/bin/python3
#coding:UTF-8

import os
import glob
import traceback
import re
import sys

class sigma:
    # instance variable
    base_path = None
    repo_name = 'Azure-Sentinel'

    severity_pattern = re.compile(r'[Ss]everity:\s(?P<rule_severity>.+)[\n$]?')
    name_pattern = re.compile(r'[Nn]ame:\s(?P<rule_name>.+)[\n$]?')
    version_pattern = re.compile(r'[Vv]ersion:\s(?P<rule_version>[\d.]+)[\n$]?')
    rule_pattern = re.compile(r'[Kk]ind:\s(?P<rule_kind>.+)[\n$]?')

    result_separator = '","'

    ##
    # constructor
    ##
    def __init__(self, verbose_mode):
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.repo_path = self.base_path + '/' + self.repo_name

        if verbose_mode:
            print('[DEBUG] base_path\t: ' + self.base_path)
            print('[DEBUG] repo_path\t: ' + self.repo_path)

    def print_debug(self, message):
        print('[DEBUG] '+ message)

    def CheckRepo(self, verbose_mode):
        try:
            if(os.path.isdir(self.repo_path)):

                # debug
                if verbose_mode:
                    self.print_debug('Repository check OK.')

                return 0

            else:
                print('[ERROR] Repository check NG. Repository is nothing.')
                return 1
        
        except:
            print('[ERROR] Repository check failed. except happend.')
            return 1

    def MakeList(self, result_filePath, target_severity, verbose_mode):
        ##
        # Get yaml files
        ##
        sigma_path = glob.glob(self.repo_path + '/**/*.yaml', recursive=True)

        for i in range(len(sigma_path)):

            sigma_path[i] = sigma_path[i].replace(self.base_path + '/','')
            
            # debug
            if verbose_mode:
                self.print_debug('target sigma file\t\t: '+ sigma_path[i])

            try:
                with open(sigma_path[i]) as sigma_file:
                
                    if verbose_mode:
                        self.print_debug('sigma file opend.')

                    ##
                    # Read full sigma file text.
                    ##
                    sigma_fileBody = sigma_file.read()

                    # debug
                    if verbose_mode:
                        self.print_debug('Load sigma file complete.')

                    ##
                    # ! Check valid sigma file.
                    ##
                    sigma_fileBodyCheck = sigma_fileBody.lower()

                    if ('severity: ' in sigma_fileBodyCheck)\
                    and ('name: ' in sigma_fileBodyCheck)\
                    and ('version: ' in sigma_fileBodyCheck)\
                    and ('kind: ' in sigma_fileBodyCheck):

                        # debug
                        if verbose_mode:
                            self.print_debug('Check valid sigma OK.')

                        ##
                        # Get rule severity.
                        ##
                        rule_severity = re.search(self.severity_pattern, sigma_fileBody).group('rule_severity')

                        ##
                        # Unmatch severity, go to next file.
                        ## 
                        if target_severity != "All" and target_severity != rule_severity:

                            # debug
                            if verbose_mode:
                                self.print_debug('Unmatch severity. Target severity\t: ' + target_severity)
                                self.print_debug('rule_severity\t: ' + rule_severity)

                            continue
                        
                        # debug
                        if verbose_mode:
                            self.print_debug('Match severity\t\t\t: ' + rule_severity)

                        ##
                        # Get rule name.
                        ##
                        rule_name = re.search(self.name_pattern, sigma_fileBody).group('rule_name')

                        # debug
                        if verbose_mode:
                            self.print_debug('Rule name\t\t\t: ' + rule_name)

                        ##
                        # Get version.
                        ##
                        rule_version = re.search(self.version_pattern, sigma_fileBody).group('rule_version')

                        # debug 
                        if verbose_mode:
                            self.print_debug('Rule version\t\t\t: ' + rule_version)

                        ##
                        # Get kind.
                        ##
                        rule_kind = re.search(self.rule_pattern, sigma_fileBody).group('rule_kind')

                        # debug
                        if verbose_mode:
                            self.print_debug('Rule kind\t\t\t: ' + rule_kind)

                        ##
                        # Write result.
                        ##
                        with open(result_filePath, mode='a') as rf:
                            rf.write('"' + rule_name + self.result_separator + rule_severity + self.result_separator\
                                        + rule_version + self.result_separator + rule_kind + self.result_separator + sigma_path[i] + '"\n')

                        # debug
                        if verbose_mode:
                            self.print_debug('Wrote a result.')

                    else:
                        # debug
                        if verbose_mode:
                            self.print_debug('Check valid sigma NG.')
                            self.print_debug('Severity in sigma file\t\t: ' + str('severity: ' in sigma_fileBodyCheck))
                            self.print_debug('Name in sigma file\t\t: ' + str('name: ' in sigma_fileBodyCheck))
                            self.print_debug('Version in sigma file\t\t: ' + str('version: ' in sigma_fileBodyCheck))
                            self.print_debug('Kind in sigma file\t\t: ' + str('kind: ' in sigma_fileBodyCheck))
                            self.print_debug('Next sigma file.')
                            self.print_debug('----------------')
                        continue

            except:
                traceback.print_exc()
                sys.exit()