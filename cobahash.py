import hashlib
h = hashlib.sha256("A>B,5000\n")

terkecil = 9999999999

for i in range(100000000,1000000,-1):
	nonce = "%d\n" % (i)
	h.update(nonce)
	print i, h.hexdigest()
	
	hexa= h.hexdigest()[:10]
	#print hexa
	
	nilai = int(hexa,16)
	
	if (nilai<terkecil):
		print "lebih kecil, nonce = ", terkecil
		terkecil = nilai
		hexaterkecil = hexa
		nonceterkecil = nonce
		hashterkecil = h.hexdigest()
	
print "Nilai hash terkecil (desimal) ", terkecil
print "Hexa = ", hexaterkecil
print "Hash = ", hashterkecil
print "Nonce = ", nonceterkecil
