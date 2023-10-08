import requests
from bs4 import BeautifulSoup

# 该网站通过id进行区分 故采用拆分后循环的方式对网址进行更新
base = "https://db2.ouryao.com/yd2015/view.php?v=txt&id="
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
        # 读取药物名称专用
        item_name = soup.findAll("title")
        fw = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\cache.txt", 'w', encoding='utf-8')
        # 为防止出现重叠情况应先做前文删除，下同。
        fw.truncate(0)
        fw.write(str(item))
        # 将ResultSet类型转换为字符串类型
        paragraphs_function = ""
        for x in item:
            paragraphs_function = paragraphs_function + str(x)

        paragraphs_usage = ""
        for x in item:
            paragraphs_usage = paragraphs_usage + str(x)

        paragraphs_caution = ""
        for x in item:
            paragraphs_caution = paragraphs_caution + str(x)

        # 将临时txt中的【功能与主治】导出至其临时txt
        index_function = paragraphs_function.find("【功能与主治】", 0, len(paragraphs_function))
        finish_function = paragraphs_function.find("【", index_function + 1, len(paragraphs_function))
        fw_function_mid = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\function_mid.txt", 'w+', encoding='utf-8')
        fw_function = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\function_mid.txt", 'w', encoding='utf-8')
        fw_function_mid.truncate(0)
        fw_function_mid.write(paragraphs_function[index_function: finish_function])
        for text in fw_function_mid.readlines():
            if text.split():
                fw_function.write(text)

        # 将临时txt中的【用法与用量】导出至其临时txt
        index_usage = paragraphs_usage.find("【用法与用量】", 0, len(paragraphs_usage))
        finish_usage = paragraphs_usage.find("【", index_usage + 1, len(paragraphs_usage))
        fw_usage_mid = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\usage_mid.txt", 'w+', encoding='utf-8')
        fw_usage = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\usage.txt", 'w', encoding='utf-8')
        fw_usage_mid.truncate(0)
        fw_usage_mid.write(paragraphs_usage[index_usage: finish_usage])
        for text in fw_usage_mid.readlines():
            if text.split():
                fw_usage.write(text)

        # 将临时txt中的【注意】导出至其临时txt
        index_caution = paragraphs_caution.find("【注意】", 0, len(paragraphs_caution))
        finish_caution = paragraphs_caution.find("【", index_caution + 1, len(paragraphs_caution))
        fw_caution_mid = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\caution_mid.txt", 'w+', encoding='utf-8')
        fw_caution = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\caution.txt", 'w', encoding='utf-8')
        fw_caution_mid.truncate(0)
        fw_caution_mid.write(paragraphs_caution[index_caution: finish_caution])
        for text in fw_caution_mid.readlines():
            if text.split():
                fw_caution.write(text)

        # 将临时txt中的药物名称导出至其临时txt
        fw_name = open("F:\\Files\\Files\\作业\\大创\\python\\cache\\name.txt", 'w', encoding='utf-8')
        before = str(item_name).split(" ")[0]
        after = before.split(">")[1]
        fw_name.write(after)

        print("第" + str(num) + "次请求成功")

    # 被拦截时
    else:
        print("第" + str(num) + "次请求失败")
