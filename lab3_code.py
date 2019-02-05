class Currency:
    unit_name = "currency" # class variable because it's true of ALL instances of this class (unless overridden in a subclass)

    def __init__(self, value):
        self.value = value
        self.base_rate = 1 #always

    def conversion(self, result_currency_reference):
        if(type(self) == Pound):
            rate = Pound.rate
        elif (type(self) == Yuan):
            rate = Yuan.rate
        elif (type(self) == Dollar):
            rate = Dollar.rate
        else:
            return "Can't convert. Please enter a valid currency."

        #Conversion
        value_in_currency = self.value * rate
        value_at_reference_rate = value_in_currency / result_currency_reference.rate
        return result_currency_reference(value_at_reference_rate)

# Complete class Dollar with class variable(s) and a constructor method. Ensure that the conversion method in its parent class will work for it by looking at the attributes that method refers to.
# Class Dollar's exchange rate should be 20 units of Currency.
class Dollar(Currency):
    unit_name = "Dollar"
    rate = 20
    def __init__(self,value):
        super(Dollar,self).__init__(value)

    def __repr__(self):
        if self.value <=1:
            return "{} {}".format(self.value, self.unit_name)
        else:
            return "{} {}s".format(self.value, self.unit_name)

class Yuan(Currency):
    unit_name = "Yuan"
    rate = 8
    def __init__(self,value):
        super(Yuan,self).__init__(value)

    def __repr__(self):
        return "{} {}".format(self.value, self.unit_name)


class Pound(Currency):
    unit_name = "Pound"
    rate = 15
    def __init__(self,value):
        super(Pound,self).__init__(value)

    def __repr__(self):
        if self.value <=1:
            return "{} {}".format(self.value, self.unit_name)
        else:
            return "{} {}s".format(self.value, self.unit_name)



class Bank:
    initial_value = 0
    def __init__(self, name, unit, current_account = 0):
        self.name = name
        self.unit = unit
        self.current_account = unit(current_account)
        #name, unit, current_account are instance variables

    def __str__(self):
        return "{} Bank holds the {} currency and currently holds {} of {}".format(self.name, self.current_account.unit_name, self.current_account.value, self.current_account.unit_name)
        #"<NAME> Bank holds the <CURRENCY> currency and currently holds <VALUE> of <CURRENCY>"
    def deposit(self, currency):
        if not isinstance(currency, self.unit):
            return "ERROR: cannot deposit that currency."
        else:
            self.current_account.value+=currency.value
            return "successful deposit"

jpMorgan = Bank("J.P.Morgan", Dollar, 1)
barclays = Bank("Barclays", Pound, 1)
bank_of_china = Bank("Bank of China", Yuan, 1)

if __name__ == "__main__":
    dollar = Dollar(1)
    pound = Pound(1)
    yuan = Yuan(1)
    print(yuan.conversion(Pound))
    print(pound.conversion(Pound))
    print(pound.conversion(Dollar))
    print(dollar)
    two_dollars = Dollar(2)
    print(two_dollars)
    ##test of the first part
    print(jpMorgan.current_account.value)
# 1
    print(jpMorgan)
    print(jpMorgan.deposit(dollar))
# # should show: 'successful deposit'
    print(jpMorgan.current_account.value)
# # should show: 2
    print(jpMorgan.deposit(pound))
# # should show: 'ERROR: cannot deposit that currency.'
