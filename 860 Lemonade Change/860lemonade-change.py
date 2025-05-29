class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiver = 0
        tenner = 0

        #Go through each bill
        for cust_bill in bills:
            if cust_bill==5:
                #add to fiver count
                fiver+=1
            elif cust_bill ==10:
                #give 5$ change
                if fiver>0:
                    fiver-=1
                    tenner+=1
                else:
                    #cant provide change
                    return False
            else: #cust_bill = 20
            #give 15$ change back
                if tenner>0 and fiver>0:
                    #give change: 1*10$ and 1*5$
                    fiver -=1
                    tenner-=1
                elif fiver>=3:
                    #give change as 3*5$
                    fiver-=3
                else:
                    #Cant give back change
                    return False
        #made it through all customers. 
        return True