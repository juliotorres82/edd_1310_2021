from DoubleList import DoubleLinkedList


l = DoubleLinkedList()
l.is_empty()
l.append(15)
l.is_empty()
l.append(27)
l.append(30)
l.append(3)
l.transversal()
l.remove_from_head(15)
l.transversal()
l.get_size()
l.reverse_transversal()
l.remove_from_tail(15)
l.find_from_head(3)
l.find_from_tail(3)