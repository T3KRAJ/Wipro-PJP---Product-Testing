// Tek Raj Joshi
// Superset ID: 1368453

using System;
public class Program3
{
   public static void Main( )
    {
        Console.Write("Enter the temperature in Celsius: "); 
        int celsius = Convert.ToInt32(Console.ReadLine());
 
        Console.WriteLine("Kelvin = {0}", celsius + 273);
        Console.WriteLine("Fahrenheit = {0}", celsius * 18 / 10 + 32);
    }
}