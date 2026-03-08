# frozenset_bundles.py
# Day 9 PM – Part B: Frozenset Bundle Discount System

import timeit

# ══════════════════════════════════════════════════════════════════
"""
WHAT IS FROZENSET?
------------------
A frozenset is an immutable version of a Python set.
- Like a set: unordered, no duplicates, supports set operations
  (union, intersection, difference, etc.)
- Unlike a set: CANNOT be modified after creation (no add/remove/discard)
- Because it is immutable, frozenset is HASHABLE → can be used as a
  dictionary key or stored inside another set.

SET vs FROZENSET
-----------------
| Feature          | set          | frozenset          |
|------------------|--------------|--------------------|
| Mutable          | ✅ Yes       | ❌ No              |
| Hashable         | ❌ No        | ✅ Yes             |
| Dict key         | ❌ No        | ✅ Yes             |
| add/remove       | ✅ Yes       | ❌ Not available   |
| Set operations   | ✅ Yes       | ✅ Yes             |

WHEN TO USE FROZENSET IN REAL SYSTEMS
---------------------------------------
1. Dictionary keys that represent combinations (e.g., product bundles,
   feature flags, permission sets) — sets can't be dict keys but frozensets can.
2. Caching / memoization — frozensets are hashable so they work as
   cache keys in functools.lru_cache.
3. Storing sets inside another set — e.g., a set of frozensets to
   represent unique groupings without repetition.
4. Config/rules that must not be mutated after creation — frozenset
   enforces immutability at the data-structure level.
"""
# ══════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────
# 2. Bundle Discount Dictionary
#    Keys are frozensets of category combinations
# ─────────────────────────────────────────────
bundle_discounts = {
    frozenset({"Electronics", "Books"}):    10,   # 10% off
    frozenset({"Clothing", "Home"}):        15,   # 15% off
    frozenset({"Electronics", "Clothing"}): 8,    # 8%  off
    frozenset({"Books", "Home"}):           12,   # 12% off
    frozenset({"Electronics", "Books", "Clothing", "Home"}): 20,  # all-category mega deal
}


# ─────────────────────────────────────────────
# 3. Bundle Checker Function
# ─────────────────────────────────────────────
def check_bundle_discount(cart_categories: set) -> dict:
    """
    Check if the cart's categories match any bundle deal.

    Args:
        cart_categories: a set of category strings present in the cart
                         e.g. {"Electronics", "Books"}

    Returns:
        A dict of matched bundles and their discount percentages.
        Returns empty dict if no bundle matched.
    """
    applicable = {}
    for bundle, discount in bundle_discounts.items():
        # bundle is a subset of cart categories → deal applies
        if bundle.issubset(cart_categories):
            bundle_label = " + ".join(sorted(bundle))
            applicable[bundle_label] = f"{discount}% off"
    return applicable


# ─────────────────────────────────────────────
# Demo
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  🏷️   Bundle Discount System (frozenset)")
    print("=" * 55)

    test_carts = [
        {"Electronics", "Books"},
        {"Clothing", "Home"},
        {"Electronics", "Books", "Clothing"},
        {"Electronics", "Books", "Clothing", "Home"},
        {"Books"},                                    # no bundle match
    ]

    for cart in test_carts:
        result = check_bundle_discount(cart)
        print(f"\n  Cart categories : {cart}")
        if result:
            for bundle, disc in result.items():
                print(f"    ✅  {bundle} → {disc}")
        else:
            print("    ❌  No bundle discount applicable.")

    # ─────────────────────────────────────────────
    # 4. Performance Benchmark: set vs frozenset
    # ─────────────────────────────────────────────
    print("\n" + "=" * 55)
    print("  ⏱️   Performance Benchmark: set vs frozenset")
    print("  (100,000 iterations each)")
    print("=" * 55)

    set_time = timeit.timeit(
        stmt="s = set(['Electronics', 'Books', 'Clothing', 'Home'])",
        number=100_000
    )
    frozenset_time = timeit.timeit(
        stmt="fs = frozenset(['Electronics', 'Books', 'Clothing', 'Home'])",
        number=100_000
    )

    print(f"\n  set creation       : {set_time:.4f}s")
    print(f"  frozenset creation : {frozenset_time:.4f}s")
    diff = abs(set_time - frozenset_time)
    faster = "frozenset" if frozenset_time < set_time else "set"
    print(f"\n  → '{faster}' was faster by {diff:.4f}s over 100,000 runs.")

    """
    BENCHMARK RESULTS (typical on a modern machine):
    ──────────────────────────────────────────────────
      set creation       : ~0.025s
      frozenset creation : ~0.024s

    INTERPRETATION:
    - Creation speed is nearly identical for small collections.
    - The real performance advantage of frozenset is its HASHABILITY:
      O(1) dictionary key lookups vs. the impossibility of using a
      mutable set as a key at all.
    - For large-scale systems (e.g., caching rule combinations), frozenset
      enables patterns that set simply cannot support.
    """
