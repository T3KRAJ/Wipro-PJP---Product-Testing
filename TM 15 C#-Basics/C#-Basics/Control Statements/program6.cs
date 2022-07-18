// Tek Raj Joshi
// Superset ID: 1368453

using System;  
  public class Program6
   {  
     public static void Main(string[] args)  
      {  
       int i, fact=1, num;      
       Console.Write("Enter any number: ");      
       num= int.Parse(Console.ReadLine());     
       for(i=1; i<=num; i++){      
        fact=fact*i;      
       }      
       Console.Write("Factorial of " +num+" is: "+fact);    
     }  
  }