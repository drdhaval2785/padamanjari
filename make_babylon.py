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
	num = m.group(2).strip()
	current_sutra = num.split(u'।')
	print current_sutra
	if len(current_sutra) != 3:
		print current_sutra
		prevsutra = current_sutra
		exit(0)
	result = '\n\n'+num+'|'+sutra+'|'+sutra+' '+num+'|'+num+' '+sutra+'\n'+sutra+' '+num+' <BR> '
	result = result.replace(u'।','.')
	return result

fin = codecs.open('padamanjari.txt','r','utf-8')
input = fin.readlines()	
fin.close()
output = ''
fout = codecs.open('babylon/padamanjarI.babylon','w','utf-8')
counter = 0
prevsutra = (1,1,0)
for line in input:
	if re.search(u'॥[१२३४५६७८९०। ]*॥',line):
		counter += 1
		output += add_tags1(line)
	else:
		output += line.strip()+' '
output = output.replace(u'अथ प्रथमाध्याये प्रथमः पादः पदमञ्जरी \n\n१.१.१',u'१.१.१')
fout.write(output+'\n')
fout.close()
