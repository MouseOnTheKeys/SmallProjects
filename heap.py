"""
Domaci zadatak za vezbe ASP10
Predmet:        Algoritmi i strukture podataka
Student:        Nebojša Đoric
Br. indeksa:    129/2016
Skolska godina  2019/2020
"""


def swap(i, j):
    heap[i], heap[j] = heap[j], heap[i]


def heapify(i, end):
    left = 2 * i + 1
    right = 2 * i + 2
    max_index = i
    if left < end and heap[i] < heap[left]:
        max_index = left
    if right < end and heap[max_index] < heap[right]:
        max_index = right
    if max_index != i:
        swap(i, max_index)
        heapify(max_index, end)


def heap_sort():
    end = len(heap)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(i, end)
    for i in range(end - 1, 0, -1):
        swap(0, i)
        heapify(0, i)


if __name__ == "__main__":
    # 1. Na osnovu datog heap-a:
    # a) dodati novi čvor koji ima vrednost 85 i prikazati
    # novo stanje heap-a,
    # b) ukloniti čvor 90 i prikazati novo stanje heap-a.
    print("1. zadatak:")
    # Unosenje i sortiranje heap-a
    heap = [90, 89, 70, 36, 75, 63, 65, 21, 18, 15]
    print("-Unosenje i sortiranje heap-a:")
    print("Heap pre sortiranja:")
    print(heap)
    heap_sort()
    print("Heap nakon sortiranja:")
    print(heap)
    print()
    # Dodavanje broja 85 i sortiranje heap-a
    heap.append(85)
    print("-Dodavanje broja 85 i sortiranje heap-a")
    print("Heap pre sortiranja:")
    print(heap)
    heap_sort()
    print("Heap nakon sortiranja:")
    print(heap)
    print()
    # Uklanjanje broja 90 i sortiranje heap-a
    heap.pop(len(heap) - 1)
    print("-Uklanjanje broja 90 i sortiranje heap-a")
    print("Heap pre sortiranja:")
    print(heap)
    heap_sort()
    print("Heap nakon sortiranja:")
    print(heap)
    print()
