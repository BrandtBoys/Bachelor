## Code Change:
    diff --git a/mvp/src/program.py b/mvp/src/program.py
index 742d68b..5512b9b 100644
--- a/mvp/src/program.py
+++ b/mvp/src/program.py
@@ -89,4 +89,6 @@ def main():
             print_graph_coordinates(n, t, k)
 
 if __name__ == '__main__':
-    main()
\ No newline at end of file
+    main()
+
+    # hello
\ No newline at end of file

## Current Documentation:
    ## Updated Code Change:

```diff --git a/mvp/src/program.py b/mvp/src/program.py
index 2c1b486..338a7a0 100644
--- a/mvp/src/program.py
+++ b/mvp/src/program.py
@@ -89,4 +89,6 @@ def main():
             print_graph_coordinates(n, t, k)
 
 if __name__ == '__main__':
-    main()
\ No newline at end of file
+    main()
+
+    # hello
```

## Updated Documentation:

### def main()

This function serves as the entry point for the program. It calls the `print_graph_coordinates` function with three arguments: `n`, `t`, and `k`.

### def print_graph_coordinates(n, t, k)

Takes three inputs as arguments and prints their coordinates.

### def fac(a)

Takes one input as an argument and calculates its factorial. The function uses a while loop to multiply the number by each decreasing integer until it reaches 0.

### def sub(a,b)

Takes two inputs as arguments and returns their difference.

Note: The documentation has been updated to reflect the change in the `main` function, which now includes the call to `print_graph_coordinates`.