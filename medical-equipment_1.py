#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
from common import destoryPop, countPage, hasImg_products, get_Pinfo
import math
maxium=0
page=1
START_URL=['https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/floor-pad-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/pull-cord-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/personal-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/bed-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/infrared-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/chair-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/patient-alarms-restraints/doorway-alarms.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/slings.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/transfer-devices.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/transfer-devices.html'
, 'https://www.4mdmedical.com/medical-equipment/lifts/lifts.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/surgical-instruments-devices.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/warmers.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/surgical-lights.html'
, 'https://www.4mdmedical.com/medical-equipment/surgical-equipment/surgical-tables.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/stretcher-accessories.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/or-specialty-stretchers.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/evacuation-chairs.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/ambulance-cots.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/transport-stretcher.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/foldable-pole-stretchers.html'
, 'https://www.4mdmedical.com/medical-equipment/stretchers/splint-stretchers.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/crash-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/miscellaneous.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/specimen-collection-cart.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/procedure-specialty.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/case-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/laundry-linen-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/chart-holders-racks.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/ekg-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/treatment-cart.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/utility.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/computer-stands.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/anesthesia-cart.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/medication-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/carts/hospital-carts.html'
, 'https://www.4mdmedical.com/medical-equipment/miscellaneous.html'
]
path = "chromedriver"
for goURL in START_URL:
    driver=destoryPop(goURL)#pop up destroy
    totalPN=countPage() #fetch total page number
    current_url=driver.current_url
    for page in range(1,totalPN+1):
        driver.get(current_url+"?p="+str(page))
        time.sleep(8)
        hasImg_urlList=hasImg_products() #Get URL list of products having img
        get_Pinfo(hasImg_urlList)