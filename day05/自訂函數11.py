# 自訂函數: * 與 **

def play_ground(name, *person, **ticket):
    print(name)
    print(person)
    print(ticket)


if __name__ == '__main__':
    play_ground('兒童樂園', '爸爸', '媽媽', '哥哥', '姊姊', 成人=100, 孩童=50)