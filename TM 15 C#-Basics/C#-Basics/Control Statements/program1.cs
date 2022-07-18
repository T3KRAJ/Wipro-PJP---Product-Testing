// Tek Raj Joshi
// Superset ID: 1368453

using System;
class Program1
{
public static getFibonacci()  
{  
    int a = 0, b = 1, c = 0;  
    Console.Write("{0} {1}", a,b);  
    for (int i = 2; i <= 20; i++)  
    {  
        c= a + b;  
        Console.Write(" {0}", c);  
        a= b;  
        b= c;  
    }  
}
}