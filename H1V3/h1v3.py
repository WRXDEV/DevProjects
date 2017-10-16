# Update 0.0.5 / Added 

import os, sys, time, socket, commands
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

class Messages:

	_messageMain_ = Fore.WHITE
	_messageWarn_ = Fore.RED
	_messageEntr_ = Fore.BLUE
	_messageUsag_ = {
			'Usage:':['python h1v3.py <Option> <Argument>'],
			'Single.Argument.Options:':[
				'\t-h	or 	--help	\t\t<>\t\tDisplays This Help Screen',
				'\t--interactive		\t\t<>\t\tEnters Main Loop Console'
				],
			'Multiple.Argument.Options':[
				'\t-s 	or 	--scan	\t\t<>\t\tUsage: python h1v3.py -s <Scantype> <ScantypeArguments>',
				'\t		Scan types:',
				'\t		-f 	or 	--file	<>\t\t Sets Scan Type To File 					<> Usage -f <inputfile> <FollowingArgument>',
				'\t				--sfd	<>\t\t Sets File Scan To Check For Positive Dorks	<> Usage -f <inputfile> --sfd dork1+dork2+dork3 <FollowingArgument>',
				'\t		-o   or 	--output <>\t\t Sets Output File Name 					<> Usage -f <inputfile> <FollowingArgument> -o <outputfile>',
				'\n'
				]
			}
	_messageBann_ = Fore.GREEN+Style.BRIGHT+"""  

		'|| '||'  '|' '||       ||    .           '||''|.                          
		'|. '|.  .'   || ..   ...  .||.    ....   ||   ||    ...    ....    ....  
		||  ||  |    ||' ||   ||   ||   .|...||  ||''|'   .|  '|. ||. '  .|...|| 
		||| |||     ||  ||   ||   ||   ||       ||   |.  ||   || . '|.. ||      
		|   |     .||. ||. .||.  '|.'  '|...' .||.  '|'  '|..|' |'..|'  '|...' 
                                                                              """+Fore.WHITE+"""
                                                                             
						'||' '|' 
						  || |   
						   ||    
						  | ||   
						.|   ||.    """+Fore.MAGENTA+"""

*\______________________________________________________________________________________________________/*
                    """+Fore.MAGENTA+"""                Created By The Hive For The Hive 
                    """+Fore.BLUE   +"""                      Author: """+Fore.WHITE+"""J4CK3L5YN746X6

    """
    
	def _PrintUsage_(self):
		for keys in self._messageUsag_:
			print str(keys)+'\n'
			for line in self._messageUsag_[str(keys)]:
				print str(line)
			
			
		return None
	
	def _PrintBanner_(self):
		
		print self._messageBann_
		
		return None
	
	
	
class MainOps:

    MSG = Messages()
    
    def Scan(self, TYPE=None, FILE=None, LIST=None, OUTPUT=None):
	
	if TYPE == 'file':
		
		if FILE == None:
			
			print self.MSG._messageWarn_+' Operation Failed Due To No File Entry Being Called While Scan Type Set To File'
			
			return None
			
		
		if LIST == None:
			
			print self.MSG._messageWarn_+' Operation Failed Due To No Dorks Being Entered For Parsing...'
			
			return None
			
		# Open File 
		_FileText_ = open(str(FILE)).read()
		
		_TempDict_ = {}
		
		# Create Key Lists For Each Dork
		for dork in LIST:
			
			_TempDict_[str(dork)] = []
			
		for line in _FileText_:
			
			for dork in LIST:
				
				if str(dork) in str(line):
					
					_TempDict_[str(dork)].append(str(line))
					
		# Write Output 
		if OUTPUT == None:
			
			_OUTPUTEXE_ = str(FILE)+'-Scan.txt'
			
			OUTPUT = _OUTPUTEXE_
			pass
			
		_WriteFile_ = open(str(OUTPUT), 'w')
		for key in _TempDict_:
			
			_WriteFile_.write('Dork -> '+str(key)+'\n')
			for sites in _TempDict_[str(key)]:
				_WriteFile_.write(str(sites)+'\n')
		
	return None
    
    def _MainLoop_(self):
	
	Running = True
	
	while Running == True:
		
		_UserEntry_ = raw_input(self.MSG._messageEntr_+' <> ?:>> ')
		
		# Check for multple arguments
		if str(' ') in _UserEntry_:
			
			_UserEntry_ = _UserEntry.split(' ')
			
			
			return None
			
		if _UserEntry_ in ['help', 'Help', 'HELP']:
			
			self.MSG._messageUsag_()
			
			pass
			
		elif _UserEntry_ in ['exit', 'Exit', 'EXIT', 'abort']:
			
			Running = False
			
		
		
	return None
	
# Main Loop
def Main():
	
	MSG = Messages()
	MOP = MainOps()
	
	MSG._PrintBanner_()
	
	# Variable Status Dictionary
	VarStat = {
		'_ScanSetting_':False,
		'_ScanType_':None,
		'_ScanDorkList_':[],
		'_ScanOutName_':None,
		'_ScanInputFile_':None
		
		}
		
	# Arg Check 
	for arg in sys.argv:
		
		# Help Input Check
		if arg in ['-h', '--help']:
			
			MSG._PrintUsage_()
			
			pass
			
		elif arg in ['--interactive']:
			
			MOP._MainLoop_()
			
			pass
			
		# Scan Option Check
		elif arg in ['-s', '--scan']:
			
			VarStat['_ScanSetting_'] = True
			pass
			
		# File Input Check
		elif arg in ['-f', '--file']:
			
			_EntryArg_ = sys.argv.index(str(arg))+1
			_FileEntry_ = str(sys.argv[int(_EntryArg_)])
			
			# Check If File Exists 
			_FileCheck_ = os.path.isfile(str(_FileEntry_))
			if _FileCheck_ == False:
				
				print MSG._messageWarn_+' Operation Failed Since Entry %s Location Check Returned False' % (str(_FileEntry_))
				sys.exit(1)
				
			VarStat['_ScanInputFile_'] = str(_FileEntry_)
			VarStat['_ScanType_'] 	    = 'file'
			pass
			
		# Scan For Dorks Input check
		elif arg in ['--sfd']:
			
			_EntryArg_ = sys.argv.index(str(arg))+1
			_dorkEntry_  = str(sys.argv[int(_EntryArg_)])
			
			if str('+') in str(_dorkEntry_):
				
				_DorkList_ = _dorkEntry_.split('+')
				for dork in _DorkList_:
					
					VarStat['_ScanDorkList_'].append(str(dork))
					
				pass
				
			else:
				VarStat['_ScanDorkList_'].append(str(_dorkEntry_))
				
				pass
				
			pass
			
		# File Output Check
		elif arg in ['-o', '--output']:
			
			_EntryArg_ = sys.argv.index(str(arg))+1
			_nameentry_ = str(sys.argv[int(_EntryArg_)])
			
			VarStat['_ScanOutName_'] = str(_nameentry_)
			
			pass
			
			
	if VarStat['_ScanSetting_'] == True:
		
		# Scan Checking 
		if VarStat['_ScanType_'] == None:
			
			print MSG._messageWarn_+' Operation Failed Due To Scan Operation Being True But No Scan Type Was Entered'
			sys.exit(1)
			
		MOP.Scan(TYPE=str(VarStat['_ScanType_']), FILE=str(VarStat['_ScanInputFile_']), LIST=str(VarStat['_ScanDorkList_']), OUTPUT=str(VarStat['_ScanOutName_']))
		
		pass
	
	sys.exit(1)
	
Main()