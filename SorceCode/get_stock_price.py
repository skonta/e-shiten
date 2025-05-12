import requests

def get_stock_price(sUrlPrice, stock_code="7203"):
    # 构造查询参数
    params = {
        "p_rid": "0",
        "p_board_no": "1000",
        "p_evt_cmd": "KP",  # 只要股价
        "p_issue_code": stock_code,
        "p_eno": "0"
    }

    response = requests.get(sUrlPrice, params=params)
print*

我是傻逼 aa

