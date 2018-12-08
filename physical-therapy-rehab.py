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
START_URL=['https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/mobility.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/bikes-and-helmets.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/toileting-bathing.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/seating-mobility.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/furniture.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/positioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/pediatrics/standers-gait-trainers.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/aquatic-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/storage.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/clinical-supplies.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/upper-extremity-exercise.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/reference.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/balance-total-body-conditioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/exercise-bands-tubing-balls-weights.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/rehab-supplies/lower-extremity-exercise-rebounders-flexibility.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/fitness-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/hot-cold-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/massage-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/walking-aides.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/therapy-room-essentials.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/therapy-fitness/personal-care-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/balance-total-body-conditioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/mat-platforms.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/treatment-tables.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/carts-stools.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/traction.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/rehab-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/exercise-hook-up-pole.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/treatment-furniture/work-activity-tables.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/back-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/scar-management.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/knee-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/finger-splints.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/upper-extremity-positioning.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/arthritis-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/elbow-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/cervical-collars.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/taping-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/shoulder-supports-slings.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/thumb-supports.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/compression-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/workhard-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/orthopedics/wound-care.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/soft-goods.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/exercise-equipment/strength-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/exercise-equipment/cardio-equipment.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/hot-cold-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/massage-wellness.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/iontophoresis.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/compression-therapy-products.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/hydrotherapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/biofeedback-pelvic-health.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/paraffin.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/modalities/electrotherapy-ultrasound.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/continuous-passive-motion.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/range-of-motion.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/assessments.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/dexterity-sensory.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/diagnostic-tools.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/evaluation/strength-testing.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/balls.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/vestibular-therapy.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/visual-stimulation.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/furniture.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/relaxation.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/manipulatives.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/gross-motor.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/tactile-stimulation.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/sensory-motor/sensory-development.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/casting-fracture-bracing.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/precuts.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/dynamic-splinting.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/preformed-splints.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/strapping-material.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/splinting-tools-materials-accessories.html'
, 'https://www.4mdmedical.com/physical-therapy-rehab/splinting-casting/padding-materials.html'
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