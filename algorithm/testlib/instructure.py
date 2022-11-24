# -*- coding: UTF-8 -*-
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def arrtosingleNodeList(arr):
    # 列表转单链表，支持重复val的元素复用node节点，即支持带环的链表
    node_list = []
    val_list = []
    for i in range(len(arr)):
        if arr[i] != None:
            if arr[i] in val_list:
                node = node_list[val_list.index(arr[i])]
            else:
                node = Node(arr[i])
            node_list.append(node)
            val_list.append(arr[i])
        else:
            node = Node(None)
            node_list.append(node)
            val_list.append(-1)
    for i in range(len(node_list)-1):
        node=node_list[i]
        node.next=node_list[i+1]
    return node_list[0]

def arrtoNodeList(arr):
    node_list = []
    for i in range(len(arr)):
        if arr[i] != None:
            node = Node(arr[i])
            node_list.append(node)
        else:
            node_list.append(None)
    if len(node_list) > 0:
        for i in range(len(arr)//2):
            if 2 * i + 1 < len(node_list):
                node_list[i].left = node_list[2*i+1]
            else:
                node_list[i].left = None
            if 2*i+2 < len(node_list):
                node_list[i].right = node_list[2*i+2]
            else:
                node_list[i].right = None
    for n in node_list:
        if n != None:
            print(n.value)
        else:
            print(None)
    return node_list[0]

def isValid(s,L,R):
    while L < R:
        if s[L] != s[R]:
            return False
        L+=1
        R-=1
    return True


def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    reslen = 0
    index = 0
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for j in range(1, n):
        for i in range(0, n):
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - 1 - (i + 1) + 1 <= 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            if dp[i][j] and j - i + 1 > reslen:
                reslen = j - i + 1
                index = i
    return s[index:index + reslen]

if __name__ == '__main__':
    # arr=[1,2,3,None,5,6,None]
    # head = arrtoNodeList(arr)
    s='lipwawibllrziekxgwudqghfpvsafguorthpsdihcinuasyzmttzxdluhrnfdrawabwxdgpoqabfhutzowqfhkynrhobyuygesngyxpjyilqhwyeemklicinmatyishobtitukbkpqtxwioqnztlewilnewokfqkycfuvgqmogwuvkrxphyjvhbkhpcwywfnazsoulmgdoaxyngoynmfexdcpanoyidutpzcicibjnzmybvggqbpbejsvliocotewgrfcwyebisiywjsugjxxwupryxglvkgdugbejsibuscjofrvaeexqweieldfhriftlczbuzmuizjqzxovziflaigwxrxowmhdlvrbxzeaaqxmicvigolodopbukjvkzwvxexnnweodsoscnpmuwgjhmlurwdqbwrzavjjubsueahunqwemmewqnuhaeusbujjvazrwbqdwrulmhjgwumpncsosdoewnnxexvwzkvjkubpodologivcimxqaaezxbrvldhmwoxrxwgialfizvoxzqjziumzubzcltfirhfdleiewqxeeavrfojcsubisjebgudgkvlgxyrpuwxxjgusjwyisibeywcfrgwetocoilvsjebpbqggvbymznjbiciczptudiyonapcdxefmnyognyxaodgmluoszanfwywcphkbhvjyhpxrkvuwgomqgvufcykqfkowenliweltznqoiwxtqpkbkutitbohsiytamnicilkmeeywhqliyjpxygnsegyuybohrnykhfqwoztuhfbaqopgdxwbawardfnrhuldxzttmzysaunichidsphtrougfasvpfhgqduwgxkeizrllbiwawpil'
    m = longestPalindrome(s)
    print(len(s),len(m))
    # process(head)
