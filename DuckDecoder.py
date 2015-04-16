############## DuckDecoder ##############
#  
#  Description:   Python script to decode/ display usb rubber ducky inject.bin files
#    Author(s):   JPaulMora (@jpaulmora)
#      Version:   0.1.b
#
#   Program currently supports all characters on an english keyboard mapping, I have been getting trouble identifying key
#   combinations such as ALT ENTER U since its output in hex is the same as of a STRING u command. This also happens with
#   UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW. they get translated to (STRING) u,d,l,r respectively.


import binascii 
import os
import sys

args = sys.argv                # Returns a list of all arguments, including fine name of the program (this file)

def hexstr(fn):                # This function makes use of binascii to read file in hex mode
	with open(fn, 'rb') as f:
    		content = f.read()
	Payload = (binascii.hexlify(content))
	return Payload

def dsem(h, n):               # Here we take the hex bitstream and make a list of it in chunks specified by n ie. list = [1234] n=2 return = [12,34]
    n = max(1, n)
    return [h[i:i + n] for i in range(0, len(h), n)]
	
	
  # Duck code needs two things to know what letter is sending, the first two characters specify the letter and the other two tell if there is a "modifier"
  # key, so 00 means unmodified, 01 is control key, 02 is Caps, 04 is alt key and 08 is the "Windows" or "Command" key.
	

	
