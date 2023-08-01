def intro_scene():
  """Prints the introduction to the game."""
  print("You are standing in a dark forest.")
  print("You can hear the sound of wolves howling in the distance.")
  print("What do you do?")

def look_around():
  """Prints a description of the surroundings."""
  print("You look around and see a path leading north and south.")
  print("There is also a cave to the east.")

def go_north():
  """Prints a message saying that the player has gone north."""
  print("You go north and find yourself in a clearing.")

def go_south():
  """Prints a message saying that the player has gone south."""
  print("You go south and find yourself in a swamp.")

def go_east():
  """Prints a message saying that the player has gone east and entered the cave."""
  print("You go east and enter the cave.")
  print("You are in a dark cave.")
  print("You can hear the sound of dripping water.")
  print("What do you do?")

def main():
  """The main function of the game."""
  intro_scene()
  while True:
    action = input(">>> ")
    if action == "look around":
      look_around()
    elif action == "go north":
      go_north()
    elif action == "go south":
      go_south()
    elif action == "go east":
      go_east()
    else:
      print("I don't understand what you mean.")

if __name__ == "__main__":
  main()
