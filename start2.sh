#!/bin/bash 

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar \
	-D mapred.job.name="geo-join" \
	-numReduceTasks 1 \
	-input $1 \
	-output $2  \
	-file $PWD/mapper.py -mapper $PWD/mapper.py \
	-file $PWD/reducer.py -reducer $PWD/reducer.py 
