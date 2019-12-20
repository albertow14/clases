class Usuario:
    def __init__(self, nick, email):
        self.nick = nick
        self.email = email
        self.soul_mate = None

    def register_soul_mate(self, user_soul_mate):
        self.soul_mate = user_soul_mate.nick
        user_soul_mate.soul_mate = self.nick

        

blanca = Usuario('blanca_1982', 'blanca_1982@gmail.com')
alberto = Usuario('Alberto', 'al@gm.com')

# blanca envía petición
# if alberto says yes:

alberto.soul_mate = blanca.nick
blanca.soul_mate = alberto.nick

alberto.register_soul_mate(blanca)

        