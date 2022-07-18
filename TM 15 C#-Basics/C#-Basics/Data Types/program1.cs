// Tek Raj Joshi
// Superset ID: 1368453

using System;

class DateandTime

{
    static void Main()
    {
	DateTime now = DateTime.Now;
	Console.WriteLine(" The current Month No. is : {0} ",now.Day);
	Console.WriteLine(" The current Month is : {0}\n",now.ToString("MMMM"));
    Console.WriteLine(" The current Month No. is : {0} ",now.Year);
    Console.WriteLine(" The Day of Week is : {0} ",(int)myDate.DayOfWeek);
    Console.WriteLine(" The Day of Year is : {0} ",(int)myDate.DayOfYear);
    Console.WriteLine(" The short Date is : {0}\n",now.ToString("d", new CultureInfo("hi-IN")));
    Console.WriteLine(" The long Date is : {0}\n",now.ToString("D", new CultureInfo("hi-IN")));
    }
}