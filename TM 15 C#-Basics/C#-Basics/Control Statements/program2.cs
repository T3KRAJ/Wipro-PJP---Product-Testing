// Tek Raj Joshi
// Superset ID: 1368453
using System;  

namespace palindrome  
{  
    class Program2
    {  
        static void Main(string[] args)  
        {  
            string s,revs="";  
            Console.WriteLine(" Enter string");  
            s = Console.ReadLine();  
            for (int i = s.Length-1; i >=0; i--)  
            {  
                revs += s[i].ToString();  
            }  
            if (revs == s)   
            {  
                Console.WriteLine("String is Palindrome.", s, revs);  
            }  
            else  
            {  
                Console.WriteLine("String is not Palindrome.", s, revs);  
            }  
            Console.ReadKey();  
        }  
    }  
}