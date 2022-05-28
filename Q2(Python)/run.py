# Add your shipping companies in this dictionary
shippingCompanies = {
    "XYZ": {
        "Cairo": "C",
        "Alexandria": "A"
    },
    "DXB": {
        "Cairo": "CAI",
        "Alexandria": "ALX"
    }
}


def get_city_mapping(city_name, shipping_company_name):
    """
    :return: the proper mapping that corresponds to the company in the parameters
    """
    if shipping_company_name in shippingCompanies:                      # check if the company name exist
        if city_name in shippingCompanies[shipping_company_name]:       # check if the city name exist
            return shippingCompanies[shipping_company_name][city_name]  # return the proper mapping

    return "invalid city or company name"


print(get_city_mapping("Cairo", "XYZ"))
