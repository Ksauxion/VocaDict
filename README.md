# VocaDict script: custom dictionaries in Vocaloid3-4
## The problem
A DBTool for Vocaloid3 was leaked recently, which allow you to create voicebanks with any phonemes. But the dictionaries (word-phonemes) are built in the program.
For that case I created a VocaDict script, which allow you to create your own dictionaries for any language.
## How can I create a dictionary?
The structure of dictionary (.xidict format) is the following:
List of vowels separated by comma
Whole word,word separated by syllables via -,phonemes separated by syllables via -
The vowels are not implemented now, but they will be used in further updates ig
The dictionary MUST BE SORTED!
## How can I fasten this process?
There's a few python scripts I made. They're located in VocaDictAutoTool directory.
VocaDictAutoTool.py splits your dictionary in format of "word <tab> phonemes separated by space" into a .xidict one. The errors are stored in errors.log.
VocaDictSortTool.py sorts your .xidict, which is NECESSARY.
## How to install .lua script in vocaloid?
Open "Job","Manage Job Plugins" and add the .lua script.
## How to use .lua script in vocaloid?
First of all, you should write the lyrics on the pianoroll. If you want the word to be splitted into multiple sylalables, put + to the next note until the word ends. Then run the Job plugin.
## How can I change a dictionary?
Paste the path to the dictionary into settings.txt
## The script isn't working in japanese/korean/chinese dbs!
It happens only if you have non-latin characters in lyrics. For that case, you should switch to english or spanish db and run the script there, then return to original vocaloid.
## My word is splitted by itself when I'm on english/spanish db!
If that happeds, put | at the end of the lyric.
