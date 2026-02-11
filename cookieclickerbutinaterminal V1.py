print("hi to save please create a save.txt file in the same folder that theres the game in also please use the load command to load your save everytime . AND DONT FORGET TO USE THE SAVE COMMAND")

cookies = 0
addcookies = 1
amplificatoring = 1
morecookies = 0
morecookiescost = 10
automaticcookiebaker = 0
automaticcookiebakercost = 50
farmer = 0
farmercost = 150
factories = 0
factoriescost = 500
evilautomaticcookiebaker = 0
evilautomaticcookiebakercost = 2500
extremecookiefarm = 0
extremecookiefarmcost = 5000
magiccookieproducer = 0
magiccookieproducercost = 10000
cforcookiescost = 1000
cforcookiesbought = 0
cookieascicost = 100
cookieascibought = 0
hyperactivity = 0
hyperactivitycost = 1500
hyperactivitybought = 0

while True:
  command = input("> ")

  if command == "save":
        open("save.txt","w").write("\n".join(
            f"{k}={v}" for k,v in globals().items()
            if isinstance(v,int) and k != "command"
        ))
        print("saved")

  if command == "load":
    try:
        with open("save.txt","r") as f:
            for line in f:
                name, val = line.strip().split("=")
                globals()[name] = int(val)
        print("loaded")
    except FileNotFoundError:
        print("where is the save file")

  if command == "help":
    print("commands :\ncookies : show you your cookies\ncookie : make cookies\nupgrades : show upgrades\nqolupgrades : show qol upgrades\nupgrade : upgrade a upgrade or a qol upgrade\namplificators : shows amplificators\namplificate : amplificate a amplificator\nquit : quit the game\nhelp : why are you reading what the help command does\ncredits : show you the credits\nsave : save the game\nload : loads the save")

  if command == "cookie":
    cookies = cookies + addcookies * amplificatoring

  if command == "c":
    if cforcookiesbought == 1:
      cookies = cookies + addcookies * amplificatoring

  if command == "cookies":
     if cookieascibought == 1:
       print(
"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⡿⠿⠷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀"
"\n⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣇⠀⠀⢸⣿⣿⣿⣦⡀⠀⠀⠀⠀"
"\n⠀⠀⠀⠀⢀⣴⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀"
"\n⠀⠀⠀⢠⣿⡟⠁⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀"
"\n⠀⠀⢠⣿⣿⣿⣦⣄⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣷⠀"
"\n⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢹⣿⣿⣿⡇"
"\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿"
"\n⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟"
"\n⠀⠀⠈⢿⣿⣿⣿⣿⠟⠻⣿⣿⠋⠀⠉⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢙⣿⠃"
"\n⠀⠀⠀⠈⢿⣿⣿⠁⠀⠀⠘⣿⣆⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀"
"\n⠀⠀⠀⠀⠀⠙⢿⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀ "
"\n⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⢹⣿⣿⡿⠟⠁⠀  "
"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⣿⣿⣿⣷⡤⠾⠛⠉⠀⠀⠀⠀⠀ "
,cookies)
     else:
       print(cookies)
  if command == "quit":
    quit()

  if command == "upgrades":
    print(
    "morecookies:", morecookies,
    "\ncost:", morecookiescost,
    "\ndecription : make more cookies"
    "\nautomaticcookiebaker:", automaticcookiebaker,
    "\ndecription : despite its name it dosent make cookies automatically :("
    "\ncost:", automaticcookiebakercost,
    "\nfarmer:", farmer,
    "\ncost:", farmercost,
    "\ndescription : its a farmer that is farming with faming tools and he like farming with farming tools"
    "\nfactories:", factories,
    "\ncost:", factoriescost,
    "\ndescription : a factory okay idk what to put here"
    "\nevilautomaticcookiebaker :", evilautomaticcookiebaker,
    "\ncost:", evilautomaticcookiebakercost,
    "\ndescription : its a evilautomaticcookiebaker and still dosent make cookies automatically"
    "\nextremecookiefarm:", extremecookiefarm,
    "\ncost:", extremecookiefarmcost,
    "\ndescription : its a cookie farm but EXTREME !!!!!!!"
    "\nmagiccookieproducer:", magiccookieproducer,
    "\ncost:", magiccookieproducercost,
    "\ndescription : not really sure of its origin but it produces cookies !"
)

  if command == "qolupgrades":
    print(
      "cforcookies :", cforcookiesbought,
      "\ncost:", cforcookiescost,
      "\ndescription : input c for cookies"
      "\ncookieasci :", cookieasci,
      "\ncost :", cookieascicost,
      "\ndescription : it makes a cookie asci when you look at your cookies"
)

  if command == "amplificators":
    print(
      "hyperactivity :", hyperactivitybought,
      "\ncost:", hyperactivitycost,
      "description : hyper activates your upgrades"
)

  if command == "credits":
    print("everything : Nana6401")

  if command == "upgrade morecookies":
    if cookies >= morecookiescost:
      morecookies = morecookies + 1
      cookies = cookies - (morecookiescost)
      morecookiescost = morecookiescost + 5
      addcookies = addcookies + 1
      print("bought morecookies")
    else:
      print("not enough cookies")

  if command == "upgrade automaticcookiebaker":
    if cookies >= automaticcookiebakercost:
      automaticcookiebaker = automaticcookiebaker + 1
      addcookies = addcookies + 5
      cookies = cookies - (automaticcookiebakercost)
      automaticcookiebakercost = automaticcookiebakercost + 10
      print("bought automaticcookiebaker")
    else:
      print("not enough cookies")

  if command == "upgrade farmer":
    if cookies >= farmercost:
      farmer = farmer + 1
      addcookies = addcookies + 10
      cookies = cookies - farmercost
      farmercost = farmercost + 50
      print("bought farmer")
    else:
      print("not enough cookies")

  if command == "upgrade factories":
    if cookies >= factoriescost:
      factories = factories + 1
      addcookies = addcookies + 25
      cookies = cookies - factoriescost
      factoriescost = factoriescost + 200
      print("bought factories")
    else:
      print("not enough cookies")

  if command == "upgrade evilautomaticcookiebaker":
    if cookies >= evilautomaticcookiebakercost:
      evilautomaticcookiebaker = evilautomaticcookiebaker + 1
      addcookies = addcookies + 100
      cookies = cookies - evilautomaticcookiebakercost
      evilautomaticcookiebakercost = evilautomaticcookiebakercost + 500
      print("bought evilautomaticcookiebaker")
    else:
      print("not enough cookies")

  if command == "upgrade extremecookiefarm":
    if cookies >= extremecookiefarmcost:
      extremecookiefarm = extremecookiefarm + 1
      addcookies + 300
      cookies = cookies - extremecookiefarmcost
      extremecookiefarmcost = extremecookiefarmcost + 1500
      print("bought extremecookiefarm")
    else:
      print("not enough cookies")

  if command == "upgrade magiccookieproducer":
    if cookies >= magiccookieproducercost:
      magiccookieproducer = magiccookieproducer + 1
      addcookies = addcookies + 500
      cookies = cookies - magiccookieproducercost
      magiccookieproducercost = magiccookieproducercost + 2500
      print("bought magiccookieproducer")
    else:
      print("not enough cookies")

  if command == "upgrade cforcookies":
    if cookies >= cforcookiescost:
      if cforcookiesbought == 0:
        cookies = cookies - cforcookiescost
        cforcookiesbought = cforcookiesbought + 1
        print("bought cforcookies")
      else:
        print("cforcookies already bought")
    else:
      print("not enough cookies")

  if command == "upgrade cookieasci":
    if cookies >= cookieascicost:
      if cookieascibought == 0:
        cookies = cookies - cookieascicost
        cookieascibought = cookieascibought + 1
        print("bought cookieasci")
      else:
        print("already have cookieasci")
    else:
      print("not enough cookies")

  if command == "amplificate hyperactivity":
    if cookies >= hyperactivitycost:
      if hyperactivitybought == 0:
        cookies = cookies - hyperactivitycost
        hyperactivitybought = hyperactivitybought + 1
        amplificatoring = amplificatoring + 0.25
        print("amplificated hyperactivity")
      else:
        print("hyperactivity already bought")
    else:
      print("not enought cookies")

#welcome to my spaghetti code :DDD
#i welcome any modifications to the code or mods of the code #aslong as you credit me for my spaghetti code
#also please be nice to the code or else it wont be **pastable** LOLOLOLOLOLOLOLOL defenetly didnt use chatgpt for that joke
#btw i wrote all of the code only little chatgpt was used to direct me with how to do some things otherwise it all written by me ... but
#i do have to admit defeat for the save system i did use chat gpt for that one and im sad because of it :((((( otherwise everything else is written by me
#also why am i writing this almost no one is gonna see this like why am i still writing its like i don't need to write but i still write so it writes and writes
