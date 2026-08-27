# Formal dependency graph

```text
RF-00  pinned cross-reference contract
  |
RF-01  relational field primitive
  |\
  | RF-04 local clock / metric primitive
  v      |
RF-02    RF-05 metric connection / curvature
local    |
phase    RF-N1 Newton weak-field gate
connection      |
  |             |
RF-03 curvature F=dA
  |
RF-M1 Maxwell homogeneous closure
  |
RF-M2 Maxwell sourced/action closure
   \           /
    \         /
      RF-L1 dynamic Lambda0 scalar closure
                    |
              RF-E1 Einstein-Bianchi closure
                    |
              RF-X1 unified limit audit
```

No downstream node may be promoted above the weakest unresolved prerequisite.
