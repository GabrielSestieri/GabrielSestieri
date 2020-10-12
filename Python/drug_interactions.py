import pandas as pd 
import requests
import time

def get_drugid(drug):
    url = "https://rxnav.nlm.nih.gov/REST/rxcui.json"
    params = {"name": drug}
    response = requests.get(url, params = params)
    response.raise_for_status()
    data = response.json()
    try: 
        return data['idGroup']['rxnormId']
    except:
        raise ValueError('There is no rxID')
    
def get_interactions(rxID):
    url = "https://rxnav.nlm.nih.gov/REST/interaction/interaction.json"
    params = {'rxcui': rxID}
    response = requests.get(url, params = params)
    response.raise_for_status()
    data = response.json()
    lst = []
    try: 
        pairs = (data['interactionTypeGroup'][0]['interactionType'][0]['interactionPair'])
        for i in pairs:
            d = {}
            d['drug1'] = i['interactionConcept'][0]['minConceptItem']['name']
            d['drug2'] = i['interactionConcept'][1]['minConceptItem']['name']
            d['description'] = i['description']
            lst.append(d)
    except:
        raise ValueError('404')
    
    return pd.DataFrame(lst)
    
def main(drug, path):
    a = get_drugid(drug)
    time.sleep (1/10)
    dataframe = get_interactions(a)
    dataframe.to_csv(path)
    
if __name__ == '__main__':
    main('Testosterone', 'file.txt')