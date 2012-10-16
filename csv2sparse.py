'convert CSV file to sparse (libsvm) format'

import sys, csv

def get_sparse( x ):
	output = []
	for i, value in enumerate( x ):
		if float( value ) == 0:
			continue
		output.append( "%s:%s" % ( i + 1, value ))
	return output

input_file = sys.argv[1]
output_file = sys.argv[2]

reader = csv.reader( open( input_file ))
writer = csv.writer( open( output_file, 'wb' ), delimiter = " " )

headers = reader.next()

for line in reader:
	y = line[1]
	x = line[2:]
	
	x_sparse = get_sparse( x )
	writer.writerow( [ y ] + x_sparse )