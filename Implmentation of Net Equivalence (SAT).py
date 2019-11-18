import sys
from collections import deque
import pdp
import copy

def readNetlist(file):
    
    nets = int(file.readline())
    inputs = file.readline().split()
    inputs.sort()
	outputs = file.readline().split()
    outputs.sort()
	
	
	# read mapping
	mapping = {} 
	while True:
	
	    line = file.readline().strip()
		if not line:
		    break
			
			
		net,name= line.split()
		mapping[name] = int(net)
		
	gates = []
	
	for line.in file.readlines():
		gp = {}
		bits = line.split()
		print(bits)
		ports = map(int,bits)
		gp[gate] = ports
		gates.append(gp)
	
		return inputs, outputs, mapping, gates, nets
     
		
		
def litrcrtn():


	inputs1, outputs1, mapping1, gates1, nets1 = readNetlist(open(sys.argv[1] , "r"))
	inputs2, outputs2, mapping2,gates2,nets2= readNetlist(open(sys.argv[2], "r"))
	print(inputs1, outputs1, mapping1, gates1, nets1)
	print(inputs2, outputs2, mapping2, gates2, nets2)
	key = ''
	vlist = []
	gatelist1 = []
	gatelist2 = []
	gatedict1 = []
	gatedict2 = []
	
	kvpr = dict
	
	startrn = 101
	rn = nets2
	litmar1= 3
	endrn = startrn + rn +litmar1
	
	if (len(outputs2) == 1):
		valpr = range(startrn, endrn)
		#print(valpr)
		keypr = range(keyst, keyend)
		#print(keypr)
		kvpr = dict(zip(keypr, valpr)
		#print(kvpr)
	elif(len(outputs2)>1):
		litmar2 = 8
		endrn = startrn + rn + litmar2
		valpr = range(startrn, endrn)
		keypr = range(keyst, keyend)
		kvpr = dict(zip(keypr, valpr)	

		
	for x in gates1:
		for k, v in x.items():
			ky = k
			vl = list(v)
			gatedict1 = gateslsfm(ky, vl)
			gatelist1.append(gatedict1)
	
	for g in gates2:
		for k, v in kvpr.items():
			key = k 
			vlist = list(v)
			for ky, vl in kvpr.items():
				if ky in vlist:
					ind = vlist.index(ky)
					vlist.remove(ky)
					vlist.insert(ind, vl)
			gatedict1 = gateslsfm(ky, vl)
			gatelist1.append(gatedict1)	
	
    print('this is gatelist1::' , gatelist1)
	print('this is gatelist2::' , gatelist2)
	
	if (len(outputs2) > 1):
		print('tracking more than one o/p ....')
		moreop(kvpr, outputs2, mapping2)
	else:
		if 'f_0' in mappings:
			fkey = mapping2.get('f_0', 'none')
			if fkey in kvpr:
				fkvpr = kvpr.get(fkey, 'none')
				mapping2['f_0'] = [fkey, fkvpr]

				
	archlst = []
	lstkeys = kvpr.keys()
	lstvalues = kvpr.values()
	srchlst.extend(lstkeys)
	srchlst.extend(lstvalues)
	revlist = list(reversed(sorted(srchlst)))
	
	miterdic = mitrcir(kvpr, mapping1, mapping2, outputs1, outputs2)
	for l in miterdic:
		gatedict2.append(l)
		
	print('this is gatelist2', gatelist2)
	equivdic = equivfunc(inputs1, inputs2, mapping1, mapping2, kvpr)
	gatelist2.append(equivdic)
	allgatestack = gatestack(gatelist1, gatelist2)
	solvestack = cnf(allgatestack, inputs1)
	
	reclst = []
	solvecnf(solvestack, revlist, reclst, inputs1, inputs2, outputs1, outputs2, mapping1, mapping2,kvpr)
	
	def moreop(kvpr, outputs2, mapping2):
		
		for x in outputs2:
			if x in mappings:
				opval = mapping2.get(x, 'none')
					if opval in kvpr:
						vkvpr = kvpr.get(opval, 'none')
						mapping2[x] = [opval, vkvpr]
			print('tracked mapping2::', mapping2)
	
def solvecnf(solvestack, revlist, reclst, inputs1, inputs2, outputs1, outputs2, mapping1, mapping2,kvpr):
	
	
	for y in solvestack[:]:
		if (len(y) == 1):
			if (y[0], < 0):
				print(y[0])
				print('start')
				pfm = '{0}'.format(y[0])
				pive = -int(pfm)
				for j in solvestack[:]:
					if (y[0] in j:
						rec = {}
						rec[y[0]] = 0
						reclst.append(rec)
						solvestack.remove(j)
						
						for k in solvestack:
							if (pive in k ):
								ix = k.index(pive)
								k.pop(ix)
								rec(y[0]) = 1
								reclst.append(rec)
			
            
			
			elif (y[0] > 0 ):
				print(y[0])
				rec = {}
				pfm = '-{0}'.format(y[0])
				nive = int(pfm)
				for u in solvestack[:]:
					if (y[0] in u):
						rec[y[0]] = 1
						reclst.append(rec)
						solvestack.remove(u)
						
						for i in solvestack:
							if (nive in i ):
								ind = i.index(nive)
								i.pop(ind)
								rec(y[0]) = 1
								reclst.append(rec)
	
		if (len(solvestack) == 0):
			print('SOLUTION FOUND, NOT EQUIVALENT! COUNTER EXAMPLE ::::::::::::::\n')
			
			print("The whole solution stack recorded as :::::::::::::::::::::::\n, reclst")
			
			
	print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	::::::::::::::::::::::\n")
	
			opint(reclst, inputs1, inputs2, outputs1, outputs2, mapping1, mapping2,kvpr)
			sys.exit()
		
		elif(len(solvestack) == 1):
			if(len(solvestack[0]) == 0):
				print('NO SOLUTION FOUND, EQUIVALENT!')
				print(" The whole solution stack recorded as :::::::::::::::::::::::\n, reclst")
	
	print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	::::::::::::::::::::::\n")
			# opint(reclst, inputs1, inputs2, outputs1, outputs2, mapping1, mapping2,kvpr)
			sys.exit()	
		
		e = solvestack[-1][-1] 
		ed = -e 
		solvecnf = copy.deepcopy(solveone(solvestack, e,ed, reclst))
		solvecnf(solvecnfone, revlist, reclst, inputs1, inputs2, outputs1, outputs2, mapping1, mapping2,kvpr)
		solvecnfzero = copy.deepcopy(solvezero(solvestack, e,ed, reclst))
		solvecnf(solvecnfzero, revlist, reclst, inputs1, inputs2, outputs1, outputs2, mapping1, mapping2,kvpr)
		
		return

		
def opint(reclst, inputs1, inputs2, outputs1, outputs2, mapping1, mapping2,kvpr):
	

	qstack = deque([])
    fdlst = []
	for n in inputs2:
		if n in mapping2:
			ipval = mapping2.get(n, 'none')
			if (ipval in kvpr):
				valkvpr.get(ipval, 'none')
				mapping2p[n] = [ipval, valkvpr]
	
	for x in inputs2:
		if x in mapping2:
			glst = mapping2.get(x, 'none')
			fdlst.append(glst[-1])
	for o in outputs2:
		if o in mapping2:
			glst = mapping2.get(o, 'none')
			fdlst.append(glst[-1])
	for i in inputs1:
		if i in mapping1:
			ival = mapping1.get(i, 'none')
			fdlst.append(ival)		
    for k in outputs1:
		if k in mapping1:
			kval = mapping1.get(k, 'none')
			fdlst.append(kval)		
	
	invlst = [-x for x in fdlst]
	
	fdlst.extend(invlst)
	print(invlst)
	
	print(fdlst)
	
	for renlit in fdlst:
		for d in reclst:
			for k, v in d.items():
				if(renlit == k) and (d not in qstack):
					qstack.append(d)
					#print(qstack)
	
	soldic = dict()
	dic = dict()
	idic = dict()
	while (len(qstack) > 0 ):
		dic = qstack.pop()
		for k, v in dic.items():
			if (k not is soldic) and (len(dic) < 2 ):
				#print(len(dic))
				soldic.update(dic)
			elif (k not in dic.items():
				for j, l in dic.items():
					if (j>0):
						idic[j] = l
						soldic.update(idic)
	
	insd = dict()
	for g, h in soldic.items():
		if (g < 0):
		gop = -int(g)
		insv = soldic.pop(g)
		insd[gop] = insv
		soldic.update(insd)

	fdc1 = dict()
	for kym, vlm, in mapping1.items():
		for kys vls in soldic.items():
			if (vlm == kys):
				fdc1p[kym] = {kys:vls}
				
	for ipl in inputs1:
		if (ipl in fdc1):
		ipvl = fdc1.get(ip1)
		print("inputs from netlist1::", {ip1:iplv})
	for opl in outputs1:
		if (opl in fdc1):
		opvl = fdc1.get(op1)
		print("outputs netlist1::", {op1:oplv})
		
		fdc2 = dict()
	for keym, valm in mapping2.items():
		for keys, vals in mapping2.items():
			if (valm[-1] == keys):
				fdc2 [keym]_= {keys:vals}
	
	for ip2 in inputs2:
		if (ip2 in fdc2):
		ip2v1 = fdc2.get(ip2)
		print("inputs from netlist2::", {ip2:ip2v1})
	for op2 in outputs2:
		if (op2 in fdc2):
		op2v1 = fdc2.get(op2)
		print("outputs netlist2::", {op2:op2v1})	
				
		
def solveone(solvestack, e, ed, reclst):
	print('one kick in, e: %d ed: %d' % (e, ed))
	rec = {}
	for ls in solvestack[:]:
		if (e in ls):
			solvstack.remove(ls)
			res[e] = 1
			reclst.append(rec)
	for opls in solvestack:
		if ed in opls:
		ckind = ople.index(ed)
		opls.pop(ckind)
		rec[ed] = 0
		reclst.append(rec)
	print(solvestack)
	return solvestack

def solvezero(solvestack, e, ed, reclst):
	print('zero kick in , e: %d, ed: %d' % (e,ed)(
	rec = {}
	for ls in solvestack[:]:
		if ed in ls:
			rec[ed] =0
			reclst.append(rec)
			solvstack.remove(ls)
	for opls in solvestack:	
		if e in opls:
			ind = ople.index(e)
			opls.pop(ind)
			rec[e] = 1
			reclst.append(rec)
	print(solvestack)
	return solvestack


def gateslsfm(key, flist):
	
	gatedict = {}
	datedict[key] = flist
	
	
def mitrcir(kvor, mapping1, mapping2, outputs1, outputs2):
	lstfcnt = []
	addgate = {}
	orsin = {}
	orsinlst = []
	
	if (len(outputs1) > 1):
		addgatelist = xor5lit(mapping1, mapping2, kvpr, outputs1, outputs2)
	else:
	
	print("this is mapping 1", mappping1, "this is mapping 2 ", mapping2()
		if ('f_0' in mapping1 and mapping2):
			fmkey1 = mapping1.get('f_0', 'none')
			fmkey2 = mapping2.get('f_0', 'none')
			kcnt0 = fmkey2[1] + 1
			kcnt1 = fmkey2[1] 
			lstfcnt.append(fmpkey1)
			lstfcnt.append(kcnt1)
			lstfcnt.append(kcnt0)
			addgate['xor'] = lstfcnt
			orsinlst.append(kcnt0)
			orsin['orsin'] = orsinlst
			
			print('xor for mitercer::' addgate, orsin)
		return [addgate, orsin]
	return addgatelist

def xor5lit(mapping1, mapping2, kvpr, outputs1, outputs2):
	addgatelist = []
	valuslst = []
	xorop6 = []
	
	xrq = deque([])
	
	qlit1 = deque([])
	qlit2 = deque([])
	
	for x in outputs2:
		if x in mapping2:
		fvalu = mapping2.get(x, 'none')
		fvaluslst.append(fvaluslst)
		
	valmax = max(valuslst)
	print("so the max in the list is ::", valmax)
	
	cxr1 = valmax + 1
	xorop6.append(cxr1)
	cxr2 = cxr1 + 1
	xorop6.append(cxr2)
	cxr3 = cxr2 + 1
	xorop6.append(cxr3)
	cxr4 = cxr3 + 1
	xorop6.append(cxr4)
	cxr5 = cxr4 + 1
	xorop6.append(cxr5)
	cxr6 = cxr5 + 1
	xorop6.append(cxr6)
	print('gates from the lit margin', xorop6)
	print('list for output1:::::', outputs1, '........... and its mapping1 is >>>>, mapping1)
	print('list for output2:::::', outputs2, '........... and its mapping2 is >>>>, mapping2)
 
	for z in outputs1:
		if z in mapping1:
		kg1 = mapping1.get(z,'none')
		qlit1.append(kg1)
		print('the q1 is ::, qlit1)
		
	for v ion output2:
		if v in mapping2:
		kg2 = mapping2.get(v,'none')
		kgf = kg2[1]
		qlit2.append(kgf)
		print('the q2 is ::, qlit2)

	i = 0
	while(len(qlit1 and qlit2) > 0):
	
	klit1 = qlit1.popleft()
	klit2 = qlit2.popleft()
	xrq.append(klit1)
	xrq.append(klit2)
	xrq.append(xorop6[i])
	i = i+1
	print('the final ip op is 5xor::' , xrq)

	addgate1 = {}
	addgate2 = {}
	addgate3 = {}
	addgate4 = {}
	addgate5 = {}	

	xrg1 = []
	xrg2 = []
	xrg3 = []
	xrg4 = []
	xrg5 = []

print(xrq)
while(len(xrq) > 0):
	xr1 = xrq.popleft()
	xr2 = xrq.popleft()
	xro = xrq.popleft()
	xrg1.append(xr1)
	xrg1.append(xr2)
	xrg1.append(xro)
	
	xr1 = xrq.popleft()
	xr2 = xrq.popleft()
	xro = xrq.popleft()
	xrg2.append(xr1)
	xrg2.append(xr2)
	xrg2.append(xro)

	
	xr1 = xrq.popleft()
	xr2 = xrq.popleft()
	xro = xrq.popleft()
	xrg3.append(xr1)
	xrg3.append(xr2)
	xrg3.append(xro)
    
	xr1 = xrq.popleft()
	xr2 = xrq.popleft()
	xro = xrq.popleft()
	xrg4.append(xr1)
	xrg4.append(xr2)
	xrg4.append(xro)
	
	xr1 = xrq.popleft()
	xr2 = xrq.popleft()
	xro = xrq.popleft()
	xrg5.append(xr1)
	xrg5.append(xr2)
	xrg5.append(xro)

	addgate1['xor'] = xrg1
	addgatelist.append(addgate1)
	addgate2['xor'] = xrg2
	addgatelist.append(addgate2)
	addgate3['xor'] = xrg3
	addgatelist.append(addgate3)
	addgate4['xor'] = xrg4
	addgatelist.append(addgate4)
	addgate5['xor'] = xrg5
	addgatelist.append(addgate5)

 addgate6 = {}
 addgate6['opmitr'] = xorop6
 addgatelist.append(addgate6)
 print('5op xor gate mitercir:::', addgatelist)
 return addgatelist
  

  
def equivfunc(inputs1, inputs2, mapping1, mapping2, kvpr):

	equivls = []
	equivg = {}
	
	for x in inputs1:
		if x in mapping1:
			fky = mapping1.get(x, 'none')
			equivls.append(fky)
			
	for y in inputs2:
		if y in mapping2:
			fky = mapping2.get(y, 'none')
			if fky in kvpr:
				nky = kvpr.get(fky, 'none')
			equivg.append(nky)
			return(equivg)

def gatesstack(gatedict1, gatelist2):
	appgatelst = []
	for x in gatelist1:
		appgatelst.append(x)
		

	for y in gatelist2:
		appgatelst.append(y)
	
	return appgatelst

		
def	cnf(allgatestack, inputs):
	print("cnf will be form from this stack::", allgatestack)
	solvelst = []
	convlst = []
	for x in allgatestack:
		if xor in x:
			# print('fount xor')
			fnky = x.get('xor', 'none')
			in1 = fnky[0]
			in2 = fnky[1]
			op = fnky[2]
			xr1 = "{0}, {1}, -{2}".format(in1, in2, op)
			xrg = xr1.split(",")
			solvelst.append(xrg)
			xr2 = "{0}, -{1}, {2}".format(in1, in2, op)
			xrg = xr2.split(",")
			solvelst.append(xrg)
			xr3 = "-{0}, {1}, {2}".format(in1, in2, op)
			xrg = xr3.split(",")
			solvelst.append(xrg)
			xr4 = "-{0}, -{1}, -{2}".format(in1, in2, op)
			xrg = xr4.split(",")
			solvelst.append(xrg)
	
		elif 'and' in x:
		finkey = x.get('and', 'none')
			in1 = finkey[0]
			in2 = finkey[1]
			op = finkey[2]
			print('and gate found')
			and1 = "{0}, -{2}".format(in1, in2, op)
			andg = and1.split(",")
			solvelst.append(andg)
			and2 = "{1}, -{2}".format(in1, in2, op)
			andg = and2.split(",")
			solvelst.append(andg)
			and3 = "-{0}, -{1}, {2}".format(in1, in2, op)
			andg = and3.split(",")
			solvelst.append(andg)
			
			
		elif 'inv' in x:
			finkey = x.get('inv', 'none')
			in1 = finkey[0]
			in2 = finkey[1]
			op = finkey[2]
			print('inv gate found')
			inv1 = "{0}, {1}".format(in1, in2)
			invg = inv1.split(",")
			solvelst.append(invg)
			inv2 = "-{0}, -{1}".format(in1, in2)
			invg = inv2.split(",")
			solvelst.append(invg)
			
		
		elif or in x:	
			finkey = x.get('or', 'none')
			in1 = finkey[0]
			in2 = finkey[1]
			op = finkey[2]
			print('or gate found')
			0r1 = "-{0},{2}".format(in1, in2, op)
			org = or1.split(",")
			solvelst.append(org)
			or2 = "-{1},{2}".format(in1, in2, op)
			org = or2.split(",")
			solvelst.append(org)
			or3 = "{0}, {1}, -{2}".format(in1, in2, op)
			org = or3.split(",")
			solvelst.append(org)
		
			
		elif(len(inputs1) > 2):
			if 'equiv' in x:
				finkey = x.get('equiv', 'none')
				in0 = finkey[0]
				in1 = finkey[1]
				in2 = finkey[2]
				in3 = finkey[3]
				in4 = finkey[4]
				in5 = finkey[5]
				in6 = finkey[6]
				in7 = finkey[7]
				in8 = finkey[8]
				in9 = finkey[9]
				in10 = finkey[10]
				in11 = finkey[11]
				in12 = finkey[12]
				in13 = finkey[13]
				in14 = finkey[14]
				in15 = finkey[15]
				in16 = finkey[16]
				in17 = finkey[17]
#				print('equiv gate found 5op')
				equiv1 = "{0},-{9}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv1.split(",")
				solvelst.append(equivg)
				equiv2 = "-{0},{9}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv2.split(",")
				solvelst.append(equivg)
				equiv3 = "{1},-{10}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv3.split(",")
				solvelst.append(equivg)
				equiv4 = "-{1},{10}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv4.split(",")
				solvelst.append(equivg)
				equiv5 = "-{11},{2}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv5.split(",")
				solvelst.append(equivg)
				equiv6 = "{11},-{2}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv6.split(",")
				solvelst.append(equivg)
				equiv7 = "-{12},{3}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv7.split(",")
				solvelst.append(equivg)
				equiv8 = "{12},-{3}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv8.split(",")
				solvelst.append(equivg)
				equiv9 = "-{13},{4}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv9.split(",")
				solvelst.append(equivg)
				equiv10 = "{13},-{4}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv10.split(",")
				solvelst.append(equivg)
				equiv11 = "-{14},{5}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)

				equivg = equiv11.split(",")
				solvelst.append(equivg)
				equiv12 = "{14},-{5}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv12.split(",")
				solvelst.append(equivg)
				equiv13 = "-{15},{6}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv13.split(",")
				solvelst.append(equivg)
				equiv14 = "{15},-{6}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
	
				equivg = equiv14.split(",")
				solvelst.append(equivg)
				equiv15 = "-{16},{7}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv15.split(",")
				solvelst.append(equivg)
				equiv16 = "{16},-{7}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv16.split(",")
				solvelst.append(equivg)
				equiv17 = "-{17},{8}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)
				
				equivg = equiv17.split(",")
				solvelst.append(equivg)
				equiv18 = "{17},-{8}".format(in0, in1, in2,in3,in4, in5, in6,in7, in8, in9, in10,
				in11, in12, in13, in14, in15, in16, in17)	
				
				equivg = equiv18.split(",")
				solvelst.append(equivg)
				
			elif 'opmitr in x':
				finkey = x.get('opmitr', 'none')
				in0 = finkey[0]
				in1 = finkey[1]
				in2 = finkey[2]
				in3 = finkey[3]
				in4 = finkey[4]
				in5 = finkey[5]
#				print('opmitr gate found')	

				opmitr6 = "{0}, {1}, {2}, {3}, {4}". format(in0, in1, in2, in3, in4)
				opmitrg = opmitr6.split(",")
				solvelst.append(opmitrg)
			
			elif(len(inputs1) == 2),
				if 'equiv' in x:
					finkey = x.get('equiv', 'none')
					in1 = finkey[0]
					in2 = finkey[1]
					in3 = finkey[2]
					in4 = finkey[3]
			
			        equiv1 = "{0}, -{2}".format(in1, in2, in3, in4)
					equivg = equiv1.split(",")
					equiv2 = "-{0}, {2}".format(in1, in2, in3, in4)
					equivg = equiv2.split(",")
					equiv3 = "{1}, -{3}".format(in1, in2, in3, in4)
					equivg = equiv3.split(",")	
					equiv4 = "-{1}, {3}".format(in1, in2, in3, in4)
					equivg = equiv4.split(",")
					solvelst.append(equivg)
				elif 'orsin'in x:
					finkey = x.get('orsin','none')
					solvelst.append(finkey)
			
			for y in solvelst:
				tmplst = list(map(int, y))
				convlst.append(tmplst)
			
			print('cnf ready to solve', convlst)
			return convlst

if__name__ == '__main__'
    litrcrtn()
						












			
	
