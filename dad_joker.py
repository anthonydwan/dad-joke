import requests
import random
import pyfiglet
import time
import sys

def slow_text(slow_text):
    for char in slow_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')

url =  'https://icanhazdadjoke.com/search'

yesy = ["yes", "y"]
noy = ["no", "n"]

title = pyfiglet.figlet_format("DAD JOKE MACHINE!")
print(title)
slow_text("Welcome to Dad Joke Machine.")
slow_text("You just have to type a topic out,")
slow_text("and I'll give you a silly joke!")

def retry():
  slow_text('You do want to try again? Enter [Y]/[N]')
  again = input()
  if again.lower() in yesy:
    dad_joker()
  elif again in noy:
    slow_text('Cya!')
  else:
    slow_text('Wrong input!')
    retry()

def dad_joker():
  """a function for fetching dad joke"""

  slow_text("\nGimme a topic: ")
  user_input = input()

  response = requests.get(url, headers={'Accept':'Application/json'}, params={"term": user_input}).json()

  results = response['results']
  total_jokes = response['total_jokes']

  def rejoke():
    slow_text("do you want another? Enter [Y]/[N]")
    joke2 = input().lower()
    if joke2 == yesy:
      slow_text(f"on '{user_input}' again? Enter [Y]/[N]")
      cont = input().lower()
      if cont in yesy:
        slow_text(results[random.randrange(0,total_jokes)]['joke'])
        rejoke()
      elif cont in noy:
        dad_joker()
      else:
        slow_text("Wrong input!")
        rejoke()
    elif joke2 in noy:
      slow_text('Cya!')
    else:
      slow_text('Wrong input!')
      rejoke()


  if total_jokes==0:
    slow_text(f"There's nothing on the topic '{user_input}'!")
    retry()

  elif total_jokes==1:
    slow_text(f"There's one joke on the topic '{user_input}'. Let me tell you:")
    slow_text(results[0]['joke'])

  else:
    slow_text(f"There are {total_jokes} jokes on the topic '{user_input}'. Let me pick a good one for you:")
    slow_text(results[random.randrange(0,total_jokes)]['joke'])
    rejoke()


dad_joker()
