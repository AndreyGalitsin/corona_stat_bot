from bs4 import BeautifulSoup
import requests
import sys

def get_statistics(params):
    country = params.get("region")
    worldmetersLink = "https://www.worldometers.info/coronavirus/"

    def data_cleanup(array):
        L = []
        for i in array:
            i = i.replace("+","")
            i = i.replace("-","")
            i = i.replace(",",".")
            
            if i == "":
                i = "0"
            L.append(i.strip())
        return L

    try:
        html_page = requests.get(worldmetersLink)
    except requests.exceptions.RequestException as e: 
        print (e)
    bs = BeautifulSoup(html_page.content, 'html.parser')
    
    search = bs.select("div tbody tr td")
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) != -1:
            start = i
            break
    data = []
    for i in range(1,8):
        try:
            data = data + [search[start+i].get_text()]
        except:
            data = data + ["0"]
    
    data = data_cleanup(data)
    res = "\nВсего заболевших = {}\nНовые случаи за сутки = {}\nВсего умерших = {}\nНовые смерти за сутки = {}\nВылечились = {}\nБолеют на данный момент = {}\nВ критическом состоянии = {}".format(*data)
    return ({'result' : str(res)})