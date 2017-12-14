from replace.RegexReplacer import RegexReplacer

replacer = RegexReplacer()
sentence = "I'm and I'll always be the greatest !"
sentence_new = replacer.replace(sentence)

print('Original : ' + sentence)
print('After    : ' + sentence_new)


