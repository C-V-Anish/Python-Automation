from bs4 import BeautifulSoup
import requests

website="https://www.udemy.com/courses/search/?src=ukw&q=react"
html_text=requests.get('https://www.udemy.com/courses/search/?src=ukw&q=react').text
print(html_text)

soup=BeautifulSoup(html_text,'lxml')

h3=soup.find_all('h3',class_="udlite-heading-md course-card--course-title--vVEjC")
print(len(h3))

