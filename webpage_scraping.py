#!/usr/bin/python3

''' IMPORTS '''
from urllib import request
from bs4 import BeautifulSoup

''' Scraping function '''
def scraping(URL):
	pageResponse = request.urlopen(URL)
	pageData = pageResponse.read()
	return pageData

''' Parsing Function '''
def parsing(pageData):
	pageSoup = BeautifulSoup(pageData, 'html.parser')
	rawRecette = pageSoup.find_all('div', attrs = {'class': 'm_content_recette_todo'})
	recette = str(rawRecette[0]).split('<br/>')
	for etape in recette:
		if etape != '':
			print('- {}'.format(etape))
	
pageWeb = scraping('http://www.marmiton.org/recettes/recette_pates-a-la-carbonara_80453.aspx')
recette = parsing(pageWeb)
