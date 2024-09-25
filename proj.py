import ollama


inputF = open("quest.txt", "r")   #opens the text file with prompts as a read file

prompt1 =inputF.readline()
prompt2 =inputF.readline()
prompt3 = inputF.readline()  #each one of these reads the 

response1 = ollama.generate(model = 'phi3', prompt = prompt1)
response2 = ollama.generate(model = 'phi3', prompt = prompt2) #asks the ollama phi-3 model about the prompts 
response3 = ollama.generate(model = 'phi3', prompt = prompt3) #and then stores the info in different variables


outputF = open("out.txt", "w")  #opens the text file to output the answers a a write file


outputF.write(str(response1['response'])) #writes the items to the output file
outputF.write("\n\n\n")                   #Used to seperate the responses by 3 lines as it becomes really helpful
outputF.write(str(response2['response']))
outputF.write("\n\n\n")
outputF.write(str(response3['response']))

inputF.close()
outputF.close() #closes all files