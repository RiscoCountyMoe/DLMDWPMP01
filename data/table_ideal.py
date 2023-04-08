from .database import Database


class TableIdeal(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_ideal_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS ideal (x FLOAT, y1 FLOAT, y2 FLOAT, y3 FLOAT, y4 FLOAT, y5 FLOAT, y6 FLOAT, y7 FLOAT, y8 FLOAT, y9 FLOAT, y10 FLOAT, y11 FLOAT, y12 FLOAT, y13 FLOAT, y14 FLOAT, y15 FLOAT, y16 FLOAT, y17 FLOAT, y18 FLOAT, y19 FLOAT, y20 FLOAT, y21 FLOAT, y22 FLOAT, y23 FLOAT, y24 FLOAT, y25 FLOAT, y26 FLOAT, y27 FLOAT, y28 FLOAT, y29 FLOAT, y30 FLOAT, y31 FLOAT, y32 FLOAT, y33 FLOAT, y34 FLOAT, y35 FLOAT, y36 FLOAT, y37 FLOAT, y38 FLOAT, y39 FLOAT, y40 FLOAT, y41 FLOAT, y42 FLOAT, y43 FLOAT, y44 FLOAT, y45 FLOAT, y46 FLOAT, y47 FLOAT, y48 FLOAT, y49 FLOAT, y50 FLOAT);'''
        self.create_table(sql)

    def load_ideal_data(self, data):
        sql = '''INSERT INTO ideal (x, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20, y21, y22, y23, y24, y25, y26, y27, y28, y29, y30, y31, y32, y33, y34, y35, y36, y37, y38, y39, y40, y41, y42, y43, y44, y45, y46, y47, y48, y49, y50) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        values = [(row['x'], row['y1'], row['y2'], row['y3'], row['y4'], row['y5'], row['y6'], row['y7'], row['y8'], row['y9'], row['y10'], row['y11'], row['y12'], row['y13'], row['y14'], row['y15'], row['y16'], row['y17'], row['y18'], row['y19'], row['y20'], row['y21'], row['y22'], row['y23'], row['y24'], row['y25'], row['y26'], row['y27'], row['y28'], row['y29'], row['y30'], row['y31'], row['y32'], row['y33'], row['y34'], row['y35'], row['y36'], row['y37'], row['y38'], row['y39'], row['y40'], row['y41'], row['y42'], row['y43'], row['y44'], row['y45'], row['y46'], row['y47'], row['y48'], row['y49'], row['y50'])
                  for _, row in data.iterrows()]
        self.load_data_to_table(sql, values)
