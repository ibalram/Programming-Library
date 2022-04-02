import java.util.*;

class AreaPer{
  int l, b;
  int area(int l, int b)
  {

    this.l=l;
     this.b=b;
     return (l*b);
  }

  int perimeter(int l, int b)
  {
   this.l = l;
   this.b = b;
   return 2*(l+b);
  }

}

public class Main{

     public static void main(String []args){

         Scanner ab = new Scanner(System.in);
         int length, breadth;
         System.out.println("Enter First Rectangle Length");
         length = ab.nextInt();
         System.out.println("Enter First Rectangle Breadth");
         breadth = ab.nextInt();

         AreaPer ob = new AreaPer();
         System.out.println("Area is: "+ob.area(length, breadth));

         System.out.println("Enter Second Rectangle Length");
         length = ab.nextInt();
         System.out.println("Enter Second Rectangle Breadth");
         breadth = ab.nextInt();
         System.out.println("Perimeter is: "+ob.perimeter(length, breadth));
     }
}
