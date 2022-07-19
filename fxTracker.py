import os
import requests
import pandas as pd

currencies = ["AUD", "CAD", "CHF", "DKK", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "MXN", "SEK", "SGD", "THB", "USD", "VND"]

#enter your API key here
apiKey = ""

url = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers = {
    "apikey" : apiKey
}

# Possible improvement: only loop through half the currencies as the rate the other way round would just be an inverse of the previously obtained exchange rate
def get_exchange_rates():
    all_rates = []
    for curr_from in currencies:
        target_currencies = ""
        for curr_to in currencies:
            #pass when its the same currency as the rate would be 1
            if curr_from == curr_to:
                pass
            else:
                if target_currencies == "":
                    target_currencies += curr_to
                else:
                    target_currencies = target_currencies + "%2C" + curr_to

        # prepare url for a SINGLE API call for exchange rates of ONE currency against all other
        url_call = url.format(base = curr_from, symbols = target_currencies)
        response = requests.request("GET", url_call, headers=headers, data=payload)
        status_code = response.status_code
        # when code not 200, handle error
        if status_code != 200:
            print("")
            print("Failed to query exchange rates. Please try again.")
            break
        else:
            conversion_date = response.json()['date']
            conversion_rates = response.json()['rates']
            for curr in conversion_rates:
                all_rates.append([curr_from, curr, str(conversion_rates[curr])])
                #print(curr_from + "/" + curr + ": " + str(conversion_rates[curr]))

    ret = {'date':conversion_date, 'rates':all_rates}
    return ret

def display_menu():
    print("")
    print("Please enter an option")
    print("[1] List currencies")
    print("[2] Get all exchange rates")
    print("[3] Save all exchange rates to a CSV file")
    print("[4] Get exchange rates for a specific currency")
    print("[0] Exit program")

display_menu()
option = int(input("Enter option: ")) # TODO: input validation

while option != 0:
    if option == 1:
        # list all(local) currencies
        for currency in currencies:
            print(currency)
        
    elif option == 2:
        #get all exchange rates
        print("")
        print("Fetching all exchange rates. This may take a moment...")
        ret = get_exchange_rates()

        exchange_date = ret['date']
        all_rates = ret['rates']

        for rate in all_rates:
            print(rate[0] + "/" + rate[1] + ": " + rate[2])

    elif option == 3:
        #save exchange rates to a CSV file
        print("")
        print("writing exchange rates to file. This may take a moment...")
        ret = get_exchange_rates()
        exchange_date = ret['date']
        all_rates = ret['rates']

        filename = "exchange_rates.csv"
        dirname = "./" + str(exchange_date)
        #create folder with the date if not exist
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        fullpath = os.path.join(dirname, filename)
        df = pd.DataFrame(all_rates)
        df.to_csv(fullpath, index=False, header=['currency_from','currency_to','exchange_rate'])
        print("file created successfully")
            
    elif option == 4:
        #future development
        #todo: get input for currency and exchange rate
        pass
    else:
        print("Invalid option")

    
    display_menu()
    option = int(input("Enter option: "))
        
print("Closing program....")




