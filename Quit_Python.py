import requests
import json
import pprint
import random
import html

url ="https://opentdb.com/api.php?amount=1"

endGame = ""
score_correct = 0
score_incorrect = 0

while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = "Sorry! There is a problem retriving the question. Press enter to try again or type 'quit' to quit"
    else :
        valid_answer = False
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
        
        while valid_answer == False:
            user_answer = input("\nType the correct answer : ")
            try:
                user_answer = int(user_answer)
                if( user_answer > len(answers) or user_answer <= 0):
                    print("Invalid answer.")
                else:
                    valid_answer = True

            except:
                print("Invalid answer. Use only numbers.")


        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongratulation! You answered correctly")
            score_correct += 1
        else:
            print("\nSorry " + user_answer + " is incorrect. The correct answer is " + correct_answer)
            score_incorrect += 1

        print("\n#####################")
        print("Your score is: ")
        print("Correct answer : "+ str(score_correct))
        print("Inorrect answer: " + str(score_incorrect))
        print("#####################")

        endGame = input("\nPress 'enter' to play again or type 'quit' to exit the game\n").lower()

print("\nThanks for playing")
