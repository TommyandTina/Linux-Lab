# Prerequisite

This guideline assumes that you have installed all related tools and set PATH correctly

- Make 4.2

- MinGW GCC 7.3.0 or later

- CMD

# Build and Execute UT program

* Before building test program, you must use CMD and enter to unit_test folder

```
cd <repo_name>/Data/unit_test
```

* Build UT program

```
make all
```

* Execute UT program

```
./UT.exe
```

# Check coverage

* Build UT check coverage

```
make coverage
```

* Execute UT check coverage

```
./UT_coverage.exe
```

# Clean UT, UT_coverage program

```
make clean
```