import java.util.*;

// Person.java
public class Person implements Comparable<Person>{
    public int totalAccountBalance;
    public int age;
    public int salary;
    public int numOfDependents;

    public Person(int totalAccountBalance,int age, int salary, int numOfDependents){
        this.totalAccountBalance = totalAccountBalance;
        this.age = age;
        this.salary = salary;
        this.numOfDependents = numOfDependents;
    }

    @Override
    public int compareTo(Person other){
        if (this.totalAccountBalance-other.totalAccountBalance!=0)
            return this.totalAccountBalance-other.totalAccountBalance;
        if (this.age-other.age!=0)
            return this.age-other.age;
        if (this.salary-other.salary!=0)
            return this.salary-other.salary;
        return this.numOfDependents - other.numOfDependents;
    }

    @Override
    public String toString(){
        return String.format("total Account Balance: %s, age: %s, salary: %s, number Of Dependents: %s", totalAccountBalance, age, salary, numOfDependents);
    }
}


// Main.java
import java.util.*;
public class Main{
    public static void main(String[] args){
        List<Person> listOfPersons = new ArrayList<Person>();
        listOfPersons.add(new Person(0,1,1,2));
        listOfPersons.add(new Person(5,2,5,2));
        listOfPersons.add(new Person(2,42,4,2));
        listOfPersons.add(new Person(0,3,4,2));

        Collections.sort(listOfPersons);

        for(Person person: listOfPersons){
            System.out.println(person);
        }

    }
}
