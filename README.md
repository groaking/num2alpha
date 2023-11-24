# num2alpha

## Description

This Python script converts any base-10 integer into its "alphabetical number" counterpart. For example, `1` is `a`, `26` is `z`, and `28` is `ab`. This alphabetical number order is exactly what you find in the column name of most modern spreadsheet apps.

This script can also decode an alphabetical number and return its integer order in base-10.

## Usage

After downloading the Python script, open terminal and `cd` into the download location. Then execute the following:

```sh
python num2alpha.py N
```

Substitute `N` with the base-10 integer you want to encode into alphabetical number or the alphabetical number you want to decode into base-10 integer. It automatically detects whether the input prompt is a base-10 integer or an alphabetical number.

For instance, run the following to find the alphabetical number for the integer `2023`:

```sh
python num2alpha 2023
# OUTPUT: byu
```

Or type in the following in the terminal window to return the base-10 integer for the alphabetical number `hello` (can be written in lowercase, uppercase, or both):

```sh
python num2alpha hello
# OUTPUT: 3752127
```
