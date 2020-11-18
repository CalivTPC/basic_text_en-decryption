from pprint import pprint  # log()
import pyfiglet  # print_start_text()
import time  # wait()
Time = time  # wait()
# Crypto
from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet
#import rsa
#import base64

# Crypto


# Values

dict_app = {

    "session_settings": {  #Setting for the current session
        "mode": "",
        "session": "",
        "action": "",
        "action_use": "",
        "requested_key": "",
        "message": "",
        "key": {
            "session": "",
            "private": "",
            "public": "",
            "size": "",
        }
    },

    "default_settings": {  #Last used setting
        "mode": "E",
        "session": "",
        "action": "N",
        "action_use": "V",
        "requested_key": "S",
        "key": {
            "size": "4096",
        }
    },

    "keys": {
        "sizes": [
            "1024", "2048", "3072", "4096", "8192", "16384"
        ],
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
        "session": "S",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "encrypt": "V",
        "decrypt": "E"
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
        "action_use": {
            "V": "Verschlüssen",
            "E": "Entschlüsseln",
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
        "mode": "Der " + dict_app["stored_names"]["mode"][dict_app["stored_answers"]["simple_mode"]] + " ist für Leute die genau wissen, was sie tuen. \n"
            "Der "+ dict_app["stored_names"]["mode"][dict_app["stored_answers"]["explain_mode"]] + " ist für Leute welche gerne noch ein paar Zusatzinformationen haben. \n"
            "Wollen sie den " + dict_app["stored_names"]["mode"][dict_app["stored_answers"]["simple_mode"]] + "(" + dict_app["stored_answers"]["simple_mode"] + ") nutzen oder wollen sie den " + dict_app["stored_names"]["mode"][dict_app["stored_answers"]["explain_mode"]] + "(" + dict_app["stored_answers"]["explain_mode"] + ") Nutzen: ",
        dict_app["stored_answers"]["simple_mode"]: {  # simple_mode
            "session": "hier ist eine Liste der bereits erstellten Sessions. \n" +
                        str(dict_app["sessions"]) + "\n" +
                        "Bitte geben sie den namen der session an welche sie nutzen wollen" + dict_app["stored_names"]["optional_symbol"] + ": ",
            "action": "Möchten sie Keys " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["use"]] + "(" + dict_app["stored_answers"]["use"] + ")" + " oder " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["create"]] + "(" + dict_app["stored_answers"]["create"] + ") ",
            "action_use": "Möchten sie Text Verschlüsseln(" + dict_app["stored_answers"]["encrypt"] + ") oder Entschlüsseln(" + dict_app["stored_answers"]["decrypt"] + "): ",
            "kind_of_key": {
                "create": "Möchten Sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["private/public"]] + "\"(" + dict_app["stored_answers"]["private/public"] + ") erstellen oder möchten sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["session"]] + "\"(" + dict_app["stored_answers"]["session"] + ") erstellen? ",
                "use": "Möchten Sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["private/public"]] + "\"(" + dict_app["stored_answers"]["private/public"] + ") nutzen oder möchten sie einen \"" + dict_app["stored_names"]["kind_of_key"][dict_app["stored_answers"]["session"]] + "\"(" + dict_app["stored_answers"]["session"] + ") nutzen? "
                },
            "key_size":
                "Bitte geben sie an wie gross ihr Key sein soll die haben folgende Optionen \n"
                "\"1024\"(" + dict_app["stored_answers"]["1"] + "), \"2048\"(" + dict_app["stored_answers"]["2"] + "), \"3072\"(" + dict_app["stored_answers"]["3"] + "), \"4096\"(" + dict_app["stored_answers"]["4"] + "), \"8192\"(" + dict_app["stored_answers"]["5"] + "), \"16384\"(" + dict_app["stored_answers"]["6"] + "): ",

            "create_key": "Keys werden erstellt... ",
            "key": {
                "session": "Bitte geben sie einen gültigen Session Key an: ",
                "private": "Bitte geben sie einen gültigen private Key an: ",
                "public": "Bitte geben sie einen gültigen public Key an: ",
            },
            "message": {
                "to_decrypt": "Bitte geben Sie die verschlüsselte Nachricht an: ",
                "to_encrypt": "Bitte geben Sie die Nachricht ein welche sie verschlüsseln möchten: ",
            },
        },
        dict_app["stored_answers"]["explain_mode"]: {  # explain_mode
            "session": "Sie können später Sessions speichern. Was so viel heisst wie sie können den private/public/session Key speichern \n"
                        "hier ist eine Liste der bereits erstellten Sessions. \n" +
                        str(dict_app["sessions"]) + "\n" +
                        "Bitte geben sie den namen der session an welche sie nutzen wollen" + dict_app["stored_names"]["optional_symbol"] + ": ",
            "action": "Unter der auswahl \"" + dict_app["stored_names"]["action"][dict_app["stored_answers"]["create"]] + "\"(" + dict_app["stored_answers"]["create"] + ")" + " werden sie die Möglichkeit habe Private/Public/Session Keys zu erstellen.\n"
                "Mit der Option \"" + dict_app["stored_names"]["action"][dict_app["stored_answers"]["use"]] + "\"(" + dict_app["stored_answers"]["use"] + ")" + " Können sie Private/Public/Session Keys Nutzen um texte zu ver/endschlüsseln. \n"
                "Möchten sie Keys " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["use"]] + "(" + dict_app["stored_answers"]["use"] + ")" + " oder " + dict_app["stored_names"]["action"][dict_app["stored_answers"]["create"]] + "(" + dict_app["stored_answers"]["create"] + ") ",
                "action_use": "Möchten sie Text Verschlüsseln(" + dict_app["stored_answers"]["encrypt"] + ") oder Entschlüsseln(" + dict_app["stored_answers"]["decrypt"] + "): ",

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
                "1024: 0.03 sec \t 2048: 0.05 sec \t 3072:  0.15 sec \n"
                "4096: 0.25 sec \t 8192: 11.5 sec \t 16384: 39.1 sec \n"
                "Bitte geben sie an wie gross ihr Key sein soll die haben folgende Optionen \n"
                "\"1024\"(" + dict_app["stored_answers"]["1"] + "), \"2048\"(" + dict_app["stored_answers"]["2"] + "), \"3072\"(" + dict_app["stored_answers"]["3"] + "), \"4096\"(" + dict_app["stored_answers"]["4"] + "), \"8192\"(" + dict_app["stored_answers"]["5"] + "), \"16384\"(" + dict_app["stored_answers"]["6"] + "): ",

            "key": {
                "session": "Ein gültiger Session Key muss 32bit gross sein. \n" 
                    "Bitte geben sie einen gültigen Session Key an: ",
            },
            
            "message": {
                "to_decrypt": "Bitte geben Sie die verschlüsselte Nachricht an: ",
                "to_encrypt": "Bitte geben Sie die Nachricht ein welche sie verschlüsseln möchten: ",
            },
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
            dict_app["stored_answers"]["explain_mode"], dict_app["stored_answers"]["simple_mode"]
        ],

        "sessions": [
            dict_app["stored_answers"]["continue"], dict_app["sessions"]
        ],
        "action": [
            dict_app["stored_answers"]["create"], dict_app["stored_answers"]["use"]
        ],
        "action_use": [
            dict_app["stored_answers"]["encrypt"], dict_app["stored_answers"]["decrypt"]
        ],
        "kind_of_key": [
            dict_app["stored_answers"]["private/public"], dict_app["stored_answers"]["session"]
        ],
        "key_size": [
            dict_app["stored_answers"]["1"], dict_app["stored_answers"]["2"], dict_app["stored_answers"]["3"], dict_app["stored_answers"]["4"], dict_app["stored_answers"]["5"], dict_app["stored_answers"]["6"] 
        ],
    },
    "start_message": "Sie können mithilfe von \"" + dict_app["stored_answers"]["default"] + "\" die zuletzt genutzte Option wählen. \n"
        "Eine leer Eingabe wird nur akzeptiert wenn, die Auswahl optional ist, was man am \"" + dict_app["stored_names"]["optional_symbol"] + "\" erkennen kann.\n"
        "Mit \"" + dict_app["stored_answers"]["quit"] + "\" kann das Programm jederzeit beendet werden.",
    
    "parting": {
        "normal": "-",
        "wrong": "=",
    },
}

