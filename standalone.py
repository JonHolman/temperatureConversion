from temperature import Temperature

questionTemp = input('Input temperature:')
questionUnit = input('Input unit of measure:').lower()
answerUnit = input('Target unit of measure:').lower()
answerTemp = input('Student\'s response:')

correctAnswer = Temperature(questionTemp, questionUnit)
print ( correctAnswer.compareTo(answerTemp,answerUnit) )

