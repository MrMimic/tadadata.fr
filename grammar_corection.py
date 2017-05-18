
import re
import time
import json
import requests
from urllib import parse
start = time.time()

textToCorrect = 'telephonne appele apelle appelle'

''' HEADER FOR API CONNECTIONS '''
spellCheck = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': 'AZURE_KEY' }
''' SPELL CHECK PARAMETERS '''
params = parse.urlencode({
'mode': 'spell',
'mkt': 'fr-fr',
'text': textToCorrect 
})

''' SPELL CHECK REQUEST '''
rawData = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/SpellCheck/?%s" % params, headers=spellCheck)
jsonData = json.loads(rawData.text)

''' IF MISTAKE, PRINT '''
if len(jsonData['flaggedTokens']) > 0:
	print('Analysed in {} sec'.format(round(time.time() - start, 3)))
	print('- ' * 50)
	for mistake in jsonData['flaggedTokens']:
		print('Written: {}\t\tCorrect: {}\t\t(score: {})'.format(mistake['token'], mistake['suggestions'][0]['suggestion'], round(mistake['suggestions'][0]['score'], 3)))
		if mistake['suggestions'][0]['score'] > 0.8:
			textToCorrect = re.sub(mistake['token'], mistake['suggestions'][0]['suggestion'], textToCorrect)
	print('- ' * 50)
	print('Corrected output :\n{}'.format(textToCorrect))
else:
	print('Good boy, everything\'s correct')
