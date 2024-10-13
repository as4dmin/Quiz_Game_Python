import requests
import json
import pprint
import random
import html

url ="https://opentdb.com/api.php?amount=1"

endGame = ""
while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = "Sorry! There is a problem retriving the question. Press enter to try again or type 'quit' to quit"
    else :
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "- " + html.unescape(answer))
            answer_number +=  1
        
        user_answer = input("\nType the correct answer : ")

        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongratulation! You answered correctly")
        else:
            print("\nSorry " + user_answer + " is incorrect. The correct answer is " + correct_answer)
        
        endGame = input("\nPress 'enter' to play again or type 'quit' to exit the game\n")
