import requests
import json

base_url = "https://endpointsq.fxcorporate.com/symbol/data?platform=pwa_new"
languages = ["ara","chs","cht","deu","enu","esp","fra","gre","heb","ita"]
cat_url = base_url +"&type=cat"
alt_url = base_url +"&type=alt"

def pull(url, lang):
    r = requests.get(url + "&lc=" + lang)
    json_data = r.json()
    with open(f"{lang} {url[-3:]}.json","w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

for i in languages:
    pull(cat_url, i)
    pull(alt_url, i)
    




