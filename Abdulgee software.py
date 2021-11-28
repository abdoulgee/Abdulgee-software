import string


print("         BARKA DAZUWA MAKE A FREE TRANSFER         ")

print("""         YOU CAN MAKE A FREE TRANSFER
                        BY
            USING ABDULGEE SOFTWARE""")
     
print("""DOMIN NEMAN TAIMAKO AKAN YADDA ZAKACIRE KUDII RUBUTA
:help:""")



gee = ""
while gee != "exist":
	gee = input("> ").lower()
	if gee == "withdraw":
		input("account number:")
		input("account name:")
		input("bank name:")
		input("amount:")
		print("""
                   SUCCESSFULLY
                    TRANSFERRED
			""")
	elif gee == "check balance":
			print("""
	YOUR BALANCE IS  $480000		
			""")
	elif gee == "help":
		print("""
domin neman taimako:
1.withdraw - cire kudi
2.check balance - duba balance
3.exist - domin fita
4.help - domin taimako
		""")
	else:
		print("sake duba rubutunka")