from django.shortcuts import render, HttpResponse
import requests
import json
from covid import Covid



# Create your views here.

def index(request):
    covid = Covid()

    #data = covid.get_data()

    india_cases = covid.get_status_by_country_name("India")

    #print(india_cases)

    india_confirmed = india_cases['confirmed']

    #print("Confirmed", india_confirmed)

    india_active = india_cases['active']

    #print("Active", india_active)

    india_deaths = india_cases['deaths']

    #print("Deaths", india_deaths)

    india_recovered = india_cases['recovered']

    #print("Recovered", india_recovered)

    confirmed = covid.get_total_confirmed_cases()

    recovered = covid.get_total_recovered()

    deaths = covid.get_total_deaths()

    active = covid.get_total_active_cases()

    #print(india_cases)


    context = {
        #'data': data,
        'india_confirmed': india_confirmed,
        'india_active': india_active,
        'india_deaths': india_deaths,
        'india_recovered': india_recovered,
        'confirmed': confirmed,
        'deaths': deaths,
        'active': active,
        'recovered': recovered,
    }

    return render(request, 'stats/index.html', context)


def maharashtra(request):

    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    data = response.json()

    zone_response = requests.get("https://api.covid19india.org/zones.json")
    zone_data = zone_response.json()

    #mum_zone = zone_data['zones'][316]['zone']


    #print(data)
    mum = data["Maharashtra"]['districtData']['Mumbai']
    mum_active = mum['active']
    mum_confirmed = mum['confirmed']
    mum_deceased = mum['deceased']
    mum_recovered = mum['recovered']
    mum_zone = zone_data['zones'][332]['zone']

    #Mumbai end

    ah = data["Maharashtra"]['districtData']['Ahmednagar']
    ah_active = ah['active']
    ah_confirmed = ah['confirmed']
    ah_deceased = ah['deceased']
    ah_recovered = ah['recovered']
    ah_zone = zone_data['zones'][316]['zone']
    #Ahmednagar end

    ak = data["Maharashtra"]['districtData']['Akola']
    ak_active = ak['active']
    ak_confirmed = ak['confirmed']
    ak_deceased = ak['deceased']
    ak_recovered = ak['recovered']
    ak_zone = zone_data['zones'][317]['zone']
    #akola end

    am = data["Maharashtra"]['districtData']['Amravati']
    am_active = am['active']
    am_confirmed = am['confirmed']
    am_deceased = am['deceased']
    am_recovered = am['recovered']
    am_zone = zone_data['zones'][318]['zone']

    #Amravati end

    ab = data["Maharashtra"]['districtData']['Aurangabad']
    ab_active = ab['active']
    ab_confirmed = ab['confirmed']
    ab_deceased = ab['deceased']
    ab_recovered = ab['recovered']
    ab_zone = zone_data['zones'][319]['zone']
    #Aurangabad end

    bd = data["Maharashtra"]['districtData']['Beed']
    bd_active = bd['active']
    bd_confirmed = bd['confirmed']
    bd_deceased = bd['deceased']
    bd_recovered = bd['recovered']
    bd_zone = zone_data['zones'][320]['zone']
    #Beed end

    bhand = data["Maharashtra"]['districtData']['Bhandara']
    bhand_active = bhand['active']
    bhand_confirmed = bhand['confirmed']
    bhand_deceased = bhand['deceased']
    bhand_recovered = bhand['recovered']
    bhand_zone = zone_data['zones'][321]['zone']
    #Bhandara end

    bld = data["Maharashtra"]['districtData']['Buldhana']
    bld_active = bld['active']
    bld_confirmed = bld['confirmed']
    bld_deceased = bld['deceased']
    bld_recovered = bld['recovered']
    bld_zone = zone_data['zones'][322]['zone']
    #Buldhana end

    chdp = data["Maharashtra"]['districtData']['Chandrapur']
    chdp_active = chdp['active']
    chdp_confirmed = chdp['confirmed']
    chdp_deceased = chdp['deceased']
    chdp_recovered = chdp['recovered']
    chdp_zone = zone_data['zones'][323]['zone']
    #Chandrapur end

    dhl = data["Maharashtra"]['districtData']['Dhule']
    dhl_active = dhl['active']
    dhl_confirmed = dhl['confirmed']
    dhl_deceased = dhl['deceased']
    dhl_recovered = dhl['recovered']
    dhl_zone = zone_data['zones'][324]['zone']
    #dhule end

    gdch = data["Maharashtra"]['districtData']['Gadchiroli']
    gdch_active = gdch['active']
    gdch_confirmed = gdch['confirmed']
    gdch_deceased = gdch['deceased']
    gdch_recovered = gdch['recovered']
    gdch_zone = zone_data['zones'][325]['zone']
    #Gadchiroli end

    gond = data["Maharashtra"]['districtData']['Gondia']
    gond_active = gond['active']
    gond_confirmed = gond['confirmed']
    gond_deceased = gond['deceased']
    gond_recovered = gond['recovered']
    gond_zone = zone_data['zones'][326]['zone']
    #Gondia end

    hing = data["Maharashtra"]['districtData']['Hingoli']
    hing_active = hing['active']
    hing_confirmed = hing['confirmed']
    hing_deceased = hing['deceased']
    hing_recovered = hing['recovered']
    hing_zone = zone_data['zones'][327]['zone']
    #Gondia end

    jlg = data["Maharashtra"]['districtData']['Jalgaon']
    jlg_active = jlg['active']
    jlg_confirmed = jlg['confirmed']
    jlg_deceased = jlg['deceased']
    jlg_recovered = jlg['recovered']
    jlg_zone = zone_data['zones'][328]['zone']
    #Jalgaon end

    jln = data["Maharashtra"]['districtData']['Jalna']
    jln_active = jln['active']
    jln_confirmed = jln['confirmed']
    jln_deceased = jln['deceased']
    jln_recovered = jln['recovered']
    jln_zone = zone_data['zones'][329]['zone']
    #jalna end

    kol = data["Maharashtra"]['districtData']['Kolhapur']
    kol_active = kol['active']
    kol_confirmed = kol['confirmed']
    kol_deceased = kol['deceased']
    kol_recovered = kol['recovered']
    kol_zone = zone_data['zones'][330]['zone']
    #kolhapur end

    ltr = data["Maharashtra"]['districtData']['Latur']
    ltr_active = ltr['active']
    ltr_confirmed = ltr['confirmed']
    ltr_deceased = ltr['deceased']
    ltr_recovered = ltr['recovered']
    ltr_zone = zone_data['zones'][331]['zone']
    #latur end

    ngp = data["Maharashtra"]['districtData']['Nagpur']
    ngp_active = ngp['active']
    ngp_confirmed = ngp['confirmed']
    ngp_deceased = ngp['deceased']
    ngp_recovered = ngp['recovered']
    ngp_zone = zone_data['zones'][334]['zone']
    #nagpur end

    nded = data["Maharashtra"]['districtData']['Nanded']
    nded_active = nded['active']
    nded_confirmed = nded['confirmed']
    nded_deceased = nded['deceased']
    nded_recovered = nded['recovered']
    nded_zone = zone_data['zones'][335]['zone']
    #nanded end

    ndb = data["Maharashtra"]['districtData']['Nandurbar']
    ndb_active = ndb['active']
    ndb_confirmed = ndb['confirmed']
    ndb_deceased = ndb['deceased']
    ndb_recovered = ndb['recovered']
    ndb_zone = zone_data['zones'][336]['zone']
    #nandurbar end

    nsk = data["Maharashtra"]['districtData']['Nashik']
    nsk_active = nsk['active']
    nsk_confirmed = nsk['confirmed']
    nsk_deceased = nsk['deceased']
    nsk_recovered = nsk['recovered']
    nsk_zone = zone_data['zones'][337]['zone']
    #nashik end

    osb = data["Maharashtra"]['districtData']['Osmanabad']
    osb_active = osb['active']
    osb_confirmed = osb['confirmed']
    osb_deceased = osb['deceased']
    osb_recovered = osb['recovered']
    osb_zone = zone_data['zones'][338]['zone']

    #osmanabad end

    plg = data["Maharashtra"]['districtData']['Palghar']
    plg_active = plg['active']
    plg_confirmed = plg['confirmed']
    plg_deceased = plg['deceased']
    plg_recovered = plg['recovered']
    plg_zone = zone_data['zones'][339]['zone']
    #palghar end

    prb = data["Maharashtra"]['districtData']['Parbhani']
    prb_active = prb['active']
    prb_confirmed = prb['confirmed']
    prb_deceased = prb['deceased']
    prb_recovered = prb['recovered']
    prb_zone = zone_data['zones'][340]['zone']
    #parbhani end

    pune = data["Maharashtra"]['districtData']['Pune']
    pune_active = pune['active']
    pune_confirmed = pune['confirmed']
    pune_deceased = pune['deceased']
    pune_recovered = pune['recovered']
    pune_zone = zone_data['zones'][341]['zone']
    #pune end

    rgd = data["Maharashtra"]['districtData']['Raigad']
    rgd_active = rgd['active']
    rgd_confirmed = rgd['confirmed']
    rgd_deceased = rgd['deceased']
    rgd_recovered = rgd['recovered']
    rgd_zone = zone_data['zones'][342]['zone']
    #raigad end

    rtn = data["Maharashtra"]['districtData']['Ratnagiri']
    rtn_active = rtn['active']
    rtn_confirmed = rtn['confirmed']
    rtn_deceased = rtn['deceased']
    rtn_recovered = rtn['recovered']
    rtn_zone = zone_data['zones'][343]['zone']

    #ratnagiri end

    sgl = data["Maharashtra"]['districtData']['Sangli']
    sgl_active = sgl['active']
    sgl_confirmed = sgl['confirmed']
    sgl_deceased = sgl['deceased']
    sgl_recovered = sgl['recovered']
    sgl_zone = zone_data['zones'][344]['zone']
    #sangli end

    satr = data["Maharashtra"]['districtData']['Satara']
    satr_active = satr['active']
    satr_confirmed = satr['confirmed']
    satr_deceased = satr['deceased']
    satr_recovered = satr['recovered']
    satr_zone = zone_data['zones'][345]['zone']
    #satara end

    sindhu = data["Maharashtra"]['districtData']['Sindhudurg']
    sindhu_active = sindhu['active']
    sindhu_confirmed = sindhu['confirmed']
    sindhu_deceased = sindhu['deceased']
    sindhu_recovered = sindhu['recovered']
    sindhu_zone = zone_data['zones'][346]['zone']
    #sindhudurg end

    slp = data["Maharashtra"]['districtData']['Solapur']
    slp_active = slp['active']
    slp_confirmed = slp['confirmed']
    slp_deceased = slp['deceased']
    slp_recovered = slp['recovered']
    slp_zone = zone_data['zones'][347]['zone']
    #solapur end

    thn = data["Maharashtra"]['districtData']['Thane']
    thn_active = thn['active']
    thn_confirmed = thn['confirmed']
    thn_deceased = thn['deceased']
    thn_recovered = thn['recovered']
    thn_zone = zone_data['zones'][348]['zone']
    #thane end

    war = data["Maharashtra"]['districtData']['Wardha']
    war_active = war['active']
    war_confirmed = war['confirmed']
    war_deceased = war['deceased']
    war_recovered = war['recovered']
    war_zone = zone_data['zones'][349]['zone']
    #wardha end

    wsm = data["Maharashtra"]['districtData']['Washim']
    wsm_active = wsm['active']
    wsm_confirmed = wsm['confirmed']
    wsm_deceased = wsm['deceased']
    wsm_recovered = wsm['recovered']
    wsm_zone = zone_data['zones'][350]['zone']
    #wardha end

    ytml = data["Maharashtra"]['districtData']['Yavatmal']
    ytml_active = ytml['active']
    ytml_confirmed = ytml['confirmed']
    ytml_deceased = ytml['deceased']
    ytml_recovered = ytml['recovered']
    ytml_zone = zone_data['zones'][351]['zone']
    #yavatmal end

    context = {
        'mum_active': mum_active,
        'mum_confirmed': mum_confirmed,
        'mum_deceased': mum_deceased,
        'mum_recovered': mum_recovered,
        'mum_zone': mum_zone,

        'ah_active': ah_active,
        'ah_confirmed': ah_confirmed,
        'ah_deceased': ah_deceased,
        'ah_recovered': ah_recovered,
        'ah_zone': ah_zone,

        'ak_active': ak_active,
        'ak_confirmed': ak_confirmed,
        'ak_deceased': ak_deceased,
        'ak_recovered': ak_recovered,
        'ak_zone': ak_zone,

        'am_active': am_active,
        'am_confirmed': am_confirmed,
        'am_deceased': am_deceased,
        'am_recovered': am_recovered,
        'am_zone': am_zone,

        'ab_active': ab_active,
        'ab_confirmed': ab_confirmed,
        'ab_deceased': ab_deceased,
        'ab_recovered': ab_recovered,
        'ab_zone': ab_zone,

        'bd_active': bd_active,
        'bd_confirmed': bd_confirmed,
        'bd_deceased': bd_deceased,
        'bd_recovered': bd_recovered,
        'bd_zone': bd_zone,


        'bhand_active': bhand_active,
        'bhand_confirmed': bhand_confirmed,
        'bhand_deceased': bhand_deceased,
        'bhand_recovered': bhand_recovered,
        'bhand_zone': bhand_zone,

        'bld_active': bld_active,
        'bld_confirmed': bld_confirmed,
        'bld_deceased': bld_deceased,
        'bld_recovered': bld_recovered,
        'bld_zone': bld_zone,

        'chdp_active': chdp_active,
        'chdp_confirmed': chdp_confirmed,
        'chdp_deceased': chdp_deceased,
        'chdp_recovered': chdp_recovered,
        'chdp_zone': chdp_zone,

        'dhl_active': dhl_active,
        'dhl_confirmed': dhl_confirmed,
        'dhl_deceased': dhl_deceased,
        'dhl_recovered': dhl_recovered,
        'dhl_zone': dhl_zone,

        'gdch_active': gdch_active,
        'gdch_confirmed': gdch_confirmed,
        'gdch_deceased': gdch_deceased,
        'gdch_recovered': gdch_recovered,

        'gond_active': gond_active,
        'gond_confirmed': gond_confirmed,
        'gond_deceased': gond_deceased,
        'gond_recovered': gond_recovered,
        'gond_zone': gond_zone,

        'hing_active': hing_active,
        'hing_confirmed': hing_confirmed,
        'hing_deceased': hing_deceased,
        'hing_recovered': hing_recovered,
        'hing_zone': hing_zone,

        'jlg_active': jlg_active,
        'jlg_confirmed': jlg_confirmed,
        'jlg_deceased': jlg_deceased,
        'jlg_recovered': jlg_recovered,
        'jlg_zone': jlg_zone,

        'jln_active': jln_active,
        'jln_confirmed': jln_confirmed,
        'jln_deceased': jln_deceased,
        'jln_recovered': jln_recovered,
        'jln_zone': jln_zone,

        'kol_active': kol_active,
        'kol_confirmed': kol_confirmed,
        'kol_deceased': kol_deceased,
        'kol_recovered': kol_recovered,
        'kol_zone': kol_zone,

        'ltr_active': ltr_active,
        'ltr_confirmed': ltr_confirmed,
        'ltr_deceased': ltr_deceased,
        'ltr_recovered': ltr_recovered,
        'ltr_zone': ltr_zone,

        'ngp_active': ngp_active,
        'ngp_confirmed': ngp_confirmed,
        'ngp_deceased': ngp_deceased,
        'ngp_recovered': ngp_recovered,
        'ngp_zone': ngp_zone,

        'nded_active': nded_active,
        'nded_confirmed': nded_confirmed,
        'nded_deceased': nded_deceased,
        'nded_recovered': nded_recovered,
        'nded_zone': nded_zone,

        'ndb_active': ndb_active,
        'ndb_confirmed': ndb_confirmed,
        'ndb_deceased': ndb_deceased,
        'ndb_recovered': ndb_recovered,
        'ndb_zone': ndb_zone,

        'nsk_active': nsk_active,
        'nsk_confirmed': nsk_confirmed,
        'nsk_deceased': nsk_deceased,
        'nsk_recovered': nsk_recovered,
        'nsk_zone': nsk_zone,

        'osb_active': osb_active,
        'osb_confirmed': osb_confirmed,
        'osb_deceased': osb_deceased,
        'osb_recovered': osb_recovered,

        'plg_active': plg_active,
        'plg_confirmed': plg_confirmed,
        'plg_deceased': plg_deceased,
        'plg_recovered': plg_recovered,
        'plg_zone': plg_zone,

        'prb_active': prb_active,
        'prb_confirmed': prb_confirmed,
        'prb_deceased': prb_deceased,
        'prb_recovered': prb_recovered,
        'prb_zone': prb_zone,

        'pune_active': pune_active,
        'pune_confirmed': pune_confirmed,
        'pune_deceased': pune_deceased,
        'pune_recovered': pune_recovered,
        'pune_zone': pune_zone,

        'rgd_active': rgd_active,
        'rgd_confirmed': rgd_confirmed,
        'rgd_deceased': rgd_deceased,
        'rgd_recovered': rgd_recovered,
        'rgd_zone': rgd_zone,

        'rtn_active': rtn_active,
        'rtn_confirmed': rtn_confirmed,
        'rtn_deceased': rtn_deceased,
        'rtn_recovered': rtn_recovered,
        'rtn_zone': rtn_zone,

        'sgl_active': sgl_active,
        'sgl_confirmed': sgl_confirmed,
        'sgl_deceased': sgl_deceased,
        'sgl_recovered': sgl_recovered,
        'sgl_zone': sgl_zone,

        'satr_active': satr_active,
        'satr_confirmed': satr_confirmed,
        'satr_deceased': satr_deceased,
        'satr_recovered': satr_recovered,
        'satr_zone': satr_zone,

        'sindhu_active': sindhu_active,
        'sindhu_confirmed': sindhu_confirmed,
        'sindhu_deceased': sindhu_deceased,
        'sindhu_recovered': sindhu_recovered,
        'sindhu_zone': sindhu_zone,

        'slp_active': slp_active,
        'slp_confirmed': slp_confirmed,
        'slp_deceased': slp_deceased,
        'slp_recovered': slp_recovered,
        'slp_zone': slp_zone,

        'thn_active': thn_active,
        'thn_confirmed': thn_confirmed,
        'thn_deceased': thn_deceased,
        'thn_recovered': thn_recovered,
        'thn_zone': thn_zone,

        'war_active': war_active,
        'war_confirmed': war_confirmed,
        'war_deceased': war_deceased,
        'war_recovered': war_recovered,
        'war_zone': war_zone,

        'wsm_active': wsm_active,
        'wsm_confirmed': wsm_confirmed,
        'wsm_deceased': wsm_deceased,
        'wsm_recovered': wsm_recovered,
        'wsm_zone': wsm_zone,

        'ytml_active': ytml_active,
        'ytml_confirmed': ytml_confirmed,
        'ytml_deceased': ytml_deceased,
        'ytml_recovered': ytml_recovered,
        'ytml_zone': ytml_zone,

    }

    return render(request, 'stats/maharashtra.html', context)
