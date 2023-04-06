import sys
import requests




#Promt user for n number of Bitcoin for them to buy
#while True:
if len(sys.argv) == 2:
    try:
        number = float(sys.argv[1])
        #Tilstreb å formatere verdien så tidleg som mogleg.
        print(number)
    except:
        print("wrong input")
else:
    print("missing input")
    sys.exit()

#Get JSON object form coindesk api og gjere om prisen til en float
#Benytt exceptions requests.RequestException
if type(number) == float:
    try:
        api_BC = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #Ikkje noko brukbart før json innholdet er hentet ut.
        response = api_BC.json()
    except requests.RequestException:
        print("RequestException")
        sys.exit(1)

#Output cost of n bitcoins i USD til 4 desimalar
output = number * response['bpi']['USD']['rate_float']
round(output, 4)
print(f"Please pay {output}$ for your {number} bitcoin.")