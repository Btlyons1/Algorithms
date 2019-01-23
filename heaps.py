#heaps and heapq

#Tree-base structure
 # - Heap: Each node has a value smaller than either child
 # - Shape: Tree filled by level, left to right

 #Minimal structure has impressive characteristics
 # -Min in O(1)
 # - Add and Remove in O(log n)

# heapify will replaces parents with smaller of its children n//2 -1 internal nodes

class Heap:
    def __init__(self, values = None):
        """Construct list from values"""
        if values is None:
            self.ar = []
        else:
            self.ar = list(values)

        self.n - len(self.ar)

        start = self.n//2 -1
        for i in range(start, -1, -1):
            self.heapify (i)

    def isEmpty(self):
        """Determine if heap is empty."""
        return self.n == 0

    def __len__(self):
        """Return size of heap."""
        return self.n

    def pop(self):
        """Return smallest value and repair heap"""

        if self.n == 0:
            raise ValueError("Heap is empty")

        val = self.ar[0]
        self.n -= 1
        self.ar[0] = self.ar[self.n]
        self.heapify(0)
        return val

    def add(self, value):
        if self.n == len(self.ar):
            self.ar.append(value)
        else:
            self.ar[self.n] = value
        i = self.n
        self.n += 1

        # Correct structure to root
        while i > 0:
            parent = (i - 1) // 2
            if self.ar[i] < self.ar[parent]:
                self.ar[i], self.ar[parent] = self.ar[parent], self.ar[i]
                i = parent
            else:
                break

    def heapify(self, i):
        """Heapify sub-array [i, end)."""
        left = 2 * i + 1
        right = 2 * i + 2

        # Find smallest element of A[i], A[left], and A[right]
        if left < self.n and self.ar[left] < self.ar[i]:
            smallest = left
        else:
            smallest = i

        if right < self.n and self.ar[right] < self.ar[smallest]:
            smallest = right

        # If smallest is not already the parent then swap and propagate
        if smallest != i:
            self.ar[i], self.ar[smallest] = self.ar[smallest], self.ar[i]
            self.heapify(smallest)

    def __repr__(self):
        """Return representation of heap as array."""
        return 'heap:[' + ','.join(map(str, self.ar[:self.n])) + ']'


# Huffman Encoding

import heapq

class Node:
    def __init__(self, prob, symbol = None):
        """ Create node for given symbol and probability. """
        self.left = None
        self.right = None
        self.symbol = symbol
        self.prob = prob


    # Need comparator method at a minimum to work with heapq
    def __lt__(self, other):
        return self.prob < other.prob

    def encode(self, encoding):
        """ Return bit encoding in traveral"""
        if self.left is None and self.right is None:
            yield (self.symbol, encoding)
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield v

class Huffman:
    def __init__(self, initial):
        self.initial = initial

        # Count frequencies
        freq = {}
        for _ in initial:
            if _ in freq:
                freq[_] += 1
            else:
                freq[_] = 1

        # Construct priority queue
        pq = []
        for symbol in freq:
            pq.append(Node(freq[symbol], symbol))
        heapq.heapify(pq)


        #Huffman encoding algorithm
        while len(pq) > 1:
            n1 = heapq.heappop(pq)
            n2 = heapq.heappop(pq)
            n3 = Node(n1.prob + n2.prob)
            n3.left = n1
            n3.right = n2
            heapq.heappush(pq, n3)

        # Record
        self.root = pq[0]
        self.encoding = {}
        for sym,code in pq[0].encode(''):
            self.encoding[sym]=code

    def __repr__(self):
        """ Show Encoding"""
        return 'Huffman:' + str(self.encoding)


    def encode(self, s):
        """Return bit string for encoding."""
        bits = ''
        for _ in s:
            if not _ in self.encoding:
                raise ValueError("'" + _ + "' is not encoded character")
            bits += self.encoding[_]
        return bits

    def decode(self, bits):
        """Decode ASCII bit string for simplicity."""
        node = self.root
        s = ''
        for _ in bits:
            if _ == '0':
                node = node.left
            else:
                node = node.right

            if node.symbol:
                s += node.symbol
                node = self.root

        return s



h = Huffman('aaabc')
print (h)
h.encode("bababababab")
code = h.encode("bababababab")
print (code)
print (h.decode(code))