
from collections import defaultdict
class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.schema = defaultdict(defaultdict)
        for name, col in zip(names, columns):
            self.schema[name]["len_columns"] = col
            self.schema[name]["max_id"] = 1
        

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.schema:
            return False
        table = self.schema[name]
        if "len_columns" in table and len(row) != table["len_columns"]:
            return False

        max_id = table["max_id"]

        if "rows" in table:
            table["rows"][max_id] = row
        else:
            table["rows"] = {max_id: row} 

        table["max_id"] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.schema:
            return
        table = self.schema[name]
        if "rows" in table and rowId in table["rows"]:
            del table["rows"][rowId]


    def sel(self, name: str, rowId: int, columnId: int) -> str:
        # value of cell
        if name not in self.schema:
            return "<null>"
        table = self.schema[name]
        if columnId <= table["len_columns"] and "rows" in table and rowId in table["rows"]:
            row = table["rows"][rowId]
            return row[columnId-1]

        return "<null>"

    def exp(self, name: str) -> List[str]:
        if name not in self.schema:
            return []
        table = self.schema[name]
        result = []
        if "rows" in table:
            for id, row in table["rows"].items():
                cur_row = [str(id)] + row
                cur_row_str = ",".join(cur_row)
                result.append(cur_row_str)
        return result