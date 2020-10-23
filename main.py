from pprint import pprint
import pyfiglet
import time
Time = time

# Values

dict_app = {

    "sessionSettings": {  #Setting for the current session
        "mode": "S",
        "session": "",
        "action": ""
    },

    "defaultSettings": {  #Last used setting
        "mode": "S",
        "session": "",
        "action": "N"
    },

    "storedAnswers": {  #Posible answers
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
        "create": "G",
        "use": "U",
        "quit": "Q"
    },

    "storedNames": {  #Full names for shortcuts
        "mode": {
            "E": "Explain Mode",
            "S": "Simple Mode",
        },
        "action": {
            "G": "Generieren",
            "U": "Nutzen",
        },
        "divisor": "-> ",
        "optionalSymbol": "*",
    },

    "sessions": {
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
        "mode": "Wollen sie den " + dict_app["storedNames"]["mode"][dict_app["storedAnswers"]["simpleMode"]] + "(" + dict_app["storedAnswers"]["simpleMode"] + ") nutzen oder wollen sie den " + dict_app["storedNames"]["mode"][dict_app["storedAnswers"]["explainMode"]] + "(" + dict_app["storedAnswers"]["explainMode"] + ") Nutzen: ",
        "S": {  # SimpleMode
            "session": "Welche session wollen Sie nutzen? " + "(" + dict_app["storedAnswers"]["1"] + ")" + " (" + dict_app["storedAnswers"]["2"] + ")" + " (" + dict_app["storedAnswers"]["3"] + ")" + " (" + dict_app["storedAnswers"]["4"] + ")" + " (" + dict_app["storedAnswers"]["5"] + ")" + dict_app["storedNames"]["optionalSymbol"] + ": ",
            "action": "Möchten sie Keys " + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["use"]] + "(" + dict_app["storedAnswers"]["use"] + ")" + " oder " + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["create"]] + "(" + dict_app["storedAnswers"]["create"] + ") ",
        },
        "E": {  # ExplainMode
            "session": "Sie können später Sessions speichern. Was so viel heisst wie sie können den privat/public/session Key speichern \n""Welche session wollen Sie nutzen? " + "(" + dict_app["storedAnswers"]["1"] + ")" + " (" + dict_app["storedAnswers"]["2"] + ")" + " (" + dict_app["storedAnswers"]["3"] + ")" + " (" + dict_app["storedAnswers"]["4"] + ")" + " (" + dict_app["storedAnswers"]["5"] + ")" + dict_app["storedNames"]["optionalSymbol"] + ": ",
            "action": "Unter der auswahl \"" + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["create"]] + "\"(" + dict_app["storedAnswers"]["create"] + ")" + " werden sie die Möglichkeit habe Private/Public/Session Keys zu erstellen.\n""Mit der Option \"" + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["use"]] + "\"(" + dict_app["storedAnswers"]["use"] + ")" + " Können sie Privat/Public/Session Keys Nutzen um texte zu ver/endschlüsseln. \n""Möchten sie Keys " + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["use"]] + "(" + dict_app["storedAnswers"]["use"] + ")" + " oder " + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["create"]] + "(" + dict_app["storedAnswers"]["create"] + ") "
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
            dict_app["storedAnswers"]["create"], dict_app["storedAnswers"]["use"], dict_app["storedAnswers"]["default"]
        ]
    },
    "startMessage": "In den meisten Fällen können Sie mithilfe von \"" + dict_app["storedAnswers"]["default"] + "\" die zulest genutzte Option wählen. \nEine leer Eingabe wird nur akzeptiert wenn, die Auswahl optional ist, was man am \"" + dict_app["storedNames"]["optionalSymbol"] + "\" erkennen kann.\n""Mit \"" + dict_app["storedAnswers"]["quit"] + "\" kann das Programm jederzeit beendet werden.",
    "parting": "-" * 110
}

# ! Values

# Start


