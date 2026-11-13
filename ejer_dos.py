# Ejercicio 4. Venta al por mayor con descuento y obsequio
# Un supermercado vende cierto producto por docenas a un precio unitario por docena de 20 USD. Por una promoción se aplican las siguientes reglas según la cantidad de docenas que compre el cliente:
# • Si compra más de 3 docenas: se aplica un descuento del 15 % sobre el monto bruto y, además, se obsequia una unidad del producto por cada docena comprada.
# • Si compra 3 docenas o menos: se aplica un descuento del 10 % sobre el monto bruto y no hay obsequio.
# Salidas esperadas: monto bruto de la compra, valor del descuento, monto neto a pagar y cantidad de unidades de obsequio.

docena=20
compra=int(input("Digite cuantas docenas compro "))

if compra>3:
    total=(compra*docena)*(1-15/100)
else:
    total=(compra*docena)*(1-10/100)
    
print("Agregue un print")