import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(HANGMANPICS[0])

words=["egypt","ahley","monster", "stars","space"]
random_word=random.choice(words)
#عرض مسافات بنفس عدد حروف الكلمة 

desplay=[]
desplay=["_"]*len(random_word)
print(' '.join(desplay))
lives=6
#قائمة تحتوي الحروف اللي اتخمنت
guessed_latters=[]

while "_" in desplay and lives>0:
    user_guess=input("pls guess a latter=").lower()

#هل الحرف تم تخمينه
    if user_guess in guessed_latters:
        print("you already guessed this latter")
        print("you have ",lives,"lives")

        continue
#في حالة لم يسبق تخمين الحرف
    guessed_latters.append(user_guess)  


    if user_guess not in random_word:
         lives-=1
         print(HANGMANPICS[6-lives])
    else:
     for position in range(len(random_word)):
       if random_word[position]==user_guess:
          desplay[position]=user_guess
    print(' '.join(desplay))
    print("you have ",lives,"lives")

if lives ==0:
   print("""
you loseee

""")    
   print(HANGMANPICS[-1])
else:
   print("""

**********
YOU WINNN
**********         


""")   