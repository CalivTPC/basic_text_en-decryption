from pprint import pprint
import pyfiglet

# Values

dict_app = {

    "sessionSettings": {  #Setting for the current session
        "mode": "S",
        "session": ""
    },

    "defaultSettings": {  #Last used setting
        "mode": "S",
        "session": ""
    },

    "storedAnswers": {  #Posible snswers
        "yes": "Y",
        "no": "N",
        "default": "D",
        "explainMode": "E",
        "simpleMode": "S",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "continue": "",
        "create": "M",
        "use": "N"
    },

    "StoredNames": {  #Full names for shortcuts
        "mode": {
            "E": "Explain Mode",
            "S": "Simple Mode",
        },
        "action": {
            "M": "Machen",
            "N": "Nutzen"
        },
    },

    "seesions": {
        "1": {
            "names": [],
            "publicKeys": [],
            "privateKeys": [],
            "sessionKeys": [],
        },
        "2": {
            "names": [],
            "publicKeys": [],
            "privateKeys": [],
            "sessionKeys": [],
        },
        "3": {
            "names": [],
            "publicKeys": [],
            "privateKeys": [],
            "sessionKeys": [],
        },
        "4": {
            "names": [],
            "publicKeys": [],
            "privateKeys": [],
            "sessionKeys": [],
        },
        "5": {
            "names": [],
            "publicKeys": [],
            "privateKeys": [],
            "sessionKeys": [],
        },
    }
}


texts = {
    # Questions
    "questions": {
        "mode": "Wollen sie den " + dict_app["StoredNames"]["mode"][dict_app["storedAnswers"]["simpleMode"]] + "(" + dict_app["storedAnswers"]["simpleMode"] + ") nutzen oder wollen sie den " + dict_app["StoredNames"]["mode"][dict_app["storedAnswers"]["explainMode"]] + "(" + dict_app["storedAnswers"]["explainMode"] + ") Nutzen: ",
        "S": {  # SimpeMode
            "session": "Welche session wollen Sie nutzen? " + "(" + dict_app["storedAnswers"]["1"] + ")" + " (" + dict_app["storedAnswers"]["2"] + ")" + " (" + dict_app["storedAnswers"]["3"] + ")" + " (" + dict_app["storedAnswers"]["4"] + ")" + " (" + dict_app["storedAnswers"]["5"] + ")*: ",
            "action": "Möchten sie Keys " + dict_app["StoredNames"]["action"][dict_app["storedAnswers"]["use"]] + "(" + dict_app["storedAnswers"]["use"] + ")" + " oder " + dict_app["StoredNames"]["action"][dict_app["storedAnswers"]["create"]] + "(" + dict_app["storedAnswers"]["create"] + ") ",
        },
        "E": {  # ExplainMode
            "session": "Sie können später Sessions speichern. Was soviel heisst wie sie können den privat/public/session Key speichern \n""Welche session wollen Sie nutzen? " + "(" + dict_app["storedAnswers"]["1"] + ")" + " (" + dict_app["storedAnswers"]["2"] + ")" + " (" + dict_app["storedAnswers"]["3"] + ")" + " (" + dict_app["storedAnswers"]["4"] + ")" + " (" + dict_app["storedAnswers"]["5"] + ")*: ",
            "action": "Unter der auswahl \"" + dict_app["StoredNames"]["action"][dict_app["storedAnswers"]["create"]] + "\"(" + dict_app["storedAnswers"]["create"] + ")" + " werden sie die Möglichkeit habe Private/Public/Session Keys zu erstellen.\n""Mit der Option \"" + dict_app["StoredNames"]["action"][dict_app["storedAnswers"]["use"]] + "\"(" + dict_app["storedAnswers"]["use"] + ")" + " Können sie Privat/Public/Session Keys Nutzen um texte zu ver/endschlüsseln. \n""Möchten sie Keys " + dict_app["StoredNames"]["action"][dict_app["storedAnswers"]["use"]] + "(" + dict_app["storedAnswers"]["use"] + ")" + " oder " + dict_app["StoredNames"]["action"][dict_app["storedAnswers"]["create"]] + "(" + dict_app["storedAnswers"]["create"] + ") "
        },
    },
    # ! Questions

    # Possible Answers
    "answerOptions": {"mode": [
            dict_app["storedAnswers"]["explainMode"], dict_app["storedAnswers"]["simpleMode"], dict_app["storedAnswers"]["default"]
        ],

        "sessions": [
            dict_app["storedAnswers"]["1"], dict_app["storedAnswers"]["2"], dict_app["storedAnswers"]["3"], dict_app["storedAnswers"]["4"], dict_app["storedAnswers"]["5"], dict_app["storedAnswers"]["continue"], dict_app["storedAnswers"]["default"]
        ],
        "action": [
            dict_app["storedAnswers"]["create"]
        ]
    },
    "startMessage": "In den meisten Fällen können Sie mithilfe von \"" + dict_app["storedAnswers"]["default"] + "\" die zulest genutzte Option wählen. \nEine leer Eingabe wird nur akzeptiert wenn, die Auswahl optional ist, was man am \"*\" erkennen kann.\n"
}

