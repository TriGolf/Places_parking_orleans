import urllib.request
import json

with urllib.request.urlopen('https://data.orleans-metropole.fr/api/explore/v2.1/catalog/datasets/om-mobilite-parcs-stationnement/records?select=nb_places_disponibles%2Cnb_places%2Cnom&limit=100&refine=type_parking%3A%22Parking%22&refine=insee%3A45234') as r :
    data = json.load(r)

nb_results = data['total_count']
results = data['results']

nb_places = 0
nb_places_libres = 0

for x in range(nb_results):
    result = results[x]
    nb_places = result['nb_places']
    nb_places_libres = result['nb_places_disponibles']
    nom = result['nom']
    pourcentage = (nb_places_libres/nb_places)*100
    print(f'{nom} : \n     Places libres : {nb_places_libres} \n     Places totales : {nb_places} \n     Pourcentage de places libres : {round(pourcentage,2)}%\n')
