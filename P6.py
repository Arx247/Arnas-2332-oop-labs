#Arnas Oonsadao, 633040233-2
"""
Lab 2 Variables and Collections: Problem 6
"""
olympics2020_str = "Badminton: Thailand vs. Great Britain,"\
                   " Table Tennis: Thailand vs. Japan"
def text():
    print("For some Olympics 2020 games of Thai athletes:")
    a, b, c = olympics2020_str.split(":")
    d, e, f, g, h, i, j, k, l, m = olympics2020_str.split()
    print("For %s the game is between"%(a), b.replace("Table Tennis", ""))
    print("For",b.replace("Thailand vs. Great Britain,", ""), ", the game is between", k, l, m)
if __name__ == '__main__':
    text()