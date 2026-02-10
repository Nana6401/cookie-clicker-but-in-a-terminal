print("THIS GAME IS STILL INCOMPLETE A SAVE SYSTEM IS TO COME WHEN I WANT TO SO RN THIS GAME HAS NO SAVE SYSTEM YOU HAVE BEEN WARNED (don't come crying why is my save gone please)")

cookies = 0
addcookies = 1
morecookies = 0
morecookiescost = 10
automaticcookiebaker = 0
automaticcookiebakercost = 50
farmer = 0
farmercost = 150
factories = 0
factoriescost = 500
cforcookies = 0
cforcookiescost = 1000
cforcookiesbought = 0

while True:
  command = input("> ")

  if command == "help":
    print("commands :\ncookies : show you your cookies\ncookie : make cookies\nupgrades : show upgrades\nqolupgrades : show qol upgrades\nupgrade : upgrade a upgrade or a qol upgrade\nquit : quit the game\nhelp : why are you reading what the help command does\ncredits : show you the credits")

  if command == "cookie":
    cookies = cookies + addcookies

  if command == "c":
    if cforcookiesbought = 1:
      cookies = cookies + addcookies

  if command == "cookies":
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
    "\ndecription : its a farmer that is farming with faming tools and he like farming with farming tools"
    "\nfactories:", factories
    "\ncost:",factoriescost
    "\ndescription : a factory okay idk what to put here"
)

  if command == "qolupgrades":
    print(
      "cforcookies :", cforcookiesbought
      "\ncost:", cforcookiescost
      "\ndescription : input c for cookies"
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
      factories = factories
      addcookies = addcookies + 25
      cookies = cookies - factoriescost
      factoriescost = factoriescost + 200

  if command == "upgrade cforcookies":
    if cookies >= cforcookiescost:
      if cforcookiesbought = 0
        cookies = cookies - cforcookiescost
        cforcookiesbought = cforcookiesbought + 1
      else print("cforcookies already bought")
    else print("not enough cookies")

#welcome to my spaghetti code :DDD
#i welcome any modifications to the code or mods of the code #aslong as you credit me for my spaghetti code
#also please be nice to the code or else it wont be **pastable** LOLOLOLOLOLOLOLOL defenetly didnt use chatgpt for that joke
#btw i wrote all of the code only little chatgpt was used to direct me with how to do some things otherwise it all written by me
