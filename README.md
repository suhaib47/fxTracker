# fxTracker

fxTracker is a Python program that fetches currency exchange rates with the option of writing it to a csv file.

The list of currencies used:
AUD, CAD, CHF, DKK, EUR, GBP, HKD, IDR, INR, JPY, MXN, SEK, SGD, THB, USD, VND

## Installation
This program uses the Exchange Rates API to get exchange rates. You can create a free account [here](https://exchangeratesapi.io/). You will obtain an API key, enter that key in the quotes below:

```python
apiKey = ""
```

Ensure you have [Python](https://www.python.org/downloads/) installed, at least version 3.9.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages. (Note: pip3 for python 3)

```bash
pip3 install requests
pip3 install pandas
```

## Usage
Run the program by:
```python 
python fxTracker.py
```

Follow the instructions and simply enter your option.

**Option 1 to List currencies**  
This option will list out the currencies available and used in the program  

**Option 2 to Get all exchange rates**  
This option will get the exchange rates of all combinations of the currencies and print them out to the console.

**Option 3 to Save all exchange rates to a CSV file**  
This option will get the exchange rates of all combinations of the currencies and save them to a csv file named "exchange_rates.csv". The file will be saved in a folder named with the date of the exchange rates. The folder will be created if it does not exist.

**Option 4 to Get exchange rates for a specific currency**  
This feature is not available yet and has been left for future development

**Option 0 to Exit program**
