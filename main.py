import random
from random import randint

#sentenca vazia = e
# Lucas Schwengber / Maximiliano Meyer
def checkGR(nterm_test,prod):
	gr_nterm_test = nterm_test.split('\n')
	gr_prod = prod.split('\n')

	for x in range (0,len(gr_nterm_test)):
		if not (len(gr_nterm_test[x]) == 1 and gr_nterm_test[x].isupper()):
			return 'false'
			
	for x in range (0,len(gr_prod)):
		gr_temp = gr_prod[x].split('/')
		for i in range (0,len(gr_temp)):
			if len(gr_temp[i]) == 1:
				if not gr_temp[i].islower(): 
					return 'false'
			elif (len(gr_temp[i]) == 2):
				if not (gr_temp[i][0].islower() and gr_temp[i][1].isupper()):
					return 'false'

	return 'true'

def checkGLC(nterm_test,prod):
	gr_nterm_test = nterm_test.split('\n')
	gr_prod = prod.split('\n')


	for x in range (0,len(gr_nterm_test)):
		if not (len(gr_nterm_test[x]) == 1 and gr_nterm_test[x].isupper()):
			return 'false'
			
	for x in range (0,len(gr_prod)):
		gr_temp = gr_prod[x].split('/')
		for i in range (0,len(gr_temp)):
			if gr_temp[i] == 'e':
				return 'false'
				

	return 'true'

def checkGSC(nterm_test,prod):
	gr_nterm_test = nterm_test.split('\n')
	gr_prod = prod.split('\n')

	for x in range (0,len(gr_prod)):
		gr_temp = gr_prod[x].split('/')
		for i in range (0,len(gr_temp)):
			if not (len(gr_nterm_test[x]) <= len(gr_temp[i])):
				return 'false'
			if gr_temp[i] == 'e':
				return 'false'
	return 'true'

def checkPadrao(prod,nterm,term):
	for x in range (0,len(prod)):
		if not (prod[x] == '/' or prod[x] == '\n'):
			if not (prod[x] in nterm or prod[x] in term):
				return 'erro'
	for x in range (0,len(nterm)):
		if not nterm[x] == ',':
			if not nterm[x].isupper():
				return 'erro'
	for x in range (0,len(term)):
		if not term[x] == ',':
			if not term[x].islower():
				return 'erro'
	return 'ok'

def geraSent(prod,nterm_test,ini):
	gera_nterm = nterm_test.split('\n')
	gera_prod = prod.split('\n')
	cont = 0
	print(ini)
	while cont!=len(ini):
		cont=0
		i=0
		while i < len(ini):
			if ini[i].islower():
				cont+=1
				flag=0
			else:
				flag = 0
				x =0
				while ((x < len(gera_nterm)) or flag == 0):
					if ini[i] == gera_nterm[x]:
						prod_sent = gera_prod[x].split('/');
						ini = ini.replace(ini[i],prod_sent[randint(0,len(prod_sent)-1)],1)
						x = len(gera_nterm)+1
						flag=1
					x+=1
				print(ini)	
			if(flag==1):
				i=0
			else:
				i+=1


def checkGramatica(nterm_test,prod):
	if(checkGR(nterm_test,prod) == 'true'):
		return 'Gramatica Regular'
	elif(checkGLC(nterm_test,prod) == 'true'):
		return 'Gramatica Livre de Contexto'
	elif(checkGSC(nterm_test,prod) == 'true'):
		return 'Gramatica Sensivel ao Contexto'
	else:
		return 'Gramatica Irrestritas'

def verificaSimbolos(temp_prod,temp_nterm,ini,p):
	#print len(temp_prod[0])
	#print temp_nterm
	pest = p
	

	for x in range(len(temp_prod)-1):
		if '/' not in temp_prod[x]:
			if temp_nterm[x] in temp_prod[x]:
				remover = temp_nterm[x]+ '->' +temp_prod[x] + '\n'
				pest = pest.replace(remover,'')
				pest = pest.replace(temp_nterm[x],'')
				pest = pest.replace(temp_nterm[x].lower(),'')


	if(pest != p):
		print('Resultado da remocao de simbolos estereis')
		print('P\'={\n'+pest+'}')
	


	pina = pest
	for x in range(len(temp_nterm)):
		flag = 0
		if(temp_nterm[x] is not ini):
			for y in range(len(temp_prod)):
				if temp_nterm[x] in temp_prod[y]:
					flag = 1
			if(flag == 0):
				remover = temp_nterm[x]+ '->' +temp_prod[x] + '\n'
				#print remover
				pina = pina.replace(remover,'')
				#print remover
				


	#print temp_prod2
	#print temp_nterm2
	#print('Resultado da remocao de simbolos inacessiveis:')
	if(pina != pest):
		print('Resultado da remocao de simbolos inacessiveis:')
		print('P\'\'={\n'+pina+'}')


	










def main():

	
	nterm = raw_input('Nao Terminais: ')
	#nterm = 'A,B'
	term = raw_input('Terminais: ')
	#term = 'a,b'

	prod = ''
	nterm_size = nterm.split(',')
	print('\nDigite a producao:')
	for x in range(0,len(nterm_size)):
		temp = raw_input(nterm_size[x]+': ')
		prod = prod + temp + '\n'

	ini = raw_input('Simbolo Inicial: ')
	#ini = 'A'

	#print da gramatica formada
	print('\nG=({'+nterm+'},{'+term+'},P,'+ini+')')
	temp_prod = prod.split('\n')
	p = ''
	for x in range(0,len(nterm_size)):
		p = p + nterm_size[x] + '->' + temp_prod[x] + '\n'
	print('P={\n'+p+'}')
	temp_nterm = nterm.split(',')
	
	verificaSimbolos(temp_prod,temp_nterm,ini,p) # TRABALHO 2 AQUI

	prod = prod.strip();
	nterm_test = '\n'.join(nterm_size)
	print('\nPadrao = '+ checkPadrao(prod,nterm,term))
	print('Gramatica = '+checkGramatica(nterm_test,prod))

	print('Derivacao 1:')
	#geraSent(prod,nterm_test,ini)
	print('\nDerivacao 2:')
	#geraSent(prod,nterm_test,ini)
	print('\nDerivacao 3:')
	#geraSent(prod,nterm_test,ini)

if __name__ == "__main__":
    main()

# Eliminar simbolos inuteis - da pra fazer - remover simbolos que nao possuem 

# Eliminar producao unitaria simples - EX: S -> A passa a ser S -> Derivacoes de A