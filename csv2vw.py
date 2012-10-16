'convert [Merck specific] CSV file to VW format'

'''
Usage:
csv2vw.py train.csv train.vw
csv2vw.py test.csv test.vw True		<--- for a test set, set the third argument to true to fill in labels with zeroes
'''

import sys, csv

def construct_line( label, line, tag = '' ):
	new_line = []
	if float( label ) == 0.0:
		label = "0"
		
	if tag:
		new_line.append( "%s 1 %s|" % ( label, tag ))
	else:
		new_line.append( "%s |" % ( label ))
	
	for i, item in enumerate( line ):
		if float( item ) == 0.0:
			continue
		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
		
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line
	
###########################################################	
	
input_file = sys.argv[1]
output_file = sys.argv[2]
try:
	test_set = bool( sys.argv[3] )
except IndexError:	
	test_set = False

i = open( input_file )
o = open( output_file, 'wb' )

reader = csv.reader( i )
headers = reader.next()

counter = 0

for line in reader:
	molecule = line.pop( 0 )
	if test_set:
		activity = 0
	else:
		activity = line.pop( 0 )
	
	new_line = construct_line( activity, line, molecule )
	o.write( new_line )	
	
	counter += 1
	if counter % 1000 == 0:
		print counter