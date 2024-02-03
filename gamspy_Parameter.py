from gamspy import Container, Set, Parameter
import pandas as pd

dist = pd.DataFrame(
    [
        ("seattle", "new-york", 2.5),
        ("seattle", "chicago", 1.7),
        ("seattle", "topeka", 1.8),
        ("san-diego", "new-york", 2.5),
        ("san-diego", "chicago", 1.8),
        ("san-diego", "topeka", 1.4),
    ],
    columns=["from", "to", "thousand_miles"],
)

m = Container()

i = Set(m, "i", ["*"], records = dist["from"].unique())
j = Set(m, "j", ["*"], records = dist["to"].unique())
a = Parameter(m, "a", [i, j], records = dist)

print(a.records)

#         from        to  value
# 0    seattle  new-york    2.5
# 1    seattle   chicago    1.7
# 2    seattle    topeka    1.8
# 3  san-diego  new-york    2.5
# 4  san-diego   chicago    1.8
# 5  san-diego    topeka    1.4