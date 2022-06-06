"""
Zodule (Zoda module System)
"""

import zipfile
import getpass
import shutil
import os
import datetime
import sys
import json


class Config:
	dirs={
	"zodule": "zodule",
	"sourcefiles": "source"
}
	files={
	"data": "zodule.data.json",
	"config": "zodule.cfg.json",
	"changes": "zodule.chages.json"
}

class Zipper:
	def __init__(self,dir,src:list,zip=False):
		self.src=src
		self.zip=zip
		self.dir=dir
		self.files=[]
		self.dirs=[]
		
		self.found()
		self.zoduledir=self.dir+"/"+Config.dirs["zodule"]
		self.sourcefiledir=self.zoduledir+"/"+Config.dirs["sourcefiles"]	
		self.createfiles(zip)
		
	def found(self):
		for i in self.src:
			if i in os.listdir(self.dir):
				if os.path.isfile(os.listdir()[i]):
					self.files.append(i)
				elif os.path.isdir(os.listdir()[i]):
					self.dirs.append(i)
				else:
					print("Bu ne lan ben böyle birşey ne gördüm ne duydum :{")
			else:
				print(f"file/dir {i} not inside in {self.dir} ")

	def createfiles(self,mode,recreate=False):
		os.mkdir(self.zoduledir)
		os.mkdir(self.sourcefiledir)
		
		
		with open(f"{self.zoduledir}/{Config.files['data']}","w") as data:
			jsdata={
"name": f"{self.dir}"
}
			json.dump(jsdata,data)
		with open(f"{self.zoduledir}/{Config.files['changes']}","w") as changes:
			data=f"""
//created at {datetime.datetime.now()}
create:{getpass.getuser()}::{datetime.datetime.now()}::{self.zoduledir}/{Config.files["changes"]}
"""		
			changes.write(data)

		self.copyfiles()

	def copyfiles(self):
		for dir in self.dirs:
			shutil.copytree(dir,self.sourcefiledir
		
		for file in self.files:
			shutil.copy(file,self.sourcefiledir)

class Unzipper:
	def __init__(self,file):
		self.file=file
		self.unzip()
	def unzip(self):
		pass
		#TODO: add unzip
Zipper("test",["test.py"])
