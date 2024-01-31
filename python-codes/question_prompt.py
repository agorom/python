from Question import Question

question_prompt = [
	"What colour are Apples? \n(a) red/green \n(b) purple \n (c)blue\n\n",
	"What colour are Bananas? \n(a) tean \n(b) magenta (c)yellow\n\n",
	"What colour are Strawberry? \n(a) yellow \n(b) red \n(c) blue\n\n"
]

questions = [
	Question(question_prompt[0], "a"),
	Question(question_prompt[1], "c"),
	Question(question_prompt[2], "b")
]



def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)

		if answer == question.answer:
			score += 1

	print(f"You got {score} / {len(questions)} correct")

run_test(questions)

	#return score




