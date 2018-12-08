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
START_URL=['https://www.4mdmedical.com/daily-living-aids/reading-writing-aids/magnifiers.html'
, 'https://www.4mdmedical.com/daily-living-aids/reading-writing-aids/hand-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/visual-hearing-impaired-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/cups-drinking-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/feeders-arm-supports.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/miscellaneous.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/dining-accessories.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/utensils.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/plates-bowls.html'
, 'https://www.4mdmedical.com/daily-living-aids/dining-aids/kitchen-supplies.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/shoelaces-fasteners.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/dressing-education.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/slippers-socks.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/grooming-accessories.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/sock-stocking-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/hip-kits.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/oral-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/medication-supplies.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/shoehorns.html'
, 'https://www.4mdmedical.com/daily-living-aids/dressing-aids/dressing-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/oral-motor-tools.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/speech-assessments.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/assistive-technology-speech-communication.html'
, 'https://www.4mdmedical.com/daily-living-aids/speech-communication/cognitive-assessments.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/brushes-scrub-sponges.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/bath-shower.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/hand-held-showers.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/bathing.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/mirrors-toileting-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/commodes.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/toilet-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/grab-bars-rails.html'
, 'https://www.4mdmedical.com/daily-living-aids/bath-toileting/miscellaneous.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/household-helpers.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/scissors.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/automotive-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/mouth-sticks-head-pointers.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/door-knob-turners.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/trolleys-carts.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/bedroom-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/furniture-risers.html'
, 'https://www.4mdmedical.com/daily-living-aids/home-accessories/telephones.html'
, 'https://www.4mdmedical.com/daily-living-aids/hygiene-products/oral-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/hygiene-products/denture-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/hygiene-products/shaving-cream.html'
, 'https://www.4mdmedical.com/daily-living-aids/medication-aids/pill-crushers.html'
, 'https://www.4mdmedical.com/daily-living-aids/medication-aids/pill-crushers.html'
, 'https://www.4mdmedical.com/daily-living-aids/low-vision/magnifiers.html'
, 'https://www.4mdmedical.com/daily-living-aids/low-vision/talking-devices.html'
, 'https://www.4mdmedical.com/daily-living-aids/miscellaneous-aids.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/grooming-supplies.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/urinals.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/hand-sanitizers.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/bedside-products.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/miscellaneous.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/cleansing.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/creams-ointments.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/oral-care.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/enemas.html'
, 'https://www.4mdmedical.com/daily-living-aids/personal-care/tissues.html'
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