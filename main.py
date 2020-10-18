from pprint import pprint

dictApp = {
    "sessionSettings": {
        "mode": "S"
    },
    "defaultSettings": {
        "mode": "S",
    },
    "storedAnswers":
        {"yes": "Y",
         "no": "N",
         "default": "D",
         "cancel": "C",
         "explainMode": "E",
         "simpleMode": "S"},

    "StoredNames": {
        "mode": {
            "E": "Explain Mode",
            "S": "Simple Mode",
        },
    },
}


texts = {
    "questions": {"mode": "Wollen sie den " + dictApp["StoredNames"]["mode"]["S"] + "(" + dictApp["storedAnswers"]
    ["explainMode"] + ") nutzen oder wollen sie den " + dictApp["StoredNames"]["mode"]["E"] + "(" + dictApp["storedAnswers"]
    ["simpleMode"] + ") Nutzen: "},

    "answerOptions": {"mode": [
        dictApp["storedAnswers"]["explainMode"], dictApp["storedAnswers"]["simpleMode"], dictApp["storedAnswers"]["default"]
        ]}

}

def start():
    restoreData()
    requestMode()

    save()


def restoreData():
    dictAppTxt = open("dictApp.txt")
    global dictApp
    dictApp = eval(dictAppTxt.read())
    dictAppTxt.close()

    textsTxt = open("texts.txt")
    global texts
    texts = eval(textsTxt.read())
    textsTxt.close()


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
    answer = basicRequest(texts["questions"]["mode"], texts["answerOptions"]["mode"])
    if answer == dictApp["storedAnswers"]["simpleMode"]:
        dictApp["defaultSettings"]["mode"] = answer
        dictApp["sessionSettings"]["mode"] = answer
        print("Sie nutzen nun den " + dictApp["StoredNames"]["mode"][answer])
    elif answer == dictApp["storedAnswers"]["explainMode"]:
        dictApp["defaultSettings"]["mode"] = answer
        dictApp["sessionSettings"]["mode"] = answer
        print("Sie nutzen nun den " + dictApp["StoredNames"]["mode"][answer])
    else:
        dictApp["sessionSettings"]["mode"] = dictApp["defaultSettings"]["mode"]
        print("Sie nutzen nun den " + dictApp["StoredNames"]["mode"][dictApp["defaultSettings"]["mode"]])


def log():
    pprint("dictApp: " + str(dictApp))
    pprint("texts: " + str(texts))


start()