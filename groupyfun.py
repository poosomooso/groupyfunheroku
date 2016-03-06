import groupy

groups = groupy.Group.list()
print(groups)
bots = groupy.Bot.list()[0]
print(bots)
bots.post('snails are a lie')