# ! Values

# Start


def start():
    # restore_data()
    # Requests

    interactive_methods = [
        print_start_message,
        request_mode,
        request_session_use,
        request_action,
    ]
    for i in range(len(interactive_methods)):
            wait(.2)
            interactive_methods[i]()
            wait(.2)
            print_parting("normal", 114)

    # ! Requests

    if dict_app["session_settings"]["action"] == dict_app["stored_answers"]["create"]:
        start_create()
    elif dict_app["session_settings"]["action"] == dict_app["stored_answers"]["use"]:
        start_use()

    save()


def start_create():
    interactive_methods = [
        request_kind_of_key_create,
        request_key_size
    ]


    for i in range(len(interactive_methods)):
        if dict_app["session_settings"]["requested_key"] == dict_app["stored_answers"]["session"]:
            continue
        wait(.2)
        interactive_methods[i]()
        wait(.2)
        print_parting("normal", 114)

    if dict_app["session_settings"]["requested_key"] == dict_app["stored_answers"]["private/public"]:
        create_public_private_key()
    elif dict_app["session_settings"]["requested_key"] == dict_app["stored_answers"]["session"]:
        create_session_key()    

    print("not written yet")


def start_use():
    interactive_methods = [
        request_kind_of_key_use,
        request_action_use,
        request_message,
    ]

    for i in range(len(interactive_methods)):
        wait(.2)
        interactive_methods[i]()
        wait(.2)
        print_parting("normal", 114)
    
    if dict_app["session_settings"]["requested_key"] == dict_app["stored_answers"]["private/public"]:
        request_private_public_key()
    elif dict_app["session_settings"]["requested_key"] == dict_app["stored_answers"]["session"]:
        request_session_key()
    
    print("not written yet")
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

