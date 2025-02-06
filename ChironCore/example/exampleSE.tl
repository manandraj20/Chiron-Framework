struct :Test :testvar
:testvar = :x + 20
if :testvar <= 30 [
   :y = :y + 40
] else [
   :testvar = :x + 22
]
