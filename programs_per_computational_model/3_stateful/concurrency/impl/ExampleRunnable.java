import java.lang.Runnable;
import java.lang.Thread;

public class ExampleRunable implements Runnable {
    public int count = 0;
    public void run() {
        System.out.println("Commencing Example Runnable");
        try {
            while(count < 5){
                count++;
                Thread.sleep(500);
            }
        }
        catch(InterruptedException e) {
            System.out.println("Thread interrupted" + e.getMessage());
        }
        System.out.println("Example Runnable done!");
    }
}