def basic_request(text, answer_options):
    was_wrong = False
    list_inclouded = False
    while True:
        if was_wrong:
            print_parting("wrong", 114)
            print("Möglich Antworten: " + str(answer_options))
            print_parting("wrong", 114)

        answer = input(text)

    # hardcode
        # Default
        if answer.upper() == dict_app["stored_answers"]["default"]:
            return answer.upper()
        # ! Default
        # Quit
        elif answer.upper() == dict_app["stored_answers"]["quit"]:
            quit()
         # ! Quit
    # ! hardcode

        if includes_list(answer_options):
            list_inclouded = True
            answer_options = handle_list_basic_request(answer_options)

        elif not list_inclouded:
            answer = answer.upper()
            
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


def request_session_use():
    answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["session"], texts["answer_options"]["sessions"])
    if answer == dict_app["stored_answers"]["default"]:
        if dict_app["default_settings"]["session"] == "":
            print(dict_app["stored_names"]["divisor"] + "Sie fahren nun ohne Session fort")
        else:
            dict_app["session_settings"]["session"] = dict_app["default_settings"]["session"]
            print(dict_app["stored_names"]["divisor"] + "Sie haben die Session \"" + dict_app["default_settings"]["session"] + "\" gewählt")
#
#    elif answer == "kek":
#        print("tut mir leid. Kuchen ist kein geigneter Namen für eine Session ")
#    elif answer == "latest":
#        print("Gratuliere du hast es geschaft den einzigen Namen zu wählen, welcher vom Programm nicht zugelassen ist! ")
#
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


def request_kind_of_key_create():
    answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["kind_of_key"]["create"], texts["answer_options"]["kind_of_key"])
    if answer == dict_app["stored_answers"]["default"]:
        dict_app["session_settings"]["requested_key"] = dict_app["default_settings"]["requested_key"]
        print(dict_app["stored_names"]["divisor"] + "Sie haben \"" + dict_app["stored_names"]["kind_of_key"][dict_app["session_settings"]["requested_key"]] + "\"(" + dict_app["session_settings"]["requested_key"] + ") gewählt")
    else:
        dict_app["session_settings"]["requested_key"] = answer
        dict_app["default_settings"]["requested_key"] = answer
        print(dict_app["stored_names"]["divisor"] + "Sie haben \"" + dict_app["stored_names"]["kind_of_key"][dict_app["session_settings"]["requested_key"]] + "\"(" + dict_app["session_settings"]["requested_key"] + ") gewählt")
     

