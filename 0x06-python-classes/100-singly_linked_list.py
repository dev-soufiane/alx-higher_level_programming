#!/usr/bin/python3
""" Singly linked list task """


class Node:
    """ A class that defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """ initializing the node """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ get the data attribute """
        return self.__data

    @data.setter
    def data(self, value):
        """ set the data attribute """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ retrieve next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set the next_node attribute """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """

    def __init__(self):
        """ initializing a node """
        self.__head = head

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """ prints the entire list in stdout """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
