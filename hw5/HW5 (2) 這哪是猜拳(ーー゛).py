"""
一樣的，在閱讀題目後
我們知道題目要我們找到第二行那個數字位在第一行數列的哪一個區間
而有底下幾種可能性會DATA_ERROR：
1. 數列中有負數
2. 指定數字不在0~1之間
3. 數列總和與1的誤差超過1e-6（之所以會容許誤差是因為浮點數的關係）

而這題還有一個地方要特別去注意的是：如果誤差小於1e-6
則右邊自動延伸到1，為甚麼需要這麼搞剛？

舉例來說，
我第一行輸入0.2,0.4,0.39999999999999999999999999
第二行輸入1，
第一行加起來的確在數值容許的範圍之中，但是加起來只有0.99999999999999999999999999
第二行的1竟然會找不到，最終輸出DATA_EEROR
所以為了避免這樣的極端情形，我們必須自動延展數列的最右端為1
（這也是大部分同學13.會錯的原因）
"""
def gen_random(problist, runif):
    list_len = len(problist)
    acc_prob = 0
    who = 0

    """
    一樣的，在開始之前，我們先準備好需要的變數
    因為我們會不只一次用到len(problist)這個函數
    那我就直接把這個定義成一個變數就好了
    這樣就不需要反覆呼叫函式
    """

    if runif < 0 or runif > 1:
        return None

    for i in range(list_len):
        if problist[i] < 0 or problist[i] > 1:
            return None
        acc_prob += problist[i]

        if i == list_len - 1 and abs(acc_prob - 1) < 1e-6:
            acc_prob = 1
        
        if runif <= acc_prob and runif > acc_prob - problist[i]:
            who = i

    """
    上面這段唯二的問題是在who到底在幹嘛以及右界延伸要怎麼去處理。
    
    acc_prob就是計算累積機率嘛，一但我的累積機率加上去超過runif的時候
    就代表是在這個區間裡面
    但是如果不也去看說runif有沒有大於上一次的累積機率的話
    who就會一直一直被疊上去
    舉例來說，0.1,0.2,0.3,0.4，我想要找0.25在哪一間區間
    當我0.1 + 0.2 = 0.3時，累積機率已經超過0.25了，所以who = 1
    但是繼續往上加0.3 + 0.3 = 0.6，累積機率還是大於0.25，
    所以如果我沒有再加上是否大於上一個累積機率（0.6 - 0.3 = 0.3）的話
    who又會被繼續加上去=2

    之所以不用break來做的原因是因為，
    我們必須把整個累積機率算完，再去計算誤差有沒有在容許的範圍之中
    因此貿然break我又要再跑另外一個迴圈來執行，超沒效率的
    """
    
    if abs(acc_prob - 1) > 1e-6:
        return None

    return who

prob = input()
ru = float(input())

prob = prob.split(',')
for i in range(len(prob)):
    prob[i] = float(prob[i])

out1 = gen_random(prob, ru)
if(out1 == None or out1 == -1):
    print("DATA_ERROR")
else:
    print(out1)
