// Tek Raj Joshi
// Superset ID: 1368453

using System;
public class Program2
{
    public static void Main()
    {
        string str;
        int l = 0;
        Console.Write("Input the string : ");
        str = Console.ReadLine();
        while (l < str.Length)
        {
            Console.Write("{0} ", str[l]);
            l++;
        }
        Console.Write("\n\n");
    }
}