import urllib.request 
from bs4 import BeautifulSoup as bs 
import pandas as pd



def Remove(urls): 
    all_urls = []
    for url in urls:
        if url not in all_urls:
            all_urls.append(url)
    return all_urls
urls_list = ['http://skyserver.sdss.org/dr15/en/tools/explore/summary.aspx?plate=574&mjd=52347&fiber=203','http://skyserver.sdss.org/dr15/en/tools/explore/summary.aspx?plate=1168&mjd=52731&fiber=10','http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237648720142336237', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237648720679338252', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237648722827346065', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655369293234205', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655463773863971', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237663916812468282', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655129299222696', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655129299222708', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651250439520527', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651250439520292', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651250439717040', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237663531875827772', 'http://skyserver.sdss.org/dr15/en/tools/explore/summary.aspx?plate=266&mjd=51630&fiber=1', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237661850944602135', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237666338116206711', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237666338116206712', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287803486', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287803794', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287738018', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287738198', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651225172705461', 'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651225172705483']
nonduplicate = Remove(urls_list)

def scrp_mag(x):
    magnitudes = []
    names = []
    flux_density = []
    H_alpha = []
    H_beta = []
    H_delta = []
    H_gamma = []
    for url in x:
        soup = bs(urllib.request.urlopen(url).read())
        if soup.findAll('div', attrs={'class':'warning'}):  
            for link in soup('tr')[79].findAll('td')[2]:
                mag = link.string
                mag_r = float(mag)
                magnitudes.append(mag_r)
        else:
            for link in soup('tr')[78].findAll('td')[2]:
                mag = link.string
                mag_r = float(mag)
                magnitudes.append(mag_r)
        for major in soup.findAll('h1', attrs={'id':'sdssname'}):
            name_1 = major.string 
            names.append(name_1)
    name_sorted = [name for _, name in sorted(zip(magnitudes, names))] 
    magnitudes.sort()    
    for magnitude in magnitudes: 
        added_mag = float (magnitude + 27.04)
        mult_mag = float(added_mag * -0.4)
        flux = float(10**mult_mag)
        flux_density.append(flux)
    return flux_density, magnitudes, name_sorted

df = pd.DataFrame({"Galaxy's Name":scrp_mag(nonduplicate)[2],'r Magnitude':scrp_mag(nonduplicate)[1],'Flux':scrp_mag(nonduplicate)[0]}) 
df.to_csv('test1.csv', index=False, encoding='utf-8')
