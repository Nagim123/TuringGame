from typing import List
from abc import ABCMeta, abstractmethod

class TextGenerator() :
    """
    Abstract class for any text generator
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_text(self, beginning : str, number : int) -> List[str] :
        """
        Generate the full text based on some fragment
        """