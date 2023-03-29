# Don't know the exact rules for the decription, so I'm considering that numbers should be empty values and other characters that are not alphabet are spaces
# This way the result gives the message perfectly as: This is Matrix
# If this is not considered the message would be: This is Matr ix
# Which is also understandable, but the word is cutted in the middle by a space

import string

alphabet = string.ascii_letters

message = """7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!"""

message_list = message.split("\n")
message_matrix = [list(text) for text in message_list]

decripted_message = ""

for i in range(len(message_matrix[0])):
    for j in range(len(message_matrix)):
        if (message_matrix[j][i] in alphabet):
            decripted_message += message_matrix[j][i]
        else:
            try:
                int(message_matrix[j][i])
            except:
                if (decripted_message) and (decripted_message[-1] != " "):
                    decripted_message += " "
        # If the rule is just changing the characters by space, than it would be like this:
        # else:
        #     if (decripted_message) and (decripted_message[-1] != " "):
        #         decripted_message += " "

print(decripted_message)