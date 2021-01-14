#Amount INTEGER Amount to withdraw entered by the user
#FiftyDollar INTEGER Number of $50 notes to dispense
#TwentyDollar INTEGER Number of $20 notes to dispense
#TenDollar INTEGER Number of $10 notes to dispense
#Temp INTEGER Used in the calculation of the number of each note required

# input amount
# check  the amount is less or greater then 500
# check the amount to bea multiple of 10
# withdraw the monee

MyFile = open("TEXT RECORD", "r") # enter the record of teh text fles
ThisBank = int(input("Which bank ..(Three digit code)? ")) # enter the three digit code 
DispenserLine = 0
while 1:
    DispenserLine = MyFile.readline()
    if not DispenserLine:
        break
    DispenserCode = DispenserLine[0:5]
    Bank = DispenserLine[6:9]
    if Bank == ThisBank:
        DispenserCount = DispenserCount + 1
        print(DispenserCode)
MyFile.close()
print("There are %d dispensers for this bank" % (DispenserCount))
id(DispenserLine)
