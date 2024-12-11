#Create a class called TheaterTicket. TheaterTicket
#should have two attributes (instance variables): section
#and matinee. Make sure the variable names match those
#words. section will be a string; matinee will be a boolean.
#
#TheaterTicket should have a constructor with two required
#parameters, one for each of those attributes (section and
#matinee in that order).
#
#TheaterTicket should also have a method called
#get_ticket_price. get_ticket_price should have one
#additional parameter (other than self): quantity, an
#integer representing the number of tickets between 1 and
#10.
#
#get_ticket_price should return the price of the tickets
#represented by the instance. The price is determined first
#by section:
#
# - If section is 'floor', the price is 200.
# - If section is 'orchestra', the price is 100.
# - If section is 'mezzanine', the price is 60.
# - If section is 'gallery', the price is 30.
#
#The section price is multiplied by the number of tickets.
#Then, if matinee is true, $20 per ticket is deducted from
#the final cost. The price should be returned as an integer.
#
#For example:
#
# test_ticket = TheaterTicket('floor', True)
# print(test_ticket.get_ticket_price(5)) -> 900
#
#A floor ticket is $200. There are 5 tickets, for a total
#of $1000. The show is a matinee, so $20 per ticket is
#deducted, and $1000 - ($20 * 5) = $900. So, the method
#returns 900.
#
#HINT: Quantity is NOT an attribute of the object; it is
#an argument only passed into the get_ticket_price method.


#Write your class here!

class TheaterTicket:
    def __init__(self, section, matinee):
        # Initialize the attributes
        self.section = section
        self.matinee = matinee

    def get_ticket_price(self, quantity):
        # Determine the base price per ticket based on the section
        if self.section == 'floor':
            price_per_ticket = 200
        elif self.section == 'orchestra':
            price_per_ticket = 100
        elif self.section == 'mezzanine':
            price_per_ticket = 60
        elif self.section == 'gallery':
            price_per_ticket = 30
        else:
            raise ValueError("Invalid section")

        # Calculate the total price
        total_price = price_per_ticket * quantity

        # Deduct $20 per ticket if it's a matinee
        if self.matinee:
            total_price -= 20 * quantity

        return total_price


#The code below will test your class. If it works, it
#should print floor, True, and 900.
test_ticket = TheaterTicket('floor', True)
print(test_ticket.section)
print(test_ticket.matinee)
print(test_ticket.get_ticket_price(5))


