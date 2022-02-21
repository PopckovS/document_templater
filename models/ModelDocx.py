from docxtpl import DocxTemplate


class ModelDocx:
    """Определяет модель файла Docx"""

    context = None

    def __init__(self, type, name, path):
        self.type = type
        self.name = name
        self.writer = DocxTemplate(path)

    def save(self, path):
        """Рендерит и сохраняет файл"""
        self.writer.render(self.context)
        self.writer.save(path)

    def _get_data(self):
        """Получает данные для рендеринга шаблона"""
        #   csv_dict - словарь с данными из CSV
        # excel_dict - словарь с данными из Excel
        pass

    def create_context(self):
        """Создает контекст для заполнения шаблона документа"""


