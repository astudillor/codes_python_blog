#!/usr/bin/env python
import scipy.sparse as sparse
import matplotlib.pyplot as plt
import scipy.io as io
import numpy as np

#Downloading the matrix from SPARSEKIT
problem = "SPARSKIT/drivcav/e05r0200"
mm = np.lib._datasource.Repository('ftp://math.nist.gov/pub/MatrixMarket2/')
f = mm.open('%s.mtx.gz' % problem)
A = io.mmread(f).tocsr()
f.close()
#Default Ploting
plt.spy(A)
plt.show()
#Closer to Matlab's result
plt.spy(A,markersize=1.0)
plt.show()
