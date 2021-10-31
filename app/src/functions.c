#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
float add(float x, float y) {
    return x + y;
}

EMSCRIPTEN_KEEPALIVE
int fib(int n) {
    if(n <= 0){
        return 0;
    }
    int i, t, a = 0, b = 1;
    for (i = 1; i < n; i++) {
        t = a + b;
        a = b;
        b = t;
    }
    return b;
}

EMSCRIPTEN_KEEPALIVE
int fib_rec(int n) {
    if (n <= 1)
        return n;

    return fib_rec(n - 1) + fib_rec(n - 2);
}

int fib_dynamic_programming(int n)
{
     
    // Declare an array to store
    // Fibonacci numbers.
    // 1 extra to handle
    // case, n = 0
    int f[n + 2];
    int i;
 
    // 0th and 1st number of the
    // series are 0 and 1
    f[0] = 0;
    f[1] = 1;
 
    for(i = 2; i <= n; i++)
    {
         
       //Add the previous 2 numbers
       // in the series and store it
       f[i] = f[i - 1] + f[i - 2];
    }
    return f[n];
}
