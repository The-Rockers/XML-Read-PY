import csv

class Player:
	def __init__(self, last, first, s1, s2, s3, s4):
		self.last = last
		self.first = first
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.s4 = s4
		
	def __str__(self):
		return("{0} {1}. scores: {2},{3},{4},{5} \n".format(self.first, self.last, self.s1, self.s2, self.s3, self.s4))
	
	def __repr__(self):
		return str(self)

class AbsentError(Exception):
	"""class to handle '-1' entries for a player's score"""
	pass

def largest(i):
	big = 0
	w = 0
	for n in range(len(i)):
		if i[n] > big:
			big = i[n]
			w = n
	return w

def smallest(i):
	smal = 10000
	w = 1000
	for n in range(len(i)):
		if smal > i[n]:
			smal = i[n]
			w = n
	return w



f = open('register.csv')
g = open('output.txt', 'w')
h = open('excluded.txt', 'w')


l1 = f.read()
l1 = l1.split('\n')
l1.pop()

x = list()

for n in range (len(l1)):
	l1[n] = l1[n].split(',')
	
	x.append(Player((l1[n])[0], (l1[n])[1], int((l1[n])[2]), int((l1[n])[3]), int((l1[n])[4]), int((l1[n])[5])))

#print(x)
sum = list()
avg = 0
mn = 0
for n in range(len(x)):
	try:
		sum.append(x[n].s1 + x[n].s2 + x[n].s3 + x[n].s4)
		avg += sum[n]
		if (x[n].s1 == -1) or (x[n].s2 == -1) or (x[n].s3 == -1) or (x[n].s4 == -1):
			raise AbsentError(x[n])
	except AbsentError:
		out_h = str(x[n].first + " " + x[n].last + " did not participate in round(s):")
		if (x[n].s1 == -1):
			out_h += " 1"
		if (x[n].s2 == -1):
			out_h += " 2"
		if (x[n].s3 == -1):
			out_h += " 3"
		if (x[n].s4 == -1):
			out_h += " 4"
		out_h += "\n"
		h.write(out_h)
		continue


b = largest(sum)
c = smallest(sum)
print("Highest cumulative score: ", x[b], "	cumulative score: ", sum[b])
print(" Lowest cumulative score: ", x[c], "	cumulative score: ", sum[c])

sum.sort()
avg /= (len(sum))
avg = round(avg, 1)

if len(sum) % 2 == 0:
	mn = (((sum[len(sum) // 2]) + (sum[(len(sum) // 2)-1]))/2)
	mn = round(mn, 1)
else:
	mn = sum[len(sum)//2]
	
print("Average cumulative score: ", avg, "\n median cumulative score: ", mn, "\n")




#round-based analysis

avg_round = list()
avg_len = list()
for n in range(4):
	avg_len.append(len(x))
	avg_round.insert(n, 0)

for n in range(len(x)):
	if x[n].s1 != -1:
		avg_round[0] += x[n].s1
	else:
		avg_len[0] -= 1
	if x[n].s2 != -1:
		avg_round[1] += x[n].s2
	else:
		avg_len[1] -= 1
	if x[n].s3 != -1:
		avg_round[2] += x[n].s3
	else:
		avg_len[2] -= 1
	if x[n].s4 != -1:
		avg_round[3] += x[n].s4
	else:
		avg_len[3] -= 1

for k in range(4):
	avg_round[k] /= avg_len[k]
	avg_round[k] = round(avg_round[k],1)
	print("Average for round ", (k+1), " is: ", avg_round[k])

sum2 = list()
sum3 = list()
for n in range(len(x)):
	sum2.append(x[n].s1 + x[n].s2 + x[n].s3 + x[n].s4)
	if (x[n].s1 == -1):
		sum2[n] += 1
	if (x[n].s2 == -1):
		sum2[n] += 1
	if (x[n].s3 == -1):
		sum2[n] += 1 
	if (x[n].s4 == -1):
		sum2[n] += 1
	
for n in range(len(x)):
	d = largest(sum2)
	sum3.append(d)
	sum2[d] = 0

for n in range(len(x)):
	s = x[(sum3[n])]
	out_g = (str(s.first) + " " + str(s.last) + ", Total score: " + str(s.s1 + s.s2 + s.s3 + s.s4) + "\n")
	g.write(out_g)

f.close()
g.close()
h.close()

