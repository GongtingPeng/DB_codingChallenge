# Candidate: Tina Peng

# Problem 1

import re

def clean_names(raw_names): 
	output = []
	# define regex to find 'dba'
	r = re.compile("\W*[Dd][\.\-\s]*[Bb][\.\-\s]*[Aa]\W+")
	for name in RAW_NAMES:
		# split by dba
	    comp = re.split(r, name)
	    output.append([None, None])
	    # for each string, trim the non-alpha part at begin and end
	    for idx, c in enumerate(comp):
	        n = len(c)
	        i, j = 0, n-1
	        while not c[i].isalpha():
	            i += 1
	        while not c[j].isalpha():
	            j -= 1
	        # handle underscore.
	        # TODO: more edge cases? 
	        output[-1][idx] =  c[i:j+1].replace('_', ' ')
	output = [tuple(x) for x in output]
	return output

RAW_NAMES = [
'SPV Inc., DBA: Super Company',
'Michael Forsky LLC d.b.a F/B Burgers .',
'*** Youthful You Aesthetics ***',
'Aruna Indika (dba. NGXess)',
'Diot SA, - D. B. A. *Diot-Technologies*',
'PERFECT PRIVACY, LLC, d-b-a Perfection,',
'PostgreSQL DB Analytics',
'/JAYE INC/',
' ETABLISSEMENTS SCHEPENS /D.B.A./ ETS_SCHEPENS',
'DUIKERSTRAINING OOSTENDE | D.B.A.: D.T.O. '
]

CLEANED_NAME_PAIRS = [
('SPV Inc', 'Super Company'),
('Michael Forsky LLC', 'F/B Burgers'),
('Youthful You Aesthetics', None),
('Aruna Indika', 'NGXess'),
('Diot SA', 'Diot-Technologies'),
('PERFECT PRIVACY, LLC', 'Perfection'),
('PostgreSQL DB Analytics', None),
('JAYE INC', None),
('ETABLISSEMENTS SCHEPENS', 'ETS SCHEPENS'),
('DUIKERSTRAINING OOSTENDE', 'D.T.O'),
]

assert clean_names(RAW_NAMES) == CLEANED_NAME_PAIRS
