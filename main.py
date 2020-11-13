from pprint import pprint  # log()
import pyfiglet  # print_start_text()
import time  # wait()
Time = time  # wait()
# Crypto
from Crypto.PublicKey import RSA
#from cryptography.fernet import Fernet
#import rsa
#import base64

# Crypto


# Values

dict_app = {

    "session_settings": {  #Setting for the current session
        "mode": "",
        "session": "",
        "action": "",
        "requested_key": "",
        "key": {
            "size": "",
        }
    },

    "default_settings": {  #Last used settinghttp://www.koalastothemax.com/?aHR0cDovL3d3dy5leHRvbGUuY29tL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDE0LzA1L3JpY2tfYXN0bGV5LmpwZw==
        "action": "E",
        "requested_key": "P",
        "key": {
            "size": "1024",
        }
    },

    "sessions": [
        "test_session",
        "default_session",
        "private",
        "save",
    ],
    "stored_answers": {  #Posible answers
        "yes": "Y",
        "no": "N",
        "default": "D",
        "explain_mode": "E",
        "simple_mode": "S",
        "continue": "",
        "create": "E",
        "use": "N",
        "quit": "Q",
        "private/public": "P",
        "session": "S"
    },

    "stored_names": {  #Full names for shortcuts
        "mode": {
            "E": "Explain Mode",
            "S": "Simple Mode",
        },
        "action": {
            "E": "Erstellen",
            "N": "Nutzen",
        },
        "kind_of_key": {
            "P": "Private/Public",
            "S": "Session"
        },
        "divisor": "-> ",
        "optional_symbol": "*",
    },
}


