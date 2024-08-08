import requests
import json 
import os
import configparser
# from requests.auth import HTTPBasicAuth


# Получение текущей директории
cur_file_name = os.path.basename(__file__)
path_cur_file = os.path.abspath(__file__)
cur_path = path_cur_file.replace(cur_file_name, '')


# Забираем ключ
config = configparser.ConfigParser()
config.read('key.ini')
key_api = config['DEFAULT'].get('key')


# Забираем конфиги API
with open(cur_path + 'config_api.json') as file:
    json_key = json.load(file)
api_content_type = json_key.get('Content-type') # Формат передаваемых данные
url_api = json_key.get('url') # Получение основной ссылки API
method_api_list_infoblock = json_key.get('list_infoblock') # Получение списка инфоблоков
method_api_infoblock = json_key.get('infoblock') # Получение инфоблока
method_api_list_element = json_key.get('list_element') # Получение списка элементов
method_api_element = json_key.get('element') # Получение элемента
method_api_categories = json_key.get('categories') # Получение списка элементов
method_api_search = json_key.get('search')



#key_api = HTTPBasicAuth('key', json_key.get('key'))

# Получение данных из API через GET
def requests_aspire(method,
                url= url_api,
                content_type = api_content_type,
                key = key_api,
                id_block= 5, # Блок "привилегии" 
                id_element= 1, # Просто первый элемент
                id_category= 18
                ):

    """На данный момент есть методы:
        - list_block - Список блоков
        - block - Блок
        - list_element - Список элементов
        - element - Элемент 
        - search - Поиск элемента по фильтру
    """

    headers = {
        "Content-Type": content_type
    }

    if method == 'list_block':
        url_method = ''.join([url, method_api_list_infoblock])
        url_key = '?'.join([url_method, f'key={key}'])
        url_final = url_key
        return requests.get(url=url_final)
    
    elif method == 'block':
        url_method = ''.join([url, method_api_infoblock])
        url_key = '?'.join([url_method, f'key={key}'])
        url_final = '&'.join([url_key, f'id={id_block}'])
        return requests.get(url=url_final)

    elif method == 'categories':
        url_method = ''.join([url, method_api_categories])
        url_key = '?'.join([url_method, f'key={key}'])
        url_final = '&'.join([url_key, f'iblock={id_block}'])
        return requests.get(url=url_final)

    elif method == 'list_element':
        url_method = ''.join([url, method_api_list_element])
        url_key = '?'.join([url_method, f'key={key}'])
        url_final = '&'.join([url_key, f'iblock={id_block}'])
        return requests.get(url=url_final)

    elif method == 'element':
        url_method = ''.join([url, method_api_element])
        url_key = '?'.join([url_method, f'key={key}'])
        url_final = '&'.join([url_key, f'iblock={id_block}', f'id={id_element}'])
        return requests.get(url=url_final)
    
    elif method == 'search':
        url_method = ''.join([url, method_api_search])
        url_key = '?'.join([url_method, f'key={key}'])
        url_final = '&'.join([url_key])
        return requests.get(url=url_final)

    else:
        print('Метод отсутсвует')

    