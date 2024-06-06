import csv
from datetime import datetime

"""
result = [
    {
        'title': title,
        'link': link,
        'engine': engine
    },
    ...
]
"""


def result_to_csv(result):
    now = datetime.now()
    filename = now.strftime('%Y-%m-%dT%H:%M:%S') + '.csv'

    data = []
    for r in result:
        row = [r['title'], r['link'], r['engine']]
        data.append(row)
    
    f = open(f'./datas/{filename}', mode='w')
    f.write('')
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)
    f.close()
