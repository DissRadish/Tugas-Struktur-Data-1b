"""
Module Name: structures.py
Description: Implementasi Struktur Data Linear Queue (FIFO) & Stack (LIFO)
             dengan pendekatan Object-Oriented & Encapsulation.
"""

from collections import deque
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class StructureEmptyError(Exception):
    """Custom Exception ketika melakukan pop/dequeue pada struktur data kosong."""
    pass


class QueueLinear(Generic[T]):
    """
    Implementasi Queue berbasis FIFO (First-In, First-Out)
    menggunakan collections.deque untuk efisiensi $O(1)$.
    """
    def __init__(self) -> None:
        self._container: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Menambahkan elemen baru ke akhir antrean."""
        self._container.append(item)

    def dequeue(self) -> T:
        """Menghapus dan mengembalikan elemen paling depan dari antrean."""
        if self.is_empty():
            raise StructureEmptyError("Gagal Dequeue: Antrean dalam kondisi kosong.")
        return self._container.popleft()

    def peek(self) -> Optional[T]:
        """Melihat elemen terdepan tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self._container[0]

    def is_empty(self) -> bool:
        """Memeriksa apakah antrean kosong."""
        return len(self._container) == 0

    def get_all(self) -> List[T]:
        """Mengembalikan representasi list seluruh elemen."""
        return list(self._container)


class StackLinear(Generic[T]):
    """
    Implementasi Stack berbasis LIFO (Last-In, First-Out)
    menggunakan Python Dynamic Array (List) untuk efisiensi $O(1)$.
    """
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        """Menambahkan elemen baru ke teratas tumpukan."""
        self._container.append(item)

    def pop(self) -> T:
        """Menghapus dan mengembalikan elemen paling atas dari tumpukan."""
        if self.is_empty():
            raise StructureEmptyError("Gagal Pop: Tumpukan Undo dalam kondisi kosong.")
        return self._container.pop()

    def peek(self) -> Optional[T]:
        """Melihat elemen teratas tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self._container[-1]

    def is_empty(self) -> bool:
        """Memeriksa apakah tumpukan kosong."""
        return len(self._container) == 0

    def get_all(self) -> List[T]:
        """Mengembalikan representasi list seluruh elemen."""
        return list(self._container)