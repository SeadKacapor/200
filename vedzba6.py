import os 
apsPath = 'C:\\Users\\Korisnik\\Documents\\Python Practice\\aaa'
os.chdir(apsPath) 

os.chdir('spartanci')

counter = 1 
while counter <= 200:
	open(f'{counter}.py','a').close()
	counter = counter + 1
