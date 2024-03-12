class ResizeableArray {

    private int[] array;
    private int numberOfElements;
    private int _size;
    public ResizeableArray(int size){
        array = new int[size];
        _size = size;
    }

    public void add(int index, int element){
        if(numberOfElements < _size)
            array[index] = element;
        else {
            resize();
            array[index] = element;
        }
        numberOfElements++;
    }

    public int get(int index) {
        return array[index];
    }

    private void resize(){
        int[] newArray = new int[_size * 2];
        for(int i = 0; i < _size; i++){
            newArray[i] = array[i];
        }
        array = newArray;
    }
}

class Main{
    public static void main(String arg[]){
        ResizeableArray items = new ResizeableArray(10);

        for(int i = 0; i < 20; i++){
            items.add(i, i + 1);
        }

       for(int i = 0; i < 20; i++){
            System.out.println("item " + i + " " + items.get(i));
        }
    }
}

