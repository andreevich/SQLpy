from datetime import datetime	
def log(a):
	log = open('./log.txt', 'a')
	log.write(str(datetime.now())+":\t"+str(a)+"\n")
	log.close()