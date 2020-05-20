import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=278'
contents = requests.get(url)

# jika menampilkan output 200 maka OK
print(contents)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]

# membuat variabel dictionary
sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['zuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()

    i += 1
print(sholat['subuh'])