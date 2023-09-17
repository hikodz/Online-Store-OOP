from json import loads, dumps
import requests  
import json
import webbrowser as web
from simple_chalk import chalk
import pyfiglet as pyf
from inquirer import Text, prompt, List
import time 
import os
from random import randint
import smtplib
from random import randint
from re import findall
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import colorama
from  pycountry import countries
from datetime import datetime
from twilio.rest import Client
from urllib import request

Red = "\033[1;31m"  #
Green = "\033[1;32m"  # 'هGreen
Yellow = "\033[1;33m"  # Yellow
Blue = "\033[1;34m"  # Blue
Purple = "\033[1;35m"  # Purple
Cyan = "\033[1;36m"  # Cyan
White = "\033[1;37m"  # Whit

B = colorama.Fore

card_regex_patterns = {
    "Visa": r'^4[0-9]{12}(?:[0-9]{3})?$',
    "MasterCard": r'^5[1-5][0-9]{14}$',
    "American Express": r'^3[47][0-9]{13}$',
    "Discover": r'^6011[0-9]{12}$',
    "JCB": r'^(?:2131|1800|35\d{3})\d{11}$',
    "Diners Club": r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
    "Maestro": r'^(?:5[0678]\d\d|6304|6390|67\d\d)\d{8,15}$',
    "UnionPay": r'^62[0-9]{14,17}$',
    "Amex Card": r"^3[47][0-9]{13}$",
    "BCGlobal": r"^(6541|6556)[0-9]{12}$",
    "Carte Blanche Card": r"^389[0-9]{11}$",
    "Diners Club Card": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
    "Discover Card": r"^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$",
    "Insta Payment Card":r" ^63[7-9][0-9]{13}$",
    "Visa Master Card": r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$",
    "Visa Master Card": r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$"
}

#! here api and id serach engine google website please be cerfull for use this information access
API = "AIzaSyBF9neN0flONQNlOrMnzzgnsQcmtSmmTlw"
ID = "1280c2d1a93454710"
#! Path data users and books in file json you can change bath :
message_path = r"/Users/HikoDz/Desktop/codezilla-cours/Section 20/project-online-store/message-email/message-code-ver.txt"
create_path = r"/Users/HikoDz/Desktop/codezilla-cours/Section 20/project-online-store/message-email/message-create-account.txt"
product_path = r'/Users/HikoDz/Desktop/codezilla-cours/Section 20/project-online-store/shop-data.json'
user_path = r'/Users/HikoDz/Desktop/codezilla-cours/Section 20/project-online-store/user-data.json'
#📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛📛
#! load data from json file
with open(create_path, 'r') as cr:
    create = cr.read()

with open(message_path, 'r') as ms:
    ver = ms.read()

with open(product_path, 'r') as dbFTC : 
    load_product = loads(dbFTC.read())

with open(user_path, 'r') as dbUS : 
    load_user = loads(dbUS.read())
#🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁
class EffectText():

    def animate_rocket(self):
        distance_from_top = 20
        while True:
            print("\n" * distance_from_top)
            print("          /\         ")
            print("          ||        ")
            print("          ||        ")
            print("         /||\        ")
            print("         save       ")

            time.sleep(0.2)
            os.system('clear')  
            distance_from_top -= 1
            if distance_from_top < 0:
                distance_from_top = 20
    def animate_text(self, text):
        number_of_characters=1
        while number_of_characters < len(text):
            print("\n")
            print(text[0:number_of_characters])
            number_of_characters += 1
            if number_of_characters > len(text):
                number_of_characters = 0
            time.sleep(0.05)
    def animate_die(self):
        die= ["   \n O \n   "]   #1
        die.append("  O\n   \n0  ")   #2
        die.append("O  \n 0 \n  0")   #3
        die.append("O 0\n   \n0 0")   #4
        die.append("O 0\n 0 \n0 0")   #5
        die.append("O 0\n0 0\n0 0")   #6
        for roll in range(0,15):
            os.system('clear')
            print("\n")
            number = randint(0,5)
            print(die[number])
            time.sleep(0.2) 
            return
    def animate_space_invader(self):
        distance_from_top = 0
        distance_from_left_side = 0
        step = 1
        while True:
            print("\n" * distance_from_top)
            print((" " * distance_from_left_side) + "_^_")
            print((" " * distance_from_left_side) + "/|\\")
            distance_from_left_side += step
            if distance_from_left_side > 20 or distance_from_left_side <= 0:
                step = -step 
                distance_from_top += 2
                if distance_from_top > 20:
                    distance_from_top = 0
                    distance_from_left_side = 0
                    step = 1
            time.sleep(0.05)
            os.system('clear')  



