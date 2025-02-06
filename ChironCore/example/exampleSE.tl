struct :Test :testvar
int :testArray[30]
:testArray[:x + 1] = :x + 20
:testvar = :testArray[:x + 1] + 20
if :testvar <= 30 [
   :testvar = :x + 40
] else [
   :testvar = :x + 22
]