class Node(object):
    def __init__(self,name=None,value=None):
        self._name=name
        self._value=value
        self._left=None
        self._right=None
        self._codevalue='0'

#哈夫曼树类
class HuffmanTree(object):
    #根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
    def __init__(self,char_weights):
        self.codeway = {}#存储节点对应的编码数，1or0
        self.a=[Node(part[0],part[1]) for part in char_weights]  #根据输入的字符及其频数生成叶子节点
        while len(self.a)!=1:#如果没有到达根节点
            self.a.sort(key=lambda node:node._value,reverse=True)#根据节点的value进行从大到小的排序
            c=Node(value=(self.a[-1]._value+self.a[-2]._value))#对于权值最小的两个节点加和作为新节点c的value
            c._left=self.a.pop(-1)#把排序完的树叶节点挂靠在c上，作为左右节点
            c._right=self.a.pop(-1)
            self.a.append(c)#bac作为节点连在树上
        self.root=self.a[0]
#方法一
    def pre(self, tree, length,l):
        if l==0:
            self.b=[0]*length
        node = tree
        if (not node):
            return
        elif node._name:
            print(node._name + '的编码为:',end=' ')
            for i in range(l):
                print(self.b[i],end=' ')
            print('\n')
            return

        #是树的左子节点的话赋值为0，直到到达叶结点之后print了编码，再对考虑右子树
        self.b[l] = 0
        self.pre(node._left, length,l + 1)
        self.b[l] = 1
        self.pre(node._right,length,l + 1)

#方法二
    # 函数得到每一个叶结点的路径
    def binaryTreePaths(self, root):
        if not root:#如果root不存在
            return []
        if not root._left and not root._right:#如果root就是一个叶节点
            return [str(root._value)]
        pathList = []#用来存储路径
        if root._left:#沿左子树下行递归遍历直到到达了叶节点
            root._left._codevalue = '0'
            pathList+=self.binaryTreePaths(root._left)
            self.codeway[root._left._value]=root._left._codevalue
        if root._right:
            root._right._codevalue='1'
            pathList+=self.binaryTreePaths(root._right)
            self.codeway[root._right._value] = root._right._codevalue
        for index, path in enumerate(pathList):#枚举pathList,得到对应节点路径的存放路径
            pathList[index]=str(root._value) + ' ' + path
        # for index,path in enumerate(self.codeway):

            # self.codeway[index] =str(root._codevalue) + ' ' + path
            # print(root._value,root._codevalue)
            #用这个打印每一节点对应的编码
        return pathList
     #生成哈夫曼编码
    def code_way(self):
        return self.codeway
if __name__=='__main__':
    #输入的是字符及其频数
    char_weights=[('a',9),('b',12),('c',6),('d',3),('e',5),('f',15)]
    tree=HuffmanTree(char_weights)
    length=len(char_weights)
#方法二
    pathList = tree.binaryTreePaths(tree.root)
    codeway=tree.code_way()
    print(codeway)
    print("路径输出为： ",pathList)
    for i in pathList:
        i=i.split(' ')[1:]#根节点不参与编码，所以切掉
        print("数字 ",i[-1],"的编码是：",end='')
        for j in i:
            print(codeway[int(j)],end='')
        print('\n')
#方法一
    tree.pre(tree.root,length,0)
