# This Python file uses the following encoding: utf-8
import re,codecs,sys
import transcoder
def changelist(input):
	changelist = [(u'\ufeff ',u''),(u'\ufeff',u''),(u'\u2028',u'#2%'),(u'\xd8',u'#4%'),(u'\xc3',u''),(u'\xc2',u''),] # 
	regexlist = [(r'([#][2][%])i([a-zA-Z0-9 ."~/|]+[>])','\g<1><\g<2>'),(r'"nd[a-z]i','')]
	for (a,b) in changelist:
		input = input.replace(a,b)
	for (a,b) in regexlist:
		input = re.sub(a,b,input)
	input = input.replace(u'#2%','\n')
	input = input.replace(u'/','|')
	input = input.replace(u'<','')
	input = input.replace(u'>','')
	return input
def snchanges(indata):
	okwords = open('snfile.txt').read().split()
	if re.search(r'\s["][sn]',indata):
		for okword in okwords:
			rep = '"#'+okword[1:]
			indata = indata.replace(okword,rep)
	return indata
def slpchanges(indata):
	okwords = open('slpchanges.txt').read().split()
	for okword in okwords:
			splits = okword.split(':')
			if not len(splits) == 2:
				print splits
			else:
				indata = indata.replace(splits[0],splits[1])
	return indata
def alterations(filein,fileout):
	fin = codecs.open(filein,'r','utf-8')
	data = fin.read()
	fin.close()
	data = data.strip()
	print 'making preprocess changes'
	data = changelist(data)
	print "Debugging and writing to log.txt"
	log = codecs.open('log.txt','a','utf-8')
	log.write('#'+filein+"#\n")
	words = data.split(' ')
	counter=1
	out = []
	for i in xrange(len(words)):
		word = words[i]
		word = snchanges(word)
		# Creating log for श ङ issue. See https://github.com/drdhaval2785/padamanjari/issues/1
		"""
		if re.search(r'\s["][sn]',word):
			changed = snchanges(word)
			#log.write(str(counter)+":"+word+"\n")
			counter = counter+1
			if not changed == word:
				out.append(changed)
			else:
				out.append(word)
		# Creating log for ङ issue. See https://github.com/drdhaval2785/padamanjari/issues/2
		if re.search(r'"n[^aAiIuUfFxXeEoOykglnm]',word):
			out.append(word)
			rep = word.replace('\n',' ')
			log.write(str(counter)+":"+rep+"\n")
			counter = counter+1
		else:
			out.append(word)
		"""
		out.append(word)
	data = ' '.join(out)
	log.close()
	print 'changing to slp1'
	output = transcoder.transcoder_processString(data,'vel','slp1')
	#fout1 = codecs.open(fileout,'w','utf-8')
	#fout1.write(output)
	#fout1.close()
	output = slpchanges(output)
	print 'changing to Devanagari'
	output = transcoder.transcoder_processString(output,'slp1','deva')
	output = output.replace('#','')
	#output = output.replace('\n','<br/>')
	print 'putting the data in output folder'
	fout1 = codecs.open(fileout,'w','utf-8')
	fout1.write(output)
	fout1.close()
if __name__=="__main__":
	filein = sys.argv[1]
	print 'started handling', filein
	fileout = 'output/'+'.'.join(filein.split('.')[:-1])+'.txt'
	fileout = fileout.replace('PADAMANJARI/PADAMANJARI/','')
	alterations(filein,fileout)
	print
