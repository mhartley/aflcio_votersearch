import urllib.request
import json

def geo_api(location):
    location = location.replace(' ', '+')
    address = location
    apikey =  'AIzaSyCKjvW-c9UV2u1bkLqe0If6Fh8A5HgcUW4' # MORGAN'S ACCOUNT 
    gmapsrequesturl = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (address, apikey)
    print(gmapsrequesturl)
    try:
        with urllib.request.urlopen(gmapsrequesturl) as response:
            str_response = response.read().decode('utf-8')
            data = json.loads(str_response)
            if data['status'] == 'OK':
                data = data['results'][0]['geometry']['location']
                data['status'] = 'OK'
            elif data['status'] == "ZERO_RESULTS":
                data = {'status': "ZERO_RESULTS"}
    except IOError:
        data = {'status':'ERROR'}
    return data