import random
import sqlite3


class Character:
    # role - это роль персонажа(1 - бандит, 0 - мирный). num - это числовой номер персонажа
    # bandits - это список бандитов
    def __init__(self, role, num, bandits):
        self.role = role
        self.life = True
        self.num = num
        self.trigger = 0
        self.bandits = bandits
        self.dialogue_trigger = ["Я считаю игрока номер {} бандитом!", "Я думаю бандит это игрок номер {}",
                                 "Я один заметил, что игрок номер {} очень подозрителен?",
                                 "Я уверен, игрок номер {} бандит", "Вы все еще не поняли, что игрок номер {} бандит?",
                                 "Меня сегодня одолела бессоннеца, всю ночь размышлял о тебе, игрок номер {}," +
                                 "\n" + " бандит это ты! я уверен!",
                                 "Не слушайте игрока номер {}! он бандит!"]
        self.dialogue_trigger2 = ["Игрок номер [] мирный, думаю ему можно доверять," +
                                  "за игроком номер {} стоит понаблюдать...", "Думаю игрок номер [] мирный," +
                                  " но про игрока номер {} готов заявить обратное", "Игрока номер [] не трогать!" +
                                  "Сейчас убираем игрока номер {}.", "Я поддерживаю игрока номер []." +
                                  "Думаю игрок номер {} бандит."]

    def dead(self):
        self.life = False
        return self.role

    def message(self, dead_list, mode=1):
        if mode == 1:
            victim = random.choice(range(1, 11))
            char_dial = random.choice(self.dialogue_trigger)
            if self.role == 0:
                while self.trigger == victim or victim == self.num or victim in dead_list:
                    victim = random.choice(range(1, 11))
                self.trigger = victim
                char_dial = char_dial.replace("{}", str(self.trigger))
            if self.role == 1:
                while self.trigger == victim or victim in self.bandits or victim in dead_list:
                    victim = random.choice(range(1, 11))
                self.trigger = victim
                char_dial = char_dial.replace("{}", str(self.trigger))
            con = sqlite3.connect("DetectivBD.db")
            cur = con.cursor()
            temporary_variable = """INSERT INTO character(id, victim,  role)
             VALUES({}, {}, {})""".format(self.num, str(victim), self.role)
            result = cur.execute(temporary_variable).fetchall()
            con.commit()
            con.close()
            return str(self.num) + ": " + char_dial
        elif mode == 2:
            self.friend = "-1"
            con = sqlite3.connect("DetectivBD.db")
            cur = con.cursor()
            result2 = None
            if str(cur.execute("""select attack from character
                         where id = {}""".format(self.num)).fetchall()[0][0]) != "None":
                temporary_variable = """SELECT * FROM character
                            WHERE id = {}""".format(random.choice(str(cur.execute("""select attack from character
                            where id = {}""".format(self.num)).fetchall()[0][0]).split()))
                result = cur.execute(temporary_variable).fetchall()
                result2 = result[0][2]
            if str(result2) != "None":
                temporary_variable = random.choice(str(result2).split())
            else:
                temporary_variable = "-1"
            con.close()
            self.friend = temporary_variable
            if self.friend == "-1" or int(self.friend) in dead_list or self.friend == str(self.num):
                victim = random.choice(range(1, 11))
                char_dial = random.choice(self.dialogue_trigger)
                if self.role == 0:
                    while self.trigger == victim or victim == self.num or victim in dead_list:
                        victim = random.choice(range(1, 11))
                    self.trigger = victim
                    char_dial = char_dial.replace("{}", str(self.trigger))
                elif self.role == 1:
                    while self.trigger == victim or victim in self.bandits or victim in dead_list:
                        victim = random.choice(range(1, 11))
                    self.trigger = victim
                    char_dial = char_dial.replace("{}", str(self.trigger))
                con = sqlite3.connect("DetectivBD.db")
                cur = con.cursor()
                temporary_variable = """ UPDATE character SET victim = "{}"
                 WHERE id = {}""".format(str(victim), self.num)
                result = cur.execute(temporary_variable).fetchall()
                con.commit()
                con.close()
                return str(self.num) + ": " + char_dial
            else:

                victim = random.choice(range(1, 11))
                char_dial = random.choice(self.dialogue_trigger2)
                if self.role == 0:
                    while self.trigger == victim or victim == self.num or victim in dead_list or\
                            str(victim) == self.friend:
                        victim = random.choice(range(1, 11))
                    self.trigger = victim
                    char_dial = char_dial.replace("{}", str(self.trigger))
                    char_dial = char_dial.replace("[]", str(self.friend))
                elif self.role == 1:
                    while self.trigger == victim or victim in self.bandits or victim in dead_list \
                            or str(victim) == self.friend:
                        victim = random.choice(range(1, 11))
                    self.trigger = victim
                    char_dial = char_dial.replace("{}", str(self.trigger))
                    char_dial = char_dial.replace("[]", str(self.friend))
                con = sqlite3.connect("DetectivBD.db")
                cur = con.cursor()
                temporary_variable = """ UPDATE character SET victim = "{}"
                                 WHERE id = {}""".format(str(victim), self.num)
                result = cur.execute(temporary_variable).fetchall()
                con.commit()
                con.close()
                if self.friend == str(victim):
                    char_dial = random.choice(self.dialogue_trigger)
                    char_dial = char_dial.replace("{}", str(victim))
                return str(self.num) + ": " + char_dial

    def checked(self):
        return self.role

    def night(self, dead_list):
        victim = random.choice(range(1, 11))
        while victim in self.bandits or victim in dead_list:
            victim = random.choice(range(1, 11))
        return victim

    def life_check(self):
        return self.life