# ! Values

# Start


def start():
    print_start_text()
    #restore_data()
    request_mode()
    request_session()
    request_action()
    save("file")

# ! Start

# Storage


def restore_data():
    dict_app_txt = open("dictApp.txt")
    global dict_app
    dict_app = eval(dict_app_txt.read())
    dict_app_txt.close()

    texts_txt = open("texts.txt")
    global texts
    texts = eval(texts_txt.read())
    texts_txt.close()


def save(method):
    if method == "file":
        dict_app_txt = open("dictApp.txt", "w")
        dict_app_txt.write(str(dict_app))
        dict_app_txt.close()

        texts_txt = open("texts.txt", "w")
        texts_txt.write(str(texts))
        texts_txt.close()
    elif method == "session":
        print("something")

# ! Storage

# Requests


def basic_request(text, answer_options):
    while True:
        answer = input(text).upper()
        for i in range(len(answer_options)):
            if answer == answer_options[i]:
                return answer


def request_mode():
    answer = basic_request(texts["questions"]["mode"], texts["answerOptions"]["mode"])
    if answer == dict_app["storedAnswers"]["simpleMode"]:
        dict_app["defaultSettings"]["mode"] = answer
        dict_app["sessionSettings"]["mode"] = answer
        print("Sie nutzen nun den " + dict_app["StoredNames"]["mode"][answer])
    elif answer == dict_app["storedAnswers"]["explainMode"]:
        dict_app["defaultSettings"]["mode"] = answer
        dict_app["sessionSettings"]["mode"] = answer
        print("Sie nutzen nun den " + dict_app["StoredNames"]["mode"][answer])
    else:
        dict_app["sessionSettings"]["mode"] = dict_app["defaultSettings"]["mode"]
        print("Sie nutzen nun den " + dict_app["StoredNames"]["mode"][dict_app["defaultSettings"]["mode"]])
    print_parting()


def request_session():
    answer = basic_request(texts["questions"][dict_app["sessionSettings"]["mode"]]["session"], texts["answerOptions"]["sessions"])
    if answer == dict_app["storedAnswers"]["default"]:
        dict_app["sessionSettings"]["session"] = dict_app["defaultSettings"]["session"]
        print("Sie haben die Option (" + dict_app["defaultSettings"]["session"] + ") gewählt")
    else:
        print("Sie haben die Option (" + answer + ") gewählt")
        dict_app["defaultSettings"]["session"] = answer
        dict_app["sessionSettings"]["session"] = answer
    print_parting()


def request_action():
    answer = basic_request(texts["questions"][dict_app["sessionSettings"]["mode"]]["action"], texts["answerOptions"]["action"])

    print_parting()
# ! Requests

# Else


def log():
    pprint("dictApp: " + str(dict_app))
    pprint("texts: " + str(texts))


def print_start_text():
    ascii_welcome = pyfiglet.figlet_format("En / Decryption")
    print(ascii_welcome)
    print(texts["startMessage"])


def print_parting():
    print("\n")

# ! Else


start()
