import sys
import os
sys.path.append( 
	os.path.join(
		os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ),
		os.path.dirname(os.path.basename(__file__))
		)
)