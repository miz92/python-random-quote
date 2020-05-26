import random
last = len(quotes)-1
rand = random.randint(0,last)
def bab():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rand])

if __name__== "__main__":
  bab()
