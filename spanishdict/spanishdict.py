import sys
import requests
import json
import pyperclip
import crayons

print("Spanishdict Autosolver - {}".format(crayons.white("Pepsipu / Sommy Hoshmeed", bold=True)))
try:
	quiz = requests.get(sys.argv[1])
	print(crayons.green("Connection to {} is a go!".format(sys.argv[1]), bold=True))
except:
	print(crayons.red("Connection to {} is a failure!".format(sys.argv[1]), bold=True))
answers = json.loads(quiz.text.partition("window.SD_QUIZ_DATA = ")[2].partition("</script>")[0])
while True:
	print("Input question:")
	question = str(input())
	found = False
	for x in range(len(answers["questions"])):
		if question in answers["questions"][x]["body"]:
			print("Possible answer in attempt [{}] - '{}'. Copied to clipboard.".format(crayons.yellow(x), crayons.blue(answers["questions"][x]["correctAnswer"], bold=True)))
			pyperclip.copy(answers["questions"][x]["correctAnswer"])
			found = True
	if found == False:
		print(crayons.red("No answer found! Maybe remove some letters?", bold=True))