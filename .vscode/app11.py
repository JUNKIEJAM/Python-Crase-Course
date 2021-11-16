message=input(">")
words=message.split(' ')  #we will get the input string as a list
emojis={
    ":)":"😃",
    ":(":"☹️"
}
output=""
for word in words:
   output+= emojis.get(word,word)
   output+=" "
   
print(output)


