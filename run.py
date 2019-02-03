"""
use this run over all videos

"""

import labeler

# read all files in the video directory 
files = ['out.mp4'] # add code here

for file in files:
	s = labeler.Labeler(file, 'frames')
	s.readFile()
	s.viewFrames()
	s.writeLabeledFrames()