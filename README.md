# cpu-memory-order-determinism — x86-TSO memory-order determinism-surface oracle

The determinism **surface** of the CPU memory model, measured on real x86 silicon (cuda Compute oracle, native C
litmus harness -- because of the Python GIL it is NOT measurable in Python). The byte-lock is **ARCH-DEPENDENT**:
this is the x86-TSO lower bound; on ARM/POWER it differs (staged).

## Determinism surface (x86-TSO)
- **PROVEN nondet cell:** `sb` (store-buffering) -- x86 TSO reorders ONLY store-load.
- **Positive control (self-validation):** `sb_fenced` = 0 -- the seq_cst fence eliminates the reorder.
- **MATCH baseline:** iriw/wrc/isa2/2+2W/mp/lb = 0 (multi-copy-atomic + store/load order preserved).

## BOUNDARY: byte-lock-safe <=> fence/seq_cst OR a non-store-load pattern.

## Verification (hardware-free, GREEN): python3 verify.py . Source: cuda fleet/litmus_harness.c.
