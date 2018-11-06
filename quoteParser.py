import random, sys, json, time
from pprint import pprint


def main(source, target):
    # Get the movie quote code
    with open(source) as f:
        sourceFile = f.readlines()
    sourceFile = [x.strip() for x in sourceFile]

    # Ready to create the new Python file
    pythonFile = open(target, "w")

    # Load the quote/code relationships
    with open('quotes.json') as f:
        jsonFile = json.load(f)

    for line in sourceFile:
        print "line: " + line
        for quote in jsonFile["data"]:
            print "quote: "  + quote["quote"]
            if quote["quote"] in line:
                print "Success!: " + quote["code"]
                pythonFile.write(quote["code"] + line.split(quote["quote"])[1])
    pythonFile.close()


    rewrite = open(source, "w")
    for line in sourceFile:
        rewrite.write(line + '\n')

    rewrite.close()

if __name__ == "__main__":
    main(str(sys.argv[1]), str(sys.argv[2]))
