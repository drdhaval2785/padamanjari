# This Python file uses the following encoding: utf-8
import re,codecs
import transcoder
def changelist(input):
	changelist = [(u'\ufeff ',u''),(u'\ufeff',u''),(u'\u2028',u'#2%'),(u'\xd8',u'#4%'),(u'\xc3',u'#5%'),(u'\xc2',u''),] # 
	regexlist = [(r'([#][2][%])i([a-zA-Z0-9 ."~/|]+[>])','\g<1><\g<2>'),]
	for (a,b) in changelist:
		input = input.replace(a,b)
	for (a,b) in regexlist:
		input = re.sub(a,b,input)
	input = input.replace(u'#2%','\n')
	input = input.replace(u'/','|')
	return input
def alterations(filein,fileout):
	fin = codecs.open(filein,'r','utf-8')
	data = fin.read()
	fin.close()
	data = data.strip()
	print 'making preprocess changes'
	data = changelist(data)
	print 'changin to slp1'
	output = transcoder.transcoder_processString(data,'vel','slp1')
	fout = codecs.open(fileout,'w','utf-8')
	fout.write(output)
	fout.close()
	print 'changing to deva'
	output = transcoder.transcoder_processString(output,'slp1','deva')
	fout1 = codecs.open('output1.txt','w','utf-8')
	fout1.write(output)
	fout1.close()
alterations('test.htm','output.txt')
