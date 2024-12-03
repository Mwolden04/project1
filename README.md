# Requirements

In order to get things working, there are somethings that must be downloaded.
<ul><li>proj3.py</li><li>url.txt</li><li>requirement.yaml</li></ul>

The items above are important as the output will not work without them. I have made certain changes to the code due to the amount of time it takes for phi-3 to output text. I have reduced the amount of comments extracted from the second product to 95.

Apart from these items, you can also pull the following (though they will not change the result):
<ul><li>comments1.txt</li><li>comments2.txt</li><li>comments3.txt</li><li>comments4.txt</li>
<li>Sentiments1.txt</li><li>Sentiments2.txt</li><li>Sentiments3.txt</li><li>Sentiments4.txt</li>
<li>CS325figure.png</li></ul>

While these won't necassarily help the output work, they will allow you to see what the output will look like. You should get 4 comment files, 5 sentiment files, and a graph at the end of the code. I have not included the last sentiments file as it should have nothing in it when finished outputting.

# What You Must Do

There is one thing you MUST do to run this: download Beautiful Soup.

If you don't know how to download it, <a href="https://www.youtube.com/watch?v=cXSg-_p9ZHw&list=PLdUbYIcf68-v4nr1XM_Q85MGm5Mcj1IS3&index=4" target="_blank">here</a> is a video that will help you understand what to do.


The requirements file should have everything you will need if included when running it. If there are any modules that are unadded, use pip through the terminal to add it. Example: no module 'module' found. In terminal: pip install module

# What Will Happen

|Good|Bad|
|----|---|
|The four URLs will have comments taken from them|The code needs modifying for differing URLs|
|Each product's comments will be output on different files|Phi-3 is extremely slow. When I timed it, it took about 19 minutes to run.|
|Each Sentiment for the different products will be put in different files|N\A|
|a graph will be output at the end that will show what comments are good, bad, or neutral based on phi-3 thoughts.|N\A|

You can see what the comments and sentiments will look like by checking the files already added.

The output graph should look as follows:
![graph](https://github.com/Mwolden04/project1/blob/final/CS325figure.png)