texts = {
    # Questions
    "questions": {
        "mode": "Wollen sie den " + dict_app["stored_names"]["mode"][dict_app["stored_answers"]["simple_mode"]] + "(" + dict_app["stored_answers"]["simple_mode"] + ") nutzen oder wollen sie den " + dict_app["stored_names"]["mode"][dict_app["stored_answers"]["explain_mode"]] + "(" + dict_app["stored_answers"]["explain_mode"] + ") Nutzen: ",
        dict_app["stored_answers"]["simple_mode"]: {  # simple_mode
            "session": "hier ist eine Liste der bereits erstellten Sessions. \n" +
                        str(dict_app["sessions"]) + "\n" +
                        "Bitte geben sie den namen der session an welche sie nutzen wollen: ",
            "action": "Möchten sie Keys " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["use"]] + "(" + dict_app["stored_answers"]["use"] + ")" + " oder " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["create"]] + "(" + dict_app["stored_answers"]["create"] + ") ",
            "kind_of_key": {
                "create": "Möchten Sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["private/public"]] + "\"(" + dict_app["stored_answers"]["private/public"] + ") erstellen oder möchten sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["session"]] + "\"(" + dict_app["stored_answers"]["session"] + ") erstellen? ",
                "use": "Möchten Sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["private/public"]] + "\"(" + dict_app["stored_answers"]["private/public"] + ") nutzen oder möchten sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["session"]] + "\"(" + dict_app["stored_answers"]["session"] + ") nutzen? "
                },
            "key_size":
                "Bitte geben sie an, wie gross Ihr schlüssel sein soll. Die Zahl sollte zwischen 256 und 4096 liegen: ",
            "create_key":
                "Keys werden erstellt... "
            
        },
        dict_app["stored_answers"]["explain_mode"]: {  # explain_mode
            "session": "Sie können später Sessions speichern. Was so viel heisst wie sie können den private/public/session Key speichern \n"
                        "hier ist eine Liste der bereits erstellten Sessions. \n" +
                        str(dict_app["sessions"]) + "\n" +
                        "Bitte geben sie den namen der session an welche sie nutzen wollen: ",
            "action": "Unter der auswahl \"" + dict_app["stored_names"]["action"][dict_app["stored_answers"]["create"]] + "\"(" + dict_app["stored_answers"]["create"] + ")" + " werden sie die Möglichkeit habe Private/Public/Session Keys zu erstellen.\n"
                "Mit der Option \"" + dict_app["stored_names"]["action"][dict_app["stored_answers"]["use"]] + "\"(" + dict_app["stored_answers"]["use"] + ")" + " Können sie Private/Public/Session Keys Nutzen um texte zu ver/endschlüsseln. \n"
                "Möchten sie Keys " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["use"]] + "(" + dict_app["stored_answers"]["use"] + ")" + " oder " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["create"]] + "(" + dict_app["stored_answers"]["create"] + ") ",
            "kind_of_key": {
                "create": "Den Public Key sollten sie mit Ihrem gesprächs Partner Teilen.\n"
                    "Nur Ihr Private Key kann Nachrichten entschlüssen welche mit Ihrem Public Key verschlüsselt wurden. \n"
                    "Der Public Key kann nur verschlüsseln und der Private Key kann nur entschlüsseln. \n"
                    "Geben sie auf keinen Fall ihren Private Key an Jemanden weiter. \n\n"
                          
                    "Der Session Key ist ein Schlüssel mit welchen sie verschlüsseln und entschlüsseln können. \n"
                    "Er wird Normalerweise mit hilfe des Private/Public Keys übertragen und anschliesend für die Kommunikation genutzt, \n"
                    "da er deutlich weniger Recourcen braucht. \n"
                    "Möchten Sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["private/public"]] + "\"(" + dict_app["stored_answers"]["private/public"] + ") Key erstellen oder möchten sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["session"]] + "\"(" + dict_app["stored_answers"]["session"] + ") Key erstellen? ",
                "use": "Sie sollten den Public Key ihres Gesprächspartners nutzen. \n"
                    "Sonst wird er nicht in der Lage sein die verschlüsselte Nachricht zu entschlüsseln. \n"
                    "Falls sie eine Nachricht entschlüsseln möchten welche mit Ihrem \n"
                    "Public Key verschlüsselt wurde, müssen Sie Ihren Private Key verwenden. \n\n"
                       
                    "Mit dem Session Key können sie Nachrichten sowohl entschlüsseln als auch verschlüsseln. \n"
                    "Möchten Sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["private/public"]] + "\"(" + dict_app["stored_answers"]["private/public"] + ") Key nutzen oder möchten sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["session"]] + "\"(" + dict_app["stored_answers"]["session"] + ") Key nutzen? "

            },
            "key_size":
                "Hier sehen sie, wie lange Schlüssel mit einer bestimmter Grösse etwa brauchen, um erstellt zu werden.\n"
                "256:  0.003 sec \t 512:  0.11 sec \t 1024: 0.79 sec \n"
                "2048: 6.55  sec \t 3072: 23.4 sec \t 4096: 72.0 sec \n"
                "Bitte geben sie an, wie gross Ihr schlüssel sein soll. Die Zahl sollte zwischen 256 und 4096 liegen: ",
            
        },
    },
    # ! Questions
    "informations":{
        dict_app["stored_answers"]["simple_mode"]: {  #simple_mode 

        },

        dict_app["stored_answers"]["explain_mode"]: {  #explain_mode
            "create_key":
                "Die dauer des erstellen hängt mit ihrer cpu leistung und der grösse des Keys zusammen \n"
                "Falls das Programm länger als 1 min braucht, sollten sie das Programm neustarten und einen kleineren Key wählen \n"
                "Keys werden erstellt... "
        },
    },
    # Possible Answers
    "answer_options": {"mode": [
            dict_app["stored_answers"]["explain_mode"], dict_app["stored_answers"]["simple_mode"], dict_app["stored_answers"]["default"]
        ],

        "sessions": [
            dict_app["stored_answers"]["continue"], dict_app["sessions"]
        ],
        "action": [
            dict_app["stored_answers"]["create"], dict_app["stored_answers"]["use"], dict_app["stored_answers"]["default"]
        ],
        "kind_of_key": [dict_app["stored_answers"]["private/public"], dict_app["stored_answers"]["session"], dict_app["stored_answers"]["default"]
        ],
        "key_size": ["256", "4096"]
    },
    "start_message": "In den meisten Fällen können Sie mithilfe von \"" + dict_app["stored_answers"]["default"] + "\" die zulest genutzte Option wählen. \n"
        "Eine leer Eingabe wird nur akzeptiert wenn, die Auswahl optional ist, was man am \"" + dict_app["stored_names"]["optional_symbol"] + "\" erkennen kann.\n"
        "Mit \"" + dict_app["stored_answers"]["quit"] + "\" kann das Programm jederzeit beendet werden.",
    
    "parting": {
        "normal": "-",
        "wrong": "=",
    },
}

# ! Values

# Start


