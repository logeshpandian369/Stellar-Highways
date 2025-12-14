# Problem: Stellar Highways

The Galactic Federation wants to build a hyperspace highway connecting Sector 0 to Sector $M$. The highway is a straight line of length $M$ light-years.

There are $N$ types of construction nanobots available. The $i$-th type of nanobot:
1.  Constructs a segment of length $L_i$.
2.  Can only be deployed at a starting position $x$ if $x \equiv R_i \pmod K$.

You start construction at position $0$. When a nanobot is deployed at position $x$, it covers the range $[x, x + L_i]$. The next nanobot must start exactly at the end of the previous one (at position $x + L_i$).

Your goal is to reach or exceed position $M$ using the minimum number of nanobots. If it is impossible to reach $M$, output `-1`.

## Input
The first line contains three integers $M$, $K$, and $N$ ($1 \le M \le 10^{18}$, $1 \le K \le 50$, $1 \le N \le 100$).
The next $N$ lines each contain two integers $L_i$ and $R_i$ ($1 \le L_i \le 10^9$, $0 \le R_i < K$).

## Output
Output a single integer: the minimum number of nanobots required. If impossible, output `-1`.

## Examples

**Input**
```text
15 5 2
3 0
4 3
