import requests

def get_district_info(zipcode):
    resp = requests.get( 'https://congress.api.sunlightfoundation.com/districts/locate?zip={}'.format(zipcode))
    if resp.status_code != 200:
        print 'Could not get district number' + resp.status_code
    js = resp.json()
    return js

def get_district_number(zipcode):
    info = get_district_info(zipcode)
    return info['results']

def get_rep_names(zipcode):
    info = get_district_number(zipcode)
    for item in info:
        state_name = item['state']
        dist = item['district']
        resp = requests.get('https://api.propublica.org/congress/v1/members/{chamber}/{state}/{district}/cur'.format(chamber='yes', state=state_name, district=dist))
        js = resp.json()
    rep_name = js['results'][0]['name']
    return rep_name

def get_multip_rep_info(zipcode):
    info = get_district_number(zipcode)
    print info
    js = []
    for item in info:
        state_name = item['state']
        print state_name
        dist = item['district']
        print dist
        resp = requests.get('https://api.propublica.org/congress/v1/members/house/'+state_name+'/{}/current.json'.format(dist), headers={'X-API-Key': 'HeU67wOwjMas9zx1MWRRg4fB09F4YyJ87jgec6xv'})
        js.append(resp.json())
    return js

def get_1rep_name(dist):
    state_name = dist.dist_state
    my_dist = dist.dist_num
    resp = requests.get('https://api.propublica.org/congress/v1/members/house/'+state_name+'/{}/current.json'.format(my_dist), headers={'X-API-Key': 'HeU67wOwjMas9zx1MWRRg4fB09F4YyJ87jgec6xv'})
    js = resp.json()
    results = js['results']
    return results[0]['name']

def get_1rep_id(dist):
    state_name = dist.dist_state
    my_dist = dist.dist_num
    resp = requests.get('https://api.propublica.org/congress/v1/members/house/'+state_name+'/{}/current.json'.format(my_dist), headers={'X-API-Key': 'HeU67wOwjMas9zx1MWRRg4fB09F4YyJ87jgec6xv'})
    js = resp.json()
    results = js['results']
    return results[0]['id']

def get_votes(dist):
    id = get_1rep_id(dist)
    resp = requests.get('https://api.propublica.org/congress/v1/members/'+id+'/votes.json', headers={'X-API-Key': 'HeU67wOwjMas9zx1MWRRg4fB09F4YyJ87jgec6xv'})
    js = resp.json()
    results = js['results']
    return results[0]['votes']

def get_bill_name_maybe(dist):
    val = get_votes(dist)
    return val[0]['description']

def get_positon(dist):
    val = get_votes(dist)
    return val[0]['positon']
