### Solved Exercise 1)
>Take the following list of functions and arrange them in ascending order of growth rate. That is, if function g(n) immediately follows function f(n) in your list, then it should be the case that f(n) is O(g(n)).<p>
><img src="./Images/Figure_2_1.png" alt="drawing" width="100"/>

The order of functions from slowest to fastest is logarithmic -> polynomial -> exponential
<br>
log2(n) is logarithmic, n^(1/3) is polynomial, and 10^n is expotential. So far, we have:

Slowest&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fastest
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...log2(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^(1/3)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^n...<p>
n^n is easiest to compare to 10^n. We can see that when n > 10, n^n will be greater than 10^n. So now we have:
<p> 
Slowest&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fastest
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...log2(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^(1/3)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^n...<p>

The last to compare is 2^sqrt(log2(n)). <u>A useful rule of thumb in such situations is to try taking logarithms to see whether this makes things clearer.</u><br>
<img src="./Images/log_rules.png" alt="drawing" width="200"/><br>
Using rule 6, log2(2^sqrt(log2(n))) = sqrt(log2(n)) or log2(n)^(1/2). <br>
In order to have a fair comparison, let's take the log of 
* n^(1/3) = 1/3 * log2(n)  
* log2(n) = log2(log2(n))<br>

By replacing log2(n) with "z", we have:
* 1/3 * z
* log2(z)
* z^(1/2) 
<br>
Let's test z = 100. We can see that (1/3) * 100 = 33.3 is much bigger than log2(100) = 6.64 and 100^(1/2) = 10 (2nd place). The final order is:
<p> 
Slowest&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fastest
<p>
&nbsp;&nbsp;&nbsp;log2(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2^sqrt(log2(n))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^(1/3)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^n<p>

### Solved Exercise 2)
>Let f and g be two functions that take nonnegative values, and suppose that f = O(g). Show that g = Ω(f). 

For this problem, we essentially just need to unwind that big O and omega are opposites. If f is upper-bounded by g, that means g is lower-bounded by f. 
* f = O(g)  means there exists a constant c such that f(n) <= c*g(n) for all n >= n0. Thus, (1/c) * f(n) <= g(n)
* For proving g = Ω(f), there exists a constant c such that g(n) >= c * f(n) for all n >= n0. That constant is (1/c) here!

### 1)
> Suppose you have algorithms with the five running times listed below. (Assume these are the exact running times.) How much slower do each of these algorithms get when you (a) double the input size, or (b) increase the input size by one?<br>
(a) n^2<br>
(b) n^3<br>
(c) 100n^2<br>
(d) nlogn<br>
(e) 2^n<br>

When the input size is doubled (n to 2n), n^2 becomes 4n^2, so it gets slower by a **factor of 4**. n^3 becomes 8n^3, so it gets slower by a **factor of 8**. 100n^2 becomes 400n^2, so it gets slower by a **factor of 4**. nlogn becomes 2nlog(2n) = 2nlogn???, so it gets slower by a **factor of 2, plus an additive 2n**. 2^n becomes 2^(2n) - so for n = 1: 2 => 4, n = 2: 4 -> 16, n = 3: 8 -> 64. It gets slower by **the square of the previous running time**.
<p>

When the input size is increased by 1 (n to n + 1), n^2 becomes (n + 1)^2 or n^2 + 2n + 1, which is slower by an **additive of 2n + 1**. n^3 becomes (n + 1)^3 = (n^2 + 2n + 1) * (n + 1) = n^3 + 2n^2 + n + n^2 + 2n + 1 = n^3 + 3n^2 + 3n + 1, which is slower by an **additive of 3n^2 + 3n + 1**. 100n^2 becomes 100(n+1)^2, or 100n^2 + 200n + 100, which is slower by an **additive of 200n + 100**. nlogn becomes (n+1)log(n+1) or nlog(n+1) + log(n+1).... **???**<br>.
2^n becomes 2^(n+1). Since, a^m × a^n = a^m+n, then it becomes 2^n * 2, and therefore becomes slower by a **factor of 2**.

### 2)
>Suppose you have algorithms with the six running times listed below. (Assume these are the exact number of operations performed as a function of the input size n.) Suppose you have a computer that can perform 10^10 operations per second, and you need to compute a result in at most an hour of computation. For each of the algorithms, what is the largest input size n for which you would be able to get the result within an hour?<br>
(a) n^2<br>
(b) n^3<br>
(c) 100n^2<br>
(d) nlogn<br>
(e) 2^n<br>
(f) 2^2^n

10^10 operations per second, 3,600 seconds in an hour.<br> 
* n^2 = 10^10 * 3600 --> n = 6,000,000 
* n^3 = 10^10 * 3600 = (10^10 * 3600)^(1/3) --> n = 33,019
* 100n^2 = 10^10 * 3600 --> n = 600,000
* nlogn = 10^10 * 3600,  logn * e^(logn) = 10^10 * 3600,  
log(n) = (10^10 * 3600) * e ^(10^10 * 3600), --> n = 9 * 10^11????
* 2^n = 10^10 * 3600. Recall a^x = N -> x = loga(N). So n = log2(10^10 * 3600) (base of 2 matters) --> n = 45
* 2^2^n = 10^10 * 3600. Recall a^x = N -> x = loga(N). So 2^n = log2(10^10 * 3600) and then, do it again and n = log2(log2(10^10 * 3600)) --> n = 5

### 3)
> Take the following list of functions and arrange the min ascending order of growth rate. That is, if function g(n) immediately follows function f(n) in your list, then it should be the case that f(n) is O(g(n)).<br>
f1(n) = n^(2.5)<br>
f2(n) = sqrt(2n)<br>
f3(n) = n + 10<br>
f4(n) = 10^n<br>
f5(n) = 100^n<br>
f6(n) = n^2*logn

<p>
Notes: sqrt(2n) = 2n^(1/2) 
<br>
We know polynomials grower slow than exponentials so 100^n and 10^n go last (fastest).<br>
n^2*logn grows FASTER than n^2, and we know that logarithms grow <u>slower</u> than polynomials, so it grows slower than n^c for any c > 2. Therefore it goes between f3(n) and f1(n). <br>

Slowest&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fastest
<p>
&nbsp;&nbsp;&nbsp;sqrt(2n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n + 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^2*logn&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^(2.5)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100^n


### 4)
>Take the following list of functions and arrange the min ascending order of growth rate. That is, if function g(n) immediately follows function f(n) in your list, then it should be the case that f(n) is O(g(n)).<br>
g1(n) = 2^sqrt(logn)<br>
g2(n) = 2^n<br>
g3(n) = n(logn)^3<br>
g4(n) = n^(4/3)<br>
g5(n) = n^logn<br>
g6(n) = 2^2^n<br>
g7(n) = 2^n^2

First, we can determine that 2^n > 2^sqrt(logn). <br>
2^2^n > 2^n^2 since the exponential 2^n is greater than the polynomial n^2.
<br>To combine these four, 2^n is of course smaller than 2^n^2.
<br>
Now let's compare the rest: n^(4/3), n(logn)^3, or n^logn. n^logn > n(logn)^3 > n^(4/3).
<br>

* g1(n) comes before g5(n). Solve by taking the log. log(2^sqrt(logn)) ? log(n^log(n)) --> sqrt(logn) ? **logn + log(log(n))????? > logn.** So g1(n) < g5(n).<br>
* g5(n) comes before g3(n) since n^logn = logn^n < n*(logn)^3.
* g3(n) comes before g4(n). Divide both by n to be logn^3 and n^(1/3). Then by 3. logn grows slower than the polynomial n^(1/9).
* g4(n) comes before g2(n) because polynomials grow slower than exponentials. 
* g2(n) comes before g7(n). 2^n < 2^n^2
* g7(n) comes before g6(n) since we are comparing n^2 to 2^n and polynomials grow slower than exponentials


Slowest&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fastest
<p>
2^sqrt(logn)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n^logn&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n(logn)^3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbspn^(4/3)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2^n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2^n^2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2^2^n
g1(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g5(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g3(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g4(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g2(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g7(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g6(n)



### 5)
> Assume you have functions f and g such that f(n) is O(g(n)). For each of the following statements, decide whether you think it is true or false and give a proof or counterexample.<br>
(a) log2f(n) is O(log2g(n)) <br>
(b) 2^f(n) is O(2^g(n))<br>
(c) f(n)^2 is O(g(n)^2).

(a) **False**. If f(n) is O(g(n)), this means there exists a constant c such that f(n) <= c\*g(n) for all n >= n0. Thus, we would be saying that log2(f(n)) <= c*log2(g(n)). Log2 acts different with a 1 (it becomes a 0). So if g(n) = 1 and f(n) = 2, then log2(g(n)) is 0, and we can't say that log2(f(n)) <= c\*log2(g(n)).

(b) **False**. If f(n) is O(g(n)), this means there exists a constant c such that f(n) <= c\*g(n) for all n >= n0. We want to decide whether 2^f(n) <= c * 2^(g(n)).
Take f(n) = 2n and g(n) = n. Then 4^n <= c * 2^(n).

(c) **True**. If f(n) is O(g(n)), this means there exists a constant c such that f(n) <= c\*g(n) for all n >= n0. The following also holds: f(n)^2 <= c^2 * g(n)^2 for all n >= n0.


### 6)
### 7)
### 8)