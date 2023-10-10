package asn5;

public class MyDLList<E> {

    // Attributes: head, tail, size
    private MyDLListNode<E> head;
    private MyDLListNode<E> tail; 
    private int size;     
    
    // Default constructor
    public MyDLList() {
        head = null;
        tail = null; 
        size = 0; 
    }
    
    public int getSize() {
        return size;        
    }
    
    public void append(E newData) {
        MyDLListNode<E> newNode = new MyDLListNode<>(); 
        newNode.setData(newData); 
        if(this.head == null){
            this.head = newNode; 
            this.tail = newNode;  
        }
        else{ 
            newNode.setPrev(this.tail); 
            this.tail.setNext(newNode); 
            this.tail = newNode; 
        }
        this.size++; 
    }
    
    public boolean addAfter(E newData, E curData) {
        MyDLListNode<E> newNode = new MyDLListNode<>(); 
        newNode.setData(newData); 
        MyDLListNode<E> curNode = this.head;
        if(curData == null){
            newNode.setNext(this.head); 
            this.head.setPrev(newNode); 
            this.head = newNode; 
            size++; 
            return true; 
        }
        else if(curNode.equals(this.tail)){
            this.tail.setNext(newNode); 
            newNode.setPrev(this.tail); 
            this.tail = newNode; 
            return true; 
        }
        else{
            while(curNode != null){
                if(curNode.getData() != null && curNode.getData().equals(curData)){ // https://stackoverflow.com/questions/23042655/equals-method-throws-nullpointerexception
                    MyDLListNode<E> sucNode = curNode.getNext(); 
                    newNode.setPrev(curNode); 
                    newNode.setNext(sucNode);
                    if(sucNode != null){
                        sucNode.setPrev(newNode); 
                    } 
                    curNode.setNext(newNode);
                    size++; 
                    return true;
                }
                curNode = curNode.getNext(); 
            }
            return false;
        }
    }
    
    public E remove(E theData) {
        // Find the node
        MyDLListNode<E> curNode = head;
        
        while (curNode != null) {
            if (curNode.getData() != null && curNode.getData().equals(theData)) { // https://stackoverflow.com/questions/23042655/equals-method-throws-nullpointerexception
                break;
            }
            curNode = curNode.getNext();
        }
                
        if (curNode == null) {
            return null;
        } else {
            // Remove the node
            MyDLListNode<E> sucNode = curNode.getNext();
            MyDLListNode<E> predNode = curNode.getPrev();
            
            if (sucNode != null) 
                sucNode.setPrev(predNode);
            
            if (predNode != null)
                predNode.setNext(sucNode);
            
            if (curNode == head)
                head = sucNode;
            
            if (curNode == tail)
                tail = predNode;
            
            size--;
            return curNode.getData();
        }
    }
    
    public E get(int index) {
        if(index >= this.size || index < 0){
            return null; 
        }
        
        MyDLListNode<E> curNode = this.head; 
        int i = 0; 
        while(curNode != null && i < index){ // this will break when we hit the target index
            curNode = curNode.getNext();
            i++;
        }
        if(curNode != null){
            return curNode.getData(); 
        }
        return null; 
    }
    
    public String toString() {
        String result = "";
        MyDLListNode<E> curNode = this.head;
        result += "Complete the toString method.";
        while(curNode != null){
            result += curNode.getData();
            result += " "; 
            curNode = curNode.getNext();  
        }
        return result;
    }
    
}
