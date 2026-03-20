import random 
print("Welcome to word jumble game!")
word='racecar'
jumbled_word=""
n=len(word)
used_indices = []
while len(used_indices) < n:
    index = random.randint(0, n-1)
    if index not in used_indices:
        jumbled_word += word[index]
        used_indices.append(index)
      
print("Here's the word you need to guess--> ",jumbled_word)