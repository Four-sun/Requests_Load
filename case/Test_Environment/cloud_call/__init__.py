case = {"message":"运行正确","responseCode":"100000",
        "result":[{"specificationValue":[{"id":172,"key":"颜色","merchantCode":"0185","productId":44,"value":"黑色"},
                                         {"id":173,"key":"颜色","merchantCode":"0185","productId":44,"value":"红色"}],
                   "key":"颜色"}]}
print(case['result'][0]['specificationValue'][0])