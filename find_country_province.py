from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv

# 使用Headless模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # 在无GUI环境下防止出现GPU错误
driver = webdriver.Chrome(options=options)

# 设置合理的User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 打开网页
url = 'https://www.iso.org/obp/ui/#iso:code:3166:US'
driver.get(url)

# 等待页面加载完成（你可以根据实际情况调整等待时间）
driver.implicitly_wait(10)

# 获取整个表格
table = driver.find_element(By.ID, 'subdivision')

# 获取表格的所有行
rows = table.find_elements(By.TAG_NAME, 'tr')

# 打开CSV文件以写入模式，文件名为“州省.csv”
with open('州省.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # 创建CSV写入器
    csv_writer = csv.writer(csvfile)

    # 遍历每一行，并将单元格的文本以逗号分隔写入CSV文件
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        row_data = [cell.text for cell in cells]
        csv_writer.writerow(row_data)

# 关闭浏览器
driver.quit()