def letiscover(letters,type,mode):      # Function takes all the letter "C"odes on a list and all the letter "M"odes in another list.
										# The advantage of doing it like this is that when a character is sent, (lets say "a" which hex value is "0400")
										# we can divide the two chunks that make the letter so that it receives two lists like this:
										#		
										#		LettersList = [04]
										#		ModesList   = [00]       
										# 
										# Now we can tell the function to first, look for "04" in the list and get its position so we can later find
										# it in the list of **human** characters. after knowing what letter it is, we can now check wether it has been
										# modified or not (with the values of ModesList) so then we ask "is letter code Caps (02)?" since it is not, 
										# it will pass to the next question "is it normal?" since it is, then we tell it to print character on position
										# 0 of the list containing all the normal letters (list Letters in this case). 
										
										# As you may have guessed, for this to work the letter codes must be in the exact same order as the list of *human* letters,
										# this means that Hex value of letter "d" should be in the same place in the list of 'normal' letter "d"
										# That way if we find hex code of letter "x" (number 24) , we could call Letter[24] and expect it to be an "x" 
	
	Delay = 0
	String = 0
	Result = []
	
	# if lang == "en":           # languages will be supported adding lists on ifs, and default to english if variable not set.
	Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",",",".","/",";","'","[","]","\\","-","="," ","\n","1","2","3","4","5","6","7","8","9","0","BK_SPACE",'`',"TAB"]
	CapLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","<",">","?",":","\"","{","}","|","_","+","SPACE","ENTER","!","@","#","$","%","^","&","*","(",")","BK_SPACE",'~',"TAB"]
	AltLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",",",".","/",";","'","[","]","\\","-","=","SPACE\n","ENTER","1","2","3","4","5","6","7","8","9","0"]
	HexLetters = ['04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d','36', '37', '38', '33', '34', '2f', '30', '31', '2d', '2e', '2c', '28','1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27','2a','35','2b']
#	HexTypes = ['00', '01', '02', '04', '08']

	if mode == 1:                         # Mode 1 Converts the code and also adds all the "Commands" needed for re-encoding,
										  # output of this mode should be DuckEncoder ready. ie.
										  #
										  # DELAY 400
										  # STRING Hello World!
										  # ENTER
		for i in range(0,len(letters)):
		
			if letters[i] in HexLetters and type[i] == "00":
			
				if Delay != 0:
					Result.append("\nDELAY " + str(Delay) + "\n")
					
					# if the next character is a letter, and variable Delay is not 0,
					# it will print the value of Delay, which at this point is the total
					# delay the original user described in the code (see comments below).
			
				if String == 0 and str(Letters[HexLetters.index(letters[i])]) != "\n":
					Result.append("\nSTRING " )
					String = 1
				if str(Letters[HexLetters.index(letters[i])]) == "\n":
					Result.append("\nENTER " )
					String = 0
				if str(Letters[HexLetters.index(letters[i])]) == "BK_SPACE":
					Result.append("\nBACKSPACE " )
					String = 0
				if str(Letters[HexLetters.index(letters[i])]) == "TAB":
					Result.append("\nTAB " )
					String = 0
				else:
					Result.append(Letters[HexLetters.index(letters[i])])
				Delay = 0
			
			elif letters[i] in HexLetters and type[i] == "01":
				if Delay != 0:
					Result.append("\nDELAY " + str(Delay) + "\n")
				Result.append("\nCONTROL " + str(AltLetters[HexLetters.index(letters[i])]))
				Delay = 0
				String = 0
				
			elif letters[i] in HexLetters and type[i] == "02":
				if Delay != 0:
					Result.append("\nDELAY " + str(Delay) + "\n")
				
				if String == 0 and str(CapLetters[HexLetters.index(letters[i])]) != "\nENTER\n":
					Result.append("\nSTRING " )
					String = 1
				if str(CapLetters[HexLetters.index(letters[i])]) == "\nENTER\n":
					Result.append("\nENTER " )
					String = 0
				else:
					Result.append(CapLetters[HexLetters.index(letters[i])])
				Delay = 0
			
			elif letters[i] in HexLetters and type[i] == "04":
				if Delay != 0:
					Result.append("\nDELAY " + str(Delay) + "\n")
				Result.append("\nALT " + str(AltLetters[HexLetters.index(letters[i])]))
				Delay = 0
				String = 0
					
			elif letters[i] in HexLetters and type[i] == "08":
				if Delay != 0:
					Result.append("\nDELAY " + str(Delay) + "\n")
				Result.append("\nGUI " + str(AltLetters[HexLetters.index(letters[i])]))
				Delay = 0
				String = 0
			

				
			elif letters[i] == '00':
			
				# DELAY command in duck code actually starts with 00,
				# leaving only two hex digits (up to FF or 255) to specify the time
				# to wait, this means that DELAY 500 in hex is 00FF 00F5, to merge
				# these and prevent printing dumb delays
				# we tell python to add them if there are right next to each other
				# and store them in a variable.
													
				Delay = Delay + int(type[i],16)
				String = 0
		
	else:                                 # Mode two (display) is intended just to let people know what the inject.bin does, it 
										  # displays all text and key combinations but without commands. ie.
										  #
										  # Hello World!
										  #

		for i in range(0,len(letters)):
		
			if letters[i] in HexLetters and type[i] == "00":
				
				if str(Letters[HexLetters.index(letters[i])]) == "BK_SPACE":
					del Result[int(len(Result)) - 1]
					
				if str(Letters[HexLetters.index(letters[i])]) == "TAB":
					Result.append("     " )
					
				else:
					Result.append(Letters[HexLetters.index(letters[i])])
					
				
			elif letters[i] in HexLetters and type[i] == "01":
			
				Result.append("\nCONTROL " + str(AltLetters[HexLetters.index(letters[i])]) + "\n")
				
				
				
			elif letters[i] in HexLetters and type[i] == "02":

				Result.append(CapLetters[HexLetters.index(letters[i])])
				
			
			elif letters[i] in HexLetters and type[i] == "04":

				Result.append("\nALT " + str(AltLetters[HexLetters.index(letters[i])]))
				
				
					
			elif letters[i] in HexLetters and type[i] == "08":

				Result.append("\nGUI " + str(AltLetters[HexLetters.index(letters[i])]))
				
				


				
	Result.append("\n\n")
	return Result
	
def usage(reason, ecode):
	print " Usage: " + str(args[0]) + " < display|decode > inject.bin\n\n Example: " + str(args[0]) + " display /Documents/inject.bin\n"
	print reason + "\n"
	sys.exit(ecode)
	

########################## End of Functions ###################################

if len(args) > 1 and len(args) < 5 :
	try:
		filename = os.path.realpath(args[2])
	except IndexError:
		usage("Error: File not found", 1)
	else:
		List = dsem(hexstr(filename), 2)
		mode = args[1]
		chars = List[::2]
		types = List[1::2]

	if mode == "decode":
		Result = letiscover(chars,types,1)
	elif mode == "display":
		Result = letiscover(chars,types,0)
	else:
		usage("Error: No such option", -1)
		
	string = ""
	for i in range(0,len(Result)):
	
		string = string + str(Result[i])

	print string
else:
	usage("",2)