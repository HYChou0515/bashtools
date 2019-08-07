from subprocess import Popen, PIPE
import sys

def wc(filename):
	p = Popen(['wc', '-l', filename], shell=False, stderr=PIPE, stdout=PIPE)
	res, err = p.communicate()
	if err:
		raise Exception('wc command error')
	if sys.version_info[0] >= 3: #for python 3
		res = res.decode()
	return int(res.split(' ')[0])
