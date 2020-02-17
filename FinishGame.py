import sqlite3


class game_ower:
    def __init__(self, dead_list, namebd):
        self.dead_list = dead_list
        self.namebd = namebd

    def check(self):
        b = 0
        m = 0
        con = sqlite3.connect(self.namebd)
        cur = con.cursor()
        for i in range(1, 11):
            if i not in self.dead_list:
                a = """SELECT role FROM character
                            WHERE id = {}""".format(str(i))
                result = cur.execute(a).fetchall()

                # Вывод результатов на экран
                for elem in result:
                    if elem[0] == 1:
                        b += 1
                    if elem[0] == 0:
                        m += 1
        con.close()
        if b >= m:
            return 1
        elif b == 0:
            return 2
        else:
            return 0

    def end(self, num):
        con = sqlite3.connect(self.namebd)
        cur = con.cursor()
        a = """SELECT role FROM character WHERE id = {}""".format(num)
        result = cur.execute(a).fetchall()
        return result[0][0]
