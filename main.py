from gingerit.gingerit import GingerIt
import pprint

text = "Welcome to grammar check bot, just enter text want to check"

ginger_parser = GingerIt()

ginger_grammar_results = ginger_parser.parse(text)

pprint.pprint(ginger_grammar_results['result'])

ginger_corrections = ginger_grammar_results['corrections']

pprint.pprint(ginger_corrections)

print("\nNumber of grammar issues found with Ginger: " + str(len(ginger_corrections)) + "\n")

for correction in ginger_corrections:
    print("\t(Char #" + str(correction['start']) + ") Use '" + correction['correct'] + "' instead of '" + correction['text'] + "'")