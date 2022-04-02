import java.util.*;

class Matrix{
    private int n,m;
  private int[][] matrix;

  public Matrix(int n, int m){
    this.n = n;
    this.m = m;
    matrix = new int[n][m];
  }

  public void read(){
    Scanner sc = new Scanner(System.in);
    System.out.println(String.format("Enter the matrix(of size %s*%s) elements: ",n,m));
    for (int i=0; i<n; ++i)
      for(int j =0; j<m; ++j)
        matrix[i][j] = sc.nextInt();
  }

  public void print(){
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<n; ++i){
      for(int j=0; j<n; ++j){
        sb.append(matrix[i][j]+" ");
      }
      sb.append("\n");
    }
    System.out.println("Matrix is: \n"+sb.toString());
  }

  public void printSumOfDiagonal(){
    int sum = 0;
    for (int i =0; i<n; ++i){
      sum+=matrix[i][i];
    }
    System.out.println("Sum of diagonal: "+sum);
  }
  public int findLargestElement(){
    int largest = matrix[0][0];
    for (int i =0; i<n; ++i){
      for (int j =0; j<m; ++j){
        largest = Math.max(largest, matrix[i][j]);
      }
    }
    return largest;
  }
}

public class MatrixMain{
  public static void main(String []args){
    int n = 2;
    int m = 2;
    Matrix mat = new Matrix(n,m);
    mat.read();
    mat.print();
    mat.printSumOfDiagonal();
    System.out.println("Largest Element: "+mat.findLargestElement());
  }
}
