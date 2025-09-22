# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# You are given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                ten += 1
            
            change = i - 5 #greedy soln cuz we want to save as much five as possible 
                           #change is money to be returned after taking 5
            
            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False #no fives available
            
            if change == 15:   #edge cases for 15 and false if none are fulfilled
                if five>0 and ten>0:
                    five,ten = five-1,ten-1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True #return true if all that is fulfilled

        