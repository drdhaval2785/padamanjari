# This Python file uses the following encoding: utf-8
"""
Usage:
python make_babylon.py
e.g.
python make_babylon.py
"""
import re,codecs,sys
import transcoder


def add_tags1(x):
	global prevsutra
	m = re.search(u'^(.*)॥([१२३४५६७८९०। /-]*)॥',x)
	sutra = m.group(1).strip()
	num = transcoder.transcoder_processString(m.group(2).strip(),'deva','slp1')
	current_sutra = num.split('.')
	print current_sutra
	if len(current_sutra) != 3:
		print current_sutra
		prevsutra = current_sutra
		exit(0)
	result = '\n\n'+num+'|'+sutra+'|'+sutra+' '+num+'|'+num+' '+sutra+'\n'+sutra+' '+num+' <BR> '
	result = result.replace(u'।','.')
	result = result.replace(u'अथ प्रथमाध्याये प्रथमः पादः पदमञ्जरी \n\n1.1.1',u'1.1.1')
	return result

fin = codecs.open('padamanjari.txt','r','utf-8')
input = fin.readlines()	
fin.close()
output = ''
fout = codecs.open('babylon/padamanjarI.txt','w','utf-8')
counter = 0
prevsutra = (1,1,0)
for line in input:
	if re.search(u'॥[१२३४५६७८९०। ]*॥',line):
		counter += 1
		output += add_tags1(line)
	else:
		output += line.strip()+' '
fout.write(output+'\n')
fout.close()
