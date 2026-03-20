'''
with open("quiz.txt", 'w') as f:
  f.write("What is the capital of France?\n")
  f.write("Paris")
  f.close()


with open("quiz.txt", 'r'=) as f:
  content = f.read()
  print(content)
'''


def write_txt_file(questions):
  with open("quiz.txt", 'a') as f:
    for q in questions:
      f.write(f"{q}\n")
      #f.close()


def read_txt_file():
  with open("quiz.txt", 'r') as f:
    content = f.read().splitlines()
    return content


def add_question():
  while True:
    question = input("Enter the question (or type 'done' to finish): ")
    if question.lower() == 'done':
      break
    answer = input("Enter the answer: ")
    write_txt_file((question, answer))


print("**Add questions to the quiz**")
add_question()

# Reading and displaying the content of the quiz file
print("=====Quiz======")


def take_quiz(data):
  score = 0
  for i in range(0, len(data), 2):
    question = data[i]
    answer = data[i + 1]
    print(question)
    user_answer = str(input("Answer:"))
    if user_answer.lower() == answer.lower():
      score += 1
      print("Correct! \n")
    else:
      print(f"Incorrect! The correct answer is: {answer} \n")

  print(f"You scored {score} out of {len(data)/2}")


take_quiz(read_txt_file())
