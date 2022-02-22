import copy

from docxtpl import DocxTemplate, Listing
from exceptions import NotInheritedMethodTypeError, NotAllowedDocumentationTypeError
from DataTemplate.names import DOCUMENT_TYPE, DOCX_TEMPLATE


class BaseDocxTemplate:
    """Определяет модель файла Docx"""

    context, result, data = None, None, {}

    def __init__(self, type, name, path):
        self.path = path
        self.fields = self._set_docx_fields(type, name)
        self.writer = DocxTemplate(path)

    def _set_docx_fields(self, type, name):
        """
        Если тип документации разрешен, то возвращает словарь с объектами
        страницы, которые имеют набор полей в соответствии с шаблоном
        """
        if type not in DOCUMENT_TYPE or not DOCX_TEMPLATE[type][name]:
            raise NotAllowedDocumentationTypeError(
                'Не получается определить путь документации документации для `%s`' % type
            )
        self.type, self.name = type, name
        return copy.deepcopy(DOCX_TEMPLATE[type][name])

    def save(self, path):
        """Генерирует контекст, рендерит файл docx и сохраняет его"""
        self.context = self._create_context()
        self.writer.render(self.context)
        self.writer.save(path)

    def set_data(self, csv, excel):
        """Получает данные для рендеринга шаблона"""
        raise NotInheritedMethodTypeError(
            'Метод %s должен быть переопределен, в дочернем классе.' % self.set_data.__name__
        )

    def _create_context(self):
        """Создает контекст данных для заполнения шаблона документа"""
        raise NotInheritedMethodTypeError(
            'Метод %s должен быть переопределен, в дочернем классе.' % self.create_context.__name__
        )


class NoteDocx(BaseDocxTemplate):
    """Модель данных для документа 'Пояснительная записка' подходит для типов `gs` и `ngs`"""

    def set_data(self, csv, excel):
        """Получает данные для рендеринга шаблона"""
        self.data['csv'] = csv
        self.data['excel'] = excel

    def _create_context(self):
        """Создает контекст данных для заполнения шаблона документа"""
        items, registration_numbers, summ = [], [], 0

        # Проходимся по данным из CSV и Docx, на их основе создаем контент
        for csv_row in self.data['csv']:
            for ex_row in self.data['excel']:

                # находим совпадение по кадастровым номерам
                if csv_row['Кадастровый номер'] == ex_row['Кадастровый номер ']:
                    data = {}
                    for key, val in self.fields['csv'].items():
                        data[key] = csv_row[val]
                    for key, val in self.fields['excel'].items():
                        data[key] = ex_row[val]

                    items.append(data)
                    registration_numbers.append(csv_row['Кадастровый номер'])
                    summ += int(csv_row['Площадь, кв. м'])
                    data = {}

        return {'items': items, 'summ': summ, 'numbers': ', '.join(registration_numbers)}


class PetitionRemovalDocx(BaseDocxTemplate):
    """Модель данных для документа 'Ходатайство об изъятии', для документов типа `removal`"""

    def set_data(self, csv):
        """Получает данные для рендеринга шаблона"""
        self.data['csv'] = csv

    def _create_context(self):
        """Создает контекст данных для заполнения шаблона документа"""
        registration_numbers = []
        for csv_row in self.data['csv']:
            registration_numbers.append(csv_row['Кадастровый номер'])
        return {'registration_numbers': ', '.join(registration_numbers)}


class AvtodorDocx(BaseDocxTemplate):
    """Модель данных для документа 'Шаблон КТ-ГК Автодор', для документов типа `removal`"""

    def set_data(self, csv, excel):
        """Получает данные для рендеринга шаблона"""
        self.data['csv'], self.data['excel'] = csv, excel

    def _create_context(self):
        """Создает контекст данных для заполнения шаблона документа"""
        items = []

        # Проходимся по данным из CSV и Docx, на их основе создаем контент
        for csv_row in self.data['csv']:
            for ex_row in self.data['excel']:

                # находим совпадение по кадастровым номерам
                if csv_row['Кадастровый номер'] == ex_row['Кадастровый номер существующего ЗУ/КК']:
                    data = {}
                    for key, val in self.fields['csv'].items():
                        data[key] = csv_row[val]
                    for key, val in self.fields['excel'].items():
                        # data[key] = ex_row[val]

                        # TODO замена Q на N если Q пустой
                        if val == 'Примечание' and ex_row[val]:
                            data[key] = ex_row[val]
                        else:
                            data[key] = ex_row['Площадь по проекту межевания, кв. м']

                    items.append(data)

        result = {'items': items}
        return result











