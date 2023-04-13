Multiprocessing 3rd Party
=========================


Dask
----
* https://dask.org/
* Dask provides advanced parallelism for analytics, enabling performance at scale for the tools you love
* Integrates with existing projects
* Familiar for Python users
* Scale up to clusters
* Customizable

Dask arrays scale NumPy workflows, enabling multi-dimensional data analysis in earth science, satellite imagery, genomics, biomedical applications, and machine learning algorithms.

Dask dataframes scale pandas workflows, enabling applications in time series, business intelligence, and general data munging on big data.

Dask-ML scales machine learning APIs like scikit-learn and XGBoost to enable scalable training and prediction on large models and large datasets.

Dask uses existing Python APIs and data structures to make it easy to switch between NumPy, pandas, scikit-learn to their Dask-powered equivalents. You don't have to completely rewrite your code or retrain to scale up.

Dask's schedulers scale to thousand-node clusters and its algorithms have been tested on some of the largest supercomputers in the world. But you don't need a massive cluster to get started. Dask ships with schedulers designed for use on personal machines. Many people use Dask today to scale computations on their laptop, using multiple cores for computation and their disk for excess storage.

Not all computations fit into a big dataframe. Dask exposes lower-level APIs letting you build custom systems for in-house applications. This helps open source leaders parallelize their own packages and helps business leaders scale custom business logic.


.. figure:: img/multiprocessing-dask-computationalgraph.gif
