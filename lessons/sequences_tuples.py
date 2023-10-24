#3d_coordinate: tuples [float, float, float] = (1.0, 1.0, 1.0)
#player = tuples[str, int]
#lebron: Player = ("James", 6)

#Range: includes start point, does not include end point, and stapes throuhg every points in between 
#range(1,5) stops at number 1,2,3,4
#range(1,6,2) stops at nunmbers 1,3,5

#for elem in x:
#<the action>

pets: list[str] = ["Louie", "Bo", "Bear"]

for elem in pets:
    print(f"Good boy, {elem}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for i in range(0,len(names)):
    elem: str = names[i]
    print(f"{i}: {elem}")
    


