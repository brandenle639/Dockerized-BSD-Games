import subprocess
import os
terminal_title = "BSD Games"
print(f'\33]0;{terminal_title}\a', end='', flush=True)
os.system('cls' if os.name == 'nt' else 'clear')
num=""
profs=["adventure","bsdgames-adventure","go-fish","morse","quiz","snscore","wtf","arithmetic","caesar","gomoku","number","rain","teachgammon","wump","atc","canfield","hack","phantasia","random","tetris-bsd","backgammon","cfscores","hangman","pig","robots","trek","battlestar","countmail","hunt","pom","rot13","wargames","bcd","cribbage","mille","ppt","sail","worm","boggle","dab","monop","primes","snake","worms"]
profs.sort()
def main():
	global num
	print ("Choose Game")
	print ("")
	count=0
	for i in range(len(profs)):
		print("{} {}".format(count, profs[i]))
		count=count+1
	print ("")
	ans=True
	while ans:
		try:
			ans=input("What would you like to play? ")
			print ("")
			if int(ans) < len(profs):
			        os.system("/usr/games/" + profs[int(ans)])
		
		except Exception as error:
			error_string = str(error)
			print(error_string)
			print ("")

    
main()
