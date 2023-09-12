"""first memory diagram"""

name: str = "Emilie"
#stack: name L"Emilie"
print("Hello " + name)
#Output: "Hello Emilie"
print("Bye " + name)
#Output: "Bye Alussa"


"""second mem diagram"""

val: int = 1
#stack: val L1
val2: int = val + 3
#stack: val2 L4
print(val + 1)
#output: 2
print(val2)
#output: 4