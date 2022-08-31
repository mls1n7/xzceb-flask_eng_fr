"""This Module Translates french to english and english to french"""
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
    version='2022-08-05',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishtofrench(englishtext):
    """This function translates english to french"""
    frenchtranslation = language_translator.translate(
                       text=englishtext, model_id=
                        'en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def frenchtoenglish(frenchtext):
    """This function translates french to english"""
    englishtranslation = language_translator.translate(
                        text=frenchtext, model_id=
                        'fr-en').get_result()
    return englishtranslation.get("translations")[0].get("translation")
