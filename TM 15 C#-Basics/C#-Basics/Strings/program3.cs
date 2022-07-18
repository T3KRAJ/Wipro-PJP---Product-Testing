// Tek Raj Joshi
// Superset ID: 1368453

using System;
public class Exercise4
{
    public static void Main()
    {
        string str;
        string ch;
        int l = 0;
        Console.Write("Input the string : ");
        str = Console.ReadLine();

        l = str.Length - 1;
        // i) soln
        Console.Write("The characters of the string in reverse are : \n");
        while (l >= 0)
        {
            Console.Write("{0} ", str[l]);
            l--;
        }
        // ii) soln
        Console.Write(str.Substring(1, str.Length));
        // iii) soln
        Console.Write("Input the character to replace : ");
        ch = Console.ReadLine();
        string newStr = str.Replace(ch, '$');
        Console.Write(newStr);
        //    iv) soln
        string copyiedStr;
        copyiedStr = str;
        Console.Write("Copyied string:" + copyiedStr);
        Console.Write("Old String :" + str);
    }
}