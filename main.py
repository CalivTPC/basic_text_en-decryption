from pprint import pprint

dictApp = {
    "sessionSettings": {
        "mode": "S",
        "session": ""
    },
    "defaultSettings": {
        "mode": "S",
        "session": ""
    },
    "storedAnswers":
        {"yes": "Y",
         "no": "N",
         "default": "D",
         "cancel": "C",
         "explainMode": "E",
         "simpleMode": "S",
         "1": "1",
         "2": "2",
         "3": "3",
         "4": "4",
         "5": "5",
         "continue": ""
        },

    "StoredNames": {
        "mode": {
            "E": "Explain Mode",
            "S": "Simple Mode",
        },
    },
    "seesions": {
        "names": [],
        "publicKeys": [],
        "privateKeys": [],
        "sessionKeys": [],
    }
}


texts = {
    "questions": {"mode": "Wollen sie den " + dictApp["StoredNames"]["mode"]["S"] + "(" + dictApp["storedAnswers"]
                            ["simpleMode"] + ") nutzen oder wollen sie den " + dictApp["StoredNames"]["mode"]["E"] + "(" + dictApp["storedAnswers"]
                            ["explainMode"] + ") Nutzen: ",
                  "S": {
                        "session": "Welche session wollen Sie nutzen? " + "(" + dictApp["storedAnswers"]["1"] + ")" + " (" + dictApp["storedAnswers"]["2"] + ")" + " (" + dictApp["storedAnswers"]["3"] + ")" + " (" + dictApp["storedAnswers"]["4"] + ")" + " (" + dictApp["storedAnswers"]["5"] + "): "
                      },
                  "E": {
                        "session": "Sie können später Sessions speichern. Was soviel heisst wie sie können den privat/public/session Key speichern \n"
                                   "Welche session wollen Sie nutzen? " + "(" + dictApp["storedAnswers"]["1"] + ")" + " (" + dictApp["storedAnswers"]["2"] + ")" + " (" + dictApp["storedAnswers"]["3"] + ")" + " (" + dictApp["storedAnswers"]["4"] + ")" + " (" + dictApp["storedAnswers"]["5"] + "): "
                  },
                  },

    "answerOptions": {"mode": [
        dictApp["storedAnswers"]["explainMode"], dictApp["storedAnswers"]["simpleMode"], dictApp["storedAnswers"]["default"]
        ],

        "sessions": [
            dictApp["storedAnswers"]["1"], dictApp["storedAnswers"]["2"], dictApp["storedAnswers"]["3"], dictApp["storedAnswers"]["4"], dictApp["storedAnswers"]["5"], dictApp["storedAnswers"]["continue"]
    ]}
}

def start():
    #restoreData()
    requestMode()
    requestSession()
    save("file")
    log()


def restoreData():
    global dictApp, texts
    values = ["dictApp", "texts"]
    for i in range(len(values)):
        file = open(values[i] + ".txt")
        values[i] = eval(file.read())
        file.close()


def save(type):
    values = ["dictApp", "texts"]
    if type == "file":
        for i in range(len(values)):
            file = open(values[i] + ".txt", "w")
            file.write(str(values[i]))
            file.close()

    elif type == "session":
        print("something")


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


def requestSession():
    answer = basicRequest(texts["questions"][dictApp["sessionSettings"]["mode"]]["session"], texts["answerOptions"]["sessions"])
    if answer == dictApp["storedAnswers"]["1"]:
        print("answer: " + answer)
        dictApp["defaultSettings"]["session"] = answer
        dictApp["sessionSettings"]["session"] = answer

    elif answer == dictApp["storedAnswers"]["2"]:
        print("answer: " + answer)
        dictApp["defaultSettings"]["session"] = answer
        dictApp["sessionSettings"]["session"] = answer

    elif answer == dictApp["storedAnswers"]["3"]:
        print("answer: " + answer)
        dictApp["defaultSettings"]["session"] = answer
        dictApp["sessionSettings"]["session"] = answer

    elif answer == dictApp["storedAnswers"]["4"]:
        print("answer: " + answer)
        dictApp["defaultSettings"]["session"] = answer
        dictApp["sessionSettings"]["session"] = answer

    elif answer == dictApp["storedAnswers"]["5"]:
        print("answer: " + answer)
        dictApp["defaultSettings"]["session"] = answer
        dictApp["sessionSettings"]["session"] = answer

    else:
        print("answer: " + answer)
        dictApp["defaultSettings"]["session"] = answer
        dictApp["sessionSettings"]["session"] = answer


def log():
    pprint("dictApp: " + str(dictApp))
    pprint("texts: " + str(texts))


start()
