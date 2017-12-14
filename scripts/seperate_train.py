import os

SYNOPTIC_PATH='/Users/jokersmith/Applications/synoptic/'

f=open(SYNOPTIC_PATH+'traces/temp'+'.txt',"w+")
with open('traces_all.txt') as inf:
	head=''
	for line in inf:
		words = line.split()
		name=words[1].split('_')
		temp=words[1][:2]
		if (temp!=head):
			f.close()
			os.chdir(SYNOPTIC_PATH)
			os.system("./synoptic.sh -r '^(?<TYPE>),(?<txId>)' -m '\\k<txId>' -o output/qa/qa_"+name[0]+" traces/temp.txt")
			open(SYNOPTIC_PATH+'traces/temp'+'.txt', 'w').close()
			head=temp
			f=open(SYNOPTIC_PATH+'traces/temp'+'.txt',"w+")
			f.write(line)
		else:
			f.write(line)
inf.close()
f.close()
os.chdir(SYNOPTIC_PATH)
os.system("./synoptic.sh -r '^(?<TYPE>),(?<txId>)' -m '\\k<txId>' -o output/qa/qa_"+name[0]+" traces/temp.txt")