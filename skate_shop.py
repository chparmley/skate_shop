import requests


def get_skates():
    skate_websites = ['https://www.themgoods.com/collections/all/products','https://usa.shop-task.com/collections/aggressive-skates/products', 'https://oakcityskate.com/collections/aggressive-skates/products']
    product_keys = ['Aggressive Skate', 'Inline Skates', 'Skates']
    skates = {}
    for site in skate_websites:
        response = requests.get(site+'.json').json()
        result = response
        for product in result['products']:
            # print(product.keys())
            if product['product_type'] in product_keys :
                skates[product['id']] = {
                    'title':product['title'].replace('\"',''),
                    'image':product['images'][0]['src'],
                    'url':site+'/'+product['handle']
                }
    return skates

get_skates()
