import copy


class MaxHeap(object):
    def __init__(self, heap):
        self.heap = copy.deepcopy(heap)
        if self.heap:
            self.Heapify()

    def Elements(self):
        return self.heap

    def Length(self):
        return len(self.heap)

    def _GetParentIndex(self, child_index):
        return (child_index - 1) // 4

    def Heapify(self):
        size = self.Length()
        for index in reversed(range(
            self._GetParentIndex(child_index=(size - 1)) + 1
        )):
            self._Heapify(index=index, size=size)

    def _Heapify(self, index, size):
        children = self.GetChildren(index)
        if children == []:
            return
        max_child_index = children.index(max(children))
        # get actual index of max child
        max_child_index = (4 * index) + (max_child_index + 1)
        if self.heap[max_child_index] > self.heap[index]:
            self._Swap(index, max_child_index)
            if max_child_index <= size // 4:
                self._Heapify(max_child_index, size)

    def GetChildren(self, parent_index):
        children = []
        size = self.Length()
        for i in range(4):
            child_index = (parent_index * 4) + (i + 1)
            if child_index < size:
                children.append(self.heap[child_index])
            else:
                break
        return children

    def SwimUp(self, index):
        self._SwimUp(index=index)

    def _Swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def _SwimUp(self, index):
        if index == 0:
            return
        parent = (index - 1) // 4
        if self.heap[parent] > self.heap[index]:
            return
        self._Swap(parent, index)
        self._SwimUp(index=parent)

    def DisplayHeap(self):
        counter = [1, 1]
        hep = ""
        for elem in self.Elements():
            hep += str(elem) + " "
            if counter[0] == counter[1]:
                hep += "\n"
                counter[0] = 0
                counter[1] = counter[1]*4
            counter[0] += 1
        return hep

    def AddElement(self, element):
        if isinstance(element, list):
            for _element in element:
                self.heap.append(_element)
                self.SwimUp(self.Length() - 1)
        else:
            self.heap.append(element)
            self.SwimUp(self.Length() - 1)

    def GetRootValue(self):
        return self.heap[0]
