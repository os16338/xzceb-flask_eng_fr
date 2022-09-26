import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
VER_LT='2018-05-01'
trans = LanguageTranslatorV3(authenticator=authenticator,
version=VER_LT)
trans.set_service_url(url)

def english_to_french(english_text):
    language_trans = trans.translate(text=english_text, 
    model_id='en-fr').get_result()
    french_text = language_trans['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    language_trans = trans.translate(text=french_text, 
    model_id='fr-en').get_result()
    english_text = language_trans['translations'][0]['translation']
    return english_text
