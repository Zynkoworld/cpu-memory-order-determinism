# cpu-memory-order-determinism — x86-TSO memory-order determinizmus-felulet oracle

A CPU memory-model determinizmus-**felulete** valos x86 sziliciumon merve (cuda Compute-oracle, natix C
litmus-harness -- a Python GIL miatt Python-ban NEM merheto). A byte-lock **ARCH-FUGGO**: ez az x86-TSO
also-hatar; ARM/POWER-on mas (staged).

## Determinizmus-felulet (x86-TSO)
- **PROVEN nondet-cella:** `sb` (store-buffering) -- x86 TSO KIZAROLAG store-load-ot reorderel.
- **Pozitiv kontroll (onvalidacio):** `sb_fenced` = 0 -- a seq_cst fence eltunteti a reordert.
- **MATCH-baseline:** iriw/wrc/isa2/2+2W/mp/lb = 0 (multi-copy-atomic + store/load-sorrend megorzott).

## HATAR: byte-lock-safe <=> fence/seq_cst VAGY nem-store-load minta.

## Verifikacio (hardver nelkul, ZOLD): python3 verify.py . Forras: cuda fleet/litmus_harness.c.
