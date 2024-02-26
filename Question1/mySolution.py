from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

# 货币字典
currency_dict = {
    'GBP': '英镑',
    'HKD': '港币',
    'USD': '美元',
    'CHF': '瑞士法郎',
    'DEM': '德国马克',
    'FRF': '法国法郎',
    'SGD': '新加坡元',
    'SEK': '瑞典克朗',
    'DKK': '丹麦克朗',
    'NOK': '挪威克朗',
    'JPY': '日元',
    'CAD': '加拿大元',
    'AUD': '澳大利亚元',
    'EUR': '欧元',
    'MOP': '澳门元',
    'PHP': '菲律宾比索',
    'THB': '泰国铢',
    'NZD': '新西兰元',
    'KRW': '韩国元',
    'RUB': '卢布',
    'MYR': '林吉特',
    'TWD': '新台币',
    'ESP': '西班牙比塞塔',
    'ITL': '意大利里拉',
    'NLG': '荷兰盾',
    'BEF': '比利时法郎',
    'FIM': '芬兰马克',
    'INR': '印度卢比',
    'IDR': '印尼卢比',
    'BRL': '巴西里亚尔',
    'AED': '阿联酋迪拉姆',
    'ZAR': '南非兰特',
    'SAR': '沙特里亚尔',
    'TRY': '土耳其里拉'
}


# 查询方法
def get_exchange_rate(search_data, currency):
    # 初始化 Chrome WebDriver
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.boc.cn/sourcedb/whpj/')

        # 输入起始时间
        start_date_input = driver.find_element(By.NAME, 'erectDate')
        start_date_input.clear()
        start_date_input.send_keys(search_data)

        # 输入结束时间
        end_date_input = driver.find_element(By.NAME, 'nothing')
        end_date_input.clear()
        end_date_input.send_keys(search_data)

        # 选择货币代号
        currency_select = driver.find_element(By.NAME, 'pjname')
        currency_select.send_keys(currency)

        # 点击查询按钮
        search_button = driver.find_element(By.XPATH,
            '//input[@type="button" and @class="search_btn" and ''@onclick''="executeSearch()"]')
        search_button.click()

        # 等待查询结果加载完成
        time.sleep(1)

        # 获取现汇卖出价的文本内容
        exchange_rate = driver.find_element(By.XPATH, '//tr[td[contains(text(), "' + currency + '")]]').find_element(
            By.XPATH, './td[4]').text

        # 打印输入结果
        print(exchange_rate)
        with open("result.txt", "w") as f:
            f.write(f"{date} {currency} 现汇卖出价: {exchange_rate}")
    except Exception as e:
        print(f"发生异常: {e}")
    finally:
        driver.quit()


if __name__ == '__main__':
    # 查询时间和货币类型
    # date = '2021-12-31'
    # currency_type = '美元'

    # 获取查询日期
    date = sys.argv[1][:4] + '-' + sys.argv[1][4:6] + '-' + sys.argv[1][6:]

    # 获取货币类型
    currency_type = currency_dict[sys.argv[2]]

    # 获取汇率
    get_exchange_rate(date, currency_type)
