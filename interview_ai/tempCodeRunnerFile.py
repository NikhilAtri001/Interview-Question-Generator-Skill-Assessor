import os ##used for folders , files and paths(opearting system)
import re ##used for text cleaning(regular expression) egPython!!!@@@ SQL###123 -> Python SQL
import pandas as pd
from functools import lru_cache ##lru->least recently used A decorator that stores function results in memory to avoid redundant calculations
from collections import Counter ##used to find most common skill through their occurrence

DATA_DIR    = os.path.join(os.path.dirname(__file__), "data")