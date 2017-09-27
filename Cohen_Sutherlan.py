# -*- coding: utf-8 -*-

class Cohen_Sutherlan:
    def __init__(self):
        print('''
            +------wyt------+
            |               |
            |               |
            w               w
            x               x
            l               r
            |               |
            |               |
            +------wyb------+
            ''')
        self.wxl = input('wxl:')
        self.wxr = input('wxr:')
        self.wyb = input('wyb:')
        self.wyt = input('wyt:')
        self.x1 = input('p1_x1:')
        self.y1 = input('p1_y1:')
        self.x2 = input('p2_x2:')
        self.y2 = input('p2_y2:')
        self.code1 = self.trans(self.x1, self.y1)
        self.code2 = self.trans(self.x2, self.y2)
        self.check()

    #将坐标转化成code
    def trans(self, x, y):
        maps = [9,8,10,1,0,2,5,4,6]
        pos = 0
        if x >= self.wxl:
            pos += 1
        if x > self.wxr:
            pos += 1
        if y <= self.wyt:
            pos += 3
        if y < self.wyb:
            pos += 3
        return maps[pos]


    def get_interp(self):
        #计算斜率
        k = 1.0 * (self.y2 - self.y1) / (self.x2 - self.x1)

        #如果code1为内部点，交换两点
        if self.code1 == 0:
            self.code1, self.code2 = self.code2, self.code1
            self.x1, self.x2 = self.x2, self.x1
            self.y1, self.y2 = self.y2, self.y1

        intp_num = 0

        #分四种情况考虑是否存在交点
        if self.code1 & 1 == 1:
            y = self.y1 + k * (self.wxl - self.x1)
            if y >= self.wyb and y <= self.wyt:
                self.x1, self.y1 = self.wxl, y
                intp_num += 1
        if self.code1 & 2 == 2:
            y = self.y1 + k * (self.wxr - self.x1)
            if y >= self.wyb and y <= self.wyt:
                self.x1, self.y1 = self.wxr, y
                intp_num += 1
        if self.code1 & 4 == 4:
            x = self.x1 + (self.wyb - self.y1) / k
            if x >= self.wxl and x <= self.wxr:
                self.x1, self.y1 = x, self.wyb
                intp_num += 1
        if self.code1 & 8 == 8:
            x = self.x1 + (self.wyt - self.y1) / k
            if x >= self.wxl and x <= self.wxr:
                self.x1, self.y1 = x, self.wyt
                intp_num += 1
        #不存在交点则位于外部，否则将交点设置为内部点，继续调用判断函数
        if intp_num == 0:
            print("Not in the graph")
        else:
            self.code1 = 0
            self.check()



    def check(self):
        if self.code1 | self.code2 == 0:
            print("(x1, y1): (%.2f, %.2f)" % (self.x1, self.y1))
            print("(x2, y2): (%.2f, %.2f)" % (self.x2, self.y2))
        elif self.code1 & self.code2 != 0:
            print("Not in the graph")
        else:
            self.get_interp()

if __name__ == "__main__":
    Cohen_Sutherlan()