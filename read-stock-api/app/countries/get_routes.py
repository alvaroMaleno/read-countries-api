from flask import Blueprint, request, jsonify, make_response

from app.db import execute

get_countries_bp = Blueprint('get_countries_bp', __name__)


@get_countries_bp.route('/api/countries/getCountries', methods=['GET'])
def get_countries():
    COUNTRIES = """
    select 
        * 
    from 
        countries;
    """
    result = execute(query=COUNTRIES)

    if not result:
        return not_found()

    return jsonify({'countries': result})


@get_countries_bp.route('/api/countries/getCountry/Iso2', methods=['GET'])
def get_country_by_iso2(iso2=''):
    COUNTRY_BY_ISO2 = """
    select * from countries c where c.isocode2 = '{iso2}';
    """
    args = request.args
    iso2_code = args.get("iso2")

    if not iso2_code:
        iso2_code = iso2

    query = COUNTRY_BY_ISO2.format(iso2=iso2_code)
    result = execute(query=query)

    if not result:
        return not_found()

    return jsonify({'country': result[0]})


@get_countries_bp.route('/api/countries/getCountry/Iso3', methods=['GET'])
def get_country_by_iso3(iso3=''):
    COUNTRY_BY_ISO3 = """
    select * from countries c where c.isocode3 = '{iso3}';
    """
    args = request.args
    iso3_code = args.get("iso3")

    if not iso3_code:
        iso3_code = iso3

    query = COUNTRY_BY_ISO3.format(iso3=iso3_code)
    result = execute(query=query)

    if not result:
        return not_found()

    return jsonify({'country': result[0]})


@get_countries_bp.route('/api/countries/getCountry/Name', methods=['GET'])
def get_country_by_name(name=''):
    COUNTRY_BY_NAME = """
    select * from countries c where c.countryname = '{name}';
    """
    args = request.args
    country_name = args.get("name")

    if not country_name:
        country_name = name

    query = COUNTRY_BY_NAME.format(name=country_name)
    result = execute(query=query)

    if not result:
        return not_found()

    return jsonify({'country': result[0]})


def not_found():
    return make_response("Country not found", 404)