class UserSignRegistration():
    def __init__(self):
        self.login = False
        self.full_name = "..."
        self.username = "..."
        self.email = "..."
        self.password = "..."
        self.id = "..."
        self.method = False
        self.password = "..."
        self.plan = "..."
        self.code_discount = "..."
        self.card = "..."
        self.number_card = "..."
        self.Members = "..."
    #! Build function 
    def confirm_the_operation(self):
        operation_option = prompt([
                                List(
                                        "operation_option",
                                        message="Are you sure about that",
                                        choices=[
                                            "[1] Yes",
                                            "[2] No"
                                            ]
                                    )
                                    ])
        return operation_option["operation_option"] 
    def send_message(self, email=False, Phone=False, name=False, Gmail=False, sms=False, confirm=False ):
        verification_code = randint(10000, 100000)
        if Gmail:
            message = ver.replace('Client', name).replace('randint_code', str(verification_code))
            sender = "medbloul2002@gmail.com"
            password = "raqxaazztghlnxzf"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, password)
            print(chalk.green(f'Dear {name} Check Your Boxemail'))
            server.sendmail(sender, email, message)
        elif sms:
            account_sid = 'AC2f00dbba1abb310962563c0a796d0a37'
            auth_token = 'a6d564868ad2b79850e43f2d4d211806'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                        body=f"\nCodezilla Online Store\nVerification Code: {verification_code}",
                        from_='+15107616954',
                        to=Phone
                        )
        while True:
                check = input(f"{Yellow}[🫴] Verification Code: ")
                if str(verification_code) == check:
                    if confirm:    
                        message = create.replace('client', name)
                        sender = "medbloul2002@gmail.com"
                        password = "raqxaazztghlnxzf"
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(sender, password)
                        server.sendmail(sender, email, message)
                        print(chalk.green(f'Dear {name} Check Your Boxemail one more time,Please! And login'))
                    print('operation accomplished Successfully')
                    return
                else:
                    print(chalk.red("Wrong Code"))
                    continue
    def log_in(self, Target="Data_Users"):
        while True:
            information2 = prompt([
                    Text('Username', message=chalk.bgBlack("Username or Email(press enter for back option)"))
                ])
            if len(information2['Username']) == 0:
                return False
            information = prompt([
                    Text('Password', message=chalk.bgBlack("Password Forgot your password? Reset it(press enter)"))
                ])
            if  len(information['Password']) == 0:
                while True:
                    reset = prompt([
                        Text('email', message=chalk.bgBlack("Enter email for reset"))
                
                    ])  
                    confirm = self.confirm_the_operation()
                    if confirm == "[1] Yes":
                        for user in load_user[Target]:
                            if reset['email'] in user['Info']:
                                self.send_message(email=reset['email'], name=user['Info'][0], Gmail=True)
                                while True:
                                    new_password = prompt([
                                    Text('Password', message=chalk.bgBlack("New Password(Minimum 8 characters)")),
                                    Text('Confirm', message=chalk.bgBlack("Confirm New password"))
                                    ])
                                    confirm = self.confirm_the_operation()
                                    if confirm == "[1] Yes":
                                        if new_password['Password'] == new_password['Confirm']:
                                            user["Password"] = new_password['Password']
                                            print('Reset successfully ✅')
                                            self.save_to_json()
                                            return
                                    print('Please enter a correct password')
                                    continue
                            
                        print(chalk.red('Invalid email account please SignUp!!'))
                        return
                    else:
                        continue
            for user in load_user[Target]:
                if  Target =="Data_Users":
                    if (information2['Username'] in user['Info']) and (information['Password'] == user['Password']) :
                        self.login = True
                        self.username = user["Info"][0]
                        self.email = user["Info"][1]
                        self.password = user["Password"]
                        self.id = user["ID"]
                        self.full_name = user["Name"]
                        self.method = True  if user["Payment_Method"] else False
                        self.password = user["Password"]
                        self.plan = user["Plan"]
                        self.code_discount = user["Code_Discount"]
                        self.card = [card[5]for card in user["Payment_Method"]]
                        self.number_card = [card[0]for card in user["Payment_Method"]]
                        print(chalk.green(f'Login successfully ✅'))
                        return
                elif Target =="Admin_DB":
                    if (information2['Username'] in user['Info']) and (information['Password'] == user['Password']):    
                        self.login = True
                        self.username = user["Info"][0]
                        self.email = user["Info"][1]
                        self.password = user["Password"]
                        self.Members = user["Members"]
                        print(chalk.green(f'Login successfully ✅'))
                        return
            print(chalk.red('Please enter correct information'))
            continue
    def create_account(self):
        while True:
            information = prompt([
                Text('Name', message=chalk.bgBlack("Full name")),
                Text('Username', message=chalk.bgBlack("Username")),
                Text('Gmail', message=chalk.bgBlack("Eamil")),
                Text('Phone', message=chalk.bgBlack("Number Phone(+[Country Number]123456789)")),
                Text('Password', message=chalk.bgBlack("Password(Minimum 8 characters)")),
                Text('Confirm', message=chalk.bgBlack("Confirm password"))
            ])
            regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            if len(information['Name']) < 3 or len(information['Username']) < 3:
                print(chalk.red("Please check your information"))
                continue
            elif information['Password'] != information['Confirm'] or len(information['Password']) < 8:
                print(chalk.red("Please check your password(Minimum 8 characters)"))
                continue
            elif not findall(regex, information['Gmail']):
                print(chalk.red("Invalid email"))
                continue
            while True:
                send_option = prompt([
                                List(
                                        "send_option",
                                        message="Send Verification Code By",
                                        choices=[
                                            "[1] SMS",
                                            "[2] GMAIL"
                                            ]
                                    )
                                    ])
                if  send_option["send_option"] == "[1] SMS" and information['Phone'] != "+213562278350":
                    print(f'{Yellow}Unfortunately, the site we use requires verifying the number in free accounts\n{Green}but the method is effective with the verified number')
                    continue
                elif send_option["send_option"] == "[2] GMAIL":
                    self.send_message(email=information['Gmail'], name=information['Name'], Gmail=True, confirm=True)
                    break
                elif send_option["send_option"] == "[1] SMS" and information['Phone'] == "+213562278350":
                    self.send_message(email=information['Gmail'], Phone="+213562278350", sms=True, name=information['Name'])
                    break

            load_user['Admin_DB'][0]['Members'] += 1
            new_user = {
            "Name": information['Name'],
            "Info": [
                information['Username'],
                information['Gmail']
            ],
            "ID": load_user['Admin_DB'][0]['Members'] ,
            "Password": information['Password'],
            "Payment_Method": [],
            "discout_card": {
                "valid": [],
                "invalid": []
            },
            "whell of fortune": True,
            "Plan" : "Free",
            "Code_Discount" : False
                    }
            load_user["Data_Users"].append(new_user)
            self.save_to_json()
            return
    def Add_Payment(self):
        while True:    
            Card_Number = prompt([
                    Text('Card Number', message=chalk.bgBlack("Card Number(Press enter to cancel)")),
                ])
            if len(Card_Number['Card Number']) == 0:
                print('Cancel successfully ✅')
                return
            for name_card, regex_patterns in card_regex_patterns.items():
                if findall(regex_patterns, Card_Number['Card Number']):
                    print(f'You have entered a card type [+] - {Yellow} {name_card} ')
                    info_payment = prompt([
                    Text('Expiration', message=chalk.bgBlack("Expiration (MM/YY)")),
                    Text('CVC', message=chalk.bgBlack("CVC")),
                    Text('Name', message=chalk.bgBlack("Name")),
                    Text('Country', message=chalk.bgBlack("Country"))
                ])
                    show_Invalid = False
                    format_ex = False
                    try:
                        month, year = map(int, info_payment['Expiration'].split('/'))
                        expiration_date = datetime(year=2000 + year, month=month, day=1)
                        current_date = datetime.now()
                        if expiration_date <= current_date:
                            format_ex = True
                    except ValueError:
                        format_ex = True
                    if format_ex :
                        show_Invalid = True
                    elif  len(info_payment['CVC'])!=3 or not info_payment['CVC'].isnumeric():
                        show_Invalid = True
                    elif len(info_payment['Name'])< 4:
                        show_Invalid = True
                    elif not countries.get(name=info_payment['Country']):
                        show_Invalid = True
                    if show_Invalid:
                        break
                    confirm = self.confirm_the_operation()
                    if confirm == "[1] Yes":
                        for user in load_user["Data_Users"]:
                            if user["ID"] == self.id:
                                user["Payment_Method"].append([
                                                                Card_Number['Card Number'],
                                                                info_payment['Expiration'],
                                                                info_payment['CVC'],
                                                                info_payment['Name'],
                                                                info_payment['Country'],
                                                                name_card
                                                                ])
                                self.method = True 
                                print(chalk.green("Added Successfully ✅"))
                                self.card = [card[5]for card in user["Payment_Method"]]
                                self.number_card = [card[0]for card in user["Payment_Method"]]
                                self.save_to_json()
                                return True
                    break
                    
            print(chalk.red("Invalid Card"))
            continue

    def purchase_history(self):
        ...

    def advance_setting(self):
        while True:
            option = prompt([
            List(
                    "Advance",
                    message="What you need?",
                    choices=["Change Password", "Show Payment Method", "Change Email", "Change Plan Account", "Show My information",  "Exit 🔌"],
                ),
                ])
            if option["Advance"] == "Change Password":
                while True:
                    New_password = prompt([
                        Text('password', message=chalk.bgBlack("Enter current password")),
                        Text('N_Password', message=chalk.bgBlack("New Password(Minimum 8 characters)")),
                        Text('Confirm', message=chalk.bgBlack("Confirm New Password"))
                    ])
                    if New_password['password'] != self.password or New_password['N_Password'] != New_password['Confirm'] or len(New_password['N_Password']) < 8 :
                        print(chalk.red('Invalid Information!!'))
                        continue
                    for user in load_user["Data_Users"]:
                        if self.username in user["Info"]:
                            user["Password"] = New_password['N_Password']
                            self.password = New_password['N_Password']
                            self.save_to_json()
                            print('Reset successfully ✅')
                            
                    break
            elif option["Advance"] == "Show Payment Method":
                if self.method:
                    for user in load_user["Data_Users"]:
                        if user["ID"] == self.id:
                            for method in user["Payment_Method"]:
                                print(f" {Red}{'+'*20}\
                                    \n{Yellow}[+]Card number: {Cyan}****{method[0][-4:]}\
                                    \n{Yellow}[+]Expiration: {Cyan}{method[1]}\
                                    \n{Yellow}[+]CVC: {Cyan}{method[2]}\
                                    \n{Yellow}[+]Type: {Cyan}{method[5]}\
                                    \n{Yellow}[+]Name: {Cyan}{method[3].title()}\
                                    \n{Yellow}[+]Country: {Cyan}{method[4].title()}\
                                    \n {Red}{'+'*20}")
                            edit_method = prompt([
                                List(
                                        "edit",
                                        message="I need",
                                        choices=["Remove Payment Method", "Add Payment Method", "Exit"],
                                    ),
                                    ])
                            if edit_method["edit"] == "Remove Payment Method":
                                remove = prompt([
                                        List(
                                                "remove",
                                                message="I need",
                                                choices=[f'{self.number_card.index(method)+1}- ****{method[-4:]}' for method in self.number_card]
                                            ),
                                            ])
                                user["Payment_Method"].pop(int(remove["remove"][0])-1)
                                self.save_to_json()
                                self.number_card = [card[0]for card in user["Payment_Method"]]
                                self.method = True  if user["Payment_Method"] else False
                                print("Remove successfully ✅")
                                break
                            elif edit_method["edit"] == "Add Payment Method":
                                self.Add_Payment()
                                continue
                            elif edit_method["edit"] == "Exit":
                                continue
                else:
                    print('Please Add Payment Method')
                    self.Add_Payment()
                    continue
            elif option["Advance"] == "Change Email":
                while True:
                    New_email = prompt([
                            Text('new', message=chalk.bgBlack("Enter new email"))
                        ])
                    regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
                    if not findall(regex, New_email['new']):
                        print(chalk.red("Invalid email"))
                        continue
                    else:
                        for user in load_user["Data_Users"]:
                            if user["ID"] == self.id:
                                user["Info"][1] = New_email['new']
                        self.email = New_email['new']
                        self.save_to_json()
                        print(chalk.green("Change email successfully ✅"))
                        break
                
            elif option["Advance"] == "Change Plan Account":
                while True:
                    push = False
                    plan_use = 'Free'
                    plan = prompt([
                                    List(
                                            "plan",
                                            message="Change To",
                                            choices=["Free", "Premium", "Advance", "Exit"],
                                        ),
                                        ])
                    for user in load_user["Data_Users"]:
                        if user["ID"] == self.id:
                            user_plan = user
                    if plan["plan"] == "Free"  and self.plan !=  "Free":
                        self.plan = "Free"
                        user_plan["Plan"] = "Free"
                        print('Change Plan successfully ✅')
                        self.save_to_json()
                        continue
                    elif plan["plan"] == "Premium" and self.plan != "Premium" :
                        push = True
                        plan_use = "Premium"
                    elif plan["plan"] == "Advance" and self.plan != "Advance":
                        push = True
                        plan_use = "Advance"
                    elif  plan["plan"] == "Exit":
                        break
                    if push and not self.method:
                        fix = self.Add_Payment()
                        if fix == True :
                            code_discount_creat = f'C{self.username[:3]}{self.id}O{load_user["Admin_DB"][0]}S'
                            user_plan["Code_Discount"] = code_discount_creat
                            self.code_discount = code_discount_creat
                            user_plan["Plan"] = plan_use
                            self.plan = plan_use
                            print('Change Plan successfully ✅')
                            self.save_to_json()
                            self.card = [card[5]for card in user_plan["Payment_Method"]]
                            continue
                    elif push and  self.method:
                        chioce = prompt([
                                    List(
                                            "By",
                                            message="Pay By",
                                            choices=self.card
                                        )
                                        ])
                        self.plan = plan_use
                        user_plan["Plan"] = plan_use
                        code_discount_creat = f'{self.username[:3]}{self.id}{load_user["Admin_DB"][0]["Members"]}'
                        user_plan["Code_Discount"] = code_discount_creat
                        self.code_discount = code_discount_creat
                        print('Change Plan successfully ✅')
                        self.save_to_json()
                        continue
                    print(f'You Account is already {plan["plan"]}')
                    continue
            elif option["Advance"] == "Show My information":
                print(f'''
{White}[+] - Full Name:{Yellow}{self.full_name}\n
{White}[+] - Username:{Yellow}{self.username}\n
{White}[+] - Email:{Yellow}{self.email}\n
{White}[+] - Password:{Yellow}{self.password}\n
{White}[+] - ID:{Yellow}{self.id}\n
{White}[+] - Plan:{Yellow}{self.plan}
''')
            elif option["Advance"] == "Exit 🔌":
                return
    def save_to_json(self):
        with open(user_path, 'w') as dbUS:
            dbUS.write(dumps(load_user, indent=4))
        return 'successfully ✅'
    def save_to_json_shop(self):
        with open(product_path, 'w') as dbFTC:
            dbFTC.write(dumps(load_product, indent=4))
        return 'successfully ✅'





