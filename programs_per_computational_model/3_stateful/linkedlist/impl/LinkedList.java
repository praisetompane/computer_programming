public class LinkedList {
    Node head;
    
    LinkedList() {
        head = null;
    }
    
    public Node appendToTail(int data) {
        Node end = new Node(data, null);
        if(head == null) {
            head = end;
            return end;
        }
        Node currentNode = head;
        while(currentNode.next != null) {
            currentNode = currentNode.next;
        }
        currentNode.next = end;
        return end;
    }

    public Node deleteNode(int data) {
        Node currentNode = head;
        if(currentNode.data == data) {
            return head.next;
        }
        while(currentNode.next != null) {
            if(currentNode.next.data == data) {
                currentNode.next = currentNode.next.next;
                return head;
            }
            currentNode = currentNode.next;
        }
        return head;
    }
}
