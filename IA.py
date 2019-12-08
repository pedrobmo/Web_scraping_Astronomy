import urllib.request 
from bs4 import BeautifulSoup as bs 
import pandas as pd
import statistics
import math 


#Remove repeated urls in SDSS urls 
def Remove_sdss(urls): 
    all_urls_sdss = []
    for url in urls:
        if url not in all_urls_sdss:
            all_urls_sdss.append(url)
    return all_urls_sdss
urls_list_sdss = ['http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237648721753210967',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655463773929482',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237663915738464267',
'http://skyserver.sdss.org/dr15/en/tools/explore/summary.aspx?plate=574&mjd=52347&fiber=203',
'http://skyserver.sdss.org/dr15/en/tools/explore/summary.aspx?plate=1168&mjd=52731&fiber=10',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237648720142336237',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237648720679338252',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237648722827346065',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655369293234205',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655463773863971',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237655129299222696', 
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651250439520527',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651250439520292',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651250439717040', 
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237663531875827772',
'http://skyserver.sdss.org/dr15/en/tools/explore/summary.aspx?plate=266&mjd=51630&fiber=1',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237661850944602135', 
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237666338116206711',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237666338116206712',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287803486',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287803794',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287738018',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651212287738198',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651225172705461',
'http://skyserver.sdss.org/dr15/en/tools/explore/Summary.aspx?id=1237651225172705483']
nonduplicate_sdss = Remove_sdss(urls_list_sdss)

#Removes the repeated urls that are encountered in Simbad urls
def Remove_simbad(urls):
    all_urls_simbad = []
    for url in urls:
        if url not in all_urls_simbad:
            all_urls_simbad.append(url)
    return all_urls_simbad
urls_list_simbad = ['http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=SDSS%20J094846.29%2B001618.9&submit=SIMBAD%20search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=LEDA+214189+++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=MCG%2B11-12-032++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+3165++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=+2MASX%20J15530802%2B4538230+++&submit=SIMBAD%20search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=2MFGC+7571&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=2MASS+J09473199-0029408+++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=MCG%2B00-25-025++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+5379++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+5376++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=MCG%2B08-29-044++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=2MASX%20J16035172%2B4922302&submit=SIMBAD%20search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=UGC+10168++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=LEDA+2334204&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+2805++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=2MASX+J09465141-0102290+++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+5752++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=+UGC+807++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+450++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+6345++++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=MCG%2B10-24-112+++&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+6338&submit=SIMBAD+search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=2MASX%20J17153166%2B5730085&submit=SIMBAD%20search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=2MASX%20J17140081%2B5722267&submit=SIMBAD%20search',
'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=LEDA+2563411++++&submit=SIMBAD+search']

nonduplicate_simbad = Remove_simbad(urls_list_simbad)

angular_diameters =[]
magnitudes = []
names = []
flux_density = []
erro_r_given = []
z_error_given = []
distances = []
diameters = []
luminosities = []
common_names = []
velocities = []

numbers_1 = [0, 4, 6, 10, 15, 16, 19, 20, 23, 24]
numbers_2 = [1,2,3,5,7,8,9,11,12,17,18,21,22]
#Calls the value of the angular diameter from the simbad website 
def simbad(web):
    for url in web:
        soup = bs(urllib.request.urlopen(url).read())
        for i in numbers_1:
            if web.index(url)== i:
                for d in soup('td')[28].findAll('tt')[0]:
                    d_new = d.string
                    d_str = str(d_new)
                    ang_diameter = float(d_str[1:6])
                    angular_diameters.append(ang_diameter)
        if web.index(url)== 13:
            for d in soup('td')[26].findAll('tt')[0]:
                d_new = d.string
                d_str = str(d_new)
                ang_diameter = float(d_str[1:6])
                angular_diameters.append(ang_diameter)
        elif web.index(url)== 14:
            for d in soup('td')[32].findAll('tt')[0]:
                d_new = d.string
                d_str = str(d_new)
                ang_diameter = float(d_str[1:6])
                angular_diameters.append(ang_diameter)
        for i in numbers_2:
            if web.index(url)== i:
                for d in soup('td')[30].findAll('tt')[0]:
                    d_new = d.string
                    d_str = str(d_new)
                    ang_diameter = float(d_str[1:6])
                    angular_diameters.append(ang_diameter)
        for name in soup.findAll('title', attrs={'itemprop': 'name'}):
            name_gal = name.string 
            common_names.append(name_gal)
    return angular_diameters, common_names

call_simbad = simbad(nonduplicate_simbad)

result_ang_diam = call_simbad[0]
result_common_names = call_simbad[1]

