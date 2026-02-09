Introduction
Understanding algorithm efficiency requires both theoretical analysis and empirical evaluation. Input distribution and implementation details can significantly influence real-world performance. This report analyzes Randomized Quicksort and Hashing with Chaining, focusing on their efficiency and scalability under different conditions.

Randomized Quicksort
Randomized Quicksort is a divide-and-conquer sorting algorithm that selects its pivot uniformly at random. This strategy prevents adversarial input orders and improves robustness compared to deterministic pivot selection (Cormen et al., 2022).

Average Case Analysis
Using indicator random variables, the expected number of comparisons in Randomized Quicksort is:
EC= 𝑂(𝑛log𝑛)
This bound holds regardless of the initial input order, giving Randomized Quicksort expected 
O(nlogn) performance (Cormen et al., 2022).

Empherical Results
Randomized Quicksort was compared with Deterministic Quicksort across multiple input distributions:
| Input Type        | Deterministic QS | Randomized QS |
| ----------------- | ---------------- | ------------- |
| Random            | Fast             | Fast          |
| Sorted            | RecursionError   | Fast          |
| Reverse Sorted    | RecursionError   | Fast          |
| Repeated Elements | RecursionError   | Stable        |
Deterministic Quicksort exhibits worst-case 𝑂(𝑛2) behavior on structured inputs, leading to deep recursion and runtime failure. Randomized Quicksort avoids this issue by producing balanced partitions with high probability.

Hashing with Chaining
Hashing with chaining resolves collisions by storing all colliding keys in a list at each table index. Under the assumption of simple uniform hashing, the expected time for insert, search, and delete operations is: O(1+α) where 𝛼=𝑛/𝑚 is the load factor (Kleinberg & Tardos, 2006).
Maintaining a low load factor through appropriate table sizing and resizing helps preserve constant-time performance (Sedgewick & Wayne, 2011).

Conclusion
Randomized Quicksort consistently achieves expected O(nlogn) performance and outperforms deterministic pivot selection on adversarial inputs. Hashing with chaining provides efficient dictionary operations when the load factor remains low. These results highlight the importance of randomization and careful data structure design in practical algorithm selection.

References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.
Kleinberg, J., & Tardos, É. (2006). Algorithm Design. Pearson.
Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley.