import requests, os, bs4
# Download the notes for 18.03 by Authur Mattuck from MIT

path = 'notes'  # path to store the file
url = 'https://math.mit.edu/~jorloff/suppnotes/suppnotes03/index.html'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
tabel_elem = soup.select('table')

for i in range(len(tabel_elem)):
    t = tabel_elem[i]
    a = t.select('a')
    n = 1
    for doc in a:
        file_name = doc.text
        file_name = '_'.join(file_name.split(':'))
        dest = doc.get('href')
        doc_url = os.path.dirname(url) + '/' + dest
        print(f'Donwloading the {n} file, {file_name}')
        doc_res = requests.get(doc_url)
        doc_res.raise_for_status()
        if i == 1:
            file_path = os.path.join(path, 'E'+ str(n) + '_'+ file_name+ '.pdf')
        else:
            file_path = os.path.join(path, str(n) + '_'+ file_name+ '.pdf')
        print(file_path)
        docFile = open(file_path, 'wb')
        for chunk in doc_res.iter_content(100000):
            docFile.write(chunk)
        docFile.close()
        n += 1

print('Done')
        