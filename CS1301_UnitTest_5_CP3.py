#This problem will make use of the TheaterTicket class you wrote
#in Problem 1. You can copy/paste it into this problem if you want
#to, but you don't need to. When you click Submit, your code will
#be tested with our TheaterTicket class.
#
#Write a function called find_best_ticket. find_best_ticket should
#have three parameters: a list of available tickets (a list of
#instances of the TheaterTicket class), a quantity (an integer),
#and a budget (an integer).
#
#find_best_ticket should return the price of the most expensive
#tickets available from the list that is less than or equal to
#the given budget for the given quantity of tickets. If there are no
#available tickets that come under the budget for the given quantity,
#find_best_ticket should return False.
#
#As a reminder, every instance of TheaterTicket has a method called
#get_ticket_price. get_ticket_price has one parameter, a quantity.
#get_ticket_price returns the cost of the given quantity of that
#ticket. For example, if quantity is 5 and budget is 500, then the
#function would return the largest number to result from calling
#get_ticket_price(5) from each instance in the list of TheaterTicket.
#
#For example, imagine that the customer's budget was $100 for 5
#tickets. The only tickets that could be affordable at this price
#would be gallery seats at the matinee, which are $10 per ticket
#(the next lowest price would be gallery seats at a non-matinee,
#at $30 per ticket or $150, over the customer's budget).
#
#So, if there was a ticket in the list of tickets that with
#'gallery' as the section and True for matinee, then
#find_best_ticket would return $50, the price of five gallery
#matinee tickets. If not, it would return False, since no other
#tickets are affordable.
#
#HINT: You don't need to worry about the inner workings of the
#TheaterTicket class. You just need to find the highest result
#under the given budget from calling get_ticket_price(quantity).


#Write your function here!

class TheaterTicket:
    def __init__(self, section, matinee):
        self.section = section
        self.matinee = matinee

    def get_ticket_price(self, quantity):
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

        total_price = price_per_ticket * quantity
        if self.matinee:
            total_price -= 20 * quantity

        return total_price


def find_best_ticket(available_tickets, quantity, budget):
    best_price = False

    for ticket in available_tickets:
        ticket_price = ticket.get_ticket_price(quantity)

        if ticket_price <= budget:
            if best_price is False or ticket_price > best_price:
                best_price = ticket_price

    return best_price

#You can do this problem without having direct access to the
#definition of the TheaterTicket class. However, if you would like,
#you may copy your code from Problem 1 here to test your
#function. If you do that, you may uncomment the following lines
#to test your function out. Note that our autograder will use our
#copy of TheaterTicket, not yours; so if your class doesn't match
#the description, your code may work with your class but not with
#ours.
#
#If you do copy/paste in your TheaterTicket class and uncomment
#these lines, they should print 50, False, 200, 400

#available_ticket_1 = TheaterTicket('gallery', True)
#available_ticket_2 = TheaterTicket('floor', True)
#available_ticket_3 = TheaterTicket('floor', False)
#available_ticket_4 = TheaterTicket('orchestra', False)
#available_tickets = [available_ticket_1, available_ticket_2,
#                     available_ticket_3, available_ticket_4]
#
#print(find_best_ticket(available_tickets, 5, 100))
#print(find_best_ticket(available_tickets, 5, 40))
#print(find_best_ticket(available_tickets, 1, 1000))
#print(find_best_ticket(available_tickets, 4, 500))
