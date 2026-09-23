#!/usr/bin/env python3
"""verify.py — HARDWARE-FREE verification of the cpu-memory-order-determinism oracle.
Recomputes the measurement_byte_lock from anchor.json + the semantic invariant. exit 0 = GREEN."""
import json, hashlib, sys
a = json.load(open("anchor.json")); spec = json.load(open("BYTE_LOCK_SPEC.json"))
lit = a["litmus"]
canon = json.dumps({"arch": a["arch"],
                    "gt": sorted([[l["op"], l["verdict"], bool(l["observed"])] for l in lit]),
                    "boundary": a["determinism_surface"]["byte_lock_safe_iff"]},
                   sort_keys=True, separators=(",", ":"))
bl = hashlib.sha256(canon.encode()).hexdigest()
bl_ok = bl == spec["byte_locks"]["measurement_byte_lock"]
proven = [l for l in lit if "PROVEN" in l["verdict"]]
fenced = next((l for l in lit if l["op"] == "sb_litmus_fenced_control"), None)
sb = next((l for l in lit if l["op"] == "sb_litmus_store_buffering"), None)
inv_ok = (len(proven) == 1 and sb is not None and "PROVEN" in sb["verdict"]
          and fenced is not None and fenced["observed"] is False)
ok = bl_ok and inv_ok
print(f"measurement_byte_lock: {bl[:24]}  {'OK' if bl_ok else 'MISMATCH!'}")
print(f"invariant (1 PROVEN sb + fenced-control==0 self-validation): {'OK' if inv_ok else 'BROKEN'}")
print(f"litmus: {len(lit)} tests | PROVEN reorder: {[p['op'] for p in proven]} | boundary: {a['determinism_surface']['byte_lock_safe_iff']}")
print("GREEN" if ok else "RED")
sys.exit(0 if ok else 1)
