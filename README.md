# McGalaxy

##### V1.0 10.26.19

**McGalaxy**, by Marco Harnam Kaisth, allows a user to enter a constellation, and outputs the arrangement of McDonald's in the USA and Canada that most resembles that constellation in relative distance and orientation.

## Running McGalaxy

Simply run mcgalaxy.py using Python3 through (depending on your default version of Python) either:

```
py mcgalaxy.py
```

or

```
python3 mcgalaxy.py
```

Then, enter a set of stars or one of the named constellation options. Currently, McGalaxy supports 146 named stars and two constellation. At any point, to see a list of all supported stars and constellations, input:

```
"h"
```

or

```
"help"
```

To exit the program, simply input:

```
"x"
```

or

```
"exit"
```

Because of the number of McDonald's on the list (15,592), and because the program checks each n-length combination of these McDonald's (where n is the number of stars in the input constellation), it is prohibitive to run McGalaxy including the whole data set on most consumer hardware. As such, by default, McGalaxy only looks at McDonald's in Alaska. To broaden your search to all McDonald's in the USA and Canada simply add the flag

```
-all
```

anywhere within your input string. To underscore the immensity of this computation, the program needs to evaluate $\approx 6 \times10^{25}$ possible combinations of McDonald's locations to find which best suits the big dipper!

## Examples

When running McGalaxy, you'll be greeted by this message:

```
$ py mcgalaxy.py
Welcome to McGalaxy! This program allows you to input any
constellation or set of stars, and outputs the set of McDonalds in the US
and Canada that most resembles it in relative distance and orientation.
By default, this program limits your search to only Alaska.
However, use the "-all" flag anywhere in your input to search the whole
data set! Be warned, this is extremely long and intensive, and not
feasible for most devices.
Input "h" or "help" to see what constellations and stars are availible,
or input a constellation or set of stars by proper name below! Exit with "x" or "exit"
```

An example input, for the star's "Deneb", "Lacaille 9352" and "Babcock's star" is simply, in any order

```
Deneb Babcock's star Lacaille 9352
```

Which yields the output

```
The McDonalds that most resemble ['Deneb', "Babcock's star", 'Lacaille 9352'] are:
McDonalds [WM]-Anchorage,AK 3101 A St [WM], Anchorage,AK, (907) 561-5137,Services: wifi
McDonalds-Anchorage,AK 5000 W International Airport Rd, Anchorage,AK, (907) 243-0085,Services: none
McDonalds-Ketchikan,AK 2417 Tongass Ave Ste 108, Ketchikan,AK 99901, (907) 225-1704,Services: dt/wifi
Input "x" or "exit" to exit or continue exploring the McGalaxy!
```

To see which McDonald's most resemble a constellation included in McGalaxy, simply input that constellation as is shown on the help screen. Inputting

```
h
```

yields the help screen:

```
McGalaxy supports the following stars:
                      Sol
					  ...
                p Eridani
Any of these stars can be named by proper name, in any sequence
McGalay also supports the following constellations:
['Big_Dipper', 'Aquila']
Make sure to only use whitespace to delimit your inputs!
Additionally, since the number of McDonald's locations is so large
as to be prohibitive for searching, McGalaxy automatically searches only within Alaska. To
expand your search to all McDonald's in the US and Canada, add the flag "-all" anywhere
within your input, but be warned! It'll take a long time on powerful hardware!
```

As such, to find which McDonald's most resemble the Big Dipper, simply input

```
Big_Dipper
```

To expand this search to all of the US and Canada, simply add the "-all" flag making the command

```
Big_Dipper -all
```

## Acknowledgements

The idea for McGalaxy (and the name!) was conceieved of by [Ethan Mertz](https://github.com/ethanmertz/).
Star data is from the [HYG Database](http://www.astronexus.com/hyg).
McDonald's data is from [POI Factory](http://www.poi-factory.com/node/11154).

## Contact

Reach out with any questions to [mhk@mhk.dev](mailto:mhk@mhk.dev)