from pprint import pprint
import pyfiglet
import time
from cryptography.fernet import Fernet
Time = time

# Values

dict_app = {

    "sessionSettings": {  #Setting for the current session
        "mode": "S",
        "session": "",
        "action": "",
        "requested_key": ""
    },

    "defaultSettings": {  #Last used setting
        "mode": "S",
        "session": "",
        "action": "E",
        "requested_key": "P"
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
        "create": "E",
        "use": "N",
        "quit": "Q",
        "restart": "R",
        "private/public": "P",
        "session": "S"
    },

    "storedNames": {  #Full names for shortcuts
        "mode": {
            "E": "Explain Mode",
            "S": "Simple Mode",
        },
        "action": {
            "E": "Erstellen",
            "N": "Nutzen",
        },
        "kind_of_key":{
            "P": "Private/Public",
            "S": "Session"
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
            "kind_of_key":{
                "create": "Möchten Sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["private/public"]] + "\"(" + dict_app["storedAnswers"]["private/public"] + ") erstellen oder möchten sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["session"]] + "\"(" + dict_app["storedAnswers"]["session"] + ") erstellen? ",
                "use": "Möchten Sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["private/public"]] + "\"(" + dict_app["storedAnswers"]["private/public"] + ") nutzen oder möchten sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["session"]] + "\"(" + dict_app["storedAnswers"]["session"] + ") nutzen? "
            },
        },
        "E": {  # ExplainMode
            "session": "Sie können später Sessions speichern. Was so viel heisst wie sie können den private/public/session Key speichern \n""Welche session wollen Sie nutzen? " + "(" + dict_app["storedAnswers"]["1"] + ")" + " (" + dict_app["storedAnswers"]["2"] + ")" + " (" + dict_app["storedAnswers"]["3"] + ")" + " (" + dict_app["storedAnswers"]["4"] + ")" + " (" + dict_app["storedAnswers"]["5"] + ")" + dict_app["storedNames"]["optionalSymbol"] + ": ",
            "action": "Unter der auswahl \"" + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["create"]] + "\"(" + dict_app["storedAnswers"]["create"] + ")" + " werden sie die Möglichkeit habe Private/Public/Session Keys zu erstellen.\n""Mit der Option \"" + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["use"]] + "\"(" + dict_app["storedAnswers"]["use"] + ")" + " Können sie Private/Public/Session Keys Nutzen um texte zu ver/endschlüsseln. \n""Möchten sie Keys " + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["use"]] + "(" + dict_app["storedAnswers"]["use"] + ")" + " oder " + dict_app["storedNames"]["action"][dict_app["storedAnswers"]["create"]] + "(" + dict_app["storedAnswers"]["create"] + ") ",
            "kind_of_key": {
                "create": "Den Public Key sollten sie mit Ihrem gesprächs Partner Teilen.\n""Nur Ihr Private Key kann Nachrichten entschlüssen welche mit Ihrem Public Key verschlüsselt wurden. \n""Der Public Key kann nur verschlüsseln und der Private Key kann nur entschlüsseln. \n""Geben sie auf keinen Fall ihren Private Key an Jemanden weiter. \n\n""Der Session Key ist ein Schlüssel mit welchen sie verschlüsseln und entschlüsseln können. \n""Er wird Normalerweise mit hilfe des Private/Public Keys übertragen und anschliesend für die Kommunikation genutzt, \n""da er deutlich weniger Recourcen braucht. \n""Möchten Sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["private/public"]] + "\"(" + dict_app["storedAnswers"]["private/public"] + ") Key erstellen oder möchten sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["session"]] + "\"(" + dict_app["storedAnswers"]["session"] + ") Key erstellen? ",
                "use": "Sie sollten den Public Key ihres Gesprächspartners nutzen. \n""Sonst wird er nicht in der Lage sein die verschlüsselte Nachricht zu entschlüsseln. \n""Falls sie eine Nachricht entschlüsseln möchten welche mit Ihrem \n""Public Key verschlüsselt wurde, müssen Sie Ihren Private Key verwenden. \n\n""Mit dem Session Key können sie Nachrichten sowohl entschlüsseln als auch verschlüsseln. \n ""Möchten Sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["private/public"]] + "\"(" + dict_app["storedAnswers"]["private/public"] + ") Key nutzen oder möchten sie einen \"" + dict_app["storedNames"]["kind_of_key"][dict_app["storedAnswers"]["session"]] + "\"(" + dict_app["storedAnswers"]["session"] + ") Key nutzen? "
            },
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
        ],
        "kind_of_key": [dict_app["storedAnswers"]["private/public"], dict_app["storedAnswers"]["session"], dict_app["storedAnswers"]["default"]]
    },
    "startMessage": "In den meisten Fällen können Sie mithilfe von \"" + dict_app["storedAnswers"]["default"] + "\" die zulest genutzte Option wählen. \nEine leer Eingabe wird nur akzeptiert wenn, die Auswahl optional ist, was man am \"" + dict_app["storedNames"]["optionalSymbol"] + "\" erkennen kann.\n""Mit \"" + dict_app["storedAnswers"]["quit"] + "\" kann das Programm jederzeit beendet werden.",
    "parting": "-" * 114
}

