# NOTE: This program requires pyperclip to work well.
#
# Pyperclip can be found at https://github.com/asweigart/pyperclip
# and installed with pip install pyperclip.
#
# This program implements a keyword cipher, with the option to copy output to the clipboard.
#

import pyperclip

print "WELCOME TO VAISHANT'S WORD CODE ENCODER AND DECODER"
print ""

while True:
        
        #COLLECTING USER INFORMATION
        while True:
                mode = str(raw_input("Enter E, D, or EXIT, for encryption, decryption and exiting the application: "))
                if mode == "E" or mode == "e":
                        modetxt = "encryption"
                        break
                elif mode == "D" or mode == "d":
                        modetxt = "decryption"
                        break
                elif mode == "EXIT" or mode == "exit":
                        modetxt = "exit"
                        break
                else:
                        print "Please enter a valid mode, or EXIT."
                        print ""
                        continue
                break

        #EXIT IF THE USER WISHES TO

        if modetxt == "exit":
                exit()

        #INITIALISING VARIABLES
        alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        alpharl = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
        alpharllist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        dellist = []
        alpharlval = {}
        print ""
        message = raw_input("Enter the message: ")
        message = message.upper().strip()
        print ""
        key = raw_input("Enter the keyword: ")
        key = key.upper().strip().replace(" ","")
        keyalphalist = []
        keyalphadict = {}
        codedict = dict()
        output = ""

        #CREATING CODE ALPHABET
        for letter in key:
                if letter not in keyalphalist:
                        keyalphalist.append(str(letter))
                        dellist.append(letter)
                else:
                        continue

        dellist.sort()
        dellist.reverse()

        for letter in dellist:
                a = alpharl[letter]
                a=a-1
                del alpharllist[a]
                
        for letter in alpharllist:
                keyalphalist.append(letter)
                
        #MAKING DICTIONARY
        c=0
        for letter in keyalphalist:
                s = alpha[c]
                codedict[s] = letter
                c = c+1

        #ENCODING/DECODING
        if modetxt == "encryption":
                for letter in message:
                        try:
                                output = output + codedict[letter]
                        except:
                                output = output + letter
        elif modetxt == "decryption":
                c=0
                codedict.clear()
                for letter in keyalphalist:
                        s=alpha[c]
                        codedict[letter] = s
                        c = c+1
                for letter in message:
                        try:
                                output = output + codedict[letter]
                        except:
                                output = output + letter
                       
        #PRINTING OUTPUT
        print ""
        print "Your output is: "
        print output
        print ""

        #OPTIONAL COPYING
        while True:
                copyornot = raw_input("Would you like to copy the output to the clipboard (Y or N): ")
                copy = copyornot.upper()
                if copy == "Y":
                        pyperclip.copy(output)
                        #os.system("echo %s | clip" %(output))
                        print ""
                        break
                elif copy == "N":
                        print ""
                        break
                else:
                        print "Please enter a valid choice."
                        print ""
                        continue

        #NEXT ITERATION
        exiting = raw_input("Press enter to continue.")
        print ""
