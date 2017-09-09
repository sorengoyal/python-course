sentence = "in the beginning God created the heavens and the earth Now the earth was formless and empty darkness was over the surface of the deep and the Spirit of God was hovering over the waters And God said Let there be light and there was light God saw that the light was good and he separated the light from the darkness God called the light day and the darkness he called night And there was evening and there was morning the first day"
wordList = sentence.lower().split(' ')
counts = {}
for (i,word) in enumerate(wordList):
    if( word not in counts):
        counts[word] = 1
    counts[word] += 1
for word in counts:
    print(word + ' ' + str(counts[word]))
