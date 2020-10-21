from pprint import pprint
import pyfiglet
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
                        "session": "Welche session wollen Sie nutzen? " + "(" + dictApp["storedAnswers"]["1"] + ")" + " (" + dictApp["storedAnswers"]["2"] + ")" + " (" + dictApp["storedAnswers"]["3"] + ")" + " (" + dictApp["storedAnswers"]["4"] + ")" + " (" + dictApp["storedAnswers"]["5"] + ")*: "
                      },
                  "E": {
                        "session": "Sie können später Sessions speichern. Was soviel heisst wie sie können den privat/public/session Key speichern \n"
                                   "Welche session wollen Sie nutzen? " + "(" + dictApp["storedAnswers"]["1"] + ")" + " (" + dictApp["storedAnswers"]["2"] + ")" + " (" + dictApp["storedAnswers"]["3"] + ")" + " (" + dictApp["storedAnswers"]["4"] + ")" + " (" + dictApp["storedAnswers"]["5"] + ")*: "
                    },
                  },

    "answerOptions": {"mode": [
        dictApp["storedAnswers"]["explainMode"], dictApp["storedAnswers"]["simpleMode"], dictApp["storedAnswers"]["default"]
        ],

        "sessions": [
            dictApp["storedAnswers"]["1"], dictApp["storedAnswers"]["2"], dictApp["storedAnswers"]["3"], dictApp["storedAnswers"]["4"], dictApp["storedAnswers"]["5"], dictApp["storedAnswers"]["continue"], dictApp["storedAnswers"]["default"]
    ]},
    "startMessage": "In den meisten Fällen können Sie mithilfe von \""+ dictApp["storedAnswers"]["default"] + "\" die zulest genutzte Option wählen. \nEine leer Eingabe wird nur akzeptiert wenn, die Auswahl optional ist, was man am \"*\" erkennen kann.\n"
}

def start():
    startText()
    restoreData()
    requestMode()
    requestSession()
    save("file")


def startText():
    asciiWelcome = pyfiglet.figlet_format("En / Decoder")
    print(asciiWelcome)
    print(texts["startMessage"])

def restoreData():
    dictAppTxt = open("dictApp.txt")
    global dictApp
    dictApp = eval(dictAppTxt.read())
    dictAppTxt.close()

    textsTxt = open("texts.txt")
    global texts
    texts = eval(textsTxt.read())
    textsTxt.close()


def save(method):
    if method == "file":
        dictAppTxt = open("dictApp.txt", "w")
        dictAppTxt.write(str(dictApp))
        dictAppTxt.close()

        textsTxt = open("texts.txt", "w")
        textsTxt.write(str(texts))
        textsTxt.close()
    elif method == "session":
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
    if answer == dictApp["storedAnswers"]["default"]:
        dictApp["sessionSettings"]["session"] = dictApp["defaultSettings"]["session"]
        print("Sie haben die Option (" + dictApp["defaultSettings"]["session"] + ") gewählt")
    else:
        print("Sie haben die Option (" + answer + ") gewählt")
        dictApp["defaultSettings"]["session"] = answer
        dictApp["sessionSettings"]["session"] = answer


def log():
    pprint("dictApp: " + str(dictApp))
    pprint("texts: " + str(texts))


start()
