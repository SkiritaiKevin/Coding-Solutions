package asn5;

public class MyDLListNode<E> {
    private MyDLListNode<E> prev; 
    private MyDLListNode<E> next; 
    private E data; 


    // getters
    public MyDLListNode<E> getPrev(){
        return prev; 
    }

    public MyDLListNode<E> getNext(){
        return next; 
    }

    public E getData(){
        return data; 
    }

    //setters
    public void setPrev(MyDLListNode<E> prev){
        this.prev = prev; 
    }

    public void setNext(MyDLListNode<E> next){
        this.next = next; 
    }

    public void setData(E data){
        this.data = data; 
    }
}

