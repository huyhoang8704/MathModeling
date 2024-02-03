from gamspy import Container, Set , Parameter
import pandas as pd

m = Container()

i = Set(m,
        name = "i",
        description = "mining regions",
        records = ["china","ghana","russia","s-leone"])
n = Set(m,
        name = "n",
        description = "ports",
        records = ["accra","freetown","leningrad","shanghai"])

s = pd.Series(
    index=pd.MultiIndex.from_tuples([("china", "shanghai"),
                                    ("ghana", "accra"),
                                    ("russia", "leningrad"),
                                    ("s-leone", "freetown")])
)


multi_in = Set(m,
               name = "in",
               domain = [i, n],
               description = "mines to ports map",
               uels_on_axes=True,
               records=s)

print(multi_in.records)