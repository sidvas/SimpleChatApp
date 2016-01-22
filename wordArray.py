import csv

#File to extract string arrays of words and swear words
swear_words = ['anal', 'anus', 'arse', 'ass', 'asshole', 'ballsack', 'balls', 'bastard', 'behenchod', 'bitch',
 'biatch', 'bloody', 'blowjob', 'blow job', 'bollock', 'bollok', 'boner', 'boob', 'boobies', 
 'bugger', 'bum', 'butt', 'buttplug', 'chut', 'clitoris', 'cock', 'coon', 'crap', 'cunt',
 'damn', 'dick', 'dickhead', 'dildo', 'dyke', 'fag', 'faggot', 'feck', 'fellate', 'fellatio', 'felching',
 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange', 'gandu', 'Goddamn', 'God damn',
 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmao', 'lmfao', 'motherfucker', 'muff',
 'nigger', 'nigga', 'omg', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy', 'queer', 'scrotum',
 'sex', 'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'sonofabitch', 'tit', 'titties',
 'tosser', 'trololol', 'turd', 'twat', 'vagina', 'wank', 'whore', 'wtf', 'xenophobe']
 
common_words_and_swears = ['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it', 'I', 'that',
 'for', 'you', 'he', 'with', 'on', 'do', 'say', 'this', 'they', 'at', 'but', 'we', 'his',
 'from', 'not', 'by', 'she', 'or', 'as', 'what', 'go', 'their', 'can', 'who', 'get', 'if',
 'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will', 'up', 'one', 'time', 'there',
 'year', 'so', 'think', 'when', 'which', 'them', 'some', 'me', 'people', 'take', 'out', 'into',
 'just', 'see', 'him', 'your', 'come', 'could', 'now', 'than', 'like', 'other', 'how', 'then',
 'its', 'our', 'two', 'more', 'these', 'want', 'way', 'look', 'first', 'also', 'new', 'because',
 'day', 'use', 'no', 'man', 'find', 'here', 'thing', 'give', 'many', 'well', 'only', 'those', 'tell',
 'very', 'even', 'back', 'any', 'good', 'woman', 'through', 'us', 'life', 'child', 'work', 'down',
 'may', 'after', 'should', 'call', 'world', 'over', 'school', 'still', 'try', 'last', 'ask', 'need',
 'too', 'feel', 'three', 'state', 'never', 'become', 'between', 'high', 'really', 'something', 'most',
 'another', 'much', 'family', 'own', 'leave', 'put', 'old', 'while', 'mean', 'keep', 'student', 'why',
 'let', 'great', 'same', 'big', 'group', 'begin', 'seem', 'country', 'help', 'talk', 'where', 'turn',
 'problem', 'every', 'start', 'hand', 'might', 'American', 'show', 'part', 'against', 'place', 'such',
 'again', 'few', 'case', 'week', 'company', 'system', 'each', 'right', 'program', 'hear', 'question',
 'during', 'play', 'government', 'run', 'small', 'number', 'off', 'always', 'move', 'night', 'live', 
 'Mr', 'point', 'believe', 'hold', 'today', 'bring', 'happen', 'next', 'without', 'before', 'large',
 'million', 'must', 'home', 'under', 'water', 'room', 'write', 'mother', 'area', 'national', 'money',
 'story', 'young', 'fact', 'month', 'different', 'lot', 'study', 'book', 'eye', 'job', 'word', 'though',
 'business', 'issue', 'side', 'kind', 'four', 'head', 'far', 'black', 'long', 'both', 'little', 'house',
 'yes', 'since', 'provide', 'service', 'around', 'friend', 'important', 'father', 'sit', 'away', 'until',
 'power', 'hour', 'game', 'often', 'yet', 'line', 'political', 'end', 'among', 'ever', 'stand', 'bad', 'lose',
 'however', 'member', 'pay', 'law', 'meet', 'car', 'city', 'almost', 'include', 'continue', 'set', 'later',
 'community', 'name', 'five', 'once', 'white', 'least', 'president', 'learn', 'real', 'change', 'team', 'minute',
 'best', 'several', 'idea', 'kid', 'body', 'information', 'nothing', 'ago', 'lead', 'social', 'understand',
 'whether', 'watch', 'together', 'anal', 'anus', 'arse', 'ass', 'asshole', 'ballsack', 'balls', 'bastard', 'behenchod', 'bitch',
 'biatch', 'bloody', 'blowjob', 'blow job', 'bollock', 'bollok', 'boner', 'boob', 'boobies', 
 'bugger', 'bum', 'butt', 'buttplug', 'chut', 'clitoris', 'cock', 'coon', 'crap', 'cunt',
 'damn', 'dick', 'dickhead', 'dildo', 'dyke', 'fag', 'faggot', 'feck', 'fellate', 'fellatio', 'felching',
 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange', 'gandu', 'Goddamn', 'God damn',
 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmao', 'lmfao', 'motherfucker', 'muff',
 'nigger', 'nigga', 'omg', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy', 'queer', 'scrotum',
 'sex', 'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'sonofabitch', 'tit', 'titties',
 'tosser', 'trololol', 'turd', 'twat', 'vagina', 'wank', 'whore', 'wtf', 'xenophobe']
swears = []
with open('commonwords.csv', 'rt') as f1:
	reader = csv.reader(f1)
	i = 0
	for row in reader:
		i += 1
		if(i<300):
			swears.append(row[0])
print(swears)

