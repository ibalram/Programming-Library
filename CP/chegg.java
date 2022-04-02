class Utilities{
    public getTaxReport(int status, int income){
        // declaring three variable to store the tax payments
        double part1=0,part2=0,part3 = 0;

        if (status>2 || status<1){    // Checking if status is illegal
            return "Illegal Status: "+status;
        }

        if (status==1) { // checking the status
            result += "Single Filing:"; // if the status is single then add Single Filling to the result
            if (income >8350){ // if income is greater than base tax value
                part1 = 8350*(0.10); // compute the part1
                if (income>33950) { // if the income is greater than the second limit then
                    part2 = (33950-8350)*(0.15); // compute part2 and part3
                    part3 = (income-33950)*(0.25);
                }else { // if the income lies in second range which means it has only two parts
                    part2 = (income-8350)*0.15; // compute the part2
                }
            }else {
                part1 = income*0.10; // if the income is less than the first range upper Limit which means it has only ¢
            }
        else { //if the status is married
            result+="Married Filing:"; //add the married filling to the result
            if(income >16700){
                part1 = 16700*(0.10);
                if(income>67900){
                    part2 = (67900-16700)*(0.15); // compute part2 and part3
                    part3 = (income-67900)*(0.25);
                }else { // if the income is less than 67900 then it has only part2
                    part2 = (income-16700)*0.15; // compute the part2
                }
            }else { //if the income is less than 16700 which means it has only part1
                part1 = income*0.10;
            }
        }
        double totalTax = part1+part2+part3; // computing the total
        if(part3>0) { // if part3 is greater than 0 then the person have all three parts
            result += String.format(" $%.2f (Part I: $%.2f, Part II: $%.2f, Part III: $%.2f)", totalTax, part1, part2,part3);
        }else if(part2>0) {// if the part2 is > 0 then he has only part1 and part2
            result += String.format(" $%.2f (Part I: $%.2f, Part II: $%.2f)",totalTax,part1,part2 );
        }else { //else he has only part1
            result += String.format(" $%.2f (Part I: $%.2f)", totalTax, part1);
        }
    }
}
