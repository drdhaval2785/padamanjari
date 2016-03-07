# This Python file uses the following encoding: utf-8
import re,codecs
import transcoder
def changelist(input):
	changelist = [(u'\ufeff ',u''),(u'\ufeff',u''),(u'\u2028',u'#2%'),(u'\xd8',u'#4%'),(u'\xc3',u'#5%'),(u'\xc2',u''),] # 
	regexlist = [(r'([#][2][%])i([a-zA-Z0-9 ."~/|]+[>])','\g<1><\g<2>')]
	for (a,b) in changelist:
		input = input.replace(a,b)
	for (a,b) in regexlist:
		input = re.sub(a,b,input)
	input = input.replace(u'#2%','\n')
	input = input.replace(u'/','|')
	return input
def snchanges(indata):
	okwords = open('snfile.txt').read().split()
	for okword in okwords:
		rep = '"#'+okword[1:]
		indata = indata.replace(okword,rep)
	return indata
def alterations(filein,fileout):
	fin = codecs.open(filein,'r','utf-8')
	data = fin.read()
	fin.close()
	data = data.strip()
	print 'making preprocess changes'
	data = changelist(data)
	print "Debugging and writing to log.txt"
	log = codecs.open('log.txt','w','utf-8')
	words = data.split(' ')
	counter=1
	out = []
	for i in xrange(len(words)):
		word = words[i]
		if re.search(r'\s["][sn]',word,):
			changed = snchanges(word)
			log.write(str(counter)+":"+word+"\n")
			counter = counter+1
			if not changed == word:
				out.append(changed)
			else:
				out.append(word)
		else:
			out.append(word)
	data = ' '.join(out)
	log.close()
	print 'changing to slp1'
	output = transcoder.transcoder_processString(data,'vel','slp1')
	fout = codecs.open(fileout,'w','utf-8')
	fout.write(output)
	fout.close()
	print 'changing to deva'
	output = transcoder.transcoder_processString(output,'slp1','deva')
	output = output.replace('#','')
	fout1 = codecs.open('output1.txt','w','utf-8')
	fout1.write(output)
	fout1.close()
alterations('test.htm','output.txt')
