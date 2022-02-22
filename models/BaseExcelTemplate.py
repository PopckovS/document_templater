import copy

from openpyxl_templates import TemplatedWorkbook, TemplatedWorksheet

# TODO УЗНАТЬ !
# from xlsxtpl.writerx import BookWriter
from xltpl.writer import BookWriter
from DataTemplate.names import DOCUMENT_TYPE, EXCEL_TEMPLATE


class ModelSheet:
    """
    Определяет модель страницы файла Excel
        meta_fields - мета информация для генерации полей
        fields - сами данные
    """

    meta_fields, fields = {}, {}

    def __init__(self, type, name):
        self.type, self.name = self._set_sheet_meta_fields(type, name)

    def _set_sheet_meta_fields(self, type, name):
        """Устанавливаем откуда брать данные для шаблона, из Excel или Docx документа"""
        if type in DOCUMENT_TYPE:
            self.meta_fields = copy.deepcopy(EXCEL_TEMPLATE[type][name])
            return type, name

    def set_data(self, csv_dict, excel_dict):
        """Устанавливает данные"""
        self.fields['csv'] = csv_dict
        self.fields['excel'] = excel_dict

    # TODO определяет как соединять данные для создания контекста для шаблона,
    #  основная логика в род классе, но этот метод будет вынесен в дочерний,
    #  бросать исключение если не переопределен в дочернем классе.
    def create_context(self):
        """Возвращает словарь с данными для вставки в шаблон страницы"""
        csv_meta, csv_dict = self.meta_fields['csv'], self.fields['csv']
        excel_meta, excel_dict = self.meta_fields['excel'], self.fields['excel']
        items, data = [], {}
        context = {
            'sheet_name': self.name,
            'items': []
        }

        # заполняем страницу данными только из CSV
        if excel_meta is None:
            for row in csv_dict:
                for key, val in csv_meta.items():
                    data[key] = row[val]
                items.append(data)
                data = {}
        # заполняем страницу данными из CSV и Excel
        else:
            for csv_row in csv_dict:
                for ex_row in excel_dict:
                    # если кадастровый номер из разных источников совпадает
                    if csv_row['Кадастровый номер'] == ex_row['Кадастровый номер ']:
                        for key, val in csv_meta.items():
                            data[key] = csv_row[val]
                        for key, val in excel_meta.items():
                            data[key] = ex_row[val]
                items.append(data)
                data = {}

        context['items'] = items
        return context


class BaseExcelTemplate:
    """Определяет модель файла Excel"""

    type, result, template = None, None, None
    payloads, data, sheets = [], {}, {}

    def __init__(self, type, path):
        """Создает объект файла"""
        self.template = path
        self.writer = BookWriter(path)
        self.sheets = self._set_sheets_template(type)

    def set_data(self, csv_dict, excel_dict):
        """Сохраняет данные для рендеринга страницы, передает их каждой из страниц"""
        self.data['csv'] = csv_dict
        self.data['excel'] = excel_dict
        for sheet in self.sheets.values():
            sheet.set_data(csv_dict=csv_dict, excel_dict=excel_dict)

    def _set_sheets_template(self, type):
        """Если тип документации разрешен, то возвращает словарь с объектами страниц"""
        if type in DOCUMENT_TYPE:
            self.type = type
            sheets = list(EXCEL_TEMPLATE[type].keys())
            sheets_obj = {sheet: ModelSheet(type, sheet) for sheet in sheets}
            return sheets_obj

    def _get_payloads(self):
        """Возвращает список со словарями, 1 словарь это данные для 1 страницы шаблона xlsx"""
        # TODO кастамная штука, привязана к количеству страниц, лучше вынести в настройки.
        self.payloads = [sheet.create_context() for sheet in self.sheets.values()]
        for index in range(len(self.payloads)):
            self.payloads[index]['tpl_index'] = index
        # self.payloads[1]['tpl_index'] = 1
        return self.payloads

    def save(self, path):
        """Рендерит и сохраняет файл"""
        data = self._get_payloads()
        self.writer.render_sheets(payloads=data)
        self.writer.save(path)
        self.result = path
        return path





