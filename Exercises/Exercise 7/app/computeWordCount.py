from functools import reduce
def shuffle(pairs):
        d = {}
        for pair in pairs:
                if not d.get(pair[0]):
                        d[pair[0]] = []
                d[pair[0]].append(pair[1])
        return [(key, d[key]) for key in d]

"""in the beginning God created the heavens and the earth Now the earth was formless and empty darkness was over the surface of the deep and the Spirit of God was hovering over the waters And God said Let there be light and there was light God saw that the light was good and he separated the light from the darkness God called the light day and the darkness he called night And there was evening and there was morning—the first day
"""
def computeWordCount(text):
    mapOut = [(word.lower(),1) for word in text.split(' ')]
    shuffOutput = shuffle(mapOut)
    reduceOut = [(key, reduce(lambda sum, x: sum+x, value)) for (key, value) in shuffOutput]
    return reduceOut
