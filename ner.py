import spacy
from spacy import *
import html,re ,contractions,emoji,unidecode
from textblob import TextBlob
from google_trans_new import google_translator

nlp = spacy.load('en_core_web_sm')

def normalization(sentence,tokenize=True):
   textBlb = TextBlob(sentence)
   textCorrected = textBlb.correct()
   sentence = html.unescape(sentence)
   regex = re.compile(r'[\n\r\t]')
   sentence = regex.sub(" ", sentence)
   sentence = re.sub(r'http\S+', '', sentence)
   sentence = re.sub('@[^\s]+','',sentence)
   try:
          lang = detect(sentence)
          if lang != 'en':
              translator = google_translator()
              sentence = translator.translate (sentence,lang_tgt='en')
   except :
          try:
              translator = google_translator()
              sentence = translator.translate (sentence,lang_tgt='en')
          except:
              pass
   sentence = contractions.fix(sentence)
   sentence = unidecode.unidecode(sentence)
   return sentence

def tags(sentence):
	sentence=normalization(sentence)
	doc = nlp(sentence)
	NER=[]
	for ent in doc.ents:
	        NER.append(ent.text)
	        NER.append(ent.label)
	return NER