class AccessDataBase(UserSignRegistration):
    #! Build function 
    def timer_offer(self, time_need=False, offer=False):
        time_offer = time_need
        while time_offer > 0:
            m, s = divmod(time_offer, 60)
            h, m = divmod(m, 60)
            time_left = f'{offer} {str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}'
            print(time_left + '\r', end="")
            time.sleep(1)
            time_offer-= 1
        return
    def Info_User(self):
        members = 0
        plans = {"Advance": 0,  "Free": 0, "Premium": 0}
        for user in load_user["Data_Users"]:
            plans[user["Plan"]] += 1
            members += 1
        for plan, total in plans.items():
            print(f'{Green}{plan}: {Cyan}{total} {Yellow}Users Now')
        print(f'{Green}Members:{Cyan}{members} {Yellow}Users Now')

    def Info_Item(self):
        while True:
            info_type = prompt([
                    List(
                            "Type",
                            message="Show",
                            choices=[
                                "[1] Food",
                                "[2] Tech",
                                "[3] Courses",
                                "[4] Back"]
                        )
                        ])
            if info_type["Type"] == "[1] Food":
                available_food = {}
                for item in load_product["Products_Food"]:
                    available_food.setdefault(item["category"], [])
                    available_food[item["category"]].append(item["name"])
                for category, item_name in available_food.items():
                    print(f"{Green}{category}")
                    for name_item in item_name:
                        print(f'\t{Cyan}{name_item}')
            elif info_type["Type"] == "[2] Tech":
                available_tech = {}
                for item in load_product["Products_Tech"]:
                    available_tech.setdefault(item["category"], [])
                    available_tech[item["category"]].append(item["name"])
                for category, item_name in available_tech.items():
                    print(f"{Green}{category}")
                    for name_item in item_name:
                        print(f'\t{Cyan}{name_item}')
                
            elif info_type["Type"] == "[3] Courses":
                available_cours = {}
                for item in load_product["Courses"]:
                    available_cours.setdefault(item["category"], [])
                    available_cours[item["category"]].append(item["name"])
                for category, item_name in available_cours.items():
                    print(f"{Green}{category}")
                    for name_item in item_name:
                        print(f'\t{Cyan}{name_item}')
            elif info_type["Type"] == "[4] Back":
                break
    def Budjet(self):
        ...
    def Add_Discount(self, Limited_Offer=False, black_friday=False, discount=False):
        Discount_option = prompt([
                List(
                        "Discount_option",
                        message="What you need added",
                        choices=[
                            "[1] Limited Offer",
                            "[2] Black Friday",
                            "[3] Discount",
                            "[4] Back"]
                    )
                    ])
        if Discount_option["Discount_option"] == "[1] Limited Offer":
            ...
        elif Discount_option["Discount_option"] == "[2] Black Friday":
            ...
        elif Discount_option["Discount_option"] == "[3] Discount":
            ...
        elif Discount_option["Discount_option"] == "[4] Back":
            return
    def Add_New_Product(self):
        while True:
            info_type = prompt([
                        List(
                                "Type",
                                message="Add New",
                                choices=[
                                    "[1] Food",
                                    "[2] Tech",
                                    "[3] Courses",
                                    "[4] Back"]
                            )
                            ])
            if info_type["Type"] == "[1] Food":
                available_category = {}
                for categ in load_product["Products_Food"]:
                    available_category.setdefault(categ["category"])
                category = prompt([
                        List(
                                "Type",
                                message="Add New",
                                choices=[cat for cat in available_category.keys()]
                            )
                            ])
                for_cancel = prompt([
                                    Text('Name', message=chalk.bgBlack("Name (Press enter for cancel)"))
                                    ])
                if len(for_cancel['Name']) == 0:
                    continue
                new_food = prompt([
                                    Text('Price', message=chalk.bgBlack("Price")),
                                    Text("Description", message=chalk.bgBlack("Description"))
                                    ])
                ingred = []
                while True:
                    ingredients = prompt([
                                        Text('ingredient', message=chalk.bgBlack("ingredient(press enter for stop)"))
                                        ])
                    if len(ingredients["ingredient"]) == 0:
                        break
                    ingred.append(ingredients["ingredient"])
                try:
                    float(new_food['Price'])
                except ValueError:
                    print(chalk.red('Invalid Price'))
                    continue
                confirm = self.confirm_the_operation()
                if confirm == "[1] Yes":
                    load_product["Products_Food"].append({        
                        "category": category["Type"],
                        "name": for_cancel['Name'],
                        "price":float(new_food['Price']),
                        "description": new_food["Description"],
                        "ingredients": ingred,
                        "Discount": []
                            })
                    self.save_to_json_shop()
                    print(chalk.green('Added successfully ✅'))
                else:
                    continue
                
            elif info_type["Type"] == "[2] Tech":
                available_category = {}
                for categ in load_product["Products_Tech"]:
                    available_category.setdefault(categ["category"])
                category = prompt([
                        List(
                                "Type",
                                message="Add New",
                                choices=[cat for cat in available_category.keys()]
                            )
                            ])
                for_cancel = prompt([
                                    Text('Name', message=chalk.bgBlack("Name (Press enter for cancel)"))
                                    ])
                if len(for_cancel['Name']) == 0:
                    continue
                new_tech = prompt([
                                    Text('Price', message=chalk.bgBlack("Price")),
                                    Text("Description", message=chalk.bgBlack("Description")),
                                    Text("quantity", message=chalk.bgBlack("Quantity")),
                                    Text("display", message=chalk.bgBlack("Display")),
                                    Text("camera", message=chalk.bgBlack("Camera")),
                                    Text("processor", message=chalk.bgBlack("Processor")),
                                    Text("storage", message=chalk.bgBlack("Storage")),
                                    Text("battery", message=chalk.bgBlack("Battery"))
                                    ])

                try:
                    float(new_tech['Price'])
                    float(new_tech['quantity'])

                except ValueError:
                    print(chalk.red('Invalid Price or Quantity'))
                    continue
                confirm = self.confirm_the_operation()
                if confirm == "[1] Yes":
                    load_product["Products_Tech"].append({
                            "name": for_cancel['Name'],
                            "description": new_tech["Description"],
                            "category": category["Type"],
                            "price": float(new_tech['Price']),
                            "currency": "USD \ud83d\udcb5",
                            "availability": True,
                            "quantity": float(new_tech["quantity"]),
                            "Discount": [],
                            "details": {
                                "display": new_tech["display"],
                                "camera": new_tech["camera"],
                                "processor": new_tech["processor"],
                                "storage": new_tech["storage"],
                                "battery": new_tech["battery"]
                            }
                        })
                    self.save_to_json_shop()
                    print(chalk.green('Added successfully ✅'))
                else:
                    continue
            elif info_type["Type"] == "[3] Courses":
                available_category = {}
                for categ in load_product["Courses"]:
                    available_category.setdefault(categ["category"])
                category = prompt([
                        List(
                                "Type",
                                message="Add New",
                                choices=[cat for cat in available_category.keys()]
                            )
                            ])
                for_cancel = prompt([
                                    Text('Name', message=chalk.bgBlack("Name (Press enter for cancel)"))
                                    ])
                if len(for_cancel['Name']) == 0:
                    continue
                new_cours = prompt([
                                    Text('Price', message=chalk.bgBlack("Price")),
                                    Text("Description", message=chalk.bgBlack("Description")),
                                    Text("duration", message=chalk.bgBlack("duration")),
                                    Text("level", message=chalk.bgBlack("level")),
                                    Text("instructor", message=chalk.bgBlack("instructor")),
                                    Text("language", message=chalk.bgBlack("language"))
                                    ])

                try:
                    float(new_cours['Price'])
                except ValueError:
                    print(chalk.red('Invalid Price'))
                    continue
                confirm = self.confirm_the_operation()
                if confirm == "[1] Yes":
                    load_product["Courses"].append({
            "name":for_cancel['Name'],
            "description": new_cours["Description"],
            "category": category["Type"],
            "price": float(new_cours['Price']),
            "currency": "USD \ud83d\udcb5",
            "availability": True,
            "students": 0,
            "Discount": [],
            "rating": "\u2b50\ufe0f",
            "details": {
                "duration":new_cours["duration"],
                "level": new_cours["level"],
                "instructor": new_cours["instructor"],
                "language": new_cours["language"]
                        }
            })
                    self.save_to_json_shop()
                    print(chalk.green('Added successfully ✅'))
                else:
                    continue
            elif info_type["Type"] == "[4] Back":
                break
    def Edit_Product(self):
        while True:
            info_type = prompt([
                        List(
                                "Type",
                                message="Add New",
                                choices=[
                                    "[1] Food",
                                    "[2] Tech",
                                    "[3] Courses",
                                    "[4] Back"]
                            )
                            ])
            if info_type["Type"] == "[1] Food":
                Target = "Products_Food"
            elif info_type["Type"] == "[2] Tech":
                Target = "Products_Tech"
            elif info_type["Type"] == "[3] Courses":
                Target = "Courses"
            elif info_type["Type"] == "[4] Back":
                break
            edit_option = prompt([
                    List(
                            "edit_option",
                            message="What you need edit",
                            choices=[
                                "[1] Quantity",
                                "[2] Price",
                                "[3] Availability",
                                "[4] Back"]
                        )
                        ])
            if edit_option["edit_option"] =="[1] Quantity":
                ...
            elif edit_option["edit_option"] =="[2] Price":
                ...
            elif edit_option["edit_option"] =="[3] Availability":
                ...
            elif edit_option["edit_option"] =="[4] Back":
                continue





