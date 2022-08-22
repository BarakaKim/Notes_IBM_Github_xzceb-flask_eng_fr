""" Module to translate the text"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
def english_to_french(text1):
    """ function to convert Eng to French"""
    frenchtranslation=language_translator.translate(
        text=text1,
        model_id='en-fr'
    ).get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(text1):
    """ function to convert Eng to French"""
    englishtranslation=language_translator.translate(
        text=text1,
        model_id='fr-en'
    ).get_result()
    return englishtranslation.get("translations")[0].get("translation")
#def english_to_french(english_text):
 #   """ function to convert Eng to French"""
    #if english_text=="":
        #french_text = "Null input"
        #print(frenchText)
    #else:
        #conv = language_translator.translate(english_text,model_id='en-fr').get_result()
        #print(json.dumps(conv, indent=2, ensure_ascii=False))
        #french_text=(conv["translations"][0]["translation"])         
    #return french_text

#def french_to_english(french_text):
 #   """ function to convert French to Eng"""
  #  if french_text=="":
   #     english_text = "Null input"
    #else:
     #   conv2 = language_translator.translate(french_text,model_id='fr-en').get_result()
        #print(json.dumps(englishText, indent=2, ensure_ascii=False))
      #  english_text=(conv2["translations"][0]["translation"])
    #return english_text