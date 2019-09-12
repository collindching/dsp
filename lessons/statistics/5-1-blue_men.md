[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

#### What percentage of the U.S. male population is between 5'10" and 6'1"?

Given that the average height is 178 cm and standard deviation is 7.7 cm for men. To solve this, I convert centimeters to inches first. To calculate percentage of U.S. population between those two heights, I find the difference between their cumulative probabilities.

```python
from scipy.stats import norm

def to_inches(cm):
    return .39*cm

pct = norm.cdf(73,to_inches(178), to_inches(7.7)) \
        - norm.cdf(70, to_inches(178), to_inches(7.7))

pct
```

`pct` = 0.3068216439959962, so 30.7% of the U.S. population is between 5'10" and 6'1".

