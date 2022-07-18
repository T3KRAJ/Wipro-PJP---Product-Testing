// Tek Raj Joshi
// Superset ID: 1368453

using System;
class Program3 {
  
    public static void Main()
    {
        int[] arr = new int[] {1, 9, 6, 7, 5, 9};
        Array.Sort(arr);
        Array.Reverse(arr);
        foreach(int value in arr)
        {
            Console.Write(value + " ");
        }
    }
}