# ! Values

# Start


def start(request_start):
    # restore_data()
    # Requests
    interactive_methods = [
        print_start_text,
        request_mode,
        request_session,
        request_action,
        request_kind_of_key
    ]
    for i in range(request_start, len(interactive_methods)):
        wait(.2)
        interactive_methods[i]()
        wait(.2)
        print_parting()
    # ! Requests
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
            elif answer == dict_app["storedAnswers"]["restart"]:
                print_parting()
                print(dict_app["storedNames"]["divisor"] + "Restart")
                print_parting()
                start(0)
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


def request_kind_of_key():
    if dict_app["sessionSettings"]["action"] == dict_app["storedAnswers"]["create"]:
        answer = basic_request(texts["questions"][dict_app["sessionSettings"]["mode"]]["kind_of_key"]["create"], texts["answerOptions"]["kind_of_key"])
        if answer == dict_app["storedAnswers"]["default"]:
            dict_app["sessionSettings"]["requested_key"] = dict_app["defaultSettings"]["requested_key"]
            print(dict_app["storedNames"]["divisor"] + "Sie haben \"" + dict_app["storedNames"]["kind_of_key"][dict_app["sessionSettings"]["requested_key"]] + "\"(" + dict_app["sessionSettings"]["requested_key"] + ") gewählt")
        else:
            dict_app["sessionSettings"]["requested_key"] = answer
            dict_app["defaultSettings"]["requested_key"] = answer
            print(dict_app["storedNames"]["divisor"] + "Sie haben \"" + dict_app["storedNames"]["kind_of_key"][dict_app["sessionSettings"]["requested_key"]] + "\"(" + dict_app["sessionSettings"]["requested_key"] + ") gewählt")
    elif dict_app["sessionSettings"]["action"] == dict_app["storedAnswers"]["use"]:
        answer = basic_request(texts["questions"][dict_app["sessionSettings"]["mode"]]["kind_of_key"]["use"], texts["answerOptions"]["kind_of_key"])
        if answer == dict_app["storedAnswers"]["default"]:
            dict_app["sessionSettings"]["requested_key"] = dict_app["defaultSettings"]["requested_key"]
            print(dict_app["storedNames"]["divisor"] + "Sie haben \"" + dict_app["storedNames"]["kind_of_key"][dict_app["sessionSettings"]["requested_key"]] + "\"(" + dict_app["sessionSettings"]["requested_key"] + ") gewählt")
        else:
            dict_app["sessionSettings"]["requested_key"] = answer
            dict_app["defaultSettings"]["requested_key"] = answer
            print(dict_app["storedNames"]["divisor"] + "Sie haben \"" + dict_app["storedNames"]["kind_of_key"][dict_app["sessionSettings"]["requested_key"]] + "\"(" + dict_app["sessionSettings"]["requested_key"] + ") gewählt")

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
    print("Something went wrong! Try to restart")
    exit()

# ! Else


start(0)