#Main runner and returns the arranged magnitudes as well as names, flux, angular diameters, errors, distances, and luminosity 
def main(x):
    for url in x:
        soup = bs(urllib.request.urlopen(url).read())

        #uses the url to find the magnitudes from SDSS url 
        if soup.findAll('div', attrs={'class':'warning'}): 
            for link in soup('tr')[79].findAll('td')[2]:
                mag = link.string
                mag_r = float(mag)
                magnitudes.append(mag_r)
            for link in soup('tr')[83].findAll('td')[2]:
                link_err = float(link)
                erro_r_given.append(link_err)
        else:
            for link in soup('tr')[78].findAll('td')[2]:
                mag = link.string
                mag_r = float(mag)
                magnitudes.append(mag_r)

            #finds the error given to each magnitude by the SDSS website
            for link in soup('tr')[82].findAll('td')[2]:
                link_err = float(link)
                erro_r_given.append(link_err)
            for link in soup('td', attrs={'valign':'top', 'class':'t'})[4]:
                z_err = float(link)
                z_error_given.append(z_err)
                
        #finds the name of the galaxy that is given by SDSS 
        for major in soup.findAll('h1', attrs={'id':'sdssname'}):
            name_1 = major.string 
            names.append(name_1)

    #sorts all the values so far 
     

    #calculates the flux that will be used to find the luminsity    
    for magnitude in magnitudes: 
        added_mag = float(magnitude + 27.04)
        mult_mag = float(added_mag * -0.4)
        flux = float(10**mult_mag)
        flux_density.append(flux)
    
    #the bands of the balmer series to each of the galaxies 

    alpha = [6697.307, 6711.199, 6663.462, 6593.255, 7130.173, 6991.977, 7113.771, 6697.305, 6603.891, 6608.457, 6723.571, 6700.390, 6695.761, 6956.649, 6602.372, 6703.474, 6663.462, 6815.534, 6602.372, 6790.471, 6767.059, 6743.729, 6757.715, 6768.616, 6746.832]
    beta = [4960.208, 4971.644, 4936.281, 4884.275, 5282.020, 5179.644, 5271.085, 4961.352, 4891.026, 4896.660, 4979.664, 4962.493, 4960.208, 5153.473, 4891.026, 4965.924, 4936.281, 5048.939, 4891.026, 5030.372, 5013.026, 4995.743, 5006.106, 5014.182, 4998.044]
    gamma = [4428.943, 4438.131, 4406.563, 4360.135, 4715.199, 4624.876, 4705.438, 4428.943, 4367.168, 4371.193, 4446.313, 4430.983, 4428.943, 4601.506, 4367.168, 4434.044, 4407.579, 4508.168, 4367.168, 4490.554, 4476.101, 4459.643, 4468.892, 4477.133, 4462.724]
    delta = [4185.044, 4194.691, 4164.957, 4120.975, 4456.562, 4370.187, 4446.313, 4186.007, 4126.673, 4131.427, 4202.426, 4186.972, 4185.044, 4348.104, 4126.673, 4189.865, 4164.857, 4259.906, 4126.673, 4244.241, 4229.608, 4215.023, 4223.767, 4230.581, 4216.965]
    balmer_alpha = 6562.8
    balmer_beta = 4861.3
    balmer_gamma = 4340.5
    balmer_delta = 4101.7
    z_alpha =[]
    z_beta =[]
    z_gamma =[]
    z_delta =[]
    # GIFLENS-https://media1.giphy.com/media/llVv0wZh0PTLW/200.gif
    #sorts the bands according to the magnitudes (change since the sort should be through the diameter (indpenedent variable))

    #find the z values for ecah of the bands 
    for h in alpha: 
        ratio_alpha = h/balmer_alpha
        z_a_value = float(ratio_alpha - 1)
        z_alpha.append(z_a_value)
    for h in beta: 
        ratio_beta = h/balmer_beta
        z_b_value = float(ratio_beta - 1)
        z_beta.append(z_b_value)
    for h in gamma: 
        ratio_gamma = h/balmer_gamma
        z_g_value = float(ratio_gamma - 1)
        z_gamma.append(z_g_value)
    for h in delta: 
        ratio_delta = h/balmer_delta
        z_d_value = float(ratio_delta - 1)
        z_delta.append(z_d_value)

    #averages the bands and finds its uncertainty 
    
    average_red = []
    st_dev_z =[]
    i = 0
    while i<=24:
        added_zs = z_alpha[i] + z_beta[i] + z_gamma[i] + z_delta[i]
        average_z = float(added_zs/4)
        average_red.append(average_z)
        standard = [z_alpha[i], z_beta[i], z_gamma[i], z_delta[i]]
        final_calc_dev = statistics.stdev(standard)
        st_dev_z.append(final_calc_dev)
        i+=1

    #calculating the distance to galaxy
    for z in average_red: 
        velocity_gal = z*299792
        velocities.append(velocity_gal)
        distance_gal = velocity_gal/73.8
        distances.append(distance_gal)

    #calculating the diameter of galaxy in kpc 
    for each in result_ang_diam:
        each = float(each)
        two_pi_multiplied = float(2*math.pi*each)
        ratio = 6*3600
        angle = float(two_pi_multiplied/ratio)
        angle_tan = math.tan(angle)
        i = result_ang_diam.index(each)
        distance = distances[i]
        Mpc_diameter = distance*angle_tan 
        kpc_diameter = Mpc_diameter*1000
        diameters.append(kpc_diameter)
    
    def propagated_error_addition(a_error, b_error):
        propagated_error = []
        for i in range(25):
            propagated = float(a_error[i] + b_error[i])
            propagated_error.append(propagated)
        return propagated

    def propagated_error_multidiv(a_error, b_error, y, a, b):
        propagated_error = []
        for i in range(25):
            a_ratio = a_error[i]/a[i]
            if b_error == 0: 
                b_ratio = 0
            else:
                b_ratio = b_error[i]/b[i]
            added = a_ratio + b_ratio
            y_error = y[i]*added
            propagated_error.append(y_error)
        return propagated_error
    
    def propagated_base10(a_error, y):
        propagated_error = []
        for i in range(25): 
            y_error = y[i]*2.303*a_error
            propagated_error.append(y_error)
        return propagated_error
        

        
    #sorting all the values according to the increasing values of the diameters 
    alpha_sorted = [value for _, value in sorted(zip(diameters, alpha))]
    beta_sorted = [value for _, value in sorted(zip(diameters, beta))]
    gamma_sorted = [value for _, value in sorted(zip(diameters, gamma))]
    delta_sorted = [value for _, value in sorted(zip(diameters, delta))]
    name_sorted = [name for _, name in sorted(zip(diameters, names))] 
    angdiameter_sorted = [angular_diameter for _, angular_diameter in sorted(zip(diameters, result_ang_diam ))]
    mag_sorted = [rmag for _, rmag in sorted(zip(diameters, magnitudes))] 
    z_sorted = [z for _, z in sorted(zip(diameters, average_red))]
    st_dev_sorted = [dev for _, dev in sorted(zip(diameters, st_dev_z))]
    velocity_sorted = [v for _, v in sorted(zip(diameters, velocities))]
    distances_sorted = [d for _, d in sorted(zip(diameters, distances))]
    flux_sorted = [ flux for _, flux in sorted(zip(diameters, flux_density))]
    common_name_sorted = [ noun for _, noun in sorted(zip(diameters, result_common_names))]
    diameters.sort()


    
    #calculating the luminosities (note that there is no need to sort this since all the lists used are already sorted)
    # GIFLENS-https://media1.giphy.com/media/FY9chKp6rulXy/200.gif
    for dis in distances_sorted:
        ratio_distances = dis/4.848355486e-12
        squared_distances = ratio_distances**2
        luminosity = flux_sorted[distances_sorted.index(dis)]*squared_distances
        luminosities.append(luminosity)
    
    v_error = propagated_error_multidiv(st_dev_sorted, 0, velocity_sorted, z_sorted, 1)
    
    distance_error = propagated_error_multidiv(v_error, 0, distances_sorted, velocity_sorted, 1)

    flux_error = propagated_base10(0.01, flux_sorted)

    lum_error = propagated_error_multidiv(2*distance_error, flux_error, luminosities, distances_sorted, flux_sorted)

    diam_error = []
    
    for i in range(25):
        first_theta = float(2*math.pi*angdiameter_sorted[i])
        second_theta = int(6*3600)
        theta = first_theta/second_theta
        multi_1 = math.tan(theta)*distance_error[i]
        squared_mult_1 = float(multi_1**2)
        cos = math.cos(theta)
        sec = float(1/cos)
        sec_squared = sec**2
        neg_dis = float(0-distances_sorted[i])
        first_theta_unc = float(2*math.pi*0.001)
        second_theta_unc = int(6*3600)
        theta_unc = first_theta_unc/second_theta_unc
        multi_2 = sec_squared*neg_dis*theta_unc
        squared_multi_2 = multi_2**2
        added_multi = squared_mult_1 + squared_multi_2
        final = math.sqrt(added_multi)
        diam_error.append(final)


    return common_name_sorted,alpha_sorted, beta_sorted, gamma_sorted, delta_sorted, z_sorted, st_dev_sorted, velocity_sorted, v_error, distances_sorted, distance_error, mag_sorted, flux_sorted, flux_error, luminosities, lum_error, angdiameter_sorted, diameters, diam_error

#creates the Excel (csv) file that can be used to be exported to Google Sheets and then beautified. 

call_main = main(nonduplicate_sdss)

df = pd.DataFrame({"Galaxy's Name":call_main[0],'alpha':call_main[1],'beta':call_main[2], 'gamma':call_main[3], 'delta':call_main[4], 'Redshift': call_main[5], 'Z error': call_main[6], 'Velocity': call_main[7], 'Velocity Error': call_main[8], 'Distance': call_main[9], 'Distance Error': call_main[10], 'R magnitude': call_main[11], 'Flux Ratio': call_main[12], 'Flux Error': call_main[13], 'Luminosity': call_main[14], 'Luminosity Error': call_main[15], 'Angular Diameter': call_main[16], 'Diameter': call_main[17], 'Diameter Error': call_main[18]}) 
df.to_csv('IA2.csv', index=False, encoding='utf-8')
