import re
txt="Computer Scince and technology"
x=re.findall("o", txt)
print(x)

import re
txt="Computer Scince and technology"
x=re.search("t", txt)
print(x)

import re
txt="Computer Scince and technology"
x=re.split("o", txt)
print(x)

import re
txt="Computer Scince and technology"
x=re.sub("o", "A",txt)
print(x)