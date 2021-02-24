def get_absolute_url(url, *args, **kwargs):
    """Получение абсолютного адреса url.
    :param url: адрес домена (обязательный)
    :param *args: (опциональный) позиционные аргументы
    :param *kwargs: (опциональный) именованные аргументы
    """    
    absolute_url = url
    
    for i in args:                          # цикл итераций по списку позиционных аргументов
        absolute_url += f'/{str(i)}'        # перед каждым позиционным аргументом добавляется '/'

    if args:
        absolute_url += '?'                 # при наличии позиционных аргументов после последнего позиционного аргумента добавляется '?'
    
    for k, v in kwargs.items():             # цикл итераций по словарю именованных аргументов
        absolute_url += f'{k}={v}&'         # между ключом и значением каждого аргумента вставляем '=', а после каждого значения добавляется '&'
        
    if kwargs:
        absolute_url = absolute_url[:-1]    # при наличии именованных аргументов делаем срез последнего символа, чтобы убрать лишний '&'

    return absolute_url


# код программы

print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))

# Должны быть следующие результаты выполнения программы
# www.yandex.ru/posts/news?id=24&author=admin
# www.google.com/images?id=24&category=auto&color=red&size=small

# проверка работы функции 'get_absolute_url' на альтернативных параметрах 
print('\r')
print(get_absolute_url('www.support2b.ru', 'article', writer='novikov'))
print(get_absolute_url('www.support2b.ru', 'article'))
print(get_absolute_url('www.support2b.ru'))
