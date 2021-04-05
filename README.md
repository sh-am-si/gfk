# Data

## Main info
 Variable | Description |
|:--------:|:-----------:|
| *period_end_date* | date of provided record |
| *translated_when* | date of modelling |
| *if_data_corrected* | information whether record was updated |
| *prod_gr_id* | Id of product group |
| *country_id_n* | Id of a country |
| *delivery_type_id* | type of record delivery to the system |
| *freq_id* | type of regularity of delivered records |
| *retailer_id* | Id of record provider |
| *brand_id* | Id of a Brand |
| *predict_automatch* | result of model prediction 0/1 |
| *class_acctual* | actual class of predicted value 0/1 |

## Size

**11 columns**

**19697 rows**

## Description

|         Variable  |  NaN count   |   NaN ratio | Role | Type | Note |
|:------------------|-----:|-----------:| :----:|:---:| :----:|
| period_end_date   |   57 | 0.00289384 | explanatory | date | 18 days (from 30  Aug till 1 Dec)|
| translated_when   |    0 | 0         | explanatory | date + time | 154 days (from 1 Sep till 1 Feb)|
| if_data_corrected |    0 | 0          | explanatory | categorical | <table> <body> <tr> <th> 0 </th> <th> 17085 </th> </tr>  <tr> <th> 1 </th> <th> 2612  </th> </tr> </tbody> </table>|
| prod_gr_id        |    0 | 0          | explanatory | categorical | <table> <body><tr> <th> 413 </th> <th> 4486 </th> </tr>  <tr> <th> 426 </th> <th> 11844 </th> </tr>  <tr> <th> 427 </th> <th> 3367  </th> </tr>  </tbody> </table> |
| country_id_n      | 1292 | 0.0655937  | explanatory | categorical | 35 entries |
| delivery_type_id  | 1335 | 0.0677768  | explanatory | categorical | 915 entries |
| freq_id           |    0 | 0          | explanatory | categorical | <table> <body> <tr> <th> 1 </th> <th> 7763 </th> </tr>  <tr> <th> 2 </th> <th> 11934  </th> </tr>  </tbody> </table> |
| retailer_id       |    0 | 0          | explanatory | categorical | 52 entries |
| brand_id          |    0 | 0          | explanatory | categorical | 199 entries |
| predict_automatch |  329 | 0.0167031  | output | | |
| class_acctual     |    0 | 0          | output | | |



# Material

- [Experimental Design and Analysis Howard J. Seltman](https://www.stat.cmu.edu/~hseltman/309/Book/Book.pdf)
- [short EDA intro](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)
- [Jupyter + GIT](https://medium.com/somosfit/version-control-on-jupyter-notebooks-6b67a0cf12a3)
- [Jupyter + Docker](https://www.dataquest.io/blog/docker-data-science/)
- [set visualization (Venn)](https://towardsdatascience.com/visualizing-intersections-and-overlaps-with-python-a6af49c597d9)
- [Pandas + Timeseries](https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/)
- [Statistics + Python](https://realpython.com/python-statistics/)
- [Probability + Statisitcs. A FIRST COURSE IN PROBABILITY](https://zalsiary.kau.edu.sa/Files/0009120/Files/119387_A_First_Course_in_Probability_8th_Edition.pdf)
# Suggestions

- rename class_acctual to class_actual

- amputate the data for the column _translated_when_ after the 1st Dec
```python 
df[df['translated_when'].dt.date > datetime('2020-12-01')]
``` 

- Countries with ids 106 and 109 are really poorly correlated

- cross tabulation showed 

    - split between _if_data_corrected_ vs _period_end_date_ except for 1st Nov 2020

    - split between _country_id_n_ vs _prod_gr_id_ except for the countries: 106, 108, 113, 116, 176

    - split between _retailer_id_ vs _freq_id_ 