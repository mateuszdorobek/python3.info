DataFrame Rolling
=================
* ``.resample(freq)``
* ``.rolling(window=10)``
* ``.shift(periods=1, freq="D")``
* ``.diff()``


SetUp
-----
>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(0)
>>>
>>>
>>> df = pd.DataFrame(
...     columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
...     index = pd.date_range('1999-12-30', periods=7),
...     data = np.random.randn(7, 4))
>>>
>>> df
             Morning      Noon   Evening  Midnight
1999-12-30  1.764052  0.400157  0.978738  2.240893
1999-12-31  1.867558 -0.977278  0.950088 -0.151357
2000-01-01 -0.103219  0.410599  0.144044  1.454274
2000-01-02  0.761038  0.121675  0.443863  0.333674
2000-01-03  1.494079 -0.205158  0.313068 -0.854096
2000-01-04 -2.552990  0.653619  0.864436 -0.742165
2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Resample
--------
>>> df.resample('W').median()
             Morning      Noon   Evening  Midnight
2000-01-02  1.262545  0.260916  0.696976  0.893974
2000-01-09  1.494079 -0.205158  0.313068 -0.742165


Rolling
-------
.. figure:: img/pandas-dataframe-stats-rolling.png

    Rolling Average

>>> df.rolling(window=30)
Rolling [window=30,center=False,axis=0,method=single]

>>> df.rolling(window=3).mean()
             Morning      Noon   Evening  Midnight
1999-12-30       NaN       NaN       NaN       NaN
1999-12-31       NaN       NaN       NaN       NaN
2000-01-01  1.176130 -0.055507  0.690957  1.181270
2000-01-02  0.841792 -0.148335  0.512665  0.545530
2000-01-03  0.717299  0.109038  0.300325  0.311284
2000-01-04 -0.099291  0.190045  0.540456 -0.420862
2000-01-05  0.403615 -0.335302  0.407754 -0.594482

>>> df.rolling(window=3).median()
             Morning      Noon   Evening  Midnight
1999-12-30       NaN       NaN       NaN       NaN
1999-12-31       NaN       NaN       NaN       NaN
2000-01-01  1.764052  0.400157  0.950088  1.454274
2000-01-02  0.761038  0.121675  0.443863  0.333674
2000-01-03  0.761038  0.121675  0.313068  0.333674
2000-01-04  0.761038  0.121675  0.443863 -0.742165
2000-01-05  1.494079 -0.205158  0.313068 -0.742165


Shift
-----
* Subtract DataFrame object from other shifted by index

>>> df - df.shift(periods=1, freq="D")
             Morning      Noon   Evening  Midnight
1999-12-30       NaN       NaN       NaN       NaN
1999-12-31  0.103506 -1.377435 -0.028650 -2.392250
2000-01-01 -1.970777  1.387876 -0.806045  1.605631
2000-01-02  0.864257 -0.288923  0.299820 -1.120599
2000-01-03  0.733041 -0.326833 -0.130796 -1.187770
2000-01-04 -4.047069  0.858777  0.551368  0.111931
2000-01-05  4.822744 -2.107984 -0.818678  0.554981
2000-01-06       NaN       NaN       NaN       NaN


Diff
----
* Subtract next row from the previous

>>> example = pd.DataFrame([20,35,70,100])
>>> example.diff()
      0
0   NaN
1  15.0
2  35.0
3  30.0

>>> df.diff()
             Morning      Noon   Evening  Midnight
1999-12-30       NaN       NaN       NaN       NaN
1999-12-31  0.103506 -1.377435 -0.028650 -2.392250
2000-01-01 -1.970777  1.387876 -0.806045  1.605631
2000-01-02  0.864257 -0.288923  0.299820 -1.120599
2000-01-03  0.733041 -0.326833 -0.130796 -1.187770
2000-01-04 -4.047069  0.858777  0.551368  0.111931
2000-01-05  4.822744 -2.107984 -0.818678  0.554981
