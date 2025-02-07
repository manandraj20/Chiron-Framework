struct :Test :testvar
int :testArray[5]
:testArray = { 1, 2, 3, 4, 5 }
:testArray[:x + 1] = :x + 20
:testvar = :testArray[:x + 1] 
if :testvar <= 30 [
   :testvar = :x + 40
] else [
   :testvar = :x + 22
]