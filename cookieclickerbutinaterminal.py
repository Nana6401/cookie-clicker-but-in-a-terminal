import time

print("THIS GAME IS STILL INCOMPLETE A SAVE SYSTEM IS TO COME WHEN I WANT TO SO RN THIS GAME HAS NO SAVE SYSTEM YOU HAVE BEEN WARNED (don't come crying why is my save gone please)")

cookies = 0
addcookies = 1
morecookies = 0
morecookiescost = 10
automaticcookiebaker = 0
automaticcookiebakercost = 50

while True:
  command = input("> ")

  if command == "help":
    print("commands :\ncookies : show you your cookies\ncookie : make cookies\nupgrades : show upgrades\nupgrade : upgrade a upgrade\nquit : quit the game\nhelp : why are you reading what the help command does")

  if command == "cookie":
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
    "\ncost:", automaticcookiebakercost
)

  if command == "upgrade morecookies":
    morecookies = morecookies + 1
    cookies = cookies - (morecookiescost)
    morecookiescost = morecookiescost + 5
    addcookies = addcookies + 1
    print("bought morecookies")

  if command == "upgrade automaticcookiebaker":
    automaticcookiebaker = automaticcookiebaker + 1
    addcookies = addcookies + 5
    cookies = cookies - (automaticcookiebakercost)
    automaticcookiebakercost = automaticcookiebakercost + 10
    print("bought automaticcookiebaker")