def start():

    # Requests
    requests = [
        print_start_text,
        request_mode,
        request_session,
        request_action,

    ]

    for i in range(len(requests)):
        if i == 4:
            if dict_app["sessionSettings"]["action"] == dict_app["storedAnswers"]["create"]:
                print("MMMM")
            elif dict_app["sessionSettings"]["action"] == dict_app["storedAnswers"]["use"]:
                print("NNNN")
            else:
                error()
        wait(.2)
        requests[i]()
        wait(.2)
        print_parting()


    # ! Requests

    # restore_data()
    save()
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


def save():
    dict_app_txt = open("dictApp.txt", "w")
    dict_app_txt.write(str(dict_app))
    dict_app_txt.close()

    texts_txt = open("texts.txt", "w")
    texts_txt.write(str(texts))
    texts_txt.close()

# ! Storage

# Requests


def basic_request(text, answer_options):
    while True:
        answer = input(text).upper()
        for i in range(len(answer_options)):
            if answer == answer_options[i]:
                return answer
            # Quit
            elif answer == dict_app["storedAnswers"]["quit"]:
                print_parting()
                print(dict_app["storedNames"]["divisor"] + "Quit/Exit")
                print_parting()
                exit()
            # ! Quit

def request_mode():
    answer = basic_request(texts["questions"]["mode"], texts["answerOptions"]["mode"])
    if answer == dict_app["storedAnswers"]["simpleMode"]:
        dict_app["defaultSettings"]["mode"] = answer
        dict_app["sessionSettings"]["mode"] = answer
        print(dict_app["storedNames"]["divisor"] + "Sie nutzen nun den " + dict_app["storedNames"]["mode"][answer])
    elif answer == dict_app["storedAnswers"]["explainMode"]:
        dict_app["defaultSettings"]["mode"] = answer
        dict_app["sessionSettings"]["mode"] = answer
        print(dict_app["storedNames"]["divisor"] + "Sie nutzen nun den " + dict_app["storedNames"]["mode"][answer])
    else:
        dict_app["sessionSettings"]["mode"] = dict_app["defaultSettings"]["mode"]
        print(dict_app["storedNames"]["divisor"] + "Sie nutzen nun den " + dict_app["storedNames"]["mode"][dict_app["defaultSettings"]["mode"]])


def request_session():
    answer = basic_request(texts["questions"][dict_app["sessionSettings"]["mode"]]["session"], texts["answerOptions"]["sessions"])
    if answer == dict_app["storedAnswers"]["default"]:
        if dict_app["defaultSettings"]["session"] == "":
            print(dict_app["storedNames"]["divisor"] + "Sie fahren nun ohne Session fort")
        else:
            dict_app["sessionSettings"]["session"] = dict_app["defaultSettings"]["session"]
            print(dict_app["storedNames"]["divisor"] + "Sie haben die Option (" + dict_app["defaultSettings"]["session"] + ") gewählt")

    elif answer == dict_app["storedAnswers"]["continue"]:
        print(dict_app["storedNames"]["divisor"] + "Sie fahren nun ohne Session fort")

    else:
        print(dict_app["storedNames"]["divisor"] + "Sie haben die Option (" + answer + ") gewählt")
        dict_app["defaultSettings"]["session"] = answer
        dict_app["sessionSettings"]["session"] = answer


def request_action():
    answer = basic_request(texts["questions"][dict_app["sessionSettings"]["mode"]]["action"], texts["answerOptions"]["action"])
    if answer == dict_app["storedAnswers"]["default"]:
        dict_app["sessionSettings"]["action"] = dict_app["defaultSettings"]["action"]
        print(dict_app["storedNames"]["divisor"] + "Sie haben die Option \"" + dict_app["storedNames"]["action"][dict_app["defaultSettings"]["action"]] + "\"(" + dict_app["defaultSettings"]["action"] + ") gewählt")
    else:
        dict_app["sessionSettings"]["action"] = answer
        dict_app["defaultSettings"]["action"] = answer
        print(dict_app["storedNames"]["divisor"] + "Sie haben die Option \"" + dict_app["storedNames"]["action"][dict_app["defaultSettings"]["action"]] + "\"(" + dict_app["defaultSettings"]["action"] + ") gewählt")

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

    print(texts["parting"])


def wait(secs):
    Time.sleep(secs)


def error():
    print("Something went wrong")
    start()

# ! Else


start()
