from players import Player


player1 = Player()
player1.setName("jose alvarado")
player1.setDesc("short, stocky and mean")
character_sheet = """
    Name: {0!s}
    Desc: {1!s}
""".format(player1.getName(), player1.getDesc())
print(character_sheet)

