from dataclasses import dataclass, field
from statistics import mean
from typing import List
 
 
@dataclass
class Student:
    name: str
    surname: str
    scores: List[int] = field(default_factory=list)
    
    def avg(self):
        return mean(self.scores)
        
u = Student("Arman", "Hakobyan", [2, 4, 6, 5, 3])
assert u.avg() == 4