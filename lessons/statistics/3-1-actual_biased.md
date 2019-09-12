[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

#### Construct the distribution for the number of children under 18 in the household, then compare that to the same distribution if we surveyed the children and asked them how many children under 18 are in their household

The variable that tracks number of children under 18 in a household is `numkdhh`. The author wants us to compare a probability distribution based on the actual data against a probability distribution based on human observation, which is prone to bias.

```python
resp = nsfg.ReadFemResp()

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

pmf = thinkstats2.Pmf(resp['numkdhh'], label='actual')
biased_pmf = BiasPmf(pmf, label='observed')
thinkplot.Pmfs([pmf,biased_pmf])
thinkplot.Show(xlabel='Number of kids', ylabel='PMF')
```

![Distribution graph](../../img/ex2-4_graph1)

If you survey children, no respondent will tell you that there are 0 children in their family, even though there are families with no children. This surveying method would introduce significant bias to the study, and shows us that it's important to question how the data was obtained so that we can draw valid conclusions from the data.