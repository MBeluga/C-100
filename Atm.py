class Atm:
    def __init__ (self,cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def checkbalance(self):
        print("Your balance is 50000")
new_user = Atm("Card_number", "pin_number")
new_user.checkbalance()

