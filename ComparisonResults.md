# Comparison Results

I ran a speedtest on my personal computer to get a general idea of how fast each method was. If you want, feel free to run the speedtest on your computer (it should take a couple minutes to complete).

_Note: The difference in speed is trivial between **Default Argument Cache**, **Global Variable Cache**, and **Class Cache**. As functools is a wrapper for a library coded in c, the functools cache is much faster (as most standard libraries should be)._

| Method                                | Time (seconds)   |
|---------------------------------------|------------------|
| Factorial With No Cache               | 0.199801 seconds |
| Factorial with Class Cache            | 0.000185 seconds |
| Factorial with Default Argument Cache | 0.000149 seconds |
| Factorial with Functools Cache        | 0.000092 seconds |
| Factorial with Global Variable Cache  | 0.000155 seconds |