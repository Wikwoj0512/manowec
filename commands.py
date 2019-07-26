def finduser(members, username):
    for mem in members:
        if mem.name.lower()==username.lower():
            return mem
    return None

def finduserbyid(members, id):
    return discord.utils.get(members, id=id)


def findtext(channels,name):
    for chan in channels:
        if chan.name.lower()==name.lower():
            return chan
    return None

def findrole(roles, nam):
    for rol in roles:
        if rol.name.lower()==nam.lower():
            return rol
    return None

def findcategory(cats, name):
    for cat in cats:
        if cat.name.lower()==name.lower():
            return cat
    return None

async def verify(message):
    try:
        mes=message.content
        guild =message.guild
        mentions=message.mentions
        type = mes[-1]
        if not type in "mko":
            await message.channel.send("Użyłeś tej komendy niepoprawnie. Poproś o pomoc innych adminów")
            return False
        guild = message.channel.guild
        if len(mentions)!=1:
            await message.channel.send("Użyłeś tej komendy niepoprawniel. Poproś o pomoc innych adminów")
            return False
        user=mentions[0]
        if not user:
            return
        roles=user.roles
        try:
            roles.remove(findrole(guild.roles,"niezweryfikowany/a"))
        except:
            pass
        basicroles=[findrole(guild.roles,"zweryfikowany")]
        for i in basicroles:
            roles.append(i)
        dict={"m": findrole(guild.roles,"typ"),"k":findrole(guild.roles,"typiara"),"o":findrole(guild.roles,"obojnak")}
        roles.append(dict[type])
        roles.remove(findrole(guild.roles, "@everyone"))
        # for i in roles:
        #     await user.add_roles(i)
        await user.edit(roles=roles)
        channel=message.channel
        await channel.send('Użytkownik pomyślnie dostał swoje role')
    except Exception as e:
        channel=message.channel
        print(e)
        await channel.send('Niestety nie udało się przydzielić ról')
