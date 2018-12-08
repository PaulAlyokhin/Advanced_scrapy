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
START_URL=['https://www.4mdmedical.com/medical-supplies/diabetic-supplies/accessories.html'
, 'https://www.4mdmedical.com/medical-supplies/diabetic-supplies/meter.html'
, 'https://www.4mdmedical.com/medical-supplies/diabetic-supplies/test-strips.html'
, 'https://www.4mdmedical.com/medical-supplies/diabetic-supplies/glucose-calibrator.html'
, 'https://www.4mdmedical.com/medical-supplies/diabetic-supplies/insulin-syringes.html'
, 'https://www.4mdmedical.com/medical-supplies/diabetic-supplies/lancet-lancet-devices.html'
, 'https://www.4mdmedical.com/medical-supplies/catheters/trays.html'
, 'https://www.4mdmedical.com/medical-supplies/catheters/external-catheters.html'
, 'https://www.4mdmedical.com/medical-supplies/catheters/urinary-drain-bags-accessory.html'
, 'https://www.4mdmedical.com/medical-supplies/catheters/foley-catheters.html'
, 'https://www.4mdmedical.com/medical-supplies/catheters/intermittent-catheters.html'
, 'https://www.4mdmedical.com/medical-supplies/catheters/irrigation-trays-syringes.html'
, 'https://www.4mdmedical.com/medical-supplies/catheters/securement.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/urological-collection-devices.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/2-piece-systems.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/cleaners-deodorants.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/skin-barriers.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/accessories.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/irrigation.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/tubing-connectors.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/pastes-powders.html'
, 'https://www.4mdmedical.com/medical-supplies/urology-ostomy/1-piece-systems.html'
, 'https://www.4mdmedical.com/medical-supplies/dietary-supplements/feeding-tubes.html'
, 'https://www.4mdmedical.com/medical-supplies/dietary-supplements/feeding-pumps.html'
, 'https://www.4mdmedical.com/medical-supplies/dietary-supplements/nutritional-supplements.html'
, 'https://www.4mdmedical.com/medical-supplies/dietary-supplements/administration-sets.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/gowns.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/bibs.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/footwear.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/head-face.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/bath-hand-towels.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/protective-clothing.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/drape-sheets-nonbedding.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/exam-shorts.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/scrubwear.html'
, 'https://www.4mdmedical.com/medical-supplies/apparel/aprons.html'
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