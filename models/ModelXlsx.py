import copy

from openpyxl_templates import TemplatedWorkbook, TemplatedWorksheet

# TODO УЗНАТЬ !
# from xlsxtpl.writerx import BookWriter
from xltpl.writer import BookWriter
from DataTemplate.names import DOCUMENT_TYPE, EXCEL_TEMPLATE


class ModelXlsx:
    """Определяет модель файла Excel"""

    type, result, template,  = None, None, None
    data, sheets, payloads = {}, {}, []

    def __init__(self, type, path):
        """Создает объект файла"""
        self.template = path
        self.writer = BookWriter(path)
        self.sheets = self._set_sheets_template(type)

    def set_data(self, csv_dict, excel_dict):
        """
        Сохраняет данные для рендеринга страницы,
        передает их каждой из страниц
        """
        self.data['csv'] = csv_dict
        self.data['excel'] = excel_dict
        for sheet in self.sheets.values():
            sheet.set_data(csv_dict=csv_dict, excel_dict=excel_dict)

    def _set_sheets_template(self, type):
        """
        Если тип документации разрешен, то возвращает словарь с объектами
        страницы, которые имеют набор полей в соответствии с шаблоном
        """
        if type in DOCUMENT_TYPE:
            self.type = type
            sheets = list(EXCEL_TEMPLATE[type].keys())
            data = {sheet: ModelSheet(type, sheet) for sheet in sheets}
            return data

    # TODO пока не используется, будущая фича
    def set_sheet(self, sheet):
        """Создает объект страницы шаблона xlsx на прямую"""
        self.sheets[sheet] = ModelSheet(sheet)

    def _get_payloads(self):
        """
        Возвращает список со словарями, каждый словарь это
        данные для конкретной страницы шаблона xlsx
        """
        self.payloads = [sheet.get_data() for sheet in self.sheets.values()]

        return self.payloads

    def save(self, path):
        """Рендерит и сохраняет файл"""
        data = self._get_payloads()
        data[0]['tpl_index'] = 0
        data[1]['tpl_index'] = 1
        self.writer.render_sheets(payloads=data)
        self.writer.save(path)
        self.result = path
        return path





