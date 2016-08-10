import math
import random

n = 239255299284384349304725149856552492038598445886956658797340414572081315025316855599003056773010145489861807217942474066769254994889937350554812114599199747011822931003470188469755565575428252755498450043694308433269873821720504733262583005940196298951811543171416951549542705533417999736765774452030314635913103516225119401185982005668156650192848448135779911780427770251154346413709247810959979685820122190878080140819951259653464493002404315741219936122712441337048287859676453307655235582246940129654549936418104588280142515645148689690033053995534499764950491215574658031050257809925263610106291
e = 51831672085074814178680269722598016921936838558306727005991561731670505910386509866184899294113023750765710594543251856658239666016521056714215727353889825219309912019100396570607753922542886645209401533085461587994461683838141339926725638136349726690307472237142348752101995510115124409635193574780938087738364459858781987481597603026016849697794677


def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def Coprime(a, b):
	if math.gcd(a,b) == 1:
		return True
	else:
		return False


def keyGen(p, q):
	myN = p*q
	phi = (p-1)*(q-1)
	print("My phi: " + '\n' + ascii(phi))

	myE = 0
	while (not Coprime(phi, myE)):
		myE = random.randrange(70001, phi)
	return myE


def convertStringtoInt(string):
	stringList = []
	for c in string:
		# Adds leading zeroes if they're missing.
		if (ord(c)<100):
			stringList.append("0"+str(ord(c)))
		else:
			stringList.append(str(ord(c)))
	result = int(''.join(stringList))
	return result


def convertInttoString(integer):
	tempstr = str(integer)
	#while (len(tempstr)%3!=0):
	#	tempstr = "0" + tempstr

	# TODO Finish conversion
	templist = [tempstr[i:i+3] for i in range(0, len(tempstr), 3)]
	print(templist)
	result = [chr(int(templist[i])) for i in range(0, len(templist))]
	fresult = ''.join(result)
	return fresult



if __name__ == '__main__':

	# Encrypting with Martin's Key. 
	print("RSA Encrypter")
	message = input("Please enter your message\n")
	message = convertStringtoInt(message)
	#Message conversion is correct

	ciphertext = pow(message, e, n)
	print(ciphertext)

	# KeyGen
	print("RSA KeyGen algorithm....")
	p = 203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123
	q = 250556952327646214427246777488032351712139094643988394726193347352092526616305469220133287929222242315761834129196430398011844978805263868522770723615504744438638381670321613949280530254014602887707960375752016807510602846590492724216092721283154099469988532068424757856392563537802339735359978831013

	myE = keyGen(p, q)
	myN = p*q
	myD = findModInverse(myE, (p-1)*(q-1))
	print("My n:\n" + ascii(myN) + '\n' + "my e:\n" + ascii(myE) + '\n')
	print("My d: " + '\n' + ascii(myD))

	print("RSA Decrypter")
	encryptedMessage = input("Please enter the message you wish to decrypt\n")
	encryptedMessage = convertStringtoInt(encryptedMessage)
	decryptedMessage = pow(encryptedMessage, myD, myN)
	decryptedMessage = convertInttoString(decryptedMessage)
	# TODO something wrong
	# print(decryptedMessage)


	# This part is Tests the code. Seems to work correctly w/ 12
	"""
	OGmessageTest = 12
	encryptedMessageTest = pow(OGmessageTest, myE, myN)
	print("my encryptedMessageTest: " + '\n' + str(encryptedMessageTest))
	decryptedMessageTest = pow(encryptedMessageTest, myD, myN)
	# TODO Something wrong
	print("my decryptedMessageTest: " + '\n' + ascii(decryptedMessageTest))
	"""