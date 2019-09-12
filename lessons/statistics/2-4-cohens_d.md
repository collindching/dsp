[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

#### Investigate whether first babies are lighter or heavier than others using Cohen's d

The question asks us to analyze the effect size of being a first-born on a newborn weight, and compare that to the effect size of being a first-born on pregnancy length. In this case, we're using Cohen's d as the effect size, which compares difference between groups in terms of standard deviations.

![equation](https://latex.codecogs.com/gif.latex?d%20%3D%20%5Cfrac%7B%5Ctext%7Bmean%20difference%7D%7D%7B%5Ctext%7Bstandard%20deviation%7D%7D%20%3D%20%5Cfrac%7B%5Cbar%7Bx_1%7D%20-%20%5Cbar%7Bx_2%7D%7D%7Bs%7D)

In this scenario, we have two groups -- first-born and not first-born babies. I'll use a pooled standard deviation, which is a weighted average of the standard deviations of the two groups.

```python
is_first = preg['birthord']==1
isnot_first = preg['birthord']>1

wt_first = preg.loc[is_first, 'totalwgt_lb']
wt_notfirst = preg.loc[isnot_first, 'totalwgt_lb']

dif = wt_first.mean() - wt_notfirst.mean()
pooled_var = (len(wt_first)*wt_first.var() + len(wt_notfirst)*wt_notfirst.var()) \
                / (len(wt_first) + len(wt_notfirst))
d = dif/np.sqrt(pooled_var)
d
```

When I ran the above code, d computed to -0.089. According to this data, first-born babies are lighter than not first-born babies by about .09 standard deviations. This is about three times the effect that being first-born has on pregnancy length.

```python
wks_first = preg.loc[is_first, 'prglngth']
wks_notfirst = preg.loc[isnot_first, 'prglngth']

dif = wks_first.mean() - wks_notfirst.mean()
pooled_var = (len(wks_first)*wks_first.var() + len(wks_notfirst)*wks_notfirst.var()) \
                / (len(wks_first) + len(wks_notfirst))
d = dif/np.sqrt(pooled_var)
d      
```

`d` = .029
