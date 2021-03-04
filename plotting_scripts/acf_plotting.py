import pydarn
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import bz2
rawacf_file = '/home/robertson/noise_work/data_files/20181220.1201.00.cly.rawacf.bz2'

with bz2.open(rawacf_file) as fp:
    rawacf_stream = fp.read()

reader = pydarn.SDarnRead(rawacf_stream, True)
records = reader.read_rawacf()
######################################
acfdata = records
pydarn.ACF.plot_acfs(acfdata, beam_num= 15, gate_num= 74, start_time=datetime(2018, 12, 20, 12, 5))
#pydarn.ACF.plot(acfdata, beam_num= 14, gate_num= 70, start_time=datetime(2020, 6, 1, 0, 5))
plt.show()


