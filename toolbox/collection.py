# Imports do Sistema Operacional
import os
import os.path
import sys
import sysconfig
import re
import shutil

# Imports do Python e bibliotecas relacionadas
import yaml
import json
import time
import glob
import random
import pathlib
import requests
import enum
from enum import Enum
from enum import unique
import datetime
from datetime import date
import unidecode
from unidecode import unidecode
import zeep
from zeep import xsd
from zeep import Client
from zeep import Settings
from zeep.plugins import HistoryPlugin

# Imports do FrameWork
import Pyautomators
import orcautomators
import webautomators
from webautomators import WebRemoteDriver

# Imports do Selenium
import selenium
from selenium import common
from selenium import webdriver
from selenium.webdriver import common
from selenium.webdriver import support
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import invisibility_of_element_located
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

# Imports Webdriver Manager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeDriverManager