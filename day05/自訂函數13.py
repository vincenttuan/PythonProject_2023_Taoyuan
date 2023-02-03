# 自訂函數: 函數式參數
# 登入成功後才能看報告或寫email

def report():
    print('密件: xxxx')

def email():
    print('撰寫 email: xxxx')


def login(func, password):
    if password == 1234:
        print('登入成功')
        func()
    else:
        print('登入失敗')


if __name__ == '__main__':
    # login(report, 1234)
    login(email, int(input('請輸入密碼: ')))

