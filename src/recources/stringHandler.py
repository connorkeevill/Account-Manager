# CK

# | encrypt()
# |----------------------------------------------------------------------
# | Returns an encrypted version of the plaintext string that has been
# | encrypted with the keyword parameter using the Vigenère cipher.
# | ----------------------------------------------------------
def encrypt(plainText, keyword):
	plainTextNums = getNumericalValues(plainText)
	keywordNums = getNumericalValues(keyword)
	newNums = []

	for letter in range(len(plainTextNums)):
		plainTextLet = plainTextNums[letter]
		keywordLet = keywordNums[letter % len(keyword)]

		newLet = plainTextLet + keywordLet
		newLet = putInRange(newLet)

		newNums.append(newLet)

	newString = getAlphabeticValues(newNums)
	encrypted = ''.join(newString)
	return encrypted


# | decrypt()
# |---------------------------------------------------------------------
# | Returns the decrypted version of the encrypted string passed as a
# | parameter, assuming the correct keyword is provided, otherwise
# | the output won't be what the user expected. The string also
# | only works if it was encrypted with the Vigenère cipher.
# |-----------------------------------------------------
def decrypt(encrypted, keyword):
	encryptedNums = getNumericalValues(encrypted)
	keywordNums = getNumericalValues(keyword)
	newNums = []

	for letter in range(len(encryptedNums)):
		encryptedLet = encryptedNums[letter]
		keywordLet = keywordNums[letter % len(keyword)]

		newLet = encryptedLet - keywordLet
		newLet = putInRange(newLet)

		newNums.append(newLet)

	newString = getAlphabeticValues(newNums)
	decrypted = ''.join(newString)
	return decrypted


# | getNumericalValues()
# |-----------------------------------------------------------------------------------------------
# | Returns a list of integers representing the string passed as the argument. The integers are
# | between 1 and 94, so they are easier to loop around if they become too high or too low.
# |------------------------------------------------------------------------------------
def getNumericalValues(string):
	numericalValues = []
	for letter in string:
		numLetter = ord(letter)
		numLetter -= 32
		numericalValues.append(numLetter)

	return numericalValues


# | getAlphabeticValues()
# |---------------------------------------------------------------------
# | Returns a list of characters that the list passed as argument was
# | representing. Each number in the list is converted back into
# | its ASCII value so it will be a recognisable character.
# |---------------------------------------------------
def getAlphabeticValues(list):
	alphabeticValues = []
	for number in list:
		number += 32
		letter = chr(number)
		alphabeticValues.append(letter)

	return alphabeticValues


# | putInRange()
# |------------------------------------------------------------------------------------
# | Puts the inputted number in the range of 1-94. The number is kept 'proportional'
# | to what is was before, allowing the number to be looped. e.g, 97 will become
# | 3, and -5 will become 89. The way this method does this is less efficient
# | than performing a modulo 94 on the number, however that won't work on
# | any negative numbers, so a while loop gets used for this instead.
# |------------------------------------------------------------
def putInRange(number):
	while number < 1:
		number += 94
	while number > 94:
		number -= 94

	return number
