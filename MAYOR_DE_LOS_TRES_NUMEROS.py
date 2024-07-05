"""" HACER UN PROGRAMA QUE PIDA 3 NÚMEROS Y DETERMINE CUÁL ES EL MAYOR """

m = float (input(" Del primer número: " ) )
n = float (input(" De el segundo número: " ) )
p = float (input( "De el tercer número: " ) )

if m > n and m > p :
    print("El mayor es",m, " ")

elif p > n:
    print("El mayor es " ,p, " ")

else:
    print("El mayor es ", n ," ")
