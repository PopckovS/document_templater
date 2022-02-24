
# типы документации
DOCUMENT_TYPES = ('type1', 'type2', 'type3')

DOCUMENT_TEMPLATE = {
    'type1': {
        'meta': {
            'link': 'registration_number'
        },
        'data': [
            {
                'registration_number': 'Номер связки данных',
                'area': 'Площадь',
                'category': 'Категория земель'
            },
            {
                'name': 'Имя',
                'address': 'Адрес',
                'date': 'Дата'
            },
        ],
        'result': {
            'excel': {
                'Документ Excel №1': {
                    'Страница №1': {
                        'items': {
                            'name': {'title': 'Имя', 'type': str()},
                            'address': {'title': 'Адрес', 'type': str()},
                            'date': {'title': 'Дата', 'type': str()},
                            'area': {'title': 'Площадь', 'type': str()},
                            'category': {'title': 'Категория земель', 'type': str()},
                            'registration_number': {'title': 'Номер связки данных', 'type': int()},
                        }
                    },
                    'Страница №2': {
                        'items': {
                            'name': {'title': 'Имя', 'type': str()},
                            'address': {'title': 'Адрес', 'type': str()},
                            'date': {'title': 'Дата', 'type': str()},
                            'area': {'title': 'Площадь', 'type': str()},
                            'category': {'title': 'Категория земель', 'type': str()},
                            'registration_number': {'title': 'Номер связки данных', 'type': int()},
                        }
                    }
                },

                'Документ Excel №2': {
                    'Страница №1': {
                        'items': {
                            'name': {'title': 'Имя', 'type': str()},
                            'address': {'title': 'Адрес', 'type': str()},
                            'date': {'title': 'Дата', 'type': str()},
                            'area': {'title': 'Площадь', 'type': str()},
                            'category': {'title': 'Категория земель', 'type': str()},
                            'registration_number': {'title': 'Номер связки данных', 'type': int()},
                        }
                    }
                }
            },

            'docx': {
                'Документ Docx №1': {
                    'items_1': {
                        'name': {'title': 'Имя', 'type': str()},
                        'address': {'title': 'Адрес', 'type': str()},
                        'date': {'title': 'Дата', 'type': str()},
                        'area': {'title': 'Площадь', 'type': str()},
                        'category': {'title': 'Категория земель', 'type': str()},
                        'registration_number': {'title': 'Номер связки данных', 'type': int()},
                    },
                    'items_2': {
                        'name': {'title': 'Имя', 'type': str()},
                        'address': {'title': 'Адрес', 'type': str()},
                    },
                    # TODO как сделать генерацию данных что вычисляются из других данных ?
                    #  а не берутся на прямую

                }
            }
        },
    }
}















