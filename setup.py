import requests
import re
import json
import creds

url = "http://www.stych.fr/elearning/planning-conduite/get-planning-proposition"

cookies = {"remember_me" : creds.remember_me}
resp = requests.get(url, cookies=cookies)

creneaux = re.search('"rowsProposition":(\[.+\]),"rowsMoniteur"', resp.text)
creneaux = json.loads(creneaux.group(1))
creneaux = [[d['info_date'], d['heure_debut'], d['heure_fin'], d['moniteur']] for d in creneaux]
with open("creneaux.txt", "w", encoding='utf-8') as f:
    f.write(json.dumps(creneaux, ensure_ascii=False))