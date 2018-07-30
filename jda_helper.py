import os
import sys
import logging
from pprint import pprint
import argparse
import configparser
from dom import *
import error_codes as ec

#========================================================================================
#                      READ PATHS AND FLAGS FROM DOM SETTINGS INI FILE                 ==
#========================================================================================
#Read dom_settings_path
dom_settings_path = os.environ.get('DOM_REFRESH_CONFIG', 'NOT_SET');

# Verify dom_settings_path
if(dom_settings_path == None or dom_settings_path == 'NOT_SET'):
  print('Environment Variable <DOM_REFRESH_CONFIG> not set. Exiting');
  sys.exit(ec.ENV_NOT_SET);

#Load DOM Settings
try:
  settings = configparser.ConfigParser();
  settings.read(dom_settings_path);

  if('PATHS' in settings):
    paths = settings['PATHS']

  if('FLAGS' in settings):
    flags = settings['FLAGS']

  if('SETTINGS' in settings):
    dom_settings = settings['SETTINGS']
except:  
  sys.exit(ec.ERROR_PARSING_CONFIG);

#========================================================================================
#                              CREATE DOM HELPER OBJECT                                ==
#========================================================================================
try:
  dom = DOMHelper(paths,dom_settings)
except InvalidConfigurationError:
  sys.exit(ec.INVALID_CONFIG_VALUES);


if(dom == None):
  print('DOM Helper could not be Instantiated. Exiting');
  sys.exit(ec.GENERIC_ERROR);

#========================================================================================
#                              PARSE COMMAND LINE ARGUMENTS(--SILENT,--LOGLEVEL)       ==
#========================================================================================
parser = argparse.ArgumentParser(description='Refresh the DOM Codebase');
parser.add_argument("-l", "--loglevel", choices=['DEBUG', 'INFO', 'ERROR'],help="Set Logging Level");
parser.add_argument("-s","--silent",help="Skips user input, reads from ini file",action="store_true");
args = parser.parse_args();

#========================================================================================
#                                     CREATE LOGGER                                    ==
#                               (LOGGING STARTS FROM HERE)                             ==
#========================================================================================

#Create Logger
if(args.loglevel != None):
  logging.basicConfig(format='%(levelname)s\\t- %(asctime)s : %(message)s',datefmt='%d/%m/%Y %I:%M:%S',filename='\\'.join([paths['LOG_FOLDER'],'jda_helper.log']), filemode='a', level=args.loglevel)


#========================================================================================
#                              READ FLAGS IF SILENT MODE IS ENABLED                    ==
#========================================================================================
#Read action flags
if(not args.silent):  
  flags['DoUpdate'] = str(input('Run Clearcase Update ? : [Y/N][Default:Y]').upper() != 'N')
  flags['DoBuild'] = str(input('Run Build ? : [Y/N][Default:Y]').upper() != 'N')
  flags['DoGenschema'] = str(input('Run Gen Schema ? : [Y/N][Default:Y]').upper() != 'N')
  flags['DoPopulateData'] = str(input('Run Populate Data ? : [Y/N][Default:Y]').upper() != 'N')

logging.debug('flags are ...' + 'DoUpdate : ' + flags['DoUpdate'] + ' DoBuild : ' + flags['DoBuild'] + ' DoGenschema : ' + flags['DoGenschema'] + ' DoPopulateData : ' + flags['DoPopulateData'])


#========================================================================================
#                              START PROCESSES SEQUENTIALLY                            ==
#========================================================================================

logging.info('Codebase Refresh Started...')

if(flags['DoUpdate'].lower() == 'true'):
  dom.clear_case_update()

if(flags['DoBuild'].lower() == 'true'):
  dom.build('build_all')

if(flags['DoGenschema'].lower() == 'true'):
  dom.gen_schema()

if(flags['DoPopulateData'].lower() == 'true'):
  dom.populate_data()

logging.info('Codebase Refresh Finished...')
sys.exit(ec.SUCCESS);