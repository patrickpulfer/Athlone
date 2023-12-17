import sys
import pydoc
import os
sys.path.insert(0,'src') # Necessary 
import App
from src import menu, basic_analysis, data_service


pydoc.pydocpath = os.getcwd()
pydoc.writedocs(os.getcwd())