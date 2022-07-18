// Tek Raj Joshi
// Superset ID: 1368453

using System;
public class Program1
{
    public static void Main()
    {
        string myStr;
        int i, len, lower_case, upper_case;
        Console.WriteLine(" Enter string");
        myStr = Console.ReadLine();
        lower_case = 0;
        upper_case = 0;
        len = myStr.Length;
        for (i = 0; i < len; i++)
        {
            if (myStr[i] >= 'a' & amp; &amp; myStr[i] <= 'z') {
            lower_case++;
        } else if (myStr[i] >= 'A' & amp; &amp; myStr[i] <= 'Z') {
            upper_case++;
        }
        Console.WriteLine("Number of lowercase words = ", lower_case);  
        Console.WriteLine("Number of Uppercase words = ", upper_case);  

    }
}