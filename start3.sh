#!/bin/bash 

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar \
	-D mapred.job.name="geo-join" \
	-numReduceTasks 20 \
	-input $1 \
	-input $2 \
	-output $3  \
	-file $PWD/mapper.py -mapper $PWD/mapper.py \
	-file $PWD/reducer.py -reducer $PWD/reducer.py 