class ShopFoodTech(AccessDataBase):
    def __init__(self):
        self.offer = ''
    #! Build function 
    def section_food(self):
        ...
    def section_tech(self):
        ...
    def section_courses(self):
        ...
    def discout_activation(self):
        ...
    def whell_of_fortune(self):
        ...
    def preview(self, link):
        API = "AIzaSyBF9neN0flONQNlOrMnzzgnsQcmtSmmTlw"
        ID = "1280c2d1a93454710"
        search = link
        url = f"https://www.googleapis.com/customsearch/v1"
        parms = {"q":search, "key":API, "cx":ID}
        res = requests.get(url, params=parms)
        result = res.json()
        if 'items' in result:
            web.open(result['items'][0]["link"])
            return
        web.open(link)
        return




def Online_Store():
    #! call classes for use function online store:
    x = B.WHITE + f'''
                ⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⢀⣿⣿⣿⡿⠟⠛⢛⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⣾⣿⠟⠁⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣸⡿⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠀⠈⠻⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⢀⡟⠁⠀⠀⠀⠀⢰⣿⣿⣿⣿⡟⠀⠀⠀⠀⠈⠛⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀{Blue} 
                    CODEZILLA ONLINE STORE{Blue}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠘⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢰⣿⠀⢘⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣷⣄⠀
                ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠻⣿⣿⡇⠀⠈⠂
                ⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠟⣹⡿⢿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠋⠀⠀⢿⣿⡇⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣭⣵⣾⠟⠁⠀⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⢸⡇⢀⡾⠀⠀⢀⣾⣿⣿⣣⠀⠀⠀⣾⣿⠃⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠉⠛⠛⠋⠁⠀⠀⠀⠀⠈⠻⣿⣿⣿⣆⠀⠀⠀⠀⣿⣿⣿⡇⢀⣴⡿⢿⣿⣿⡿⠀⠀⣴⣿⡟⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣷⣤⣤⣼⣿⣿⣿⣷⣾⠟⠁⠀⠉⠉⣀⣴⣾⠿⠋⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣤⣀⣀⣀⣙⢿⣿⣿⣿⣿⣿⠛⣿⣿⣯⣤⠶⠶⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⡟⠁⠀⠈⠻⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠟⠉⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⠾⠛⠉⠀⠀⠀⠀⠀{Blue} HIKO DZ 🇩🇿 🇵🇸 | {Blue}v 1.1.2{Red}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                '''
    y = x.replace('⠀', ' ')
    print(y)
    call_EffectText = EffectText()
    call_UserSignRegistration = UserSignRegistration()
    call_ShopFoodTech = ShopFoodTech()
    call_AccessDataBase = AccessDataBase()
    while True:    
        option_store = prompt([
                List(
                        "option_store",
                        message="Choice Option",
                        choices=[
                            "[1] Login",
                            "[2] Don't have an account? Sign up",
                            "[3] View Store",
                            "[4] Log in to control",
                            "[5] Exit"]
                    )
                    ])
        if option_store["option_store"] == "[1] Login":
                login_fun = call_UserSignRegistration.log_in()
                
                if login_fun  == False:
                    continue
                if call_UserSignRegistration.plan == "Premium":
                    p = f'''{Green}

            ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⡦⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢰⣿⣛⣉⣉⣉⣩⣭⣥⣤⣤⣤⡤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⢢⠆⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠤⠤⠄⢀⣀⣀⣀⡘⡄⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠐⠁⠀⠀⠀⠀⡀⠀⠀⢴⣶⣧⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠨⣿⣿⣷⡄⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀⠀⠀⢰⠀⠀⠙⣤⣶⣿⣿⣿⣿⡄⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⡐⠁⠀⠀⠀⠀⠀⡠⣴⠾⣷⡆⠀⢿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⣴⡄⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀
            ⠀⠀⠀⠀⢸⠀⠀⢠⠀⠀⠀⠀⠀⠀⠈⠉⢉⠿⢿⣆⢿⣿⣿⣿⣿⡀⠀⠀⠀
            ⠀⠀⠀⠀⠎⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠘⠋⢛⣟⠛⠃⠙⠻⠿⣿⡇⠀⠀⠀
            ⠀⠀⠀⢸⡄⠀⠀⡘⠋⠉⡀⢠⣾⡰⢶⣶⡖⠁⣤⣳⣿⣶⢶⣶⡌⠳⠤⣀⣀
            ⠀⠀⠀⢸⢠⠀⢀⣿⣿⣶⣿⣿⣿⠇⠀⠁⣷⣄⣈⣙⣛⣿⣿⣿⡲⡒⠒⠒⠊
            ⠀⠀⠀⠀⣿⣾⣿⣿⣿⣿⣿⣿⡟⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣟⣿⣶⡄⠀⠀
            ⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠐⣿⠿⣿⣿⣿⣿⡿⠋⠀⠙⣿⡇⠀⠀
            ⠀⠀⠀⣿⣿⡿⠁⠸⣿⣿⣿⣿⣿⣦⠸⠋⢸⣿⣿⣿⡿⠁⠀⠀⠀⢸⣷⡀⠀
            ⠀⠀⠀⣻⣿⡇⠀⠀⠀⣹⣿⡿⢻⣿⢠⡀⠸⣿⣿⣿⣧⠀⠀⠀⠀⠘⣿⣧⠀
            ⠀⠀⢠⠉⣿⠇⠀⠀⢰⠋⣿⣰⣁⡟⠀⠁⢼⣿⡿⠿⠏⠀⠀⠀⠀⠀⠋⠟⠀
            ⠀⠀⢰⣿⠋⠀⠀⠀⢀⣿⡏⠛⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⣾⡇⠀⠀⠀⢀⠎⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠜⢹⡇⠀⠀⠀⠾⣶⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠮⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀
        
    
            {Blue}[+] Account Premium [+]
                
            {White}[+] - {Yellow}Discount {Green}20%
            {White}[+] - {Yellow}Free Shipping : {Green} 0$
            {White}[+] - {Yellow}You Can Create Code Discount{Green}   {call_UserSignRegistration.code_discount}
            {White}[+] - {Yellow}Get Your Own Warehouse{Green} {Cyan}Upgrade To Advance
            {White}[+] - {Yellow}Get Unique Discount{Green} {Cyan}Upgrade To Advance
            
            {White}[+] - {Cyan} We Are With You Everywhere'''
                    print(p.replace('⠀', ' '))
                elif call_UserSignRegistration.plan == "Free":
                    f = f'''{Green}

            ⠀⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣦⡀⠀
            ⠀⢸⣿⣧⣀⣀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣀⣼⣿⡧⠀
            ⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀
            ⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠿⠿⠛⠋⠁⠀⠀⠀
        
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠀⠀⠀⠀⠀⠀⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
        
        
    
            {Blue}[+] Account Free [+]
                
            {White}[+] - {Yellow}Discount {Green}20%  {Cyan}Upgrade To Premium
            {White}[+] - {Yellow}Free Shipping : {Green} 0$  {Cyan}Upgrade To Premium
            {White}[+] - {Yellow}You Can Create Code Discount{Green}   {Cyan}Upgrade To Premium
            {White}[+] - {Yellow}Get Your Own Warehouse{Green} {Blue}Upgrade To Advance
            {White}[+] - {Yellow}Get Unique Discount{Green} {Blue}Upgrade To Advance
            
            {White}[+] - {Cyan} We Are With You Everywhere'''
                    print(f.replace('⠀', ' '))
                elif call_UserSignRegistration.plan == "Advance":
                    a = f'''{Cyan}
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⡀⠀⠀⢀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀
                ⣀⣀⣀⣤⣤⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣀⣀⣀
                ⠘⢿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿⠃
                ⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀
                ⠀⠀⠀⠀⣿⣿⡏⠉⠉⣿⣟⠛⠛⠛⠛⠛⠛⣻⣿⠉⠉⢹⣿⣿⠀⠀⠀⠀
                ⠀⠀⠀⠀⠹⣿⣷⢤⡀⠙⠉⠀⠀⠀⠀⠀⠀⠉⠋⢀⡤⣾⣿⠏⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠈⢿⣦⡁⠿⢿⠁⠀⠀⠀⠀⠈⡿⠿⢈⣴⡿⠁⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠘⢿⣿⠂⠀⣀⣠⣀⣀⣄⣀⠀⠐⣿⡿⠃⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠈⠻⠿⠿⠟⠁⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣦⣤⣀⣀⣤⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
            {Blue}[+] Account Advance [+]
                
            {White}[+] - {Yellow}Discount {Green}45%
            {White}[+] - {Yellow}Free Shipping : {Green} 0$
            {White}[+] - {Yellow}You Can Create Code Discount{Green}   {call_UserSignRegistration.code_discount}
            {White}[+] - {Yellow}Get Your Own Warehouse{Green} 
            {White}[+] - {Yellow}Get Unique Discount{Green} 
            
            {White}[+] - {Cyan} We Are With You Everywhere'''
                    print(a.replace('⠀', ' '))
                if call_UserSignRegistration.login == True:
                    while True:    
                        option_store_2 = prompt([
                            List(
                                    "option_store",
                                    message=f"{White} __Hello {Green}{call_UserSignRegistration.username} {White}in Cdezilla Online Store__",
                                    choices=[
                                        "[1] Logout",
                                        "[2] View Store",
                                        "[3] Advance Setting",
                                        "[4] Add Payment Method"
                                        ]
                                )
                                ])
                        if option_store_2["option_store"] == "[1] Logout":
                            call_UserSignRegistration.login = False
                            call_UserSignRegistration.full_name = "..."
                            call_UserSignRegistration.username = "..."
                            call_UserSignRegistration.email = "..."
                            call_UserSignRegistration.password = "..."
                            call_UserSignRegistration.id = "..."
                            call_UserSignRegistration.method = False
                            call_UserSignRegistration.password = "..."
                            call_UserSignRegistration.plan = "..."
                            call_UserSignRegistration.code_discount = "..."
                            call_UserSignRegistration.card = "..."
                            call_UserSignRegistration.number_card = "..."
                            print('Logout successfully ✅')
                            break
                        elif option_store_2["option_store"] == "[2] View Store":
                            ...
                        elif option_store_2["option_store"] == "[3] Advance Setting":
                            call_UserSignRegistration.advance_setting()
                            call_UserSignRegistration.save_to_json()
                            continue
                        elif option_store_2["option_store"] == "[4] Add Payment Method":
                            call_UserSignRegistration.Add_Payment()
                            call_UserSignRegistration.save_to_json()
        elif option_store["option_store"] == "[2] Don't have an account? Sign up":
            call_UserSignRegistration.create_account()
        elif option_store["option_store"] == "[3] View Store":
            while True:
                option_view = prompt([
                List(
                        "option_view",
                        message="Choice Option",
                        choices=[
                            "[1] Codezilla F🍔🍔D",
                            "[2] C📀dzilla Tech",
                            "[3] Codezi//a Courses",
                            "[4] Back"]
                    )
                    ])
                if option_view["option_view"] == "[1] Codezilla F🍔🍔D":
                    call_ShopFoodTech.section_food()
                elif option_view["option_view"] == "[2] C📀dzilla Tech":
                    call_ShopFoodTech.section_tech()
                elif option_view["option_view"] == "[3] Codezi//a Courses":
                    call_ShopFoodTech.section_courses()
                elif option_view["option_view"] == "[4] Back":
                    break
        elif option_store["option_store"] == "[4] Log in to control":
            admin_check = call_UserSignRegistration.log_in(Target="Admin_DB")
            if admin_check  == False:
                continue
            elif call_UserSignRegistration.login == True:
                print(chalk.green(pyf.figlet_format(text='Admin Space', font='slant')))
                while True:
                    option_admin = prompt([
                    List(
                            "option_admin",
                            message="Choice Option",
                            choices=[
                                "[1] Add Discount",
                                "[2] Add Limited Offer",
                                "[3] Add New Product",
                                "[4] Edit Product",
                                "[5] Information Item",
                                "[6] Inforamtion User",
                                "[7] Logout"]
                        )
                        ])
                    if option_admin["option_admin"] =="[1] Add Discount":
                        call_AccessDataBase.Add_Discount()
                    elif option_admin["option_admin"] == "[2] Add Limited Offer":
                        call_AccessDataBase.Add_Discount()
                    elif option_admin["option_admin"] == "[3] Add New Product":
                        call_AccessDataBase.Add_New_Product()
                    elif option_admin["option_admin"] == "[4] Edit Product":
                        call_AccessDataBase.Edit_Product()
                    elif option_admin["option_admin"] =="[5] Information Item":
                        call_AccessDataBase.Info_Item()
                    elif option_admin["option_admin"] =="[6] Inforamtion User":
                        call_AccessDataBase.Info_User()
                    elif option_admin["option_admin"] =="[7] Logout":
                        call_UserSignRegistration.login = False
                        call_UserSignRegistration.username = "..."
                        call_UserSignRegistration.password = "..."
                        call_UserSignRegistration.email = "..."
                        call_UserSignRegistration.Members = "..."
                        print('Logout successfully ✅')
                        break
        elif option_store["option_store"] == "[5] Exit":
            z =  f'''{Cyan}
    ⡌⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢀
    ⣿⣌⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠟⣱⣿
    ⢹⣿⣧⡈⠻⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠟⣡⣾⣿⠇
    ⢰⡙⢿⣿⣷⣌⠛⢿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡿⢋⣡⣾⣿⡿⣫⡆
    ⠈⢿⣦⣝⠻⣿⣿⣦⣉⠻⢿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⡿⠛⣡⣴⣿⣿⠟⣩⣾⡿⠁
    ⠀⠈⠻⣿⣷⣮⡙⢿⣿⣷⣤⡉⠻⢿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⡿⠟⢉⣴⣾⣿⠿⣋⣵⣾⣿⠟⠁⠀
    ⠀⠀⠰⣌⠻⣿⣿⣷⣬⡛⢿⣿⣷⣤⡉⠻⢿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⡿⠛⣉⣤⣾⣿⡿⢛⣥⣾⣿⣿⢟⣡⠆⠀⠀
    ⠀⠀⠀⠹⣿⣮⣙⢿⣿⣿⣷⣭⡻⣿⣿⣷⣦⣉⠻⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠟⣁⣴⣾⣿⡿⣟⣽⣾⣿⣿⠿⣋⣴⣿⠏⠀⠀⠀
    ⠀⠀⠀⠀⠈⠻⣿⣷⣬⣛⢿⣿⣿⣷⣿⣿⣿⣿⡇⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡏⢸⣿⣿⣿⣿⣾⣿⣿⡿⣛⣵⣾⡿⠟⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣷⣮⣟⢿⣿⣿⣿⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡇⢸⣿⣿⣿⣿⡿⣻⣵⣾⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣇⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⣼⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⠘⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢁⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⢻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡏⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡄⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

            {White}[+] - {Yellow}Python 3.11.3
            {White}[+] - {Yellow}This online store was programmed by : {Green} HIKO 
            {White}[+] - {Yellow}Telegram channel{Green}   SOOON
            {White}[+] - {Yellow}User Telegram{Green}      Mohamed 2002
            {White}[+] - {Yellow}Instagram account{Green}  Mohamed Rida
            {White}[+] - {Yellow}GitHub account{Green}     hikodz
            {White}[+] - {Yellow}Version 1.1.5
            {White}[+] - {Yellow}Codezilla Cours
            '''
            print(z.replace('⠀', ' '))
            while True:    
                link = prompt([
                    List(
                            "link",
                            message="Go To",
                            choices=[
                                f"{White}[+] - {Yellow}Python 3.11.3",
                                f"{White}[+] - {Yellow}GitHub account{Green}",
                                f"{White}[+] - {Yellow}Codezilla Cours",
                                f"{White}[+] - {Yellow}Show Script in Github",
                                f"{White}[+] - {Yellow}End Script"
                                ]
                        )
                        ])
                if link["link"] == f"{White}[+] - {Yellow}Python 3.11.3":
                    call_ShopFoodTech.preview('python.org')
                elif link["link"] ==f"{White}[+] - {Yellow}GitHub account{Green}":
                    call_ShopFoodTech.preview('https://github.com/hikodz')
                elif link["link"] ==f"{White}[+] - {Yellow}Codezilla Cours":
                    call_ShopFoodTech.preview('codezilla cours')
                elif link["link"] ==f"{White}[+] - {Yellow}Show Script in Github":
                    call_ShopFoodTech.preview('')
                elif link["link"] ==f"{White}[+] - {Yellow}End Script":
                    call_EffectText.animate_text(f"{Cyan}SeE YOu SoOoOoOn {Red}In {Blue}CoOdeZilla Online StOree")
                    return
                



# 🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬🎬
if __name__ == '__main__':
    Online_Store()