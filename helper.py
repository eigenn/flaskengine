

class ModelRow(object):
    def __init__(self, table_order, entity):
        self.table_order = table_order
        self.entity = entity

    def __iter__(self):
        for coloum in self.table_order:
            yield getattr(self.entity, coloum)


class ModelTable(object):
    def __init__(self, table_order, query):
        self.table_order = table_order
        self.query = query

    def __iter__(self):
        for entity in self.query:
            yield ModelRow(self.table_order, entity)

    def header(self):
        for title in self.table_order:
            yield title.title()
