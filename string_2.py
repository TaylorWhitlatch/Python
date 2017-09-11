

str = "AEGIOST aegiost"
str = str.upper()
str2 = str.replace("A", "4").replace("G","6").replace("E", "3").replace("I", "1").replace("O","0").replace("S", "5").replace("T", "7")
print str2



word = raw_input("Enter Long Vowel: ")
word = word.upper()

word2 = word.replace("EE", 5*"E").replace("OO", 5*"O").replace("AA",5*"A").replace("II", 5*"I").replace("UU", 5*"U")
word2 = word2.lower().title()
print word2
