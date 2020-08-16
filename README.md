# Estimating Bay Area Rent Prices - Project Overview  
<ul>
  <li>Used selenium to scrape data from over 12,000 apartment listings on apartments.com in the San Jose, Oakland and San Francisco areas  
  <li>Cleaned data from apartments.com and engineered features from raw text describing apartment amenities by applying NLP techniques to gain insight on what amenities might be useful to include in the final model  
  <li>Created an ML model that estimates rent prices (RMSE ~$365 on test set) given a number of inputs including # of bedrooms, # of bathrooms, square footage and amenities   
  <li>Collaborated with a friend to productionize this ML model and use it to create a web app. Web app can be accessed here: http://3.128.33.149/    
</ul>  

## Packages Used and Sources Referenced  
**Python Version:** 3.7  
**Packages:**   
* **Web Scraping:** selenium, pandas, re
* **Data Cleaning/Feature Engineering:** pandas, numpy, re, matplotlib, seaborn, sklearn, nltk
* **EDA/Model Building:** pandas, numpy, matplotlib, seaborn, scipy, sklearn, xgboost    
* **To Load Requirements to Run Pickled ML Model:** `pip install -r requirements.txt`

**Sources Referenced:**
* [Tutorial](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905) on scraping Glassdoor using selenium  
* Selenium unofficical [documentation](https://selenium-python.readthedocs.io/)  
* [Guide](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2) on productionizing an ML model (used for reference on how to pickle and load an ML model)  





