import java.util.*;

class Person{
  private String name
  private int id;

  public Person(){

  }

  public Person(String name, int id){
    this.name = name;
    this.id = id;
  }

  public void print(){
    System.out.println("Name: "+name);
    System.out.println("ID: "+id);
  }
  public void read(){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the name: ");
    this.name = sc.nextLine();
    System.out.println("Enter the id: ");
    this.id = Integer.parseInt(sc.nextLine());
  }
}

class Student extends Person{
  private int rollNo;
  private String branch;

  public Student(){

  }

  public Student(String name, int id, int rollNo, String branch){
    super(name,id);
    this.rollNo = rollNo;
    this.branch = branch;
  }

  public void print(){
    super.print();
    System.out.println("Roll No: "+rollNo);
    System.out.println("branch: "+branch);
  }
  public void read(){
    super.read();
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the roll no: ");
    this.rollNo = Integer.parseInt(sc.nextLine());
    System.out.println("Enter the branch: ");
    this.branch = sc.nextLine();
  }
}

class Employee extends Person{
  private int salary;
  private String designation;

  public Employee(){

  }

  public Employee(String name, int id, String designation, int salary){
    super(name,id);
    this.designation = designation;
    this.salary = salary;
  }

  public void print(){
    super.print();
    System.out.println("Designation: "+designation);
    System.out.println("Salary: "+salary);
  }
  public void read(){
    super.read();
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the designation: ");
    this.designation = sc.nextLine();
    System.out.println("Enter the salary: ");
    this.salary = Integer.parseInt(sc.nextLine());
  }
}


public class Inheritance{
  public static void main(String []args){
    Student stdnt = new Student("Balram", 1, 100, "Electrical");
    stdnt.print();
    Employee empl = new Employee("Akshit", 2, "Software Engg", 1000000);
    empl.print();
  }
}
