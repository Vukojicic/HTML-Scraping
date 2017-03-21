#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def main():
	url= "https://www.kupindo.com/pretraga.php?bSearchBox=1&Pretraga=dusanov+zakonik"
	url_page2="https://www.kupindo.com/pretraga.php?Pretraga=dusanov%20zakonik&CeleReci=0&iStr="

	
	for x in range(0,10):
		url_next= url_page2 + str(x)
		get_data_from_url(url_next)
	


def get_data_from_url(url):

	r= requests.get(url)

	soup=BeautifulSoup(r.content , "lxml")

	g_data=soup.find_all("div" , {"class" : "product"})
	c_data=soup.find_all("span" , {"class" : "item_price"})

	

	filename="name.xlsx"
	f=open(filename ,"a")
	f.write("")

	filename="price.xlsx"
	g=open(filename ,"a")
	g.write("")

	filename="all.txt"
	s=open(filename ,'a')
	s.write("")


	for item in g_data:
		name1=item.contents[3].text
		f.write(name1.replace(",","|")+"\n")

	for item in c_data:
		price1=str(item.contents[0])
		g.write(price1.replace("din", "").replace("\n","")+"\n")	

	for item in g_data:
		print(item.contents[3].text)
		print(item.contents[5].text)
		n1=item.contents[3].text
		n2=item.contents[5].text
		s.write(n1+"\n"+n2+"\n")

	

	

	f.close()
	g.close()
	s.close()

main()