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
        added_mag = float(magnitude + 27.04)
        mult_mag = float(added_mag * -0.4)
        flux = float(10**mult_mag)
        flux_density.append(flux)
    alpha = [6593.255, 7130.173, 6991.977, 7113.771, 6697.305]
    beta = [4884.275, 5282.02, 5179.644, 5269.872, 4961.352]
    gamma = [4360.135, 4716.284, 4624.876, 4705.438, 4428.943]
    delta = [4120.975, 4456.562, 4370.187, 4446.313, 4186.007]
    balmer_alpha = 6562.8
    balmer_beta = 4861.3
    balmer_gamma = 4340.5
    balmer_delta = 4101.7
    z_alpha =[]
    z_beta =[]
    z_gamma =[]
    z_delta =[]
    alpha_sorted = [value for _, value in sorted(zip(magnitudes, alpha))]
    beta_sorted = [value for _, value in sorted(zip(magnitudes, beta))]
    gamma_sorted = [value for _, value in sorted(zip(magnitudes, gamma))]
    delta_sorted = [value for _, value in sorted(zip(magnitudes, delta))]
    for h in alpha_sorted: 
        ratio_alpha = h/balmer_alpha
        z_a_value = float(ratio_alpha - 1)
        z_alpha.append(z_a_value)
    for h in beta_sorted: 
        ratio_beta = h/balmer_beta
        z_b_value = float(ratio_beta - 1)
        z_beta.append(z_b_value)
    for h in gamma_sorted: 
        ratio_gamma = h/balmer_gamma
        z_g_value = float(ratio_gamma - 1)
        z_gamma.append(z_g_value)
    for h in delta_sorted: 
        ratio_delta = h/balmer_delta
        z_d_value = float(ratio_delta - 1)
        z_delta.append(z_d_value)
    def Average(vix):
        average_red = []
        i = 0
        while i<=25:
            added_zs = z_alpha[i] + z_beta[i] + z_gamma[i] + z_delta[i]
            average_z = float(added_zs/4)
            average_red.append(average_z)
            i+=1
        return average_red
    return flux_density, magnitudes, name_sorted, z_alpha, z_beta, z_gamma, z_delta, alpha, beta, gamma, delta, Average(z_alpha)

df = pd.DataFrame({"Galaxy's Name":scrp_mag(nonduplicate)[2],'r Magnitude':scrp_mag(nonduplicate)[1],'Flux':scrp_mag(nonduplicate)[0]}) 
df.to_csv('test1.csv', index=False, encoding='utf-8')
