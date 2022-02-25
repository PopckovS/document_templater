from utils.utils import get_summ, get_var_1, get_var_2


# типы документации
DOCUMENT_TYPES = ('type1', 'type2', 'type3')

TYPES = []

DOCUMENT_TEMPLATE = {
    'type1': {
        'meta': {
            'link': 'registration_number'
        },
        'data': {
            'data_1': {
                'registration_number': 'Номер для связки данных',
                'area': 'Площадь',
                'category': 'Категория земель'
            },
            'data_2': {
                'name': 'Имя',
                'address': 'Адрес',
                'date': 'Дата',
                'price': 'Цена'
            },
        },
        'result': {
            'excel': {
                # отражает собой один документ с несколькими страницами
                'Документ Excel №1': {
                    'Страница №1': {
                        'items': { # формируется только из данных источника data_2 + кастомные поля
                            'name': {'title': 'Имя', 'type': str()},
                            'address': {'title': 'Адрес', 'type': str()},
                            'date': {'title': 'Дата', 'type': str()},
                            'price': {'title': 'Цена', 'type': float()},
                            'var_1': (get_var_1, 'address', 'date'),
                        }
                    },
                    'Страница №2': {
                        'items': {# формируется из источников data_1 и data_2
                            'name': {'title': 'Имя', 'type': str()},
                            'address': {'title': 'Адрес', 'type': str()},
                            'date': {'title': 'Дата', 'type': str()},
                            'area': {'title': 'Площадь', 'type': str()},
                            'category': {'title': 'Категория земель', 'type': str()},
                            'registration_number': {'title': 'Номер связки данных', 'type': int()},
                        }
                    }
                },

                # отражает собой один документ с несколькими страницами
                'Документ Excel №2': {
                    'Страница №1': {
                        'items': {# формируется из источников data_1 и data_2 и + кастомные поля
                            'name': {'title': 'Имя', 'type': str()},
                            'address': {'title': 'Адрес', 'type': str()},
                            'date': {'title': 'Дата', 'type': str()},
                            'area': {'title': 'Площадь', 'type': str()},
                            'category': {'title': 'Категория земель', 'type': str()},
                            'registration_number': {'title': 'Номер связки данных', 'type': int()},
                        },
                        'var_2': (get_var_2, 'registration_number', 'address')
                    }
                }
            },

            'docx': {
                # отражает собой один документ и все что тут указано это данные для вставки
                'Документ Docx №1': {
                    'items_1': { # формируется только из данных источника date_1 и data_2
                        'name': {'title': 'Имя', 'type': str()},
                        'address': {'title': 'Адрес', 'type': str()},
                        'date': {'title': 'Дата', 'type': str()},
                        'area': {'title': 'Площадь', 'type': str()},
                        'category': {'title': 'Категория земель', 'type': str()},
                        'registration_number': {'title': 'Номер связки данных', 'type': int()},
                    },
                    'items_2': { # формируется только из данных источника data_2
                        'name': {'title': 'Имя', 'type': str()},
                        'address': {'title': 'Адрес', 'type': str()},
                        'price': {'title': 'Цена', 'type': float()},
                    },
                                # вычисляемое поле, функция для коллбэка и аргументы которые он вычисляет
                    'summ': (get_summ, 'price')
                }
            }
        },
    }
}















