# Statistics

# Table of Contents

[1. Introduction](#section-a)  
[2. Why We Are Using Think Stats](#section-b)  
[3. Instructions for Cloning the Repo](#section-c)  
[4. Required Exercises](#section-d)  
[5. Optional Exercises](#section-e)  
[6. Recommended Reading](#section-f)  
[7. Resources](#section-g)

## <a name="section-a"></a>1.  Introduction

[<img src="https://github.com/vaughnparker/dsp/blob/master/img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)

Use Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) book for getting up to speed with core ideas in statistics and how to approach them programmatically. This book is available online, or you can buy a paper copy if you would like.

Use this book as a reference when answering the 6 required statistics questions below.  The Think Stats book is approximately 200 pages in length.  **It is recommended that you read the entire book, particularly if you are less familiar with introductory statistical concepts.**

Complete the following exercises along with the questions in this file. Some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

## <a name="section-b"></a>2.  Why We Are Using Think Stats 

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the [ThinkStats repository on GitHub](https://github.com/AllenDowney/ThinkStats2).  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  **You could import it, or you could write your own code to practice python and develop a deeper understanding of the concept.** 

Think Stats uses a higher degree of python complexity from the python tutorials and introductions to python concepts, and that is intentional to prepare you for the bootcamp.  

**One of the skills to learn here is to understand other people’s code.  And this author is quite experienced, so it’s good to learn how functions and imports work.**

---

## <a name="section-c"></a>3.  Instructions for Cloning the Repo 
Using the [code referenced in the book](https://github.com/AllenDowney/ThinkStats2), follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/metisgh/prework  
(Windows):  C:/ds/metis/metisgh/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/metisgh/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/metisgh/prework/ThinkStats2/code
```

---


## <a name="section-d"></a>4.  Required Exercises

*Include your Python code, results and explanation (where applicable).*

### Q1. [Think Stats Chapter 2 Exercise 4](2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

### Q2. [Think Stats Chapter 3 Exercise 1](3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

### Q3. [Think Stats Chapter 4 Exercise 2](4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

### Q4. [Think Stats Chapter 5 Exercise 1](5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 



### Q5. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

We're trying to solve for this equation:

![eq1](https://latex.codecogs.com/gif.latex?P%28%5Ctext%7Bidentical%20twin%7D%7C%5Ctext%7Btwin%20brother%7D%29%20%3D%20%5Cfrac%7BP%28%5Ctext%7Bidentical%20twin%7D%20%5Ccap%20%5Ctext%7Btwin%20brother%7D%29%7D%7BP%28%5Ctext%7Btwin%20brother%7D%29%7D)

At first, I had written the lefthand side as $P(\text{identical twin}|\text{twin})$, but there's an important distinction between the probability of twins and probability of twin boys. In the case of identical twins, you have either 2 boys (BB) or 2 girls (GG), so there's a 50% chance of having twin boys. In the case of fraternal twins, you have 2 boys (BB), 2 girls (GG), or 1 boy and 1 girl (BG and GB). In this scenario, there's a 25% chance of having twin boys. 

If you use the equation I mistakenly wrote, you're essentially calculating the probability that Elvis and his twin was a set of female identical twins or a set of male identical twins. But we know that Elvis and his twin were boys.

![eq2](https://latex.codecogs.com/gif.latex?P%28%5Ctext%7Bidentical%20twin%7D%20%5Ccap%20%5Ctext%7Btwin%20brother%7D%29%20%5C%5C%20%3D%20P%28%5Ctext%7Btwin%20brother%7D%20%5Ccap%20%5Ctext%7Bidentical%20twin%7D%29%20%5C%5C%20%3D%20P%28%5Ctext%7Btwin%20brother%7D%7C%5Ctext%7Bidentical%20twin%7D%29P%28%5Ctext%7Bidentical%20twin%7D%29%20%5C%5C%20%3D%20%28.5%29%5Cfrac%7B1%7D%7B300%7D)

![eq2](https://latex.codecogs.com/gif.latex?P%28%5Ctext%7Btwin%20brother%7D%29%20%5C%5C%20%3D%20P%28%5Ctext%7Btwin%20brother%7D%20%5Ccap%20%5Ctext%7Bfraternal%20twin%7D%29%20&plus;%20P%28%5Ctext%7Btwin%20brother%7D%20%5Ccap%20%5Ctext%7Bidentical%20twin%7D%29%20%5C%5C%20%3D%20P%28%5Ctext%7Btwin%20brother%7D%20%5Ccap%20%5Ctext%7Bfraternal%20twin%7D%29P%28%5Ctext%7Bfraternal%20twin%7D%29%20&plus;%20P%28%5Ctext%7Btwin%20brother%7D%7C%5Ctext%7Bidentical%20twin%7D%29P%28%5Ctext%7Bidentical%20twin%7D%29%20%5C%5C%20%3D%20%28.25%29%5Cfrac%7B1%7D%7B125%7D%20&plus;%20%28.5%29%5Cfrac%7B1%7D%7B300%7D)

`(.5/300)/(.25/125 + .5/300)` ~= .455

The probability that Elvis was an identical twin was 45.5%.

---

### Q6. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

In statistics, we often want to make statements about populations by sampling from them. Both frequentists and Bayesians have methods for making such statements, but differ on how to approach them. 

Both frequentists and Bayesians agree that, for a given probability distribution, there are true and unknown paremeters. Frequentists believe that estimates of these unknown parameters should be based on observed frequencies, and that statements about a population must be as consistent with data samples as possible. They make point estimates of parameters. 

Bayesians, on the other hand, take into account the uncertainty of these parameters in their estimates. They represent parameters probabilistically.

As a result, these schools of thought use different techniques. For parameter estimation, frequentists use MLE, whereas Bayesians use Bayes Theorem to update their beliefs.
---

## <a name="section-e"></a>5.  Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

### Q7. [Think Stats Chapter 7 Exercise 1](7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

### Q8. [Think Stats Chapter 8 Exercise 2](8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

### Q9. [Think Stats Chapter 6 Exercise 1](6-1-household_income.md) (skewness of household income)
### Q10. [Think Stats Chapter 8 Exercise 3](8-3-scoring.md) (scoring)
### Q11. [Think Stats Chapter 9 Exercise 2](9-2-resampling.md) (resampling)

---

## <a name="section-f"></a>6.  Recommended Reading

Read Allen Downey's [Think Bayes](http://greenteapress.com/thinkbayes/) book.  It is available online for free, or you can buy a paper copy if you would like.

[<img src="img/think_bayes.png" title="Think Bayes"/>](http://greenteapress.com/thinkbayes/) 

---

## <a name="section-g"></a>7.  More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.
