class Table():
    def __init__(self, p, b):
        self.a = [list([0 for j in range(b)]) for i in range(p)]

    def get_value(self, r, cl):
        try:
            return self.a[r][cl]
        except:
            return None

    def set_value(self, r, cl, val):
        self.a[r][cl] = val

    def n_rows(self):
        return len(self.a)

    def n_cols(self):
        if len(self.a) == 0:
            return 0
        else:
            return len(self.a[0])

    def delete_row(self, r):
        self.a.pop(r)

    def delete_col(self, cl):
        for i in self.a:
            i.pop(cl)

    def add_row(self, r):
        self.a.insert(r, [0 for i in range(len(self.a[0]))])

    def add_col(self, cl):
        for i in self.a:
            i.insert(cl, 0)
