'compute r2 from csv test file and predictions file. Test file with headers.'

import sys, csv
from scipy.stats.stats import pearsonr

test_file = sys.argv[1]
pred_file = sys.argv[2]

test_reader = csv.reader( open( test_file ))
test_reader.next()

pred_reader = csv.reader( open( pred_file ), delimiter = " " )

predictions = []
actual = []
for pred_line in pred_reader:
	prediction = float( pred_line[ 0 ] )
	predictions.append( prediction )
	
	line = test_reader.next()
	actual.append( float( line[1] ))
	#print float( line[1] )

r, pvalue =  pearsonr( actual, predictions )
r2 = r * r

print r2