#!/usr/bin/env python3
"""
Quick harness to run `measure_speedup_safe` with different worker counts.

Prints results to stdout for simple comparisons. Can be extended to emit
CSV for automated collection.
"""

from measure_speedup_safe import run
import multiprocessing as mp

def main():
    cpu = mp.cpu_count()
    configs = [1, max(1, cpu//2), cpu]
    print('CPU count:', cpu)
    for workers in configs:
        print('\nRunning with workers =', workers)
        res = run(workers=workers, runs=2)
        print('  seq: {:.3f}s  par: {:.3f}s  speedup: {:.2f}  eff: {:.2f}%'.format(
            res['seq_time'], res['par_time'], res['speedup'], res['efficiency']))

if __name__ == '__main__':
    main()
