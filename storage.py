greetings = ['Hey there ', 'Greetings ', 'Bonjour ', 
             'Hola ', 'Guten tag ', 'Salam ', 
             'Konnichiwa ', 'Salve ', 'Namaste ', 
             'Marhaba ', 'Privet, ', 'Xin chào ', 
             'Namaskar ', 'Ciao ', 'Barev ', 'Habari ']

commands = "%hello: I greet you \n\n %motivation: I give you some motivation (don't expect much I'm a bot) \n\n %jokes: Use this to listen to a joke! \n\n %days_since: Return the number of days that have passed since YY/MM/DD \n\n %XXX: Returns how many XXX 1 CAD is currently worth, where XXX is a currency in forex format (if that's even a thing) \n\n solar/lunar_eclipse : Returns the date the next solar/lunar eclipse will happen! \n\n "

reactions_dict = {}

def reaction_adder(link: str) -> None:
  if reactions_dict == {}:
    reactions_dict[0] = link
  else:
    if link not in reactions_dict.values:
      length = len(reactions_dict)
      reactions_dict[length] = link
