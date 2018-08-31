#get required packages/files
import os
import requests
import json
import random
from datetime import datetime
if os.path.exists(os.path.join(os.getcwd(), "config.py")): #if the config with the secret key is around, import it
    import config
else: #otherwise import the placeholder
    import config.env

#function to grab a recent quote from the API and send it to infosys
def sendQuote():
    #create the url to grab quotes from the last seven days
    key = config.quotefaultAPIKey;
    now = datetime.date().today();
    dateLimit = datetime.date().today() - 7;
    url = 'quotefault-api.csh.rit.edu/' + key + '/between/' + dateLimit + '/' + now;
    #ping the API for a JSON object of quotes from the last 7 days
    response = requests.get(url);
    #interpret the JSON
    quoteList = json.loads(response.text);
    #determine number of quotes returned
    numQuotes = len(quoteList);
    #if there are any quotes, continue with the operation
    if(numQuotes > 0):
        #pick a random number in the range of quotes returned
        rng = random.randrange(numQuotes - 1);
        #HERE'S WHERE THE CODE FOR SENDING A CHOSEN QUOTE TO INFOSYS WILL BE.  WHAT WILL IT LOOK LIKE? NOBODY KNOWS!
        return;
    else: #no quotes returned by the API, end the operation
        return;