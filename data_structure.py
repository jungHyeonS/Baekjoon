
# 노드 구현 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 링크드 리스트 클래스
class LinkedList:

    # 링크드 리스트 클래스 호출시 head 값 세팅
    def __init__(self, data):
        self.head = Node(data)


    # 현재 헤드값 부터 탐색을 진행해서 다음 노드가 없을경우 노드 추가
    def addppend(self,data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)


    # 현재 헤드 기준으로 모든 노드값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 인덱스에 맞는 노드 구하기
    def get_node(self,index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    # 노드 삽입(인덱스를 기준으로)
    def add_node(self,index,value):
        # 전달 받은 데이터로 새로운 노드 생성
        new_node = Node(value)

        # 만약 index가 0이라면 새로 만든 현재 헤더가 되고 현재 헤드는 새로만든 노드가 된다 
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        # 0이 아닐경우 삽입할려는 인덱스에 이전 노드를 가져오고
        node = self.get_node(index-1)

        # 삽입할려는 인덱스 이전 노드에 next 노드 값을 저장
        next_node = node.next

        # 삽입할려는 인덱스에 이전 노드에 next는 새로 삽입한 노드가 되고
        node.next = new_node

        #새로 삽입한 노드에 next는 저장해두었던 인덱스 이전에 노드에 next
        new_node.next = next_node


    # 노드 삭제(인덱스를 기준으로)
    def delete_node(self,index):
        # 맨앞을 삭제한다면 현재 헤드의 다음 노드가 헤드가 된다
        if index == 0:
            self.head = self.head.next
            return
        #맨 앞이 아닌 중간에 노드 라면 인덱스 기준으로 이전 노드를 구하고
        node = self.get_node(index-1)

        #인적 노드에 next 값을 이전 노드에서 두칸 앞에 있는 노드
        node.next = node.next.next





link = LinkedList(1)
link.addppend(2)
link.addppend(5)
link.addppend(6)
link.addppend(7)
link.delete_node(3)
link.print_all()
# print()


# node1 = Node(1)

# head = node1

# add(3)

# print(node1.next.data)