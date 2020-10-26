from pathlib import Path
import sys
p = Path().absolute() #get path to parent dir
sys.path.append(str(p)) #append to module path

from raspimon_helper import Raspimon #class 
from raspimon_helper.helper import speak #helper file

#using class
pimon = Raspimon()
pimon.sayHello()

#using helper file with functions
speak()
