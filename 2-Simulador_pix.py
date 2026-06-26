print('Simulador de pix')
saldo= float(input('Valor da conta 💵:'))
pix= float(input('Qual o valor do pix?'))

conta=(saldo - pix)

if conta >=0:
    print('Tranferência concluída✅')
    print("saldo da conta:", conta )

else:
    print('Saldo insuficiente ❌') 
    print() 
    print("saldo da conta:", conta )  
print()
