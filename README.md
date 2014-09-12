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


### 注意事项

1. 测试用例应该从真实的文件中去抽取
2. 在本地测试通过后，将测试集copy到线上跑一遍
2. 如果本地和线上结果不一致的话，检查try/except的异常
