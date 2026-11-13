# Research Report: Iris Petal Length by Species

## Research question

Is mean petal length different among Iris setosa, Iris versicolor, and
Iris virginica?

## Dataset and method

The analysis uses the classic Iris dataset provided by
`sklearn.datasets.load_iris`. It contains 150 observations: 50 flowers
from each of the three species. Petal length, measured in centimetres,
is the primary outcome and species is the grouping variable.

The preregistered primary analysis is a one-way analysis of variance
(ANOVA), using a significance level of 0.05. Tukey's HSD is used for
pairwise comparisons after the overall ANOVA.

## Data validation

-   Rows before filtering: 150
-   Rows included: 150
-   Missing values in the required species and petal-length fields: 0
-   Exact duplicate rows in the full dataset: 1

No rows were removed for the primary analysis.

## Descriptive statistics

  Species        Count   Mean petal length (cm)   Standard deviation
  ------------ ------- ------------------------ --------------------
  Setosa            50                    1.462                0.174
  Versicolor        50                    4.260                0.470
  Virginica         50                    5.552                0.552

## Primary analysis

A one-way ANOVA found a statistically significant difference in mean
petal length among the three Iris species:

-   F-statistic: 1180.161
-   p-value: 2.857 × 10\^-91
-   Significance level: 0.05

Because the p-value is below 0.05, the null hypothesis of equal species
means is rejected. The data provide strong evidence that mean petal
length is not the same across all three species.

## Pairwise comparisons

Tukey's HSD post-hoc comparisons found statistically significant
differences for all three pairs at the 0.05 level:

  -------------------------------------------------------------------------
  Comparison      Mean difference (cm)       95% confidence Significant?
                                              interval (cm) 
  --------------- -------------------- -------------------- ---------------
  Versicolor −                   2.798       2.594 to 3.002 Yes
  Setosa                                                    

  Virginica −                    4.090       3.886 to 4.294 Yes
  Setosa                                                    

  Virginica −                    1.292       1.088 to 1.496 Yes
  Versicolor                                                
  -------------------------------------------------------------------------

The mean petal length is lowest for Setosa and highest for Virginica in
this dataset.

## Assumption and robustness checks

Levene's test indicated that group variances are not equal (statistic =
19.480, p = 3.129 × 10\^-8). This is a caution when interpreting the
classical ANOVA. As a robustness check, the non-parametric
Kruskal--Wallis test was also performed and was statistically
significant (H = 130.411, p = 4.804 × 10\^-29), supporting the
conclusion that petal-length distributions differ among species.

## Conclusion

In the classic Iris dataset, petal length differs significantly among
Setosa, Versicolor, and Virginica. The preregistered one-way ANOVA was
statistically significant, and Tukey's HSD indicated significant
differences between every pair of species. The robustness check led to
the same overall conclusion. These findings describe this dataset and
should not be interpreted as a causal effect.

## Reproducibility note

The numerical results above are calculated from the standard 150-row
Iris dataset distributed with scikit-learn. The notebook in this
repository contains the analysis code. To independently reproduce the
results, run all notebook cells in order in a Python environment with
the packages listed in `requirements-lock.txt`.

The synthetic pipeline test is a separate data-blind check; its result
should be recorded only after running the test file in the specified
environment.
