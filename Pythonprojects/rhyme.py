import requests
user=input("enter the word: ")
parameter = {}
parameter['rel_rhy'] =user
res = requests.get('https://api.datamuse.com/words',parameter)
rymr = res.json()
for i in rymr[:5]:
    print(i['word'])

