import flask
import json


def test_getCountries(client):
    result = client.get('/api/countries/getCountries')
    countries = json.loads(result.data)
    assert countries is not None
    assert len(countries['countries']) > 0


def test_getCountryByIso2(client):
    result = client.get('/api/countries/getCountry/Iso2?iso2=ES')
    country = json.loads(result.data)
    assert country is not None
    assert country['country']['isocode2'] == 'ES'


def test_getCountryByIso2__not_found(client):
    result = client.get('/api/countries/getCountry/Iso2?iso2=JJ')
    assert result.status_code == 404


def test_getCountryByIso3(client):
    result = client.get('/api/countries/getCountry/Iso3?iso3=ESP')
    country = json.loads(result.data)
    assert country is not None
    assert country['country']['isocode3'] == 'ESP'


def test_getCountryByIso3_not_found(client):
    result = client.get('/api/countries/getCountry/Iso3?iso3=LLL')
    assert result.status_code == 404


def test_getCountryByName(client):
    result = client.get('/api/countries/getCountry/Name?name=Spain')
    country = json.loads(result.data)
    assert country is not None
    assert country['country']['countryname'] == 'Spain'


def test_getCountryByName(client):
    result = client.get('/api/countries/getCountry/Name?name=Philips')
    assert result.status_code == 404
