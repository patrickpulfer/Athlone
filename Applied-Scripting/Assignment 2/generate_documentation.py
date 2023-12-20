import sys
import pydoc
import os
sys.path.insert(0,'src') # Necessary 
import App, tests, generate_documentation
from src import menu, basic_analysis, data_service, category_analysis, category_visualisations, visualisations_analysis


pydoc.pydocpath = os.getcwd()
pydoc.writedocs(os.getcwd())