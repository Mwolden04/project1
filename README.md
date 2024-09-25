#### Requirements

You must download proj.py and quest.txt

You can Download the env.yml, but I am unsure if it really matters. 
I really only messed with the environment and the language model in it.
The environment does not matter too much, but installing it will make sure nothing goes wrong as I did run everything while
running the environment

You must have phi3 for this to work (I got my version from Ollama, I do not know if your version will work).

#### what to do

whichever directory you put this in, make sure you download phi 3 to that. I ended up 
having trouble with this at first. Make sure you have downloaded phi3 and type in 'ollama pull phi3' if
you are using the version from ollama in your miniconda command prompt.

If you do use my environment, run it by typing conda env create -f env.yml

After that, you should be able to run my code.

#### what will happen

My code will only grab the first three lines of any txt file named quest.txt. 
If there is no quest.txt, it will not run.

The output will go to a file named out.txt that should appear in your directory.