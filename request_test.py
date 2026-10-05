import requests

bvid = input("Please input the BV number: ")

url = "https://api.bilibili.com/x/web-interface/view"   # 需要加User-Agent的header，否则会返回412状态码
params = {"bvid": bvid}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"} # 浏览器标准header，表明自己是浏览器，直接找一个浏览器请求就能复制到
proxies = {"http": None, "https": None}   # 不走代理

# 返回的response是一个特殊类型的东西，使用json()方法后变为一个字典
response = requests.get(url, params = params, headers = headers, proxies = proxies)
if (response.status_code == 200):
    # 先打印一些基本数据
    data = response.json()["data"]
    data_cid = data["cid"]
    data_pic = data["pic"]
    print(
        "", 
        "======BASIC DATA======", 
        f"cid: {data_cid}", 
        f"Danmu link: https://comment.bilibili.com/{data_cid}.xml", 
        f"Cover link: {data_pic}", "======================", 
    sep = "\n", end = "\n\n")

    # 然后询问是否需要额外操作
    op_code = input("1: Download cover; ELSE: Exit\nYOUR CODE: ")
    if (op_code == "1"):
        pic_res = requests.get(data_pic, headers = headers, proxies = proxies)
        pic_format = data_pic.split(".")[-1] # 读取这张图片是什么格式的
        with open(bvid + "_Cover." + pic_format, "wb") as f:
            f.write(pic_res.content)
        print("Saved successfully.")






