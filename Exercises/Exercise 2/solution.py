sentence = 'in the beginning God created the heavens and the earth Now the earth was formless and empty darkness was over the surface of the deep and the Spirit of God was hovering over the waters And God said Let there be light and there was light God saw that the light was good and he separated the light from the darkness God called the light day and the darkness he called night And there was evening and there was morning—the first day'
wordList = sentence.split(' ')
counts = []
for (i,word) in enumerate(wordList):
    counts.append([word.lower(),1])
    for w in wordList[i+1:] :
        if word.lower() == w.lower():
            counts[i][1] += 1
            wordList.remove(w)
for word,count in counts:
    print(word + ' ' + str(count))
