// Tek Raj Joshi
// Superset ID: 1368453

using System;  
public class Program2  
{  
    public static void Main() 
{       
    int i,n,sum=0;
	Console.Write("Input the 10 numbers : \n"); 
	for (i=1; i<=10; i++)
	{
        Console.Write("Number-{0} :",i);
        n = Convert.ToInt32(Console.ReadLine());		
		sum += n;
	}
	Console.Write("The sum of 10 no is : ",sum);
   }
}