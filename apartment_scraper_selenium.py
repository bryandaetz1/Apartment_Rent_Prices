# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:39:55 2020

@author: bdaet
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd


#initializing the webdriver
options = webdriver.ChromeOptions()
    
#set path to driver
driver = webdriver.Chrome(executable_path = "C:/Users/bdaet/OneDrive/Documents/Data Science/Apartments_Project/chromedriver",
                              options = options)
driver.set_window_size(1120, 1000)
    
url = 'https://www.apartments.com/santa-barbara-ca/'
driver.get(url)
apts = []

#for now, using num_listing to determine how many listings to scrape
num_listings = 5
x = 0

apt_buttons = driver.find_elements_by_class_name('placardHeader')
#while x + 1  < num_listings:               #doesn't seem like this is necessary after adding if x >= num_listings statement
        
#going through each apartment listing on page
df = pd.DataFrame(columns = ['Title','Address','Rent','Security Deposit','Square Footage', 'Availability'])
for button in apt_buttons:
    
    print('Progess: {}'.format('' + str(x) + '/' + str(num_listings)))
    if x >= num_listings:
        break
            
    apt_buttons[x].click()
    time.sleep(5)
    
    #getting elements for entire property
    title = driver.find_element_by_class_name('propertyName').text
    address = driver.find_element_by_class_name('propertyAddress').text
    
    #unique_features not working
    #unique_features = driver.find_element_by_class_name('specList js-spec shuffle-item filtered').text
    
    #getting elements from each row
    
    #beds and baths are returning empty strings for some reason, tried searching by class name and by xpath
    #beds = driver.find_elements_by_xpath("//td[@class='beds']/span[1]")    
    #baths = driver.find_elements_by_xpath("//td[@class='baths']/span[1]")
        
    rent = driver.find_elements_by_class_name('rent')
    deposit = driver.find_elements_by_class_name('deposit')     #this is also returning empty strings
    sqft = driver.find_elements_by_class_name('sqft')
    available = driver.find_elements_by_class_name('available')
    
    #repeating title and address for each listing 
    title_list = [title] * len(rent)
    address_list = [address] * len(rent)
    
    #keeping only the text portion of each element
    i = 0
    while i < len(rent):
        #beds[i] = beds[i].text
        #baths[i] = baths[i].text
        rent[i] = rent[i].text
        deposit[i] = deposit[i].text
        sqft[i] = sqft[i].text
        available[i] = available[i].text
        i = i+1
    
    #creating dictionary of data from each row
    listings_dict = ({'Title' : title_list,
                      'Address' : address_list,
                      #'Bedrooms' : beds,
                      #'Bathrooms' : baths,
                      'Rent' : rent,
                      'Security Deposit': deposit,
                      'Square Footage': sqft,
                      'Availability': available})
    
    #converting dictionary to dataframe
    listing_df = pd.DataFrame(listings_dict)
    
    #adding data from this listing to larger dataframe with data for all listings
    df = pd.concat([df, listing_df], axis = 0, sort = False)
    
    #work around for the fact that there seem to be elements with class = "rent" with no values
    #hopefully this can be eliminated by using a different find_elements_by function
    df = df.loc[df['Rent'] != '']  
    
    
    driver.back()   #to go back to original page
    apt_buttons = driver.find_elements_by_class_name('placardHeader')  #for some reason it seems this needs to be run again after going back
    x = x+1 #to move on to next apartment listing


