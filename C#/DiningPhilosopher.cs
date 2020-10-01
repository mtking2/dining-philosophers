/*
 * C# Program to Illustrate Dining Philosopher Problem
 */
using System;
using System.Threading;
class philofork
{
    bool[] fork = new bool[5]; 
    public void Get(int left, int right)
    {
        lock (this)
        {
            while (fork[left] || fork[right]) Monitor.Wait(this);
            fork[left] = true; fork[right] = true;
        }
    }
    public void Put(int left, int right)
    {
        lock (this)
        {
            fork[left] = false; fork[right] = false;
            Monitor.PulseAll(this);
        }
    }
}
class Philo
{
    int n;           
    int thinkDelay;  
    int eatDelay;    
    int left, right; 
    philofork philofork;     
    public Philo(int n, int thinkDelay, int eatDelay, philofork philofork)
    {
        this.n = n;
        this.thinkDelay = thinkDelay; this.eatDelay = eatDelay;
        this.philofork = philofork;
        left = n == 0 ? 4 : n - 1;
        right = (n + 1) % 5;
        new Thread(new ThreadStart(Run)).Start();
    }
    public void Run()
    {
        for (; ; )
        {
            try
            {
                Thread.Sleep(thinkDelay);
                philofork.Get(left, right);
                Console.WriteLine("Philosopher " + n + " is eating...");
                Console.ReadLine();
                Thread.Sleep(eatDelay);
                philofork.Put(left, right);
            }
            catch
            {
                return;
            }
        }
    }
 
}
public class philopblm
{
    public static void Main()
    {
        philofork philofork = new philofork();
        new Philo(0, 10, 50, philofork);
        new Philo(1, 20, 40, philofork);
        new Philo(2, 30, 30, philofork);
        new Philo(3, 40, 20, philofork);
        new Philo(4, 50, 10, philofork);
    }
}