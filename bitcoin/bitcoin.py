import sys
import requests

def main():

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        temp = response.json()
    except requests.RequestException:
        sys.exit("error to get request")

    if len(sys.argv) < 2:
        sys.exit("Пропущен аргумент командной строки")
    try:
        float(sys.argv[1])
        currentPrice = temp['bpi']['USD']['rate_float']
        result = "{:,}".format((float(sys.argv[1])*float(currentPrice)))
        print(f'${result}')
    except ValueError:
        print("Аргумент командной строки не число")

if __name__ == "__main__":
    main()
