from pprint import pprint
dictApp = {
    "mode": "simpleMode",
    "storedAnswers":
        {"yes": "Y",
         "no": "N",
         "default": "D",
         "cancel": "C",
         "explainMode": "E",
         "simpleMode": "S"},
}


texts = {
    "questions": {"mode": "Wollen sie den Erklärungs Mode(" + dictApp["storedAnswers"]["explainMode"] + ") nutzen oder wollen sie den Simple Mode(" + dictApp["storedAnswers"]["simpleMode"] + ") Nutzen: "},
    "answerOptions": {"mode": [
        dictApp["storedAnswers"]["explainMode"], dictApp["storedAnswers"]["simpleMode"], dictApp["storedAnswers"]["default"]
    ]}
}

def start():
    restoreData()
    requestMode()

    save()
    print("dictApp: " + str(dictApp))
    print("texts: " + str(texts))

def restoreData():
    dictAppTxt = open("dictApp.txt")
    global dictApp
    dictApp = eval(dictAppTxt.read())
    dictAppTxt.close()
    #print("dictApp: " + str(dictApp))

    textsTxt = open("texts.txt")
    global texts
    texts = eval(textsTxt.read())
    textsTxt.close()
    #print("texts: " + str(texts))


def save():
    dictAppTxt = open("dictApp.txt", "w")
    dictAppTxt.write(str(dictApp))
    dictAppTxt.close()

    textsTxt = open("texts.txt", "w")
    textsTxt.write(str(texts))
    textsTxt.close()


def basicRequest(text, answerOptions):
    while True:
        answer = input(text).upper()
        for i in range(len(answerOptions)):
            if answer == answerOptions[i]:
                return answer


def requestMode():
    if basicRequest(texts["questions"]["mode"], texts["answerOptions"]["mode"]) == dictApp["storedAnswers"]["simpleMode"]:
        print("test")


start()