def request_kind_of_key_use():
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
            dict_app["session_settings"]["key"]["size"] = dict_app["keys"]["sizes"][(int(answer) - 1)]
            dict_app["default_settings"]["key"]["size"] = dict_app["keys"]["sizes"][(int(answer) - 1)]
            print(dict_app["stored_names"]["divisor"] + "Ihre Keys werden " + dict_app["session_settings"]["key"]["size"] + " bit gross" )


def request_action_use():
    answer = basic_request(texts["questions"][dict_app["session_settings"]["mode"]]["action_use"], texts["answer_options"]["action_use"])
    if answer == dict_app["stored_answers"]["default"]:
        dict_app["session_settings"]["action_use"] = dict_app["default_settings"]["action_use"]
        print(dict_app["stored_names"]["divisor"] + "Sie haben die Option \"" + dict_app["stored_names"]["action"][dict_app["default_settings"]["action"]] + "\"(" + dict_app["default_settings"]["action"] + ") gewählt")
    else:
        dict_app["session_settings"]["action_use"] = answer
        dict_app["default_settings"]["action_use"] = answer
        print(dict_app["stored_names"]["divisor"] + "Sie haben die Option \"" + dict_app["stored_names"]["action_use"][dict_app["default_settings"]["action_use"]] + "\"(" + dict_app["default_settings"]["action_use"] + ") gewählt")


def request_session_key():
    while True:
        answer = input(texts["questions"][dict_app["session_settings"]["mode"]]["key"]["session"])
        if answer == dict_app["stored_answers"]["quit"]:
            quit()
        try:
            Fernet(answer)
            texts["questions"][dict_app["session_settings"]["mode"]]["key"]["private_public"] = answer
            break
        except:
            print("der angegebene Key ist ungültig")


def request_private_public_key():
    while True:
        answer = input(texts["questions"][dict_app["session_settings"]["mode"]]["key"]["session"])
        if answer == dict_app["stored_answers"]["quit"]:
            quit()
        try:
            Fernet(answer)
            texts["questions"][dict_app["session_settings"]["mode"]]["key"]["session"] = answer
            break
        except:
            print("der angegebene Key ist ungültig")


def request_message():
    if dict_app["session_settings"]["action_use"] == dict_app["stored_answers"]["encrypt"]:
        answer = input(texts["questions"][dict_app["session_settings"]["mode"]]["message"]["to_encrypt"])
    elif dict_app["session_settings"]["action_use"] == dict_app["stored_answers"]["decrypt"]:
        answer = input(texts["questions"][dict_app["session_settings"]["mode"]]["message"]["to_decrypt"])


# ! Requests



# Cryptography



def create_public_private_key():
    print("Abhängig von der Grösse, könnte dies ein Weilchen dauern.")
    print("Keys werden erstellt...")
    t0 = time.time()
    key = RSA.generate(int(dict_app["session_settings"]["key"]["size"]))
    t1 = time.time() - t0
    private_key = key.export_key("PEM")
    public_key = key.publickey().export_key("PEM")
    print(str(private_key, "utf8"))
    print(str(public_key, "utf8"))

    print("das erstellen der Keys hat " + str(t1) + " sec gedauert")
    
    file_session_key = open("keys/private_public/latest/public.txt", "w")
    file_session_key.write(str(public_key, "utf8"))
    file_session_key.close

    file_session_key = open("keys/private_public/latest/private.txt", "w")
    file_session_key.write(str(private_key, "utf8"))
    file_session_key.close


def use_public_private_key():
    key = RSA.importKey("keys/private_public/latest/private.txt", "keys/private_public/latest/public.txt")



def create_session_key():
    if dict_app["session_settings"]["mode"] == dict_app["stored_answers"]["explain_mode"]:
        print("Der Session Key ist immer 32bit gross. Immernoch ziemlich sicher aber ein Witz im vergleich zum Private/Public Key")
    print("Keys werden erstellt...")
    key = Fernet.generate_key()
    print(str(key, "utf8"))
    file_session_key = open("keys/session/latest/session.txt", "w")
    file_session_key.write(str(key, "utf8"))
    file_session_key.close


def encrypt_session_key():
    key = Fernet(dict_app["session_settings"]["key"]["session"])


def decrypt_session_key():
    None
    
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

start()
