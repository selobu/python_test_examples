# python_test_examples

technical python tests


## test04 optimization:
given a list of point [[x1,y1],[x2,y2],...,[xn,yn]]
p = array.array.int

calculate the minimun existing distance

constrains:


* len(P) < 2*10^4
* len p[i] = 2 all i
* |p[i][j]| < 1e-7

# Approaches:

1. No optimization, checking algorithm correctness.
2. Simplify len calculation.
3. simplify |p[i][j]| < 1e-7 calculation.
4. Using math.pow function.
5. Avoiding intermediate point allocation.
6. Computing min value by a cicle expressed in a single line.
7. Using generator.
8. Using numba and jit compiler.
9. Adding types to jit.
10. Usgin Math.dist to compute points distance.
11. Preallocating memory to store minimum values per iteration.