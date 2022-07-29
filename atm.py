money=input("how much do you have in your account")


class ATM:
    def _init_(self,card_number,pin):
        self.card_number = card_number
        self.pin=pin


    def withdrawal(self):
       if money > withdrawal_amount: 
        withdrawal_amount=input("how much do you want withrawed?") 
        money = money-withdrawal_amount
        print("Money Withdrawed")
        
       else:
        print("insufficient money in bank,try again")
   
    def balanceQuery(self):
        print(money)

    withdrawal()
    balanceQuery()