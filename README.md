### intro

It's the seed for quick scriping the hadoop streaming with python

This mapreducer demo that join two line within the same key


### startup

    > git clone https://github.com/jiahut/hadoop-streaming-python-seed.git

### test-driven

    > cat test/* | ./local.run

### hadoop run

    > alias hfs="hadoop fs"
    > hfs -copyFromLocal test test
    > ./start2 test test-output
    > hfs -cat test-output/*