def start(request_start):
    # restore_data()
    # Requests

    interactive_methods = [
        print_start_message,
        request_mode,
        request_session,
        request_action,
        request_kind_of_key,
        request_key_size,
        creat_public_private_key,
    ]
    for i in range(request_start, len(interactive_methods)):
        wait(.2)
        interactive_methods[i]()
        wait(.2)
        print_parting("normal", 114)

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
    dict_app_txt = open("values/dictApp.txt", "w")
    dict_app_txt.write(str(dict_app))
    dict_app_txt.close()

    texts_txt = open("values/texts.txt", "w")
    texts_txt.write(str(texts))
    texts_txt.close()

# ! Storage

# Requests

def handle_numeric_basic_request(answer, answer_options):
    answer = int(answer)
    if answer >= int(answer_options[0]) and answer <= int(answer_options[1]):
        return answer
    else:
        return None


def quit():
    print_parting("normal", 114)
    print(dict_app["stored_names"]["divisor"] + "Quit/Exit")
    print_parting("normal", 114)
    exit()

def includes_list(to_check):
    for i in range(len(to_check)):
        if isinstance(to_check[i], list):
            return True


def handle_list_basic_request(answer_options):
    position = []
    for i in range(len(answer_options)):
        if isinstance(answer_options[i], list):
            position.append(i)
            
    for i in range(len(position)):
        answer_options.extend(answer_options[position[i]])
        answer_options.pop(position[i])
    
    return answer_options


def is_numeric(answer_options):
    for i in range(len(answer_options)):
        if answer_options[i].isnumeric():
            return True


def basic_request(text, answer_options):
    was_wrong = False
    list_inclouded = False
    while True:
        if was_wrong:
            print_parting("wrong", 114)
            print("Möglich Antworten: " + str(answer_options))
            print_parting("wrong", 114)

        answer = input(text)

        if includes_list(answer_options):
            list_inclouded = True
            answer_options = handle_list_basic_request(answer_options)

        if answer.isnumeric() and is_numeric(answer_options):
            if handle_numeric_basic_request(answer, answer_options) == None:
                was_wrong = True
        elif not list_inclouded:
            answer = answer.upper()

    # hardcode
        # Default
        if answer == dict_app["stored_answers"]["default"]:
            return answer
        # ! Default
        # Quit
        elif answer == dict_app["stored_answers"]["quit"]:
            quit()
         # ! Quit
    # ! hardcode
            
        for i in range(len(answer_options)):
            if answer == answer_options[i]:
                return answer
            else:
                was_wrong = True
               


def request_mode():
    answer = basic_request(texts["questions"]["mode"], texts["answer_options"]["mode"])
    if answer == dict_app["stored_answers"]["simple_mode"]:
        dict_app["default_settings"]["mode"] = answer
        dict_app["session_settings"]["mode"] = answer
        print(dict_app["stored_names"]["divisor"] + "Sie nutzen nun den " + dict_app["stored_names"]["mode"][answer])
    elif answer == dict_app["stored_answers"]["explain_mode"]:
        dict_app["default_settings"]["mode"] = answer
        dict_app["session_settings"]["mode"] = answer
        print(dict_app["stored_names"]["divisor"] + "Sie nutzen nun den " + dict_app["stored_names"]["mode"][answer])
    else:
        dict_app["session_settings"]["mode"] = dict_app["default_settings"]["mode"]
        print(dict_app["stored_names"]["divisor"] + "Sie nutzen nun den " + dict_app["stored_names"]["mode"][dict_app["default_settings"]["mode"]])


def request_session():
    answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["session"], texts["answer_options"]["sessions"])
    if answer == dict_app["stored_answers"]["default"]:
        if dict_app["default_settings"]["session"] == "":
            print(dict_app["stored_names"]["divisor"] + "Sie fahren nun ohne Session fort")
        else:
            dict_app["session_settings"]["session"] = dict_app["default_settings"]["session"]
            print(dict_app["stored_names"]["divisor"] + "Sie haben die Session \"" + dict_app["default_settings"]["session"] + "\" gewählt")

    elif answer == dict_app["stored_answers"]["continue"]:
        print(dict_app["stored_names"]["divisor"] + "Sie fahren nun ohne Session fort")

    else:
        print(dict_app["stored_names"]["divisor"] + "Sie haben die Session \"" + answer + "\" gewählt")
        dict_app["default_settings"]["session"] = answer
        dict_app["session_settings"]["session"] = answer


