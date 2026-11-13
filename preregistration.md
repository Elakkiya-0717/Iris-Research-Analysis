# Research Preregistration
## Iris Flower Dataset: Comparing Petal Length Across Species

- **Student name:** ______________________________
- **Course / internship:** Data Science with Python & R – RabTech Academy
- **Preregistration date:** ________________________
- **Version:** 1.0

## 1. Study overview
This educational observational study uses the classic Iris flower dataset to examine whether mean petal length differs among *Iris setosa*, *Iris versicolor*, and *Iris virginica*. The analysis plan is specified before examining group-level outcome patterns. No new data will be collected and no intervention will be applied.

## 2. Research question
Is there a statistically significant difference in mean petal length among the three Iris species in the Iris dataset?

## 3. Objectives
- Describe petal length in each species using sample size, mean, standard deviation, median, and interquartile range.
- Test whether mean petal length differs across the three species.
- If the overall test is significant, identify differing species pairs using the prespecified post-hoc procedure.
- Document steps so the analysis can be reproduced.

## 4. Dataset and population
Use the classic Fisher/Iris dataset, expected to contain 150 observations (50 per species) and four numeric measurements. Planned source: `sklearn.datasets.load_iris` from scikit-learn. Record the package version and data-loading method in the README. If another source is used, document its URL, access date, and differences before analysis.

## 5. Variables
- **Grouping variable:** `species` (setosa, versicolor, virginica).
- **Primary outcome:** petal length (centimetres in the classic dataset).
- **Unit of analysis:** one flower row.

## 6. Hypotheses
- **H0:** μ_setosa = μ_versicolor = μ_virginica.
- **H1:** At least one species mean petal length differs.
- Two-sided test; significance level α = 0.05.

## 7. Eligibility and data-quality rules
- Include rows with a recognized species and a valid numeric petal-length value.
- Exclude rows missing/invalid on either of those fields.
- Do not exclude observations only because values look unusually high or low.
- Check exact duplicate rows and report their number. Retain them in the primary analysis and disclose this choice.
- Report row counts before and after eligibility rules.

## 8. Sample size
No new sample will be collected. Use all eligible rows (expected 150, 50 per species in the standard dataset). There is no power-based stopping rule. If the actual dataset differs, report the difference and analyze all eligible observations.

## 9. Planned analysis
1. Load the dataset reproducibly.
2. Validate required columns, types, labels, missingness, and row counts.
3. Summarize petal length overall and by species.
4. Plot petal length by species (boxplot/violin plot) and group means with uncertainty intervals.
5. **Primary test:** one-way independent-groups ANOVA, species as factor and petal length as outcome.
6. Inspect residual Q–Q plot and use Levene’s test as a variance-homogeneity diagnostic.
7. If the overall ANOVA is significant, run Tukey’s HSD for pairwise comparisons.
8. Report F statistic, degrees of freedom, p-value, group means, confidence intervals where available, and eta-squared (η²).

## 10. Robustness analysis
If diagnostics show substantial assumption departures, report the ANOVA and a prespecified Kruskal–Wallis robustness analysis. If significant, pairwise Dunn-style comparisons with multiplicity adjustment may be reported if supported by the selected software. Explain the reason; do not silently replace the primary test.

## 11. Missing data
Summarize missingness. Do not impute. Exclude rows missing species or petal length under Section 7.

## 12. Multiple comparisons
The overall ANOVA is primary at α = 0.05. Tukey’s HSD controls family-wise error across the three pairwise comparisons. Label other analyses exploratory.

## 13. Reproducibility
- Store this document as `preregistration.md`.
- Keep raw and processed data separate. If loading directly from scikit-learn, document that rather than claiming a separate raw file exists.
- Include an analysis notebook/script, README, and package-version lockfile.
- Use synthetic fixtures to test the pipeline’s input/output contract without inspecting real group outcome patterns.

## 14. Data-blind pipeline check
Before confirmatory analysis, use synthetic data with the same column names and valid species categories. Test loading, schema validation, result generation, and missing-value handling. Synthetic results are not evidence about Iris species.

## 15. Deviations
Record every change to source, variables, exclusions, tests, or software in a dated deviations section. State the reason and whether it occurred before or after examining real outcome patterns. Separate exploratory work from confirmatory analysis.

## 16. Limitations
- This is a small, historical dataset; conclusions should not be generalized to all Iris flowers without caution.
- Species are pre-existing groups, not randomized treatments; differences do not establish causation.
- Dataset measurements and provenance are inherited from the source.

## 17. References
- Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. *Annals of Eugenics, 7*(2), 179–188.
- scikit-learn documentation: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html

## 18. Sign-off
I confirm this document describes the planned research question, variables, exclusions, and analysis before conducting or interpreting the confirmatory analysis.

Student signature: ______________________________  
Date: __________________
