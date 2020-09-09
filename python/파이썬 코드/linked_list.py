class Node(): # 연결리스트에서 하나의 요소를 저장할 객체를 만드는 클래스
    # 데이터 하나를 저장할 공간(변수)
    # 다음 노드의 주소를 저장할 변수
    def __init__(self, data): #data : 매개변수(함수 외부에서 들어오는 값을 받아내는 변수)
        self.data = data
        self.next = none #다음 노드가 가리키는 변수

    def set_next(self, next):
        self.next = next
    pass

class LinkedList():
    # 노드들이 연결되어 있는 리스트
    # 데이터를 저장하는 모든 노드들을 저장하지 않음
    # 가장 앞쪽에 있는 노드(head)만을 가지고 있는다.
    def __init__(self):
        # variable annotation
        self.head : node
        self.head = none


    # 삽입, 삭제, 조회, pop
    def insert(self, data): # 해당인덱스 데이터 삭제
        # 마지막 노드에 새로운 노드를 만들어서 연결
        new_node = Node(data)
        current = self.head # 가지고 있는게 head밖에 없음
        if current == None: # 데이터가 없음!
            self.head = new_node
        else :
        # 아니면 마지막 노드를 찾아서 마지막 노드의 nest에
        # 새로운 노드를 연결해주면 된다.
            while current.next :
                current = current.next
            current.next = new_node

    def delete(self, idx): # 해당인덱스 데이터 삭제
        pass
    def get(self, idx): # 해당인덱스 데이터 조회
        current = self.head
        for i in range(idx):
            current = current.next
        return current.data
    def pop(self): #마지막 노드 삭제/반환
        pass


my_list = LinkedList()
print(my_list)