#include <stdio.h>

int main(){
	float total_cost, money_received, change, float_quarters, float_dimes, float_nickels, pennies;
	int dollars, quarters, dimes, nickels;
	printf("What is the total cost of the item? \n");
	scanf("%f", &total_cost);
	printf("What is the the amount of money received from the customer?\n");
	scanf("%f", &money_received);
	
	change = (money_received - total_cost);
	printf("The amount of change you will receive is: $%.2f\n", change);
	
	dollars = (change / 1);
	printf("Dollars: %d\n", dollars);
	
	quarters = ((change - dollars)/.25);  
	printf("Quarters: %d\n", quarters);
	
	float_quarters = (quarters * 0.25);  
	dimes = ((change - dollars - float_quarters)/.10); 
	printf("Dimes: %d\n", dimes);
	
	float_dimes = (dimes * .10); 
	nickels = ((change - dollars - float_quarters - float_dimes)/0.05); 
	printf("Nickels: %d\n", nickels);
	
	float_nickels = (nickels * 0.05); 
	pennies = (change - dollars - float_quarters - float_dimes - float_nickels)/0.01; 
	printf("Pennies: %.0f\n", pennies);

	return 0;
}
