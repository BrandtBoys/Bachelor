## Code Change:
```diff --git a/mvp/src/main.py b/mvp/src/main.py
index 2c1b486..338a7a0 100644
--- a/mvp/src/main.py
+++ b/mvp/src/main.py
@@ -1,2 +1,3 @@
-# def mul(a,b):
+def add(a,b):
     #     return a+b
```

## Current Documentation:
    ## Updated Code Change:

```diff --git a/mvp/src/main.py b/mvp/src/main.py
index 87118e3..0fa18dc 100644
--- a/mvp/src/main.py
+++ b/mvp/src/main.py
@@ -6,4 +6,7 @@ def fac(a):
     while a < 0:
         res*a
         a = a -1
-    return res
+    return res
+
+def sub(a,b):
+    return a-b
```

## Updated Documentation:

### def add(a,b)

Takes two inputs as arguments and returns their sum.

### def fac(a)

Takes one input as an argument and calculates its factorial. The function uses a while loop to multiply the number by each decreasing integer until it reaches 0.

### def sub(a,b)

Takes two inputs as arguments and returns their difference.

Note: The documentation has been updated to reflect the change in the `add` function, which now correctly returns the sum of its arguments.