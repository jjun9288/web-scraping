#No need to install. Just import. Lets import math for example

import math
print(math.ceil(1.2))
print(math.fabs(1.2))

from math import ceil, fsum     #Import particular things instead of whole modules
print(fsum([1,2,3,4,5]))

from math import fsum as sexy_sum   #We can rename it also
print(sexy_sum([1,2,3,4,5]))


