#New EVC
EVC = 770
PIN = 1111
BALANCE = 100.00
salaam_balance = 200
salaam_pin = "30302010"
my_number = 619151020
import locale

# Check and set the locale to Somali if available
try:
    locale.setlocale(locale.LC_ALL, 'so_SO.UTF-8')
except locale.Error:
    print("Somali locale not available. Using default locale.")


#create all function below
    
def show_balance():
    print("Your balance is: {}".format(locale.currency(BALANCE, grouping=True)))

def sending_amount():
    amount = int(input("Gali lacagta: "))
    new_amount = BALANCE - amount
    if amount > BALANCE:
        print("Haraagaaga kuguma filna: ")
    else:
        print("Waxaad ugu shubtay: {} Haraagaaga EVC waa: {}".format(locale.currency(amount, grouping=True),locale.currency(new_amount, grouping=True)))



def top_up():
    chose = int(input("Dooro 1 si aad adiga ugu shubato: Dooro 2 si aad qof kale ugu shubto: ")) 

    if chose == 1:
        amount = int(input("Enter Amount: "))
        new_amount = BALANCE - amount
        if amount > BALANCE:
            print("Haraagaaga kuguma filna: ")
        else:
            print("Waxaad ku shubatay: {} Haraagaaga EVC waa: {}".format(
                    locale.currency(amount, grouping=True),
                    locale.currency(new_amount, grouping=True)))
        
    elif chose == 2:
        print("Ugu shub qof kale: ")
        another_number = input("Gali number ka aad ugu shubeeso: ")
        if len(another_number)==9 and another_number[:2] == "61":
            sending_amount()
        else:
            print("qaabka number ka sax ma ahan ")
    else:
        print("number-ka aad dooratay ma ahan mid jira")
            
def pay_bill():
    chose = int(input("Dooro 1 si aad u bixiso lacagta korontada: Dooro 2 si aad u bixiso lacagta biyaha: Dooro 3 si aad u bixiso adeeg kale: "))
    if chose == 1:
        pill_to = input("Gali number EVC-ga korontada:")
        if len(pill_to) == 9 and pill_to[:2] == "61":
            sending_amount()
        else:
            print("qaabka number ka sax ma ahan ")
    else:
        print("number-ka aad dooratay ma ahan mid jira")
                



def uwareeji_evcplus():
    wareeji_evcplus = input("Gali number ka: ")
    if len(wareeji_evcplus)== 9 and wareeji_evcplus[:2] == "61":
        sending_amount()
    else:
        print("qaabka number ka sax ma ahan ")


def warbixin_kooban():
    print("number kaaga waa: {} haragaaga waa: {}".format(my_number, locale.currency(BALANCE, grouping=True)))


def salaam_bank():
    chose = int(input("1. Itus haraaga: 2. Lacag dhigasho: 3. lacag qaadasho: "))
    if chose == 1:
        pin = input("Gali binkaaga salaam Bank: ")
        if len(pin) == 8 and pin == salaam_pin:
            print("Your salaam bank Balance is: {}".format(locale.currency(salaam_balance, grouping=True)))
        else:
            print("Pin kaaga waa qalad ")
    elif chose == 2:
        amount = int(input("Fadlan gali lacagta: "))
        new_amount = BALANCE - amount
        new_balance = amount + salaam_balance
        if amount > BALANCE:
            print("Haraagaaga kuguma filna: ")
        else:
            print("Waxaad dhigatay: {} Haraagaaga Salaam bank waa: {}".format(locale.currency(amount, grouping=True),locale.currency(new_balance, grouping=True)))
    elif chose ==3:
        amount = int(input("Faldan gali lacagta: "))
        new_amount = salaam_balance - amount
        new_balance = amount + BALANCE
        if amount > salaam_balance:
            print("Haraagaaga kuguma filna: ")
        else:
            print("Waxaad Akoonkaaga kala baxday: {} Haraagaaga cusub ee EVC plus waa: {}".format(locale.currency(amount, grouping=True),locale.currency(new_balance, grouping=True)))

    else:
        print("number-ka aad dooratay ma ahan mid jira")
            
         
            
            
            
        
                

def open_evcplus():
    PINENTERED = int(input("Fadlan geli PIN-kaaga EVC-ga(Enter PIN): "))
    if PIN == PINENTERED:
        print("EVC PLUS")
        print("1. Itus Haragaaga" )
        print("2. Kaarka hadalka" )
        print("3. Bixi Bill" )
        print("4. U wareeji ECVPlus" )
        print("5. Warbixin Kooban" )
        print("6. Salaam Bank" )
        print("7. Maareynta" )
        print("8. Bill Payment" )
        
        choices = {
            1: show_balance,
            2: top_up,
            3: pay_bill,
            4: uwareeji_evcplus,
            5: warbixin_kooban,
            6: salaam_bank,
            # Add the rest of your functions if needed
        }
        
        chose = int(input("dooro mid: "))
        action = choices.get(chose)
        if action:
            action()
        else:
            print("Doorasho qaldan")

    else:
        print("wrong pin 3 attemps left ")
        
            
                      
                      
       
            

    
def open_evc_app():
    EVC = int(input("Fadlan geli PIN-kaaga(Enter PIN): "))
    if EVC == 770:
        open_evcplus()
    else:
        print("wrong pin")
      

open_evc_app()
