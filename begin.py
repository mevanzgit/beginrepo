# Webscraper Dem0
#Author: Micah Evans
#Date: 9/30/25

#Todo:
 #add populations and area 
 # Find out how to add to csv file


import requests #Sends http requests and gets html responses and store responses
from bs4 import BeautifulSoup       
import csv #Library to parse html(where responses are stored)


url = "https://www.scrapethissite.com/pages/simple/"    #URL being scraped

# Get HTML from URL store in reponse
response = requests.get(url)                            #Displays the reponse from the URL
print(response)                                         #Prints the response from the URL
#print(response.text)                                    #Prints the text from the response  

doc = BeautifulSoup(response.text, "html.parser")       #Translating it so python can understand 
#print(doc)      

country_info_boxes = doc.find_all(["div"], class_ = "col-md-4 country")  #Finding all the divs with the class name country

print(country_info_boxes)  

for country_info_box in country_info_boxes: 

    country = country_info_box.find(["h3"], class_ = "country-name")
    
    print(country.text.strip())
    
    capital = country_info_box.find(["span"], class_ = "country-capital")
    
    print(capital.text.strip())
    
    population = country_info_box.find(["span"], class_ = "country-population")
    print(population.text.strip())
    
    area = country_info_box.find(["span"], class_ = "country-area")
    print(area.text.strip())

    print("--------------")
    
    