def request_action():
    answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["action"], texts["answer_options"]["action"])
    if answer == dict_app["stored_answers"]["default"]:
        dict_app["session_settings"]["action"] = dict_app["default_settings"]["action"]
        print(dict_app["stored_names"]["divisor"] + "Sie haben die Option \"" + dict_app["stored_names"]["action"][dict_app["default_settings"]["action"]] + "\"(" + dict_app["default_settings"]["action"] + ") gewählt")
    else:
        dict_app["session_settings"]["action"] = answer
        dict_app["default_settings"]["action"] = answer
        print(dict_app["stored_names"]["divisor"] + "Sie haben die Option \"" + dict_app["stored_names"]["action"][dict_app["default_settings"]["action"]] + "\"(" + dict_app["default_settings"]["action"] + ") gewählt")


def request_kind_of_key():
     if dict_app["session_settings"]["action"] == dict_app["stored_answers"]["create"]:
         answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["kind_of_key"]["create"], texts["answer_options"]["kind_of_key"])
         if answer == dict_app["stored_answers"]["default"]:
             dict_app["session_settings"]["requested_key"] = dict_app["default_settings"]["requested_key"]
             print(dict_app["stored_names"]["divisor"] + "Sie haben \"" + dict_app["stored_names"]["kind_of_key"][dict_app["session_settings"]["requested_key"]] + "\"(" + dict_app["session_settings"]["requested_key"] + ") gewählt")
         else:
             dict_app["session_settings"]["requested_key"] = answer
             dict_app["default_settings"]["requested_key"] = answer
             print(dict_app["stored_names"]["divisor"] + "Sie haben \"" + dict_app["stored_names"]["kind_of_key"][dict_app["session_settings"]["requested_key"]] + "\"(" + dict_app["session_settings"]["requested_key"] + ") gewählt")
     elif dict_app["session_settings"]["action"] == dict_app["stored_answers"]["use"]:
         answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["kind_of_key"]["use"], texts["answer_options"]["kind_of_key"])
         if answer == dict_app["stored_answers"]["default"]:
             dict_app["session_settings"]["requested_key"] = dict_app["default_settings"]["requested_key"]
             print(dict_app["stored_names"]["divisor"] + "Sie haben \"" + dict_app["stored_names"]["kind_of_key"][dict_app["session_settings"]["requested_key"]] + "\"(" + dict_app["session_settings"]["requested_key"] + ") gewählt")
         else:
             dict_app["session_settings"]["requested_key"] = answer
             dict_app["default_settings"]["requested_key"] = answer
             print(dict_app["stored_names"]["divisor"] + "Sie haben \"" + dict_app["stored_names"]["kind_of_key"][dict_app["session_settings"]["requested_key"]] + "\"(" + dict_app["session_settings"]["requested_key"] + ") gewählt")


def request_key_size():
    if dict_app["session_settings"]["action"] == dict_app["stored_answers"]["create"]:
        answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["key_size"], texts["answer_options"]["key_size"])
        if answer == dict_app["stored_answers"]["default"]:
            dict_app["session_settings"]["key"]["size"] = dict_app["default_settings"]["key"]["size"]
            print(dict_app["stored_names"]["divisor"] + "Ihre Keys werden " + dict_app["session_settings"]["key"]["size"] + " bit gross" )
        else:
            dict_app["session_settings"]["key"]["size"] = str(answer)
            dict_app["default_settings"]["key"]["size"] = str(answer)
            print(dict_app["stored_names"]["divisor"] + "Ihre Keys werden " + dict_app["session_settings"]["key"]["size"] + " bit gross" )


# ! Requests

# Cryptography



def creat_public_private_key():
    print("Keys werden erstellt...")
    key = RSA.generate(1024)

    private_key = key.export_key("PEM")
    public_key = key.publickey().export_key("PEM")
    print(private_key)
    print(public_key)
    
    #public_key, private_key = rsa.newkeys(int(dict_app["session_settings"]["key"]["size"]))
    #private_key.exp1()


# ! Cryptography

# Else


def log():
    pprint("dictApp: " + str(dict_app))
    pprint("texts: " + str(texts))


def print_start_message():
    ascii_welcome = pyfiglet.figlet_format("En / Decryption")
    print(ascii_welcome)
    print(texts["start_message"])


def print_parting(typ, amount):
    if typ == "normal":
        print(texts["parting"]["normal"] * amount)
    elif typ == "wrong":
        print(texts["parting"]["wrong"] * amount)
    else:
        error("print_parting")
    
def wait(secs):
    Time.sleep(secs)


def error(message):
    print("Something went wrong! Try to restart the programm")
    print(message)
    exit()


# ! Else

#fun1()  # success
start(0)
