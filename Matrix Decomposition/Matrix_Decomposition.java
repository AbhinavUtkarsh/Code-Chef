import java.util.*;
import java.io.*; 

public class Matrix_Decomposition{
        public static void main (String[] args) throws java.lang.Exception{

            try{
            Scanner input_test=new Scanner(System.in);
            Integer Test=input_test.nextInt();
            
            while(Test!=0)
            {   
                BufferedReader in = new BufferedReader(new InputStreamReader(System.in)); 
                String[] input = new String[2]; 
                int N; 
                int A; 
                input = in.readLine().split(" "); 
                N = Integer.parseInt(input[0]); 
                A = Integer.parseInt(input[1]); 
                long Last=A;
                long Sum_of_Products=A;
                long Factor=1;
                int Steps_in_This_Iteration=0;
                for (int i=2;i<N+1;i++){
                    Steps_in_This_Iteration=((2*i)-1);
                    Factor=(long)Math.pow(A*Last,Steps_in_This_Iteration);
                    Last=A*Factor;
                    Sum_of_Products = Sum_of_Products + Factor;
                }
                System.out.println((Sum_of_Products%1000000007));

                Test=Test-1;
            } 
            input_test.close();
        
        }catch(Exception e){
			return;
		}
    }
}