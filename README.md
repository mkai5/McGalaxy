# McGalaxy

##### V1.0 10.26.19

McGalaxy, by Marco Harnam Kaisth, allows a user to enter a constellation, and outputs the arrangement of McDonald's in North America that most resembles that constellation in relative distance and orientation.

## Running McGalaxy

Simply run mcgalaxy.py using Python3 through (depending on your default version of Python):

```
py mcgalaxy.py
python3 mcgalaxy.py
```

Then, enter a set of stars or one of the named constellation options. Currently, McGalaxy supports 146 named stars and two constellation. At any point, to see a list of all supported stars and constellations, input:

```
"h"
```

To exit the program, simply input:

```
"x"
```

Because of the number of McDonald's on the list (15,592), and because the program checks each n-length combination of these McDonald's (where n is the number of stars in the input constellation), it is prohibitive to run McGalaxy including the whole data set on most consumer hardware. To limit your search, simply add the flag

```
-a
```

anywhere within your input string to search only McDonald's within Alaska (of which there are 31). 
To underscore the immensity of this computation, without the "-a" flag, the program needs to evaluate $\approx 6 \times10^{25}$ possible combinations of McDonald's locations!

## Acknowledgements

The idea for McGalaxy was concieved of by [Ethan Mertz](https://github.com/ethanmertz/).
Star data is from the [HYG Database](http://www.astronexus.com/hyg).
McDonald's data is from [POI Factory](http://www.poi-factory.com/node/11154).

## Contact

Reach out with any questions to [mhk@mhk.dev](mailto:mhk@mhk.dev)