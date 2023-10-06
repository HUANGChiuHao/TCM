import requests
from bs4 import BeautifulSoup

# 该网站通过id进行区分 故采用拆分后循环的方式对网址进行更新
base = "https://db2.ouryao.com/yd2015/view.php?v=txt&id=https://db2.ouryao.com/yd2015/view.php?v=txt&id="
for num in range(1, 101):
    # 2158+1=2159
    name = base+str(num)
    # 伪装正常浏览器向网站发出查询请求
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/118.0.0.0"
                      "Safari/537.36"
                      "Edg/118.0.2088.11"
            }
    response = requests.get(name, headers=head)
    # 状态码正常则继续并反馈
    if response.ok:
        text = response.text
        soup = BeautifulSoup(text, "html.parser")
        # 读取content_text的信息，将其保存至临时txt中
        item = soup.findAll("div", attrs={"id": "content_text"})
        fw = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\cache.txt", 'w', encoding='utf-8')
        fw.write(str(item))
        # 将ResultSet类型转换为字符串类型
        paragraphs_function = ""
        for x in item:
            paragraphs_function = paragraphs_function + str(x)
        paragraphs_usage = ""
        for x in item:
            paragraphs_usage = paragraphs_usage + str(x)
        paragraphs_name = ""
        # 功能与主治
        index_function = paragraphs_function.find("【功能与主治】", 0, len(paragraphs_function))
        # 注意这里要加一，否则会返回功能与主治前面的【下标
        finish_function = paragraphs_function.find("【", index_function + 1, len(paragraphs_function))
        fw_function = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\function.txt", 'w', encoding='utf-8')
        # 写出到文件
        fw_function.write(paragraphs_function[index_function: finish_function])

        # 将临时txt中的【用法与用量】导出至其临时txt
        index_usage = paragraphs_usage.find("【用法与用量】", 0, len(paragraphs_usage))
        finish_usage = paragraphs_usage.find("【", index_usage + 1, len(paragraphs_usage))
        fw_usage = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\usage.txt", 'w', encoding='utf-8')
        # 写出到文件
        fw_usage.write(paragraphs_usage[index_usage: finish_usage])

        fw_menu = open("F:\\Files\\Files\\作业\\大创\\python\\menu.txt", encoding="utf-8")
        line = fw_menu.readline()
        while line:
            fw_name = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\name.txt", 'w', encoding='utf-8')
            fw_name.write(line)
            line = fw_menu.readline()
        print("第" + str(num) + "次请求成功")
    # 被拦截时
    else:
        print("第"+str(num)+"次请求失败")
