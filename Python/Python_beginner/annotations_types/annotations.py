

class Annotation1:
	
	def __init__(self, name: str, age: int):
		pass
	
	
class Annotation2:
	from typing import Optional
	def __init__(self, name: str, age: Optional[int]):
		pass
	
	
class Annotation3:
	def __init__(self, name: str, age: int = 25):
		pass
	
class Annotation4:
	from typing import Union
	
	def __init__(self, name: str, value: Union[int, float]):
		pass


class Annotation5:
	from typing import Type
	
	AgeType = Type[int]
	
	def __init__(self, name: str, age: AgeType):
		pass


class Annotation6:
	def __init__(self: 'ClassName', name: str, age: int) -> None:
		pass


class Annotation7:
	from typing import Callable
	
	def __init__(self, name: str, callback: Callable[[str], int]):
		pass


class Annotation8:
	from typing import Any
	
	def __init__(self, data: Any):
		pass


class Annotation9:
	from typing import TypeVar
	
	T = TypeVar('T')
	
	# Here, T is a type variable, and it can be any type.
	def __init__(self, data: T):
		pass


class Annotation10:
	from typing import List, Tuple
	
	def __init__(self, person: Tuple[str, int], scores: List[int]):
		pass


class Annotation11:
	pass

