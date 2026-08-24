# Time & Space Complexity

## What Big-O measures

Big-O describes how the amount of work grows as input size `n` grows — not raw runtime. It ignores constants and lower-order terms because those become irrelevant at large `n`; only the growth *shape* determines whether an algorithm finishes in time.

| n | 10 | 10,000 |
|---|---|---|
| O(1) | 1 | 1 |
| O(log n) | ~3.3 | ~13.3 |
| O(n) | 10 | 10,000 |
| O(n log n) | ~33 | ~132,900 |
| O(n²) | 100 | 100,000,000 |
| O(2ⁿ) | 1,024 | astronomically huge |

## Reading complexity off code

- **Nested loops multiply**: two loops of size `n`, one inside the other → O(n²).
- **Sequential loops add**, and Big-O drops the sum down to the largest term: `O(n) + O(n) = O(n)`.
- **A loop that halves each step is O(log n)**: `i = n; while i > 1: i //= 2` — asks "how many times can n be halved before reaching 1," which is `log₂ n`.

## Recursion — count total calls, not depth

```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```
O(2ⁿ) — draw the call tree, it doubles at every level, `n` levels deep.

Memoized version is O(n) — every value 0..n computed exactly once; repeated calls short-circuit through the cache, killing duplicate subtrees.

## Amortized complexity

`list.append` is O(1) *amortized* — occasional resizes are O(n) but happen exponentially rarely (capacity roughly doubles each resize), so the average across all calls stays O(1). `list.insert(0, x)` has no such excuse: it shifts every element, every call, no amortization saves it.

## Space complexity

Count extra memory beyond the input itself.
- A running total (`total = 0; total += n`) → O(1) space.
- Building a new list the size of the input → O(n) space.
- **Recursion has hidden space cost: the call stack.** `factorial(n)` is O(n) *space*, not O(1) — `n` frames sit on the stack simultaneously before any unwinds.

## Best / average / worst case

Big-O with no qualifier usually means **worst case** — the number that determines whether a judge's nastiest test case causes a Time Limit Exceeded.

## Set/dict lookup precision

Hash set/map lookup is O(1) **average case**, not guaranteed worst case (hash collisions can degrade it). Say "average O(1)" to be precise.

---

# Recursion complexity — the recurrence relation method

Write the equation relating `T(n)` to smaller subproblems, then unroll it by hand. The complexity falls out mechanically.

## Shape 1 — subtract one, constant work
```
T(n) = T(n-1) + O(1)  →  O(n)
```
Unrolls to `T(0) + n×1`. Just counting down.

## Shape 2 — subtract one, linear work
```
T(n) = T(n-1) + O(n)  →  O(n²)
```
Unrolls to `1 + 2 + ... + n = n(n+1)/2`.

## Shape 3 — halve, constant work (binary search)
```
T(n) = T(n/2) + O(1)  →  O(log n)
```
Number of halvings from `n` to `1` is `log₂ n`.

## Shape 4 — halve, linear work
```
T(n) = T(n/2) + O(n)  →  O(n)
```
`n + n/2 + n/4 + ... → 2n`. Geometric series collapses — **dominated by the first (biggest) level**, everything below barely adds anything.

## Shape 5 — two calls, halve, linear merge (merge sort)
```
T(n) = 2·T(n/2) + O(n)  →  O(n log n)
```
Every level costs the same total `n` (branching ×2 and per-call work ÷2 cancel out exactly), and there are `log n` levels. Requires **branching** — this is what actually produces `n log n`, not recursion alone.

## Shape 6 — two calls, subtract one (unmemoized Fibonacci)
```
T(n) = T(n-1) + T(n-2) + O(1)  →  O(2ⁿ)
```

## The exponential signature — the one rule that matters

**Exponential blowup happens specifically when branching ≥ 2 AND the input shrinks by subtracting a constant** (not dividing).

| Shrink type | Depth | Exponential risk |
|---|---|---|
| subtract constant (`n-1`) | `n` | **yes**, if branching ≥ 2 |
| divide by constant (`n/2`, `n/3`) | `log n` | **no** — collapses to polynomial or `n log n` |

Divisive recursion with branching (e.g. `T(n) = 3·T(n/3) + O(n)`) still lands on `O(n log n)` — branching and shrink-by-division cancel per level, same mechanism as merge sort, just base-3. Big-O doesn't care about log base.

**Two questions decide everything:** how many recursive calls does each invocation make, and does the input shrink by a constant amount or a constant fraction.
