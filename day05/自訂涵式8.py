# 自訂涵式
# 假設有一數組 scores = [100, 95, 80]
# 請設計數個方法來計算總分與平均

def get_total(data):
    return sum(data)


def get_average(data):
    total = get_total(data)
    avg = total / len(data)
    return avg


def get_total_and_average(data):
    total = get_total(data)
    avg = get_average(data)
    return total, avg


if __name__ == '__main__':
    scores = [100, 95, 80]
    total, avg = get_total_and_average(scores)
    print('總分:{} 平均:{:.1f}'.format(total, avg))
