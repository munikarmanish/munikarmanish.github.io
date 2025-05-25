import json
import os
from datetime import datetime

import jsonpickle
from scholarly import ProxyGenerator, scholarly

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

print(f"Fetching author info with ID={SCHOLAR_ID}")
author = scholarly.search_author_id(SCHOLAR_ID)
print("Author found!")

print("Filling extra info about the author...")
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
#print(json.dumps(author, indent=2))

print("Writing gs_data.json...")
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

print("Writing gs_data_shieldsio.json...")
shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print("Done!")
