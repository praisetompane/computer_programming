public static void main(String[] arg) {
    ExampleRunable test = new ExampleRunable;
    Thread thread = new Thread(test);

    try {
        thread.start();
        while(test.count < 5){
            Thread.sleep(250);
        }
    } catch (Exception e) {
        System.out.println("Encountered error running thread");
    }
}