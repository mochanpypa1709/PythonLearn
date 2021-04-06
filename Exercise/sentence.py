def sentence(phrase):
    interrogatives = ("how","what","why")
    capital = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?". format(capital)
    else:
        return "{}.". format(capital)

results = []
while True:
    message = input("Say something: ")
    if message == '\end':
        break
    else:
        results.append(sentence(message))

print(" ".join(results